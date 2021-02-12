import pickle

#          pickling a python object
# cars = ['Maruti Suzuki','Ferrari','BMW']
# file = 'mycar.pkl'
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file = 'mycar.pkl'
fileobj = open(file,'rb')
mycar = pickle.load()
print(mycar)
print(type(mycar))