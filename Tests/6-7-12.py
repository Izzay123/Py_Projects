#Person - k/v FirstLastAgeCity + print -- two dictioaries for diff people. store all three in a list called people. 
# Loop through and print all info

from decimal import ConversionSyntax
from types import CoroutineType


#people = {
#    'poppy' : {
#        'first':'poppy',
#        'last':'spence',
#       'age':'5 Months',
#        'city':'Miff',
#    },
#    'braydon' : {
#        'first':'braydon',
#        'last':'dude',
#        'age' : 'too old',
#        'city':'wheat',
#    },
#    'Mollie' : {
#        'first':'Mollie',
 #       'last':'Duggie',
 #       'age':'5',
#        'city':'miff',
 #   },
#}
#for name, inf in people.items():
#    print(f"{name} and their info:")
#    fullname = f"{inf['first']} {inf['last']}"
#    age = f"{inf['age']} years old"
#    city = f"{inf['city']} is where they live."
#    print(fullname)
#    print(age)
 #   print(city)

#Pets dict - sev pets. anmal/owner. 

    
#milo = {
#        'name' : 'milo',
#        'breed' : 'king charles spaniel',
 #       'owner' : 'Isabel',
#}
#poppy = {
##        'name' : 'poppy',
#        'breed' : 'poodle',
#        'owner' : 'Melissa',
#}
#leo = {
 #   'name' : 'leo',
 #   'breed' : 'Siberian husky',
 #   'owner' : 'six people',
#}
#pets = [milo, poppy, leo]

#for pet in pets:
#    print(f"{pet['name']} is a {pet['breed']} and belongs to {pet['owner']}.\n" )

#3 places
#favorite_places = {
#    'poppy' : {
 #      'name' : 'poppy',
  #      'place1' : 'kitchen',
 #       'place2' : 'sleeping on mat',
 #       'place3' : 'fake grass',
  #  },
 #   'mollie' : {
 #       'name' : 'mollie',
 #       'place1' : 'doghouse',
 #       'place2' : 'running wild',
 #       'place3' : 'the creek',
 #   },
 #   'leo' : {
 #       'name' : 'leo',
 #       'place1' : 'the tree',
 #       'place2' : 'on a walk',
 ##       'place3' : 'going on a truck ride',
 #   },
#}
#for key,value in favorite_places.items():
#    print(f"{value['name']}'s three favorite places are {value['place1']}, {value['place2']}, and {value['place3']}.\n")
    
#dict favorite numbers continued
#fav_nums = {}

#fav_nums['Poppy'] = "2 and 3" 
#fav_nums['Izzy'] = "42 and 44"
#fav_nums['Mollie'] ="4 and 7"
#fav_nums['Jojo'] = "6 and 22"
#fav_nums['Joby'] = "5 and 13"

#fav_nums1 = fav_nums.get('Izzy', 'None found')
#print(fav_nums1)
#for key, value in fav_nums.items():
#    print(f"{key}'s favorite numbers are: {value}")

#cities - dict of info. prit each and all info
cities = {
    'Chicago' : {
        'State' : 'Illinois',
        'Country' : 'USA',
        'Fun fact' : 'A giant bean statue is downtown',
    },
    'San Diego' : {
        'State' : 'California',
        'Country' : 'USA',
        'Fun fact' : 'Beautifule mountains sit behind it',
    },
    'Whidbey Island' : {
        'State' : 'Washington',
        'Country' : 'USA',
        'Fun fact' : 'Lots of wild wolves',
    },
}

for k,v in cities.items():
        print(f"{k} is in {v['State']}, {v['Country']}. A fun fact about the city is {v['Fun fact']}!")
        

#Skipping 6-12