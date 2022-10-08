#Glossary "mock dict" continued
glossary = {}

glossary['List'] = '[ ]'
glossary['Tuple'] = '( )'
glossary['Dictionary'] = '{ : }'
glossary['&'] = 'Remainder'
glossary['//'] = 'Floor divisor'
glossary['set'] = '{ 1, 2, 3}'
glossary['.get()'] = 'Method that used specified key and returns value. Uses second argument as no value found msg'
glossary['.value()'] = 'Method that returns the value from dict pair'
glossary['.key()'] = 'Method that is default return for dict searches. Returns keys'
glossary['.items()'] = 'Method that returns key and value info from dictionary'


#for x,y in glossary.items():
#   print(f"\n{x} is/means {y}")

#Rivers 3x k/v
rivers = {
    'Mississippi':'USA',
    'Nile':'Egypt',
    'Euphrates':'Iraq',
}
#for x,y in rivers.items():
#    print(f"\nThe {x.title()} runs through the country of {y.title()}.")

#Polling 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#make list of people who should have taken poll. Loop through, thank if completed. Harrass if not

list_invitees = ['jen', 'sarah', 'edward', 'phil', 'thomas', 'geraldine', 'sascha']
for a in list_invitees:
    a = a.lower()
    if a in favorite_languages:
        print(f"Thank you {a.title()} for completing our poll.")
    else:
        print(f"{a.title()}, please complete our poll! We need your help.")