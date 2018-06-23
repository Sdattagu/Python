#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-09-04 16:57:30 -0400 (Sun, 04 Sep 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab02/process_temps.bash $
# $Revision: 92977 $

filename=$1
numArgs=$#

sumAverage=0
tim=0
localAverage=0
numberOfLines=0
N=0


if (( $numArgs != 1 ))
then
    echo Usage: process_temps.bash "<input file>"
    exit 1
elif [[ ! -r $filename ]] 
then
    echo Error: $filename is not a readable file.
    exit 2
else
    
    #Remove header from input file
    numberOfLines_t=$(wc -l $filename | cut -d' ' -f1)
    ((numberOfLines=numberOfLines_t-1))
    (tail -n $numberOfLines $filename | cat) > temp.txt


    while read line
    do
     #CALCULATE AVERAGE

        tim=$(echo $line | cut -d' ' -f1)
        #Get number of elements on the line
        N_t=$(echo $line | wc -w)
        ((N=N_t-1))

        #Convert line read into an array
        Arr=($line)

        #Sum up all elements in the array
        for (( i = 1; i <= $N; i++ ))
        do
            ((sumAverage=sumAverage+${Arr[i]}))
        done

        #Calculate average of temperatures
        ((localAverage=sumAverage/N))
        
        echo Average temperature for time $tim was $localAverage C.

        #Clean up variables for next run
        sumAverage=0
        tim=0
        localAverage=0
        N=0
    done < temp.txt
    
    #Remove temporary file
    rm temp.txt
fi

exit 0

