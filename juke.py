# This project is based in part on this Adafruit sample project
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/fancier-code-a-very-simple-jukebox


import subprocess
import random
# import re # regular expression support
import time
import sys
# import RPi.GPIO as GPIO

from glob import glob

songs_17 = glob("songs/17/*")

if len(songs_17) == 0:
    sys.exit("No songs in folder 17!")

async_song = subprocess.Popen([
    'mpg123',
    '--no-control',
    random.choice(songs_17)
])

time.sleep(10)

async_song.terminate()
