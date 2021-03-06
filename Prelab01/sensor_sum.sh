#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-28 14:53:12 -0400 (Sun, 28 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab01/sensor_sum.sh $
# $Revision: 92205 $

#file_list is the $filename.
#This contains a list of all files that need to be added to the SVN repo.
#Read this file line-by-line
    #Check whether the file is in SVN (using svn status)
        #If not in SVN, but exists, make sure it is executable.
            #If it isn't executable, ask the user if they want it to be executable
                #If y, then chmod it.
                #else, leave it alone.
        #Add file to SVN, but do not commit yet.
        
filename=$1
numArgs=$#
if (( numArgs==0 ))
then
    echo usage: sensor_sum.sh sensors.log 
elif [[ $filename != 'sensors.log' ]]
then
    echo error: $filename is not a readable file!
fi

if [[ -r $filename ]]
then
    while read line
    do
        sensorNumber=$(echo $line | cut -d'-' -f1) #Get sensor number
        N0=$(echo $line | cut -d' ' -f2) #Get N0
        #echo $N0
        N1=$(echo $line | cut -d' ' -f3) #Get N1
        #echo $N1
        N2=$(echo $line | cut -d' ' -f4) #Get N2
        #echo $N2
        ((sum=N0+N1+N2))   #Get sum of sensor values
        echo $sensorNumber $sum
    done < $filename
fi
exit 0
