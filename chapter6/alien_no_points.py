#Using get() to Access Values

#alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])

#Traceback (most recent call last):
#File "alien_no_points.py", line 2, in <module>
#print(alien_0['points'])
#KeyError: 'points'

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)