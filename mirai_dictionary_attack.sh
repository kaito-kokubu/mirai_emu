#!/bin/bash

start_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

python dictionary_attack.py

end_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

echo $start_time
echo $end_time