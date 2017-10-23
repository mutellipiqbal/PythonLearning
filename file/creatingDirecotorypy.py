import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print "Your folder is created."
            
    except OSError:
        print "Your folder was not created. " + directory

#this function creates folder in designated position.
createFolder("D:\\abc")

#this function creates folder in default position.
#createFolder('./data/')     
