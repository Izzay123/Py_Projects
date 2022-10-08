alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

del alien_0['points']
print(alien_0)

#alien_0['color'] = 'yellow'
#print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")

#alien speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #fast boi
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")