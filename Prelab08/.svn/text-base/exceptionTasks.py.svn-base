#Shounak Dattagupta
#10/22/2016

import math
import sys

from points import PointND
from points import Point3D
from points import PointGroup

def createPoint(dataString):
    #Takes in a string containing comma separated float values
        #"3.14, 2.701, 19.77"
    #Returns a PointND instance.
    # Note that the string may contain non-float values
        #"4.98, 3FA2, None"
            #In this case, return a string containing some error message.

    errorString = "The string contains non-float values."
    argList = dataString.split(",")
    tupList = []

    for value in argList:
        try:
            float(value)
        except (ValueError):
            return errorString
        else:
            tupList.append(float(value))

    return PointND(*tuple(tupList))


def distanceBetween(point1, point2):
    #Takes in two PointND instances
    #Computes and returns the distance between them.
    #Do NOT perform a cardinality check.
    #If the operation throws an error, return a string containing some error message.

    errorString = "distanceBetween(): Invalid calculation"

    try:
        result = point1.distanceFrom(point2)
    except (ValueError, IOError, OSError, IndexError, KeyError, TypeError):
        return errorString

    return result


def checkVicinity(point, pointList, radius):
    #Takes in:
        #A PointND instance
        #A list of PointND instances
        #A float radius value
    #Function should return a 3-element tuple
        #First is number of points from the pointList whose distances from point are <= radius
        #Second is number of points whose distances are > radius
        #Third is number of points who could not be checked because they were invalid.
        #Sum of elements in tuple must = len(pointList)
    #Do NOT perform a cardinality check
    #Use exception handling to solve this question.

    tupList = []
    tupCountOne = 0
    tupCountTwo = 0
    tupCountThree = 0

    for p in pointList:
        try:
            if(point.distanceFrom(p) <= radius):
                tupCountOne += 1
            elif(point.distanceFrom(p) > radius):
                tupCountTwo += 1
        except (ValueError, IOError, OSError, IndexError, KeyError, TypeError):
            tupCountThree += 1

    tupList.append(tupCountOne)
    tupList.append(tupCountTwo)
    tupList.append(tupCountThree)

    return tuple(tupList)


def checkOperation(*args):
    #Invokes the given performProcessing(*args) function
    #Passes the same input params (*args) to it
    #Function should return the following:
        #If function does not throw an exception, return True.
        #If function throws one of the OS errors, return the string:
            #"The following Error occurred: [ErrorName]"
                #[ErrorName] can be BlockingIOError, InterruptedError, ConnectionResetError, etc.
        #If function returns ConnectedRefusedError, re-throw that error
        #If function throws any other exception, return False.
    from prelab08addon import performProcessing

    try:
        performProcessing(*args)
    except (ConnectionRefusedError):
        raise ConnectionRefusedError("Connection refused error was raised.")
    except OSError as ose:
        return "The following Error occurred: " + repr(ose)[:-2]
    except:
        return False

    return True

if __name__ == "__main__":

#TESTS FOR createPoint(dataString)
    argsString = "3.14,2.701,19.77"
    argsString2 = "4.32,2.801,18.43"
    argsStringInvalid = "4.98,3FAfdls2,None"
    print("-------------------")
    #Valid case
    print("Testing createPoint(dataString)")
    print("Testing valid case")
    point1 = createPoint(argsString)
    point2 = createPoint(argsString2)

    print(str(point1))
    print(type(point1))
    print(str(point2))
    print(type(point2))

    #Invalid case
    print("-------------------")
    print("Testing invalid case")
    print(str(createPoint(argsStringInvalid)))

#TESTS FOR distanceBetween(point1, point2)
    print("-------------------")
    print("Testing distanceBetween")
    print(distanceBetween(point1, point2))

#TESTS for checkVicinity(point, pointList, radius)
    print("-------------------")
    print("Testing checkVicinity")
    print("Creating pointList...")
    pointOneString = "4.31,9.20,3.132"
    pointTwoString = "3.32, 1.32, 13.23"
    pointThreeString = "3.42"
    pointList = [createPoint(pointOneString), createPoint(pointTwoString), createPoint(pointThreeString)]
    print("pointList created.")
    print(checkVicinity(point1, pointList, 0))

#TESTS for performProcessing(*args)
    print("-------------------")
    print("Testing checkOperation")
    args = (1, 2, 3)
    print(checkOperation(*args))
    pass