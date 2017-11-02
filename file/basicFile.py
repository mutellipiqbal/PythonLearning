#file

f = open("aboutMe.txt","w")
'''
‘r’ – Read mode which is used when the file is only being read 
‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 
'''

f.write("I am lreaning Python.")

#f.read()
#or
f = open("aboutMe.txt","r") #the meothod are same.
f.close()

