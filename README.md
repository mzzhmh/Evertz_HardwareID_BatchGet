# Evertz_HardwareID_BatchGet
SW version batch get for all Evertz Sat Receivers



1. This project firstly does the data cleansing on the 2x parallels dumped raw data file 
and extracts the site and IP information of all the Evertz Satellite receivers from the dumped raw data file.

2. The HardwareIDreader.py will re-format the extracted data and query the Firmware Version of each Evertz Sat Receiver via SNMP.

3. The output will be saved in a .csv file.

4. Jenkinsfile is used for single-click deployment and it is used for running the task. 
It can be used by un-linux background staff to do the batch-get task.


This repo is used for code maintainence and the customer raw data is not uploaded in here.
