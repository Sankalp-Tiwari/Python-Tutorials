import json

# data = '{"var1":"Sankalp"}'
# parsed = json.loads(data)
# print(parsed['var1'])
# print(data)

# data2 = {"Name":"Sankalp","cars":["BMW","WagonR","Ferrari"],"Food":("tortilas","rice")}
# parsed__ = json.dumps(data2)
# print(parsed__)


data = ["heyy","Hi","Namastey"]
parsed = json.dumps(sort_keys=False)
print(parsed)
