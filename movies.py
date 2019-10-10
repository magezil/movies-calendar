#!/usr/bin/python3

import requests

API_KEY=""

if __name__ == '__main__':
    # TODO: see about getting only future movies rather than those already out
    # https://developers.themoviedb.org/3/movies/get-upcoming
    url = 'https://api.themoviedb.org/3/movie/upcoming?api_key=%s' % (API_KEY)

    r = requests.get(url)

    results = r.json().get('results', [])
    for movie in results:
        # TODO: process when make frontend or add to calendar
        print("{} - {}".format(movie['title'], movie['release_date']))
    else:
        print("No movies :(")