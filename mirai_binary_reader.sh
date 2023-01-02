#!/bin/bash

start_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

python binary_reader.py

end_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

echo start,$start_time >> ./binary_log.csv
echo end,$end_time >> ./binary_log.csv