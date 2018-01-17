# This project is based in part on this Adafruit sample project
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/fancier-code-a-very-simple-jukebox

import subprocess
import random
import time
import RPi.GPIO as GPIO
from glob import glob


GPIO.setmode(GPIO.BCM)

# Initialize the pin we'll connect to a stop button
# To disable the stop button functionality, set this to None
STOP_PIN = None

# An array of pins that will connect to buttons,
# and map to folders full of MP3s
MUSIC_PINS = [17, 22, 4]

if(STOP_PIN):
    GPIO.setup(STOP_PIN, GPIO.IN)

songs = {}
for pin in MUSIC_PINS:
    # TODO : Don't rely on working directory, use script directory,
    # like https://stackoverflow.com/a/5475224/8995
    songs[pin] = glob('songs/%s/*.mp3' % pin)
    GPIO.setup(pin, GPIO.IN)


def play(song_file):
    stop()
    # Async, main loop continues while song is playing
    print "Starting %s" % chosen
    # TODO : if we held on to a reference for this process,
    # we could .poll() before we killall to generate a skip counter
    # (I'd still keep killall, its very resilient to race conditions)
    subprocess.Popen([
        'mpg123',
        '-q',
        '--no-control',
        song_file
    ])
    # Debounce a little, holding down the button shouldn't start 2+ songs
    time.sleep(1)


def stop():
    # Synchronous, wait for killing to stop before continuing script
    subprocess.call([
        "killall",
        "mpg123"
    ])


while True:
    for pin in MUSIC_PINS:
        if (GPIO.input(pin) == False):
            if len(songs[pin]) == 0:
                print 'No songs in folder %s!' % pin
            else:
                # TODO support cycling through the folder instead of random:
                # https://stackoverflow.com/questions/2167868/getting-next-element-while-cycling-through-a-list
                chosen = random.choice(songs[pin])
                play(chosen)

    if (STOP_PIN and GPIO.input(STOP_PIN) == False):
        stop()

    time.sleep(0.1)
