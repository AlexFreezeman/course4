from classes.hh import HeadHunter
from classes.sj import SuperJob
from classes.utils import Connector


def main():
    offers_json = []
    keyword = input("Введите ключевое слово, по которому пройдёт поиск: \n")

    # поиск вакансий по ключевому слову и запись в json
    hh = HeadHunter(keyword)
    sj = SuperJob(keyword)
    for api in (hh, sj):
        api.get_offers(pages_count=5)
        offers_json.extend(api.get_formatted_offers())

    # соединяем воедино
    connector = Connector(keyword=keyword, offers_json=offers_json)

    # вывод опций для пользователя
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

