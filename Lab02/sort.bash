#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-09-07 11:20:02 -0400 (Wed, 07 Sep 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Lab02/sort.bash $
# $Revision: 93283 $

filename=$1
numArgs=$#

currentfastestCPU=0
fastestCPU=0
currentLowestCPI=0
lowestCPI=0
CPUcache4=""

if (( $numArgs != 1 ))
then
    echo Usage: ./sort.bash '<filename>'
    exit 1
elif [[ ! -e $filename ]] 
then
    echo Error: $filename does not exist
    exit 2
else
    
      exec 4> cache4.txt 

      #Print the 5 fastest performing CPUs (determined by lowest execution time)
        #Sort the file (containing execution times) in ascending order
        echo The 5 fastest CPUs:
        sort -t',' -k5 -n $filename | head -n 5
      
        #New line in between results
        echo -e 

        #Print the 3 most efficient CPUs (determined by lowest CPI)
        echo the 3 most efficient CPUs:
        sort -t',' -k4 -n $filename | head -n 3

        #New line in between results
        echo -e

        #Print all CPUs that have a cache size of 4, in order of increasing execution time
            #Grab all benchmarks with CPI 4
            while read line
            do
                #Grab cache of current benchmark
                currentCache=$(echo $line | cut -d',' -f2)

                #If cache is 4, throw into temp file (to be sorted)
                if (( currentCache==4 ))
                then
                    echo $line >> cache4.txt
                fi

            done < $filename
            #Finished grabbing all cache 4 entries, now sort. Auto prints to terminal
            echo The CPUs with cache size 4:
            sort -t',' -k5 -n -r cache4.txt

            #New line in between results
            echo -e
            rm cache4.txt

        #Print n slowest CPUs
            echo  "Enter a value for n: " 
            read userValue
        
            #Sort by slowest CPU and print $userValue with head
            sort -t',' -k5 -n -r $filename | head -n $userValue 

            echo -e 

        #Print to a file called sorted_CPI.txt
            sort -t',' -k1,1 -k4,4 $filename 
fi
exit 0
