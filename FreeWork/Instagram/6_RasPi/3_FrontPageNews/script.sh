echo "#######################################################"
date +'FORMAT' 
### mm/dd/yyyy ###
date +'%m/%d/%Y' 
## Time in 12 hr format ###
date +'%r'
## backup dir format ##
date_time=$(date +'%m/%d/%Y')
echo "Script starts"
#!/bin/sh
pkill chromium #kill all chromium processes
cd $(dirname $0)
echo $(dirname $0)
python3 /home/pi/Documents/SoftwareProjects/PYTHON/FreeWork/Instagram/6_RasPi/3_FrontPageNews/main.py
echo "Script ends"
echo "#######################################################"
