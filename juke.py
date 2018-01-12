# This project is based in part on this Adafruit sample project
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/fancier-code-a-very-simple-jukebox

import subprocess
import random
# import re # regular expression support
import time
import RPi.GPIO as GPIO
from glob import glob


GPIO.setmode(GPIO.BCM)


STOP_PIN = 4
GPIO.setup(STOP_PIN, GPIO.IN)

songs = {}
MUSIC_PINS = [17, 22]
for pin in MUSIC_PINS:
    songs[pin] = glob('songs/%s/*.mp3' % pin)
    GPIO.setup(pin, GPIO.IN)

async_song = None


def play(song_file):
    global async_song
    stop_if_playing()
    async_song = subprocess.Popen([
        'mpg123',
        '-q',
        '--no-control',
        song_file
    ])


def stop_if_playing():
    global async_song
    if async_song:
        print "Stopping"
        async_song.terminate()


while True:
    for pin in MUSIC_PINS:
        if (GPIO.input(pin) == False):
            if len(songs[pin]) == 0:
                print 'No songs in folder %s!' % pin
            else:
                chosen = random.choice(songs[pin])
                print "Starting %s" % chosen
                play(chosen)

    if (GPIO.input(STOP_PIN) == False):
        stop_if_playing()

    time.sleep(0.1)
