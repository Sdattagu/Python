#Shounak Dattagupta
#Prelab04
#9/18/2016

import re

def getWords(sentence, letter):
#10/2/2016: Does not match "it" in string.


#Takes a sentence and a single letter
    #Returns a list of the words that start or end with this letter
    #But NOT both
    #Case-insensitive

    #expr = r"([\w.-]+)@([\w.-]+)"
    #expr = r"(^[re.escape(letter)] | [re.escape(letter)]$)"
    expr =   (r"\b" + r"[^ " + re.escape(letter) + r"]" + r"[\w]*" + re.escape(letter) + r"\b") \
           + r"|" \
           + (r"\b" + re.escape(letter) + r"[\w]*" + r"[^" + re.escape(letter) + r" ]" + r"\b")

    #print(expr)
    #print(sentence)
    #print(letter)

    #m2 = re.search(expr, sentence)
    m = re.findall(expr, sentence, re.IGNORECASE)
    #print(m)
    #print(m2)
    return m


def extractFloats(s):
#Takes in a string, returns a list of strings containing all the floats present in the string.
    #Two groups, break upon "."
        #Left side of "." is the int, right side is the decimal

    expr = r"(?P<num>[+-]?\d+\.\d+)"
    #print(s)
    #print(expr)

    m = re.findall(expr, s)

    #print(m)
    return m


def getUrlParts(url):
#Format of URL: http://[BaseAddress]/[Controller]/[Action]?[QueryString]
    #[QueryString] contains LIST of field=value elements, separated by the ampersand symbol.
        #http://www.purdue.edu/Home/Calender?Year=2016&Month=September&Semester=Fall
        #2016&Month, September&Semester

#Take in a URL, return (string, string, string) tuple
    #Base address
    #Controller
    #Action

    exprSplitURL = r"/?" #Split URL based on "/" character, returns LIST[-1] is queryString (arg to second split)
                         #LIST[2] = baseAddress
                         #LIST[3] = Controller
    exprSplitQuery = r"\?" #Split query string based on "?", returns LIST, list[0] is target
    urlSplitList = []
    querySplitList = []
    result = []

    urlSplitList = re.split(exprSplitURL, url)
    querySplitList = re.split(exprSplitQuery, urlSplitList[-1])
    result.append(urlSplitList[2])
    result.append(urlSplitList[3])
    result.append(querySplitList[0])

    return tuple(result)

def getQueryString(url):
#Returns QueryString for further processing


    exprSplitURL = r"/?" #Split URL based on "/" character, returns LIST[-1] is queryString (arg to second split)
                         #LIST[2] = baseAddress
                         #LIST[3] = Controller
    exprSplitQuery = r"\?" #Split query string based on "?", returns LIST, list[0] is target
    querySplitList = []
    result = []

    urlSplitList = re.split(exprSplitURL, url)
    querySplitList = re.split(exprSplitQuery, urlSplitList[-1])
    result.append(urlSplitList[2])
    result.append(urlSplitList[3])
    result.append(querySplitList[0])

    #print(querySplitList[1])
    return querySplitList[1]

def getQueryParameters(url):
#Each query is separated by &
#Each individual query parameter is separated by =
    #Left side of = may have 1+ alpha-numeric characters (+).
    #Right side of = may have 1+ alpha-numeric characters (+).

    listOfQueries = []
    listOfQueryElements = []
    result = []

    getQueriesExpr = r"\&"
    getFieldAndValueExpr = r"\="

    #Grab the [QueryString] using getQueryString(url)
    allQueryElements = getQueryString(url)

    #Get each query as a list, split on &
    listOfQueries = re.split(getQueriesExpr, allQueryElements)

    for item1 in listOfQueries:
        listOfQueryElements = re.split(getFieldAndValueExpr, item1)
        result.append(tuple(listOfQueryElements))

    return result


def findFunctions(fileName):
#Take in a Python code file, parse it and return a list of (string, list-of-string) tuples.
    #First element of the tuple is the name of the function
        #splitDef[1]
    #Second element of the tuple is a list containing the names of the function arguments.
        #findArguments (list)

    functionNameList = []
    resultTemp = []
    result = []

    #Open the Python code file using "with" function
    with open(filename) as myFile:
        all_lines = myFile.readlines()

    #print(all_lines)

    checkDefStringExpr = r"def"
    splitOnParenthExpr = r" \("
    searchFuncNameExpr = r"[^def\s][\D][\w]+"
    splitArgumentsExpr = r"[a-z]+[\d]+"
    #print(findFunctionExpr)

    for item1 in all_lines:
        #print(item1)
        defString = re.search(checkDefStringExpr, item1)
        if(defString != None):
            #GET THE FUNCTION NAME
            splitOnParenth = re.split(splitOnParenthExpr, item1)
            #print(splitOnParenth)
            splitDef = re.search(searchFuncNameExpr, splitOnParenth[0])
            #print("group is: " + splitDef.group(0))

            #GET THE ARGUMENTS
            findArguments = re.findall(splitArgumentsExpr, item1)
            #print(findArguments)

            #Compile into result list
            resultTemp.append(splitDef.group(0))
            #print(resultTemp)
            resultTemp.append(findArguments)
            #print(resultTemp)
            resultTempTupled = tuple(resultTemp)
            #print(resultTempTupled)
            result.append(resultTempTupled)
            resultTemp = []
    #print(result)
    return result


if __name__ == "__main__":
    s = "The TART program runs on Tuesday and Thursday, but it does not start until next week."
    s1 = "The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each."
    s2 = "The signal fluctuates between -0.3452 and +12.6509 volts. Try to keep it at 6 volts."
    url = "http://www.purdue.edu/Home/Calender?Year=2016&Month=September&Semester=Fall"
    url2 = "http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here"
    filename = "findFunctionsTest.py"
    #print(getWords(s, "t"))
    #print(extractFloats(s2))
    #print(getUrlParts(url))
    #print(getQueryString(url))
    #print(getQueryParameters(url2))
    #print(findFunctions(filename))
