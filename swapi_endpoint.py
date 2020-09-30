import requests


def getFilms(_id=None):
    if _id == None:
        url = "https://swapi.dev/api/films"
        all_films = requests.get(url).json()
    else:
        url = "https://swapi.dev/api/films/{}".format(_id + 1)
        film = requests.get(url).json()
        return film
    content = all_films["results"]
    return content


def getCharacters(data):
    content_list = []
    characters = getFilms(data)["characters"]
    for character in characters:
        url = str(character)
        films = requests.get(url).json()
        content_json = {"id": data,
                        "name": str(films["name"])
                        }
        content_list.append(content_json)
    return content_list
