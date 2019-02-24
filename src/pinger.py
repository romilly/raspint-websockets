#! /usr/bin/python3
import datetime
import os
from time import sleep
from sys import stdout


HOSTS = ['cluster-001', 'cluster-002' , 'cluster-003' , 'cluster-004',
                     'raspberry-stretch', 'posty-ssd' , 'posty-ssd2' , 'posty-ssd3']


def ping(name):
    response = os.system("ping -w 1 -c 1 > /dev/null 2> /dev/null " + name)
    return 'UP' if response == 0 else 'DOWN'


def status_of(name):
    return '%20s: %s' % (name, ping(name))


def paf(text):
    print(text);
    stdout.flush()


while True:
    paf('*begin*')
    for name in HOSTS:
        paf(status_of(name))
    paf('time %s' % datetime.datetime.now().strftime('%Y-%M-%d %H:%M:%S'))
    paf('*end*')
    sleep(1)
