#Person - k/v FirstLastAgeCity + print
poppy = {}

poppy['first'] = 'poppy'
poppy['last'] = 'spence'
poppy['age'] = '5 Months'
poppy['city'] = 'Miff'

print(poppy)

#dict store fav numbers. five names/numb. print each k/v
fav_nums = {}

fav_nums['Poppy'] = 2
fav_nums['Izzy'] = 42
fav_nums['Mollie'] =4 
fav_nums['Jojo'] = 6
fav_nums['Joby'] = 5

fav_nums1 = fav_nums.get('Izzy', 'None found')
print(fav_nums1)
for x,y in fav_nums.items():
    print(x,y)
    
print(fav_nums)

#Glossary "mock dict"
glossary = {}

glossary['List'] = '[ ]'
glossary['Tuple'] = '( )'
glossary['Dictionary'] = '{ }'
glossary['&'] = 'Remainder'
glossary['//'] = 'Floor divisor'

for x,y in glossary.items():
    print(f"{x} used the {y} symbols, or it means {y}\n")
