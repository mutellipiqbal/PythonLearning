x = 7 #x is local, but we can change it as global.

def example ():
    global x #we changed x as global.
    print x
    x+=6
    print x

example()
