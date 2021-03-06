import threading
import queue
import json

class FileConsumer(threading.Thread):
    def __init__(self,name,queue,condition):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.condition = condition

    def run(self):
        while True:
            book = ""
            self.condition.acquire()
            try:
                book = self.queue.get(block=False)
                self.condition.notify()
            except queue.Empty:
                print(self.name+": queue empty. waiting.")
                self.condition.wait()
            self.condition.release()
            if book!="":
                res = book.countWords()
                out_file = open("./output/"+book.filename+"-output.txt","w")
                out_file.write(json.dumps(res,indent=2))
                out_file.close()