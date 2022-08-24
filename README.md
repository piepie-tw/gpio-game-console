# One Day Workshop for Raspberry Pi GPIO Tutorial

[![Demo for GPIO Game Console Workshop](http://i3.ytimg.com/vi/MudTVTIHFDY/maxresdefault.jpg)](https://www.youtube.com/watch?v=MudTVTIHFDY "Demo for GPIO Game Console Workshop")

## Intro
In this workshop, we will introudce the Raspberry Pi GPIO, including:
1. Basic of electronic circuit
2. How to write the code for the hardware specification
3. Design a game console with simple hardware component

The slide is available on [用Raspberry Pi學GPIO - 自己做遊戲機](https://speakerdeck.com/piepie_tw/raspberry-pi-gpio-game-console-starter-kit)


## Environment
[Raspberry Pi 4B/2G](https://www.piepie.com.tw/28040/raspberry-pi-4-model-b)/[Raspberry Pi 3B+](https://www.piepie.com.tw/19429/raspberry-pi-3-model-b-plus) + SanDisk 32G microSD  + [Raspberry Pi GPIO Game Console Kit](https://www.piepie.com.tw/2557/gpio-game-console-starter-kit) + 2021-01-11-raspios-buster-armhf-full.img

## Prerequisite
### Install required package and Python module
```shell  
$ sudo apt-get update
$ sudo apt-get install -y x11vnc python3-dev python3-pip libsdl1.2-dev 
$ sudo pip3 install spidev evdev
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
* [【Pi 4套餐B】Raspberry Pi 4 Model B/2G + SanDisk 32G microSD卡 + 官方原廠5.1V/3A電源](https://www.piepie.com.tw/31200/pi4b-2g-microsd-power-supply/)
* [GPIO Starter Kit](https://www.piepie.com.tw/2557/gpio-game-console-starter-kit)
* [More...](https://www.piepie.com.tw/purchase)
