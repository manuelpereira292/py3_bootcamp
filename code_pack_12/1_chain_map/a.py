from collections import ChainMap
import os

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99, 'hood': 400}
car_pricing = ChainMap(car_accessories, car_options, car_parts)

print (car_pricing['hood'])

print (os.environ)
