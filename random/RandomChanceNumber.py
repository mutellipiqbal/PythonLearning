
import random

number = random.randint(1,100)
counter = 7

while counter > 0:
  enter_number = input ("Enter your number: ")
  if enter_number == number:
      print "Congratulaion, you found"
      print "Your score is :", counter*20
      break
  else:
        counter = counter -1
       
        if counter == 0:
            print "You can not found. you have not chance."
            print "Assumed number is :", number                        
        else:
            print "You did not find.", counter, "Chance you have"
            if enter_number < number:
                print "Increas your number>>"
            else:
                print "Dicrease your number<<"
  
  




