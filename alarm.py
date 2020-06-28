import pygame
import time
from datetime import datetime
import sys


def song():
    filename = "D:/CloudMusic/test.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(start=0.0)
    pygame.mixer.music.fadeout(9000)
    time.sleep(9)
    print(f"歌曲{filename.split('/')[-1]}播放完毕")


def get_time():  
    now_time = "{dt:%H-%M-%S}".format(dt=datetime.now())
    now_time_split = now_time.split('-')
    now_minute = now_time_split[0] + now_time_split[1]
    return now_minute


def time_it_is(hour, minute):
    flag = 1
    while flag:
        if str(hour) + str(minute) == get_time():
            song()
            flag = 0
        elif flag == 0:
            sys.exit(0)
