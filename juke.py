# This project is based in part on this Adafruit sample project
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/fancier-code-a-very-simple-jukebox

import subprocess
import random
# import re # regular expression support
import time
import RPi.GPIO as GPIO
from glob import glob

STOP_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(STOP_PIN, GPIO.IN)

songs_17 = glob("songs/17/*")

async_song = None


def play(song_file):
    global async_song
    stop_if_playing()
    async_song = subprocess.Popen([
        'mpg123',
        '--no-control',
        song_file
    ])


def stop_if_playing():
    global async_song
    if async_song:
        print "Stopping"
        async_song.terminate()


while True:
    if (GPIO.input(17) == False):
        if len(songs_17) == 0:
            print "No songs in folder 17!"
        else:
            chosen = random.choice(songs_17)
            print "Starting ", chosen
            play(chosen)

    if (GPIO.input(STOP_PIN) == False):
        stop_if_playing()

    time.sleep(0.1)
