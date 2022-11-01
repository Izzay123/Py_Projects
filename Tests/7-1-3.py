#7-1-3
#Rental Car - 

a = input('What kind of car are you looking for?')
print(f'Let me see if I can find you a{a}.')

#7-2 Restaurant Seating
a = int(input('How many people are we seating tonight? '))
if a >= 8:
    print('Sorry you will have to wait for a table to open up.')
elif a < 8:
    print('Right this way, sir or madam.')

#7-3 Multiples of ten
a = int(input("Tell me any number and can tell you if it's a multiple of ten! : "))
if a % 10 == 0:
    print('Yep that is a multiple of ten')
elif a % 10 != 0:
    print('No that is not a multiple of ten')