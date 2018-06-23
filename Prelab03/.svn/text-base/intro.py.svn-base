#Shounak Dattagupta
#Prelab03
#9/11/2016

def getHeadAverage(l,n):

    #Slice the list to obtain first "n" elements
        #var = {l[0], ... ,l[n-1]}
    var = l[:n]
    #Take sum of list elements
    summation = sum(var)
    #Get length of list var
    length = len(var)
    #Calculate average; summation/length
    average = summation / length
    #Return average
    return average

def getTailAverage(l,m):

    length = m
    #Reverse the list in place
    reversedList = l.reverse()
    #Slice the reversed list to obtain last "n" elements
    var = l[:m]
    #Take sum of list elements
    summation = sum(var)
    #Calculate average;
    average = summation / length
    #Return average
    return average

def getTailMax(l, m):

    #Reverse the list
    l.reverse()
    #Slice to get "last" m elements (from reversed list)
    var = l[:m]
    #Sort the sliced list in ascending order
    var.sort()
    #Reverse the list (Max is arr[0])
    var.reverse()
    #Assign max
    maximum = var[0]
    #Return max
    return maximum

def getNumberAverage(l):
#The passed parameter is a mixed list (numbers, strings, Booleans)
    #Slice the list to obtain first "n" elements
        #var = {l[0], ... ,l[n-1]}
    var = l[:]
    #Take sum of list elements
    summation = sum(var)
    #Get length of list var
    length = len(var)
    #Calculate average; summation/length
    average = summation / length
    #Return average
    return average

def getFormattedSSN(n):
#n is an integer representing Social Security Number
    #Arguments are passed as strings (can use len(n) to get number of digits).
    #Return a string formatted as XXX-XX-XXX
        #Prepend the given number with zeroes, if it contains less than 9 digits

    #Set var as a string of prepended 0's to n
    var = ("{:09d}".format(n))

    #Slice var into three pieces
        #First piece of SSN: 3 digits
    varSSNA = var[0:3]
        #Second piece of SSN: 2 digits
    varSSNB = var[3:5]
        #Third piece of SSN: 4 digits
    varSSNC = var[5:9]

    #Concatenate SSN with formatting
    SSN = varSSNA + "-" + varSSNB + "-" + varSSNC

    #Return complete SSN
    return SSN


def findName(l,s):

    #Get length of the list
    #For loop run through each item in l
        #For each item in l, slice into first and last name
        #StrVar.split() splits into a list on whitespace
        #First and Last name are the two elements in the list, respectively
            # check if s is either first or last name (item exists?)
                #If s exists in item, return that item of l

    length = len(l)

    for Item in l:
        Name = Item.split(" ")
        firstName = Name[0]
        lastName = Name[1]

        nameListFirst = [firstName]
        nameListLast = [lastName]

        if((s in nameListFirst) == True):
            return Item
        elif((s in nameListLast) == True):
            return Item

def getColumnSum(mat):

    #Check how many lists there are in mat
    #Get "n" (columns)
    #Get "m" (rows)
    listsInMat = len(mat)
    n = len(mat[0])
    m = listsInMat

    #Create result
    result = []
    for item1 in range(n):
        result.append(0)

    item4 = 0
    for item2 in range(n):
        for item3 in range(m):
            result[item4] += (mat[item3])[item2]
        item4 += 1

    return result

def getFormattedNames(ln):
    #ln = ["George", "W", "Bush"]

    result = []
    print(ln)
    for item1 in range(len(ln)):
        lastName = (ln[item1])[2]
        MI = ln[item1][1]
        firstName = ln[item1][0]
        T = [lastName + ", " + firstName + " " + MI + "."]
        result = result + T

    return result

def getElementwiseSum(l1, l2):

    #Create result list
    result = []

    #Get lengths of l1 and l2
    length_L1 = len(l1)
    length_L2 = len(l2)

    #Find how long the result list will be and create the intermediate list (for adding)
    #Sum the viable elements
        #If list 1 is longer, then L2 elements can be added
            #med_length = length_L2
            #length_L3 (result list) = length of the shorter list (non-added elements are appended later)
            #med_list = L1+L2 = L1[:length_L2]
        #Else if list 2 is longer, then L1 elements can be added
            #med_length = length_L1
            #length_L3 (result list) = length of the shorter list (non-added elements are appended later)
            #med_list = L1+L2 = L2[:length_L1]
        #Once length of shortest list is found, range(shortest_length) creates a sequence from 0 -> s_l for looping.
        #Else, the lists are equal length, and can be added easily.
    #Append non-summed elements of longer list to result list.
        #Slice the non-summed elements out of longer list
        #Append in for loop
    #Return result

    if((length_L1 - length_L2) > 0):
        med_length = length_L2
        append_length = length_L1 - length_L2
        length_L3 = length_L1
        med_list = l1[:length_L2]

        for item1 in range(med_length):
            result.append(l1[item1] + l2[item1])

        elementsToAppend = l1[med_length:length_L1]
        for item2 in elementsToAppend:
            result.append(item2)

    elif((length_L2 - length_L1) > 0):
        med_length = length_L1
        length_L3 = length_L2
        med_list = l2[:length_L1]

        for item1 in range(med_length):
            result.append(l1[item1] + l2[item1])

        elementsToAppend = l2[med_length:length_L2]
        for item2 in elementsToAppend:
            result.append(item2)

    else:
        for item1 in range(length_L1):
            result.append(l1[item1] + l2[item1])

    return result


def removeDuplicates(l):
    #l is a list possibly containing duplicate elements
    #For each element in l,
        #Check if that element exists in l using "in" membership operator
        #If it exists
            #Number of times x appears in list = list.count(x)
            #While number of times x appears in the list (list.count(x)) != 0
                #Return index in the list of first item whose value is "element" (list.index(x))
                #Remove element at the returned index from the list (list.remove(x))
                #appearCount--
    u = []

    #for element in l:
    #    appearCount = l.count(element)
    #    while appearCount > 1:
    #        index = l.index(element)
    #        l.remove(element)
    #        appearCount -= 1
    #    u.append(element)

    for element in l:
        if((element in u) != True):
            u.append(element)

    return u

def getMaxOccurrence(l):
    #l is a list with possible repeat elements
    #First get a list with the unique elements by calling removeDuplicates
    #Then, for each element in the trimmed list, check occurrences
        #If the next element has a higher count, replace

    maxOccur = 0
    maxOccurElement = 0
    trimmedList = removeDuplicates(l)

    for item1 in trimmedList:
        appearCount = l.count(item1)
        if(appearCount >= maxOccur):
            maxOccur = appearCount
            maxOccurElement = item1

    return maxOccurElement

def getMaxProduct(l):
    #Check first case
        #operand1 = l[0], #operand2 = l[1], #operand3 = l[2]
        #product > 0?
    #Check last case
        #operand1 = l[len(l) - 1], operand2 = ...
        #product > 0?

    #For each element except for the very first (index[0]) and very last (index[len(l)-1])
        #Make the current element operand1
        #If the consecutive element on the left is > operand2
            #Make it operand 2
        #If the consecutive element on the right is > operand3
            #Make it operand 3
        #Take the product of the three (runningProduct)
            #If runningProduct > currentProduct
                #currentProduct = runningProduct


    operand1 = 0
    operand2 = 0
    operand3 = 0
    runningProduct = 0
    currentProduct = 0
    length = len(l)

    #First case
    operand1 = l[0]
    operand2 = l[1]
    operand3 = l[2]
    runningProduct = operand1 * operand2 * operand3
    if(runningProduct > currentProduct):
        currentProduct = runningProduct

    #Last case
    operand1 = l[len(l) - 1]
    operand2 = l[len(l) - 2]
    operand3 = l[len(l) - 3]
    runningProduct = operand1 * operand2 * operand3
    if(runningProduct > currentProduct):
        currentProduct = runningProduct

    blah = range(length)
    new_l = blah[1:(length-1)]

    for item1 in new_l:
        operand1 = l[item1]
        operand2 = l[item1 - 1]
        operand3 = l[item1 + 1]
        runningProduct = operand1 * operand2 * operand3
        if(runningProduct > currentProduct):
            currentProduct = runningProduct

    return currentProduct

if __name__ == "__main__":

    #Sample lists
    list = [1, 2, 3, 4, 5, 6, 1]
    mixedList = [2, 1.2]
    n = 1657649
    nameList = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    name = "Johnson"
    ln = [["George", "W", "Bush"], ["John", "F", "Abraham"]]
    l1 = [1, 3, 5, 7, 9, 11]
    l2 = [6, 4, 2, 1, 4, 5]
    l3 = [3, 7, -2, 2, 3, 5, -4, 5, 1, 2, 12, 74]
    l = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    mat = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

    #Use case for getHeadAverage
    resultAverageHead = getHeadAverage(list, 3)
    print("getAverageHead result is: ")
    print(resultAverageHead)
    #Use case for getTailAverage
    #resultAverageTail = getTailAverage(list, 3)
    #print("getAverageTail result is: ")
    #print(resultAverageTail)
    #Use case for getTailMax
    resultTailMax = getTailMax(list, 2)
    print("getTailMax is: ")
    print(resultTailMax)
    #Use case for getNumberAverage (mixed list)
    resultAverageMixed = getNumberAverage(mixedList)
    print("Average of mixed list is: ")
    print(resultAverageMixed)
    #Use case for getFormattedSSN
    resultGetFormattedSSN = getFormattedSSN(n)
    print("Number of digits in n is: ")
    print(resultGetFormattedSSN)
    #Use case for findName
    resultFindName = findName(nameList, name)
    print("The full name is: ")
    print(resultFindName)
    #Use case for getFormattedNames
    resultFormattedNames = getFormattedNames(ln)
    print(resultFormattedNames)
    #Use case for getElementWiseSum
    resultElementWiseSum = getElementwiseSum(l1, l2)
    print("Element Wise Sum: ")
    print(resultElementWiseSum)
    #Use case for removeDuplicates
    resultRemoveDuplicates = removeDuplicates(l)
    print("Remove duplicates: ")
    print(resultRemoveDuplicates)
    #Use case for getColumnSum
    resultColumnSum = getColumnSum(mat)
    print("Column Sum: ")
    print(resultColumnSum)
    #Use case for getMaxOccurrence
    resultMaxOccurrence = getMaxOccurrence(l)
    print("Max Occurrence: ")
    print(resultMaxOccurrence)
    #Use case for getMaxProduct
    resultMaxProduct = getMaxProduct(l3)
    print("Max Product: ")
    print(resultMaxProduct)





