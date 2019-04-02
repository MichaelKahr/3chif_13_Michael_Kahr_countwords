import threading
import queue
from FileConsumer import FileConsumer
from FileProducer import FileProducer

myqueue = queue.Queue(maxsize=9)
myCondition = threading.Condition()

fileProd1 = FileProducer(name = "Producer 1",queue=myqueue,condition=myCondition)
fileCons1 = FileConsumer(name = "Consumer 1",queue = myqueue,condition = myCondition)
fileCons2 = FileConsumer(name = "Consumer 2",queue = myqueue,condition = myCondition)
fileCons3 = FileConsumer(name = "Consumer 3",queue = myqueue,condition = myCondition)
fileProd1.start()
fileCons1.start()
fileCons2.start()
fileCons3.start()
fileProd1.join()
fileCons1.join()
fileCons2.join()
fileCons3.join()