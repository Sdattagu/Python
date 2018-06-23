#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-27 16:14:52 -0400 (Sat, 27 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab01/check_file.bash $
# $Revision: 92060 $

#Checks the following attributes in the exact order as given below and prints out the results
# -e    Exists
# -d    Directory
# -f    Ordinary File
# -r    Readable
# -w    Writable
# -x    Executable

path=$0
num_args=$#
X=1

if (( num_args!=1 ))
then
    echo Usage: ./check_file.bash '<filename>'
elif (( num_args==1 ))
then
    if [[ -e $1 ]]
    then
        echo $1 exists
    else
        echo $1 does not exist
    fi

    if [[ -d $1 ]]
    then
        echo $1 is a directory
    else
        echo $1 is not a directory
    fi

    if [[ -f $1 ]]
    then
        echo $1 is an ordinary file
    else
        echo $1 is not an ordinary file
    fi

    if [[ -r $1 ]]
    then
        echo $1 is readable
    else
        echo $1 is not readable
    fi

    if [[ -w $1 ]]
    then
        echo $1 is writable
    else
        echo $1 is not writable
    fi

    if [[ -x $1 ]]
    then
        echo $1 is executable
    else
        echo $1 is not executable
    fi
fi

exit 0
