#! /bin/bash

# $Author: ee364g03 $
# $Date: 2016-09-28 11:21:11 -0400 (Wed, 28 Sep 2016) $

function func_a 
{
    # Fill out your answer here.
    ls *.pdf | wc -l
    return    
}

function func_b
{
    # Fill out your answer here
    diff foo1.txt foo2.txt > temp.txt 
    return
}

function func_c 
{
    # Fill out your answer here
    gcc windows8.c 1>compile.out 2>compile.out
    return
}

function func_d 
{
    # Fill out your answer here
    Arr=(a.txt b.txt c.txt d.txt e.txt)
    randomnum=$(($RANDOM % 5))
    randomtxt=${Arr[$randomnum]}
    randomline=$(cat $randomtxt | head -c 7 | cat -c 2)
    echo $randomline
    return 
}

function func_e
{
    # Fill out your answer here
    
    return
}

#
# To test your function, you can call it below like this:
#
# func_a
#
