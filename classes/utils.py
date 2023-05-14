import json
import os
from datetime import datetime


class ParsingError(Exception):
    def __str__(self):
        return "Ошибка получения данных по API."


class Connector:
    def __init__(self, keyword, offers_json):
        self.__filename = f"{keyword.title()}.json"
        self.insert(offers_json)

    def insert(self, offers_json):
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(offers_json, file, ensure_ascii=False, indent=4)

    def select(self):
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        offers = [Offer(x['id'], x['title'], x['url'], x['salary_min'], x['salary_max'], x['employer'], x['api']) for x
                  in data]
        return offers


class Offer:
    __slots__ = ('id', 'title', 'url', 'salary_min', 'salary_max', 'employer', 'api')

    def __init__(self, offer_id, title, url, salary_min, salary_max, employer, api):
        self.id = offer_id
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.employer = employer
        self.api = api

    def __str__(self):
        salary_min = f"От {self.salary_min}" if self.salary_min else ""
        salary_max = f"До {self.salary_max}" if self.salary_max else ""
        if self.salary_min is None and self.salary_max is None:
            salary_min = "Не указана"
        return f'Вакансия: \"{self.title}\" \nКомпания: \"{self.employer}\" \nЗарплата: {salary_min} {salary_max} \nURL: {self.url}'


