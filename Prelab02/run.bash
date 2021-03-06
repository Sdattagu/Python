#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-09-04 15:45:14 -0400 (Sun, 04 Sep 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab02/run.bash $
# $Revision: 92961 $

#File parameters
filename=$1
outputFile=$2
numArgs=$#

#Result elements
cacheSize=0
issueWidth=0
CPI=0
executionTime=0

#Best metrics
bestProcessorName=""
bestCacheSize=0
bestIssueWidth=0
bestCPI=0
bestExecutionTime=99999

if (( numArgs==0 ))
then
    echo Usage: ./run.bash '<filename>'
elif (( numArgs==1 ))
then
    echo Please specify a file to save script output.
else

    #Check if sim_out already exists
    if [[ -e $outputFile ]]
    then
        echo sim_out.txt exists. Would you like to delete it? 
        read userResponseOne 
        if [[ $userResponseOne == y ]] || [[ $userResponseOne == yes ]]
        then
            rm $outputFile
        else
            echo Enter a new filename: 
            read userResponseTwo 
            outputFile=$userResponseTwo
        fi
    fi
    
    #Check for compilation errors
    STATUS=$(gcc $filename -o quick_sim 1>$outputFile)
    if [[ ! -z "${STATUS// }" ]] #There were errors
    then
        echo error: quick_sim could not be compiled!
        exit 1
    else

        #Open sim_out for writing
        exec 4> $outputFile

        #Generate the output file results
        #Generate Cache Sizes
        for (( cacheSize = 1; cacheSize <= 32; ((cacheSize=cacheSize*2)) ))
        do
            #Generate Issue Widths
            for (( issueWidth = 1; issueWidth <= 16; ((issueWidth=issueWidth*2)) ))
            do

                #Write results of executed binary to temp files to extract CPI and Execution time
                #CPI: -f8
                #Execution time: -f10 

                quick_sim $cacheSize $issueWidth a > temp_AMD.txt 
                CPI=$(cut -d':' -f8 temp_AMD.txt)
                executionTime=$(cut -d':' -f10 temp_AMD.txt)
                #Write results of AMD to outputFile
                echo AMD Opteron:$cacheSize:$issueWidth:$CPI:$executionTime >&4

                if (( $executionTime < $bestExecutionTime ))
                then
                    bestProcessorName="AMD Opteron"
                    bestCacheSize=$cacheSize
                    bestIssueWidth=$issueWidth
                    bestCPI=$CPI
                    bestExecutionTime=$executionTime
                fi
                    

                quick_sim $cacheSize $issueWidth i > temp_Intel.txt
                CPI=$(cut -d':' -f8 temp_Intel.txt)
                executionTime=$(cut -d':' -f10 temp_Intel.txt)
                #Write results of Intel to outputFile
                echo Intel Core i7:$cacheSize:$issueWidth:$CPI:$executionTime >&4

                if (( $executionTime < $bestExecutionTime ))
                then
                    bestProcessorName="Intel Core i7"
                    bestCacheSize=$cacheSize
                    bestIssueWidth=$issueWidth
                    bestCPI=$CPI
                    bestExecutionTime=$executionTime
                fi

            
            done
        done
    fi

    #Remove all temporary text files
    rm temp_AMD.txt
    rm temp_Intel.txt

    echo Fastest run time achieved by $bestProcessorName with cache size $bestCacheSize and issue width $bestIssueWidth was $bestExecutionTime



fi
exit 0
