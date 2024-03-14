#!/bin/bash

/bin/find /home/XL204913/script/netperf/result/ -type f -name "*.txt" -mtime +7 -exec gzip {} \;
/bin/find /home/XL204913/script/netperf/result/ -type f -name "*.gz" -exec mv {} /home/XL204913/script/netperf/result/archive/ \;
/bin/find /home/XL204913/script/netperf/result/archive/ -type f -name "*.gz"  -mtime +15 -exec rm -f {} \;
