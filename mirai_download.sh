#!/bin/bash

start_time=`date "+%Y-%m-%d %H:%M:%S"`

python downloader.py

end_time=`date "+%Y-%m-%d %H:%M:%S"`

echo $start_time
echo $end_time