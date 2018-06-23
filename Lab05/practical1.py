def isValidOutput(fileName):
#Takes in a filename containing a completed Sudoku puzzle
    #Verify whether the solution is valid or not.
        #Check that each number exists only once in its row, and column.
            #Load the file using with
            #For each character_test in the current row
                #For each row
                    #For each iterated character in the row
                        #Check if the character_test is = it_char
                        #If true, return invalid, exit.
            #Return valid.

    count = 0

    with open(fileName) as myFile:
        #Grab the lines of data
        all_lines = myFile.readlines()

    print(all_lines)
    #print(all_lines[1])
    #print(all_lines[0][0])

    #Define row
    #row = all_lines[0]
    #Test first row by itself, exclude first char.

    #for test_char in all_lines[0].strip():
    #    print(test_char)

    #for test_char in all_lines[0].strip():
    #    print(test_char)
    #    for it_char in row[1:].strip():
    #        print(row[1:])
    #        print(it_char)
    #        if(test_char == it_char):
    #            return False

    #Now test the succeeding rows.

    boolVal = True

    for row in all_lines:
        #print(row)
        for test_char in row.strip():
            count += 1
            row1 = row[0:(count-1)]
            row2 = row[count:]
            #print(test_char)
            #print(count)
            #print(row1)
            #print(row2)
            if(test_char in row2 or test_char in row1):
                #print(row[1:])
                boolVal = False
        count = 0

    return boolVal


def isColumnPuzzle(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def solvePuzzle(sourceFileName, targetFileName):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def getCallersOf(phoneNumber):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def getCallActivity():

    # TODO: Remove the "pass" before you add any code to this block.
    pass


if __name__ == "__main__":

    print(isValidOutput('invalid1.sud'))
