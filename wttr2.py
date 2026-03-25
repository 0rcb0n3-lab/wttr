import requests


def get_wttr(location):
    value = {"nTqm": "", "lang": "en"}
    url_template = (f'http://wttr.in/{location}')
    response = requests.get(f'{url_template}, params=value)
    response.raise_for_status()
    print(response.text)


def main():
    location = ['London', 'Шереметьево', 'Череповец']
    for city in location:
        get_wttr(city)


if __name__ == '__main__':
    main()
