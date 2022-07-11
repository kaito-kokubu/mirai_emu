#!/bin/bash

start_time_1=`date "+%Y-%m-%d %H:%M:%S.%6N"`

python binary_reader.py

end_time_1=`date "+%Y-%m-%d %H:%M:%S.%6N"`

#sleep 5

#start_time_2=`date "+%Y-%m-%d %H:%M:%S"`

#python binary_reader.py

#end_time_2=`date "+%Y-%m-%d %H:%M:%S"`

#sleep 5

#start_time_3=`date "+%Y-%m-%d %H:%M:%S"`

#python binary_reader.py

#end_time_3=`date "+%Y-%m-%d %H:%M:%S"`

echo $start_time_1
echo $end_time_1
#echo $start_time_2
#echo $end_time_2
#echo $start_time_3
#echo $end_time_3