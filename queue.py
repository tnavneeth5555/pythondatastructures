#queue
""" queue is first in first out"""
from queue import Queue as q

L = q() 

""" Data is inserted into Queue """ 

L.put(5) 
L.put(9) 
L.put(1) 
L.put(7) 

""" data is deleted from queue from front"""
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
