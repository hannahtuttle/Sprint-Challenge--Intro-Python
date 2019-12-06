# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    def __init__(self, name, lat, lon):
      self.name = name
      self.lat = lat
      self.lon = lon

    def __str__(self):
      return f'{self.name}, {self.lat}, {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

import csv
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open ('/Users/hannah/LambdaHW/Sprint-Challenge--Intro-Python/src/cityreader/cities.csv') as csvfile:
      city_reader = csv.DictReader(csvfile)
      for row in city_reader:
        # print(row['city'], row['lat'], row['lng'])
        cities.append(City(row['city'], float(row['lat']), float(row['lng'])))
    
  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(f'{c.name}, {c.lat}, {c.lon}')

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)
# print('Give two coordinates with latitude and longitude. The first coordinates should be the upper left coner you want to start with and the second should be the lower right corner yo want to end with.')
user_input = input('example of valid input (lat1, lon1/ lat2, lon2) --> ').split('/')
s = []
for i in user_input:
  s.append(i.split(',')) 
print(s)

def check_lat_values(first_value, second_value):
  if first_value > second_value:
    return True
  else:
    # print("Your second Lattitude is greater than you first. Invalid endpoint for lattitude.")
    return False

def check_lon_values(first_value, second_value):
  if first_value > second_value:
    return True
  else:
    # print("Your second Lattitude is greater than you first. Invalid endpoint for lattitude.")
    return False


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  if check_lat_values(lat1, lat2):

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within 
    # the specified coordinates.
    for val in cities:
        if val.lat <= lat1 and val.lon <= lon2 and val.lat >= lat2 and val.lon >= lat2:
          within.append(val)
        else:
          pass
  else:
    print("Your second Lattitude and logitude values are about the first values, please select a different set that is below first set of values.")

  return within

cityreader_stretch(float(s[0][0]), float(s[0][1]), float(s[1][0]), float(s[1][1]), cities)