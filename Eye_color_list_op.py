#You are given a 2D matrix, which represents the number of people in a room, grouped by their eye color and gender.
#The first row represents the male gender, while the second row represents females.
#The columns are the eye colors, in the following order: brown, blue, green, black
#Create a program to take eye color as input and output the percentage of people with that eye color in the room.

x = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = input('What color are we looking for? ').lower()
#your code goes here

brown = (x[0][0] + x[1][0])
blue = (x[0][1] + x[1][1])
green = (x[0][2] + x[1][2])
black = (x[0][3] + x[1][3])

all = int(brown + blue + green + black)

if color == 'brown':
    print(str(int((brown)/all*100))+'%')
elif color == 'blue':
    print(str(int((blue)/all*100))+'%')
elif color == 'green':
    print(str(int((green)/all*100))+'%')
elif color == 'black':
    print(str(int((black)/all*100))+"%")