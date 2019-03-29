import threading
import queue

myqueue = queue.Queue(maxsize=3)
myCondition = threading.Condition()
