from classes.hh import HeadHunter
from classes.sj import SuperJob
from classes.utils import Connector, Offer


def main():
    offers_json = []
    keyword = "Python"

    hh = HeadHunter(keyword)
#    hh.get_offers()
#    offers_json.extend(hh.get_formatted_offers())
#    print(offers_json)
    sj = SuperJob(keyword)
    for api in (hh, sj):
        api.get_offers(pages_count=5)
        offers_json.extend(api.get_formatted_offers())

    connector = Connector(keyword=keyword, offers_json=offers_json)

    while True:
        command = input(
            "1 - Вывести список вакансий;\n"
            "exit - для выхода.\n"
        )
        if command.lower() == 'exit':
            break
        elif command == "1":
            offers = connector.select()

        for offer in offers:
            print(offer, end='\n\n')


if __name__ == '__main__':
    main()

