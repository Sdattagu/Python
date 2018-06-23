#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-31 10:16:05 -0400 (Wed, 31 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Lab01/collect_stats.bash $
# $Revision: 92753 $

#Script should accept two arguments
    #(a) Name of the data file
    #(b) Name of the olympic sport

numArgs=$#
numOfFile=$0
numAthletesTotal=0
numMedalsTotal=0
nameAthleteMax=""
numMedalsWonMax=0

filename=olympics.txt

if (($numArgs != 2 ))
then
    echo Please provide two arguments.
    exit 1
elif [[ ! -e $1 ]] 
then 
    echo First argument is a non-existent file.
    exit 2
else
    while read line
    do
        #Number of athletes in the sport
        #get the sport on that line 
        N0=$(echo $line | cut -d',' -f2) 
        #echo $N0
        #If the grabbed sport matches the provided arg sport
        if [[ $N0 == $2 ]] 
        then
            numAthletesTotal=$((numAthletesTotal+1))
            #Grab number of medals this person won, add to running total
            N1=$(echo $line | cut -d',' -f3)
            #echo $N1
            numMedalsTotal=$((numMedalsTotal+N1))
            #If this athlete's medals are greater than current max, replace
            if (( $N1 > $numMedalsWonMax ))
            then
                #echo numMedalsWonMax is now $N1
                numMedalsWonMax=$N1
                nameAthleteMax=$(echo $line | cut -d',' -f1)
            fi           
        fi

    done < $filename
    
    #Printing final results
    echo Total athletes: $numAthletesTotal
    echo Total medals won: $numMedalsTotal
    echo $nameAthleteMax won the most medals: $numMedalsWonMax
fi    
    

exit 0
