import os

for f in os.listdir("files"):
    print(f)
    print(open("./files/10023.txt","r").read())