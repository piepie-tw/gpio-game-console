# One Day Workshop for Raspberry Pi GPIO Tutorial

[![Demo for GPIO Game Console Workshop](http://i3.ytimg.com/vi/MudTVTIHFDY/maxresdefault.jpg)](https://www.youtube.com/watch?v=MudTVTIHFDY "Demo for GPIO Game Console Workshop")

## Intro
In this workshop, we will introudce the Raspberry Pi GPIO, including:
1. Basic of electronic circuit
2. How to write the code for the hardware specification
3. Design a game console with simple hardware component

The slide is available on [用Raspberry Pi學GPIO - 自己做遊戲機](https://speakerdeck.com/piepie_tw/raspberry-pi-gpio-game-console-starter-kit)


## Environment
[Raspberry Pi 5/8GB](https://piepie.com.tw/product/raspberry-pi-5-model-b-8gb) + [RICELEE microSD 64GB](https://piepie.com.tw/product/ricelee-microsd-64g-a2) + [Raspberry Pi 27W USB-C Power Supply](https://piepie.com.tw/product/raspberry-pi-27w-usb-c-power-supply) + [Raspberry Pi GPIO Game Console Kit](https://www.piepie.com.tw/buy/2557/)，[2024-03-15-raspios-bookworm-armhf.img](https://reurl.cc/ezVAWL)

## Prerequisite
### Install required package and Python module
```shell  
$ sudo apt-get update
$ sudo apt-get remove -y python3-rpi.gpio
$ sudo apt-get install -y python3-dev python3-pip libsdl1.2-dev vim
$ sudo apt-get install -y python3-evdev python3-libevdev python3-rpi-lgpio python3-spidev 
$ sudo apt-get install -y x11vnc
```

### Emulator
1. Download pre-built emultation
```shell  
$ cd ~
$ wget http://bit.ly/2OnUMwh -O ~/advmame
```

2. Create RC file
```shell  
$ cd ~
$ chmod 755 advmame
$ ./advmame
```

3. Download Super Mario ROM
```shell  
$ cd ~
$ wget http://bit.ly/2K1dhUb -O ~/.advance/rom/suprmrio.zip
```

## Buy Raspberry Pi and GPIO Starter Kit
* [【Pi 5/8G 超值組】樹莓派 Raspberry Pi 5 Model B / 8G 超值組 (含 Pi 5/8GB 主機、原廠認證 64G A2記憶卡、官方原廠電源、外殼、官方原廠 HDMI 線)](https://www.piepie.com.tw/31200/pi4b-2g-microsd-power-supply))
* [GPIO Starter Kit](https://www.piepie.com.tw/buy/2557/)
* [More Pi 5...](https://piepie.com.tw/product-category/pi-5-related)
