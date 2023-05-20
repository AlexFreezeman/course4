from classes.hh import HeadHunter
from classes.sj import SuperJob
from classes.utils import Connector, Offer


def main():
    offers_json = []
    keyword = "Python"

    hh = HeadHunter(keyword)
    sj = SuperJob(keyword)
    for api in (hh, sj):
        api.get_offers(pages_count=1)
        offers_json.extend(api.get_formatted_offers())

    connector = Connector(keyword=keyword, offers_json=offers_json)

    while True:
        command = input(
            "1 - Вывести список вакансий;\n"
            "2 - Отсортировать вакансии по мин. зарплате (по возрастанию);\n"
            "3 - Отсортировать вакансии по мин. зарплате (по убыванию);\n"
            "exit - для выхода.\n"
        )
        if command.lower() == 'exit':
            break
        elif command == "1":
            offers = connector.select()
        elif command == "2":
            offers = connector.sort_min_offers_asc()
        elif command == "3":
            offers = connector.sort_min_offers_desc()

        for offer in offers:
            print(offer, end='\n\n')


if __name__ == '__main__':
    main()

