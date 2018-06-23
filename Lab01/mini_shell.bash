#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-31 10:54:35 -0400 (Wed, 31 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Lab01/mini_shell.bash $
# $Revision: 92781 $

#Compare to string hello, if true, print username to terminal.
while ((1==1))
do

#Enter a command 
read -p "Enter a command: " userCommand

    if [[ $userCommand == hello ]]
    then
        echo Hello $USER
    
    elif [[ $userCommand == quit ]]
    then
        echo Goodbye
        exit 0
    
    elif [[ $userCommand == compile ]] 
    then
        
        for File in *.c
        do
            oVersion=$(echo $File | cut -d'.' -f1)
            gcc -Wall -Werror ${File} -o ${oVersion}.o
             if (($? == 0 ))
             then
                 echo Compilation succeded for: ${File}
             else
                 echo Compilation failed for: ${File}
             fi
        done
    
    elif [[ $userCommand == run ]] 
    then 
        read -p "Enter filename: " filename
        read -p "Enter arguments: " arguments
        if [[ ! -x $filename ]] || [[ ! -e $filename ]]
        then
            echo Invalid filename, or does not exist 
        else
            "./"${filename} ${arguments}
        fi
    
    else
        echo Error: unrecognized input
    
    fi
    echo 
done
exit 0




