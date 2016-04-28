#! /bin/bash
# @haimapi, 20160418
# Usage: 
# type: ./log_to_file.sh e1_i or e2_i in the terminal 
# at the ith location

# file for training
for i in {1..30}
do
    iwlist wlan0 scanning >> $1tr
done

# file for testing
for i in {1..10}
do 
    iwlist wlan0 scanning >> $1te
done
