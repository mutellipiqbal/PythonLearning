

from random import randint

print "selecet s for stone, c for scissor, p for paper. You have only tree chance."

liste = ["S", "P", "C"]
machine = liste[randint(0, 2)]

counter = 3

while counter > 0:
  input1 = raw_input("Please enter s, p or c: ").upper()
  if input1 == machine:
      print "machine holds:" ,machine
      print "you are same."
     
  elif input1 =="C" and machine == "P":
      print "machine holds:" ,machine
      print "I win."
  elif input1 =="C" and machine == "S":
      print "machine holds:" ,machine
      print "machine win."

  elif input == "P" and machine =="C":
      print "machine holds:" ,machine
      print "machine win."
  elif input == "P" and machine =="S":
      print "machine holds:" ,machine
      print "I win."

         
  elif input == "S" and machine =="P":
      print "machine holds:" ,machine
      print "machine win."
  elif input == "S" and machine =="C":
      print "machine holds:" ,machine
      print "I win."



  else:
        counter = counter -1
        print "machine holds:" ,machine
       
        if counter == 0:
            print "You can not win. you have not chance."
            
        else:
            print "You did not win.", counter, "Chance you have"
         

