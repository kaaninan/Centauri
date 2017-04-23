#!/bin/bash

rosbag record -j -o blankdata -e "/epoc/(signal|quality)/(.*)"
