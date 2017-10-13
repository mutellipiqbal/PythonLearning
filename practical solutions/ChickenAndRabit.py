'''
The total numbers of rabits and chickesn are 48 and their foots are 108. Could you find how much rabits and chickens there?


for x in range(1,48):
   for y in range (1,x):
      if (x +y ==48) and (2*x + 4*y ==108):
          print "Chickin are %s.\nRabits are %s." %(x, y)
