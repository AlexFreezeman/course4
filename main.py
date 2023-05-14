from classes.hh import HeadHunter
from classes.sj import SuperJob


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
    print(offers_json[0])
    print(offers_json[-1])


if __name__ == '__main__':
    main()

