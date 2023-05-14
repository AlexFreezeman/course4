import requests
from classes.abstract import Engine
from classes.utils import ParsingError


class HeadHunter(Engine):
    def __init__(self, keyword):
        self.__header = None
        self.__params = {
            "text": keyword,
            "page": 0,
            "per_page": 100,
        }
        self.__offers = []

    def get_request(self):
        response = requests.get('https://api.hh.ru/vacancies',
                                headers=self.__header,
                                params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['items']

    def get_offers(self, pages_count=10):
        while self.__params['page'] < pages_count:
            print(f"HeadHunter: получаем данные - страница {self.__params['page'] + 1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print('Ошибка получаения данных!')
                break
            print(f"Найдено ({len(values)}) вакансий.")
            self.__offers.extend(values)
            self.__params['page'] += 1

    def get_formatted_offers(self):
        formatted_offers = []
        for offer in self.__offers:
            salary_min, salary_max = self.get_salary(offer['salary'])
            formatted_offers.append({
                'id': offer['id'],
                'title': offer['name'],
                'url': offer['alternate_url'],
                'salary_min': salary_min,
                'salary_max': salary_max,
                'employer': offer['employer']['name'],
                'api': 'HeadHunter'
            })
        return formatted_offers

    @staticmethod
    def get_salary(salary):
        formatted_salary = [None, None]
        if salary and salary['from'] and salary['from'] != 0:
            formatted_salary[0] = salary['from'] if salary['currency'].lower() == 'rur' else salary['from'] * 78
        if salary and salary['to'] and salary['to'] != 0:
            formatted_salary[1] = salary['to'] if salary['currency'].lower() == 'rur' else salary['to'] * 78
        return formatted_salary

