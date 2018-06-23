#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-09-04 14:01:43 -0400 (Sun, 04 Sep 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab02/yards.bash $
# $Revision: 92938 $

filename=$1
numArgs=$#
localSumAverage=0
localSumVariance=0
localAverage=0
localVariance=0
highestAverage=0

N=0
x_i=0

#Output the AVERAGE (localAverage) receiving yards and VARIANCE (localVariance) in receiving yards per conference
#Also output the highest AVERAGE (highestAverage) number of receiving yards among all conferences
#Var = 1/N * SUM((x - mew)^2)
    #N is the number of elements on a line
    #x is an individual element
    #mew is the average for the current line

if (( numArgs==0 ))
then
    echo Usage: yards.bash '<filename>'
elif [[ $filename != 'stats.txt' ]]
then
    echo Error: $filename is not readable
fi

if [[ -r $filename ]]
then
    while read line
    do
    #CALCULATE AVERAGE
        #Get elements on the line, plus the conference name
        N_temp=$(echo $line | wc -w)        
        conferenceName=$(echo $line | cut -d' ' -f1)

        #Number of elements (School yards)
        ((N=N_temp-1)) 

        #Convert line read into an array
        Arr=($line)

        #Sum up all elements in the array
        for (( i = 1; i <= $N; i++ ))
        do
            #echo Element being added is: ${Arr[i]}
            ((localSumAverage=localSumAverage+${Arr[i]}))
            #echo Current local sum is: $localSum
        done
        
        #Calculate local average
        ((localAverage=localSumAverage/N))
        
        #Calculate highest average
        if (( $localAverage > $highestAverage ))
        then
            highestAverage=$localAverage
        fi

    #CALCULATE VARIANCE
        
        for (( i = 1; i <= $N; i++ ))
        do
            #Get difference within summation
            ((varDifference=${Arr[i]} - localAverage))
                
            #Square the difference
            ((varDifference=varDifference*varDifference))

            #Add to running sum
            ((localSumVariance=localSumVariance+varDifference))
        done

        #Multiply by scaling factor of 1/N
        ((localVariance=localSumVariance/N))

        echo $conferenceName schools averaged $localAverage yards receiving with a variance of $localVariance

        #Clean up variables for next run
        localSumAverage=0
        localSumVariance=0
        localAverage=0
        localVariance=0
            
    done < $filename
    echo The largest average yardage was $highestAverage
fi
exit 0
