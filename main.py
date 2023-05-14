from classes.hh import HeadHunter


def main():
    offers_json = []
    keyword = "Python"

    hh = HeadHunter(keyword)
    hh.get_offers()
    offers_json.extend(hh.get_formatted_offers())
    print(offers_json)


if __name__ == '__main__':
    main()

