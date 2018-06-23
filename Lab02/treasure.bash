#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-09-07 12:01:15 -0400 (Wed, 07 Sep 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Lab02/treasure.bash $
# $Revision: 93294 $

filename=$1
numArgs=$#

found=0

if (( $numArgs != 1 ))
then
    echo Usage: ./treasure.bash '<filename>'
    exit 1
else
    #Grab the value of N
    N=$(wc -l $filename | cut -d' ' -f1)
    ((N_2=N*N))
    
    counter=0
   
    #Build scalar 1-D array
    while read line
    do
        for element in $line
        do      
            Arr[counter]=$element
            ((counter=counter+1))
        done
    done < $filename

    echo '(0,0)'
    currentIndex=0
    oldChar1=0
    oldChar2=0 
    char1=$(echo ${Arr[$currentIndex]} | cut -c1)
    char2=$(echo ${Arr[$currentIndex]} | cut -c2)
    number="$char1$char2"
    coordinates="$oldChar1$oldChar2"

    while [[ $coordinates != $number ]]
    do
       oldChar1=$(echo ${Arr[$currentIndex]} | cut -c1)
       oldChar2=$(echo ${Arr[$currentIndex]} | cut -c2) 
       coordinates="$oldChar1$oldChar2" 
       ((currentIndex=N*char1+char2))
       char1=$(echo ${Arr[$currentIndex]} | cut -c1)
       char2=$(echo ${Arr[$currentIndex]} | cut -c2)
       number="$char1$char2"
       echo "($oldChar1,$oldChar2)"
    done
    
    found=1
    echo Treasure found at: "($char1,$char2)"
fi
exit 0
