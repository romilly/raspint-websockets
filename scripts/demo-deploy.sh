#!/usr/bin/env bash
cd ~/git/active/websockets
TARGET=pi@sockety.local
ssh $TARGET 'mkdir -p socket-demo'
rsync -azP src/ $TARGET:websockets
