import requests


def get_wttr_lon_uk():
    location = 'Лондон'
    url_template = (f'http://wttr.in/{location}?3pnqTM&lang=ru')
    response = requests.get(url_template)
    response.raise_for_status()
    print(response.text)


def get_wttr_svo_ru():
    location = 'Шереметьево'
    url_template = (f'http://wttr.in/{location}?3pnqTM&lang=ru')
    response = requests.get(url_template)
    response.raise_for_status()
    print(response.text)


def get_wttr_cee_ru():
    location = 'Череповец'
    url_template = (f'http://wttr.in/{location}?3pnqTM&lang=ru')
    response = requests.get(url_template)
    response.raise_for_status()
    print(response.text)


def main():
    get_wttr_lon_uk()
    get_wttr_svo_ru()
    get_wttr_cee_ru()


if __name__ == '__main__':
    main()
