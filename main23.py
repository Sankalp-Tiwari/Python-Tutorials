def f1(*san ,**sanki):
    for items in san:
        print(items)
    for name , roles in sanki.items():
        print(f"{name} is a {roles}")

l1 = ["Sankalp","Aditya","Rituraj"]
d1 = {"Sankalp":"Library Head","Aditya":"Music Head","Rituraj":"Computer lab head"}
f1(*l1, **d1)