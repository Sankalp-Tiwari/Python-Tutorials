from pygame import mixer
from datetime import datetime
from time import time
def musicOnLoop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a ==stopper:
            mixer.music.stop()
            break

def log_now(message):
    with open('mylog.txt','a') as f:
        f.write(f"{message}{datetime.now()}\n")

if __name__ == '__main__':
    # musicOnLoop('water.mp3','stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyesecs = 20

    while True:
        if time()-init_water>watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm")
            musicOnLoop('water.mp3','drank')
            init_water = time()
            log_now("Drank Water at ")

        if time()-init_eyes>eyesecs:
            print("Eye Exercise time. Enter 'doneyes' to stop the alarm")
            musicOnLoop('water.mp3','doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at ")

        if time()-init_exercise>exsecs:
            print("Physical Activity time. Enter 'done' to stop the alarm")
            musicOnLoop("water.mp3",'done')
            init_exercise = time()
            log_now("Physical Activity done at ")