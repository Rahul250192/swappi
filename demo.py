from flask import Flask, jsonify, request
import swapi_endpoint
from cachetools import cached, TTLCache
import cachetools

app = Flask(__name__)
cache1 = TTLCache(maxsize=100, ttl=3600)
cache2 = TTLCache(maxsize=1000, ttl=3600)

films = []


@app.route('/filmlist', methods=['POST'])
@cached(cache1)
def film_list():
    all_films = swapi_endpoint.getFilms()
    for i in range(len(all_films)):
        film = {"id": i,
                "title": str(all_films[i]["title"]),
                "release_date": str(all_films[i]["release_date"])
                }
        films.append(film)

    return jsonify(films)


@app.route('/filmchar', methods=['POST'])
@cached(cache2, key=cachetools.keys.hashkey)
def film_characters():
    request_json = request.get_json()
    data = request_json.get('filmID')
    film_chars = swapi_endpoint.getCharacters(data)
    return jsonify(film_chars)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
