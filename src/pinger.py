#! /usr/bin/python3
import datetime
import os
from time import sleep
from sys import stdout


HOSTS = ['cluster-001', 'cluster-002' , 'cluster-003' , 'cluster-004',
                     'raspberry-stretch', 'posty-ssd' , 'posty-ssd2' , 'posty-ssd3']


def ping(name):
    response = os.system("ping -c 1 > /dev/null 2> /dev/null " + name)
    return 'UP' if response == 0 else 'DOWN'


def status_of(name):
    return '%20s: %s' % (name, ping(name))


while True:
    print('clear')
    stdout.flush()
    for name in HOSTS:
        print(status_of(name))
    now = datetime.datetime.now()
    t = '\r\ntime %s' % datetime.datetime.now().strftime('%Y-%M-%d %H:%M:%S')
    print(t)
    stdout.flush()
    sleep(10)
