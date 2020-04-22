#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, Amenity, Place
from models.state import State

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_site():
    '''
    HBNB is alive!
    '''
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('PLaces').values()

    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_app(e):
    '''
    teardown app context
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
