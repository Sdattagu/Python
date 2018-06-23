#! /bin/bash
#

# $Author: ee364g03 $
# $Date: 2016-08-28 15:39:45 -0400 (Sun, 28 Aug 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F16/students/ee364g03/Prelab01/svncheck.bash $
# $Revision: 92240 $

#file_list is the $filename.
#This contains a list of all files that need to be added to the SVN repo.
#Read this file line-by-line
    #Check whether the file is in SVN (using svn status)
        #If not in SVN, but exists, make sure it is executable.
            #If it isn't executable, ask the user if they want it to be executable
                #If y, then chmod it.
                #else, leave it alone.
        #Add file to SVN, but do not commit yet.
       
        filename=file_list
        if [[ -r $filename ]]
        then
            while read line
            do
                STATUS=$(svn status line) 
                           
                if [[ -z "${STATUS// }" ]] #File is not in SVN
                then
                   if [[ -e $line ]] #File exists
                   then
                       if [[ ! -x $line ]]
                       then
                           echo Do you want to make file $line executable?
                           read userResponse </dev/tty
                           if [[ $userResponse == y ]]
                           then
                               chmod +x $line
                           fi #leave it as unexecutable if the user didn't say yes.
                       fi
                   svn add $line
                   elif [[ ! -e $line ]] #File is not in SVN, file does not exist
                   then
                       echo Error: File $line appears to not exist here or in svn
                   fi
                 else
                     if [[ ! -x $line ]]
                     then
                        svn propset svn:executable ON $line
                     fi                
                 fi
            done < $filename
            svn commit 
            echo Auto-committing code
        fi
exit 0
