import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text

l1 = data.split("\n")
# print(l1)

l2 = [item.split(",") for item in l1 if len(item)!=0]
# print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2,f)

with open("myiris.pkl","rb") as f2:
    a = pickle.load(f2)
    print(a)