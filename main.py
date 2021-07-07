import requests
import operator


class SuperHero:
    def __init__(self, name):
        url = 'https://superheroapi.com/api/2619421814940190/search/'
        res = requests.get(url + name)
        data = res.json()
        self.heroname = data['results'][0]['name']
        self.intelligence = int(data['results'][0]['powerstats']['intelligence'])


def superhero_compare(sheroes_list):
    sorted_list = sorted(sheroes_list, key=operator.attrgetter('intelligence'))
    print(sorted_list[-1].heroname, 'has the highest intelligence!')


if __name__ == '__main__':
    hulk = SuperHero('Hulk')
    captain = SuperHero('Captain America')
    thanos = SuperHero('Thanos')

    superhero_compare([hulk, thanos, captain])
