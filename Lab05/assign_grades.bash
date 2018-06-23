#! /bin/bash

# $Author: ee364g03 $
# $Date: 2016-09-28 11:21:11 -0400 (Wed, 28 Sep 2016) $

numArgs=$#
filename=$0
schoolAbb=$1

#File is students.db, which is a database of students enrolled in various classes in EE and ME.
#Format:
    #<student> <score>
        #<student> = <school><courseNumber><studentID>

if (( $numArgs != 2 ))
then
    echo Please provide two arguments: a filename and a school abbreviation.
    exit 1
elif [[ ! -r $filename ]] 
then
    echo Error: $filename is not a readable file.
    exit 2
else

    while read line
    do
        studentSchool=$(echo $line | head -c 2)
        if [[ $studentSchool == $schoolAbb ]]
        then
            numericScore=$(echo $line | tail -c 3)
            courseNumber=$(echo $line | head -c 5 | tail -c 3)
            ./get_letter_grade.bash $numericScore
            touch "students.db." + $studentSchool + $courseNumber
        fi
    done < $filename
fi

exit 0
            
