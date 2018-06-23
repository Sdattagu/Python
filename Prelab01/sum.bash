#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-24 19:23:59 -0400 (Wed, 24 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab01/sum.bash $
# $Revision: 91832 $

#Sums all values passed and prints the sum.
#Assumes at least two values will be passed on the command line.
#Assumes that all passed in values are integers.

sum=0 
num_args=$#

while (( $#!=0 ))
do
    ((sum=sum+$1))
    shift
done

echo "${sum}"
exit 0
