#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-25 15:06:08 -0400 (Thu, 25 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab01/line_num.bash $
# $Revision: 91877 $

#Uses a loop and READ command 
#Take single filename as an argument and prints out the file with line nubers added to beginning of the lines.
#1) Check that user provided single argument.
    #Provide an error message and exit
#2) Check if file is readable and exit with message: Cannot read <filename> if it isn't.

path=$0
num_args=$#
X=1

if (( num_args!=1 ))
then
    echo Usage: line_num.bash '<filename>'
elif (( num_args==1 ))
then
    if [[ ! -r $1 ]]
    then
        echo Cannot read $1
    else
        filename=$1
        if [[ -r $filename ]]
        then
            while read line
            do
                echo $X:$line
                X=$((X+1))
            done < $filename
        fi 
    fi 
fi

exit 0
