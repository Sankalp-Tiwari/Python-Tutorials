import time
from functools import lru_cache

i = int(input("Enter the maxsize of chacheing"))
@lru_cache(maxsize=i)
def take_braek(sec):
    time.sleep(sec)
    return sec
if __name__ == '__main__':
    print("Executing...")
    take_braek(3)
    print("Excecuted,Executing again")
    take_braek(3)
    print("Excecuted,Executing again")
    take_braek(3)
    print("Excecuted,Executing again")
    take_braek(3)
    print("Excecuted,Executing again")
    take_braek(3)
    print("Excecuted,Executing again")
    take_braek(4)
    print("Excecuted,Executing again")
    take_braek(4)
    print("Excecuted,Executing again")
    take_braek(4)
    print("Excecuted,Executing again")
    take_braek(10)
    print("Excecuted,Executing again")
    take_braek(10)
    print("Excecuted,Executing again")
    take_braek(2)
    print("Executed...")