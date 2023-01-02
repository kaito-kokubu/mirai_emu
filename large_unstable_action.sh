#!/bin/bash

start_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

python large_unstable_action.py

end_time=`date "+%Y-%m-%d %H:%M:%S.%6N"`

echo start,$start_time >> ./large_unstable_log.csv
echo end,$end_time >> ./large_unstable_log.csv