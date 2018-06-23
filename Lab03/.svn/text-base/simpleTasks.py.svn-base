

# The following variable(s) are the only lines of code that should be outside of a function.

accounts = [
    'Mark Thomas:    $11.99   $52.08   $81.15   $79.16   $16.23   $88.11   $21.20   $0.02   ',
    'Gregory Powell:      $97.42     $96.05     $71.82     $24.79     $14.42     $60.84     $35.46     ',
    'Kevin Wood:     $93.37    $16.73    $97.05    $14.57    $53.29    ',
    'Martin Watson:     $20.53    $90.58    $22.07    $1.28    $75.40    $48.98    $36.46    $42.65    $5.01  $52.62  ',
    'Frank Young:     $32.02    $51.20    $0.99    $51.85    $88.38    $67.26    $62.72    $47.36    $38.89    ',
    'Michelle Thompson:     $2.44    $100.72    $81.44    $48.07    $68.71    $23.11    $79.23    $71.02    ',
    'Anne Harris:     $30.10    $58.32    $6.22    $3.67    $30.02    $37.65    $6.17    $41.30    $51.15    ',
    'Kelly Cooper:      $73.74     $57.63     $91.94     $42.94     $59.26     $64.30     $13.59     $19.69     $4.11 ',
    'Benjamin Foster:      $4.22     $63.02     $73.07     $99.73     $24.00     $77.79     $20.30     ',
    'Marie Perry:    $32.90   $80.27   $70.18   $68.74   $14.11   $7.38   ',
    'Cynthia Simmons:      $91.64     $56.95     $40.73     $61.28     $53.88     $77.05     $6.88     $23.37     ']

def getRowSum(accList):

    # TODO: Remove the "pass" before you add any code to this block.

    #For each item in accList
        #Split up into list of strings delimited by whitespace
        #Slice from [2] onwards (get rid of the name)
        #For each item in list from [2] onwards
            #Add to an accumulator
        #Result += accum
    #Return result

    result = []
    accumulator = 0.0

    for item1 in accList:
        accumulator = 0.0
        singleAccountName = item1.split()
        singleAccountNumbers = singleAccountName[2:]
        for item2 in singleAccountNumbers:
            accumulator += float(item2[1:])
        result.append(round(accumulator,2))

    return result


def getDoublePalindromes():

    # TODO: Remove the "pass" before you add any code to this block.

    temp1 = ""
    temp2 = ""
    temp3 = ""
    temp4 = ""
    resultTempDec = []
    resultTempBin = []
    result = []
    binVer = 0

    for item1 in range(10, 1000001):
        temp1 = str(item1)
        temp2 = str(item1)[::-1]
        temp3 = str(bin(item1))[2:]
        temp4 = str(bin(item1))[2:][::-1]

        if(temp1 == temp2):
            if(temp3 == temp4):
                result.append(item1)

    return result

def scaleVector(s, vList):

    # TODO: Remove the "pass" before you add any code to this block.
    #For each element in vList
        #Multiply by s
        #Append this to result list

    result = []

    if(type(s) is not float and type(s) is not int):
        return None
    elif(list is not type(vList) or list == []):
        return None
    else:
        for item1 in vList:
            mul = s*item1
            result.append(mul)


    return result


def convertToBoolean(num):

    # TODO: Remove the "pass" before you add any code to this block.
    #Convert to binary using bin()
    #Take from [2] onwards, store in blah
    #Check length of the string (blah), if less than 8, append 0
    #var = ("{:09d}".format(n))

    binVer = bin(num)
    blah = binVer[2:]
    result = []

    if(type(num) is not int):
       return None
    elif(num < 0 or num > 255):
       return None

    while(len(blah) < 8):
        blah = '0' + blah;

    for item1 in str(blah):
        if(item1 == '0'):
            result.append(False)
        elif(item1 == '1'):
            result.append(True)

    return result



def convertToInteger(boolList):

    # TODO: Remove the "pass" before you add any code to this block.

    result = ""

    if(type(boolList) is not list):
        return None
    elif(boolList == []):
        return None

    for item1 in boolList:
        if(item1 == True):
            result += '1'
        elif(item1 == False):
            result += '0'

    resultInt = int(result, 2)
    return result


    pass


def getWords(sentence, n):

    # TODO: Remove the "pass" before you add any code to this block.
    # sentence is a string
    # split sentence up into a blah on whitespace
    #for item1 in blah
        #Check length, if it matches n,
            #Check if it already exists in result, if not
                #Add to result list

    result = []

    blah = sentence.split()
    for item1 in blah:
        if(len(item1) == n):
            if(item1 not in result):
                result.append(item1)

    return result



def isSubListOf(superList, subList):

    # TODO: Remove the "pass" before you add any code to this block.

    #Check that sub and super are list
    #Check that len(sub) < len(super)

    #Take the superlist, convert it into a string
        #Take each element, cast to string, and store into strSuper
    #strList = " ".join(strSuper)

    #Take the sublist, convert it into a string
        #Take each element, cast to string, and store into strSub
    #strSub = " ".join(strSub)

    #Do "in" operator

    strSuper = " "
    strSub = " "

    if(type(superList) is not list):
        return None
    elif(type(subList) is not list):
        return None
    elif(len(subList) > len(superList)):
        return None

    for item1 in superList:
        temp = str(item1)
        strSuper += temp
    strList = " ".join(strSuper)

    for item2 in subList:
        temp2 = str(item2)
        strSub += temp2
    strList2 = " ".join(strSub)

    if((strList in strList2) == True):
        return True
    else:
        return False


def getElementsAt(l, i):

    # TODO: Remove the "pass" before you add any code to this block.
    #For item1 in list
        #If(len(item1) < i)
            #Add 0 to the result
        #Else
            #Add the element at that index to result

    result = []

    for item1 in l:
        if(len(item1) > i):
            result.append(item1[i])
        else:
            result.append(0)

    return result


if __name__ == "__main__":
    # TODO: Remove the "pass" before you add any code to this block.
    l = [0, 1, 2, 3]
    bList = [True, False, False, False, False, True, True, True]
    sentence = "the power of this engine matches that of the one we use last year"
    su = [0, -3, 2, 2, 8, 1, 4]
    sb = [8, 2]
    l1 = [[9, 1, 0, 3], [1, 3, 7], [11, 35, 96, -1, 85], [43, 17]]
    getRowSum(accounts)
    scaleVector(3.14, l)
    convertToBoolean(135)
    convertToInteger(bList)
    getWords(sentence, 4)
    isSubListOf(su, sb)
    getElementsAt(l1, 2)
    getDoublePalindromes()
