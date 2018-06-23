import re

def getFloatData(sensorID):
    #Takes in a sensor ID string
        #Returns a list of sensor readings that only follow the scientific notation
    #List should maintain the order of readings in the string.
    #If sensor IF passed is not valid, return an empty list.

    with open('sensors.xml') as myFile:
        all_lines = myFile.read()

    #Grab the part of the xml that has sensorID

    exprSensorsXml = r"<" + re.escape(sensorID) + r">" + r"(.*?)" + r"</" + re.escape(sensorID) + r">"
    exprFloatData = r"[+-]?[0-9]+\.[0-9]+[^eE\w]"
    processData = re.findall(exprSensorsXml, all_lines, re.DOTALL)

    #Search processData

    if(len(processData) != 0):
        m = re.findall(exprFloatData, processData[0])
        for item1 in range(len(m)):
            m[item1] = m[item1][:-1]
    else:
        m = list()

    #print(m)
    return m

def getScientificData(sensorID):
    #Takes in a sensor ID string
        #Returns a list of sensor readings that only follow the scientific notation
    #List should maintain the order of the readings in the string.
    #If sensor ID passed is not valid, return an empty list.

    with open('sensors.xml') as myFile:
        all_lines = myFile.read()

    #Grab the part of the xml that has sensorID

    exprSensorsXml = r"<" + re.escape(sensorID) + r">" + r"(.*?)" + r"</" + re.escape(sensorID) + r">"
    exprSensorData = r"[+-]?[0-9]+\.[0-9]+[e|E][+-]?[0-9]+"
    processData = re.findall(exprSensorsXml, all_lines, re.DOTALL)

    #Search processData

    if(len(processData) != 0):
        m = re.findall(exprSensorData, processData[0])
    else:
        m = list()

    return m

def getOptions(commandline):
    #Takes in a command-line string with a variable number of options
    #Returns a "sorted" list of (str, str) tuples
        #First element is option letter, WITHOUT minus sign
        #Second element is option value

    resultT = []
    result = []
    expr = r"[\-][a-z][\s]+[0-9a-z/]*"
    exp = r"[\-][a-z]"

    processLine = re.findall(expr, commandline)

    #print(processLine)

    for item1 in processLine:
        blah = item1.split(" ")
        #print(blah)
        resultT.append(blah[0])
        resultT.append(blah[-1])
        result.append(tuple(resultT))


    #print(result)
    return result
    pass


if __name__ == "__main__":
    #print(getScientificData("4IP"))
    #print(getFloatData("4IP"))
    print(getOptions("myScript.bash -v -i 2  -p  /local/bin/somefolder"))
