#!/usr/bin/python3
from datetime import datetime
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
        release_date = movie['release_date']
        # Filter out already out movies for now
        if datetime.strptime(release_date, "%Y-%m-%d") > datetime.today():
            print("{} - {}".format(movie['title'], release_date))
