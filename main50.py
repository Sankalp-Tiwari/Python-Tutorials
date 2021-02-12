f1 = open('sankalp.txt')
try:
    f = open('sankalpaa.txt')
    f.readline()
except Exception as e:
    print(e)
finally:
    try:
        f.close()
        f1.close()
    except Exception as e:
        print("No file found to close")