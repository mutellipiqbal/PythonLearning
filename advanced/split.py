import re

slpit_term = "@"
sentence = "My eimal adress is my@gomail.com"
print re.split(slpit_term, sentence)
#or

print sentence.split()

#or
print re.findall("[^!.? ]", "this is my text")
print re.findall("[^!.? ]+", "this is my text")
