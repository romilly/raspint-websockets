#!/usr/bin/env bash
#!/bin/bash
for ((COUNT = 1; COUNT <= 11; COUNT++)); do
  DOWN=$((11-$COUNT))
  echo $DOWN
  sleep 1
done