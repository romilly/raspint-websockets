#! /usr/bin/python3

import os
from time import sleep
from sys import stdout


def ping(name):
    response = os.system("ping -c 1 > /dev/null 2> /dev/null " + name)
    return 'UP' if response == 0 else 'DOWN'

while True:
    for hostname in ['cluster-001', 'cluster-002' , 'cluster-003' , 'cluster-004',
                     'raspberry-stretch', 'posty-ssd' , 'posty-ssd2' , 'posty-ssd3']:
        print(hostname, ping(hostname))
        stdout.flush()
    sleep(1.0)
