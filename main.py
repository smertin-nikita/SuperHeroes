from pprint import pprint
import requests

TOKEN = '2619421814940190'


def search_hero(name):
    """Show heroes with name"""
    response = requests.get(f'https://www.superheroapi.com/api.php/{TOKEN}/search/{name}')
    response.raise_for_status()

    data = response.json()
    pprint(data)


def get_hero(id):
    """Returns hero by id"""
    response = requests.get(f'https://www.superheroapi.com/api.php/{TOKEN}/{id}')
    response.raise_for_status()

    return response.json()


if __name__ == '__main__':
    # search_hero('Thanos')
    hulk = get_hero(332)
    cap = get_hero(149)
    thanos = get_hero(655)

    heroes = sorted([hulk, cap, thanos], key=lambda hero: hero['powerstats']['intelligence'])
    for hero in heroes[:1]:
        print(f"{hero['name']} intelligence: {hero['powerstats']['intelligence']}")


