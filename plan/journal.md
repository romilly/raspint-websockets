# Project journal for websockets

This is the repository for the code I'll be using at the
[Raspberry Pint meetup](https://www.meetup.com/Raspberry-Pint-London/events/hcjzmmyzdbjc/)
on 26 February 2019.

It uses Joe Walnes' wonderful [websocketd](https://github.com/joewalnes/websocketd)


## Tuesday 19 February 2019

I set the project up, downloaded the [32-bit ARM zip](https://github.com/joewalnes/websocketd/release),
 and copied over the scripts and web pages.
 
The demo runs on a Raspberry Pi zero with hostname sockety 
 
I copied the ARM binary to the Pi zero, unzipped it and ran
 
    mkdir ~/bin
    
I rebooted and ran
    
    unzip websocketd-0.3.1-linux_arm.zip
    mv websocketd ~/bin
    chmod a+x ~/bin/websocketd
    
I copied the scripts over to the zero using rsync:

    

    
    
     

