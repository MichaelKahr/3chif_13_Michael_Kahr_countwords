import threading
import queue
from FileConsumer import FileConsumer
from FileProducer import FileProducer

myqueue = queue.Queue(maxsize=3)
myCondition = threading.Condition()

fileProd1 = FileProducer(name = "Producer 1",queue=myqueue,condition=myCondition)
fileCons1 = FileConsumer(name = "Consumer 1",queue = myqueue,condition = myCondition)
fileProd1.start()
fileCons1.start()
fileProd1.join()
fileCons1.join()