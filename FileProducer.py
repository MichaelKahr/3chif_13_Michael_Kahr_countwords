import threading
import queue

class Book():
    def __init__(self, filename,text):
        self.filename = filename
        self.text = text

    def countWords(self):
        words = {}
        for x in self.text.split(" "):
            if x in words:
                words[x]+=1
            else:
                words[x]=0