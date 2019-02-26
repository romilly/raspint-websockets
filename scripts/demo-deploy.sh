#!/usr/bin/env bash
cd ..
TARGET_HOST=pi@sockety.local

ssh $TARGET_HOST 'mkdir -p raspint-websockets'
rsync -azP src/ $TARGET_HOST:raspint-websockets/src