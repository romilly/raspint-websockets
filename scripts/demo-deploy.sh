#!/usr/bin/env bash
cd ~/git/active/raspint-websockets
TARGET=pi@sockety.local
ssh $TARGET 'mkdir -p socket-demo'
rsync -azP src/ $TARGET:raspint-websockets/src
