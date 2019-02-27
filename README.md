# Raspberry Pint websockets talk

26 Feb 2019

This contains the source code (Python and HTML + Javascript) for my talk
on using Joe Walnes' wonderful `websocketd`.

To recreate the demo,

1. Clone this repository to a Raspberry Pi or other computer.
1. Install the appropriate webocketd binary from the
[Websockedd releases page](https://github.com/joewalnes/websocketd/releases).
1. Change the hostname in the count.html and rocket.html from `sockety` to
the hostname of the computer on which you installed `websocketd`.
1. To run the count and rocket examples
    1. Change directory on the computer where you installed `websocketd` into the src
    directory of the cloned repository.
    1. run `websocketd --staticdir=./pages --port=8000 ./count.sh`
    1. From a browser, open the rocket page at
    `http://<yourwebsockethostname>:8000/rocket.html`
    
You should see the rocket, the countdown should run down from 10 to zero, and at zero the
background colour of the page should change from green to blue.
