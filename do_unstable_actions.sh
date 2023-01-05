#!/bin/bash

while :
do
    if [ $(($RANDOM % 2)) = 1 ]; then
        . ./unstable_action.sh
    fi
    sleep 10
done