# juke-bot
Durable, simple jukebox for kids

![Juke-Bot 0.0](jukebot.jpg)

## This project needs:

 - A Raspberry Pi with analog audio support (to my knowledge that's all except the Zero)  I'm writing this with a 2013 model B, so it's pretty resource-light.
 - An SD card big enough to hold [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) and your music.
 - Some speakers that plug into your Raspberry Pi's headphone jack.
 - Power. I'm using a [two-port high-amperage USB wall charger](https://www.amazon.com/gp/product/B013US9FFY/ref=oh_aui_search_detailpage?ie=UTF8&psc=1) to power the Pi and the speakers.
 - Three durable buttons. I'm using these [big 4" light-up buttons](https://www.amazon.com/gp/product/B071FSKY6Q/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1).
 - An enclosure. I'm prototyping in a cardboard box, but will upgrade to plywood.
 - Some way to easily wire into the Pi's GPIO ports. I'm using the [Adafruit T-Cobbler](https://www.adafruit.com/product/2028) to a breadboard at the prototyping stage.
 - Some way to connect to the buttons. The microswitches on those huge buttons will take normal spade connectors, but the connectors to the LEDs are too wide, so I'll have to figure something else out.


## Getting Started

Build an SD card with Raspbian Lite.

During setup it's nice to have your Raspberry Pi on the network. Unless you have a patching plan, it'll be nice to knock it off the network when it's ready to be installed.

[Install the audio player (mpg123), and configure your Pi to always use the headphone jack](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/install-audio)

Max out the software volume of the headphone jack, so you can control it at the speaker.

```bash
sudo amixer  sset PCM,0 100%
```

Install screen and/or supervisor to run it headless.
`sudo apt-get install screen supervisor`
