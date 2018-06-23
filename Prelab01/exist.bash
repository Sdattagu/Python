#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-25 15:06:08 -0400 (Thu, 25 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab01/exist.bash $
# $Revision: 91877 $

#Takes list of filenames as an argument
#For each filename, 
    # IF File exists: print message: File <filename> is readable!
    # ELSE  IF file cannot be read: Create an empty file with that name (touch command)

#Note: When a value in a prelab or lab is presented as <variable>, it means to print the VALUE of the variable, not the STRING '<variable>'.

path=$0
num_args=$#

while (( $#!=0 ))
do
    if [[ -r $1 ]]
    then
        echo File $1 is readable!
    else
        touch $1
    fi

    shift
done

exit 0
