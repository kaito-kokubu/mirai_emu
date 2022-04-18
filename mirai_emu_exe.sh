#!/bin/bash

download_start_time=`date "+%Y-%m-%d %H:%M:%S"`

python downloader.py
 
download_end_time=`date "+%Y-%m-%d %H:%M:%S"`

binary_read_start_time=`date "+%Y-%m-%d %H:%M:%S"`

python binary_reader.py
 
binary_read_end_time=`date "+%Y-%m-%d %H:%M:%S"`

echo $download_start_time
echo $download_end_time
echo $binary_read_start_time
echo $binary_read_end_time