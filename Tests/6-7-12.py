#Person - k/v FirstLastAgeCity + print -- two dictioaries for diff people. store all three in a list called people. 
# Loop through and print all info

from decimal import ConversionSyntax
from types import CoroutineType


people = {
    'poppy' : {
        'first':'poppy',
        'last':'spence',
        'age':'5 Months',
        'city':'Miff',
    },
    'braydon' : {
        'first':'braydon',
        'last':'dude',
        'age' : 'too old',
        'city':'wheat',
    },
    'Mollie' : {
        'first':'Mollie',
        'last':'Duggie',
        'age':'5',
        'city':'miff',
    },
}
for name, inf in people.items():
    print(f"{name} and their info:")
    fullname = f"{inf['first']} {inf['last']}"
    age = f"{inf['age']} years old"
    city = f"{inf['city']} is where they live."
    print(fullname)
    print(age)
    print(city)
