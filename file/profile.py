
dosya = file ("profile.txt", "w")
dosya = open ("profile.txt", "a")

liste = ["mutellip", "ikbal", 70, 180 ]

for x in liste:
    dosya.writelines("%s\n"%(x))

dosya.close()
