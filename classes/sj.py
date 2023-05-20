import os

import requests
from classes.abstract import Engine
from classes.utils import ParsingError


class SuperJob(Engine):
    """
    класс для работы с сайтом SuperJob
    """
    def __init__(self, keyword):
        self.__header = {"X-Api-App-Id": os.environ["SJ_API_KEY"]}
        self.__params = {
            "keyword": keyword,
            "page": 0,
            "count": 100,
        }
        self.__offers = []

    def get_request(self):
        """
        получение данных с api
        """
        response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                headers=self.__header,
                                params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['objects']

    def get_offers(self, pages_count=5):
        """
        парсинг данных с сайта и запись их в список
        """
        while self.__params['page'] < pages_count:
            print(f"SuperJob: получаем данные - страница {self.__params['page'] + 1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print('Ошибка получаения данных!')
                break
            print(f"Найдено ({len(values)}) вакансий.")
            self.__offers.extend(values)
            self.__params['page'] += 1

    def get_formatted_offers(self):
        """
        форматирование списка (вычленение отображаемых полей)
        """
        formatted_offers = []
        for offer in self.__offers:
            formatted_offers.append({
                'id': offer['id'],
                'title': offer['profession'],
                'url': offer['link'],
                'salary_min': self.get_salary(offer['payment_from'], offer['currency']),
                'salary_max': self.get_salary(offer['payment_to'], offer['currency']),
                'employer': offer['firm_name'],
                'api': 'SuperJob'
            })
        return formatted_offers

    @staticmethod
    def get_salary(salary, currency):
        """
        обработка зарплаты
        """
        formatted_salary = None
        if salary and salary != 0:
            formatted_salary = salary if currency == 'rub' else salary * 75
        return formatted_salary