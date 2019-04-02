import threading
import queue
import os
import re

class Book():
    def __init__(self, filename,text):
        self.filename = filename
        self.text = text

    def countWords(self):
        words = {}
        for x in self.text.split(" "):
            x = x.split("\n")[0]
            x = re.sub('\ |\?|\.|\!|\/|\;|\:', '', x)
            if x in words:
                words[x]+=1
            else:
                words[x]=1
        return words

class FileProducer(threading.Thread):
    def __init__(self, name,queue,condition):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.condition = condition
    
    def run(self):
        for f in os.listdir("./files"):
            print(f)
            try:
                text = open("./files/"+f,"r").read()
            except:
                continue
            book = Book(f.split(".txt")[0],text)
            self.condition.acquire()
            try:
                self.queue.put(book,block=False)
                self.condition.notify()
            except queue.Full:
                #print(self.name+": queue full. Waiting")
                self.condition.wait()
            self.condition.release()