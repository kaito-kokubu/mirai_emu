#!/bin/bash

start_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

python dictionary_attack.py

end_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

echo start,$start_time >> ./dictionary_log.csv
echo end,$end_time >> ./dictionary_log.csv