#Shounak Dattagupta
#Prelab04
#9/18/2016

import sys
import glob

print(sys.version)

def uniqueLetters(s):
#Input "s" is a string containing uppercase letters; e.g.: "ABDBDARWET"

    #Parse the string and create a new one with only the unique characters
        #For each character in string
            #If the character dne in temp list
                #Add it into temp
    #temp now contains only unique characters from the string
    #Sort temp
    #Reverse temp
    #Turn temp into a string
        #join operator

    #Return temp

    temp = []
    result = ""

    for item1 in s:
        if (temp.count(item1) == 0):
            temp.append(item1)

    temp.sort()
    temp.reverse()
    result = ''.join(temp)

    #print(result)
    return result


def scaleSet(aSet, num):
#aSet = set of numbers
#num = a float, scalar

#Just mult each element of aSet by the num?

    #For each item in aSet
        #temp = aSet * num
        #Add temp into result

    #Return result
    result = []
    temp = 0

    for item1 in aSet:
        temp = item1 * num
        result.append(round(temp,2))

    #print(result)
    return result


def printNames(aSet):
#Takes in a set of first names, prints the names to console
    #One name per line
        #Ordered alphabetically

    #Parse the set and throw names into a list
        #For item1 in range(len(aSet)),
            #list.append(aSet.pop())

    #Sort the list in alphabetical order
        #list.sort()

    #print to console w/ newline char
        #for item1 in list:
            #print item1

    list = []

    for item1 in range(len(aSet)):
        list.append(aSet.pop())

    list.sort()

    for item2 in list:
        print(item2)


def getStateName(stateAbb):

    dic1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
#stateAbb is the two-letter abbreviation of the state
#Return the full name from this abbreviation
    #the abbreviation is the value, while the full name is the key

    #temp = dic1.items()

    #For key, value in dic1.items():
        #if value == stateAbb
            #return key

    for key, value in dic1.items():
        if value == stateAbb:
            #print(key)
            return key



def getZipCodes(stateName):

    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907: "IN", 10001: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}

    tempVal = ""
    result = []

    for key, value in d1.items():
        if key == stateName:
            tempVal = value

    for key, value in d2.items():
        if tempVal == value:
            tempKey = key
            result.append(tempKey)

    #print(result)
    return result

def printSortedMap(s):

    temp = []

    for (lastName, firstName, mi), weight in s.items():
        o = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
        temp.append(o)

    temp.sort()
    for item1 in temp:
        print(item1)

def switchNames(s):
#s is a dictionary in a certain form
    #key is a set of the form (Last, First, MI)

#Function should grab the key, modify the key, recreate dictionary, return
    #for key, value, in s.items():
        #last = key[0]
        #first = key[1]
        #mi = key[2]
        #string = first + " " + last
        #s_new[string] = value

    s_new = {}

    for key, value in s.items():
        first = key[0]
        last = key[1]
        mi = key[2]
        new_s = first + " " + last
        s_new[new_s] = value

    return s_new

def getPossibleMatches(record, n):
#Given dictionary of form {string: (MM, DD, YY)}, key is the person's name, value is DOB integer-tuple
    #Integers may be 1 or 2 digits

#This function takes in a dictionary (record), and an integer (n)
    #Returns a set of all the names where the input number matches either
        #day
        #month
        #year
    #Names are unique, but date may not be

    result = []

    for key, value in record.items():
        month = value[0]
        day = value[1]
        year = value[2]
        if(n == month | n == day | n == year):
            result.append(key)

    print(result)
    return result

def getPurchaseReport():

    temp = []
    temp_a = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    temp6 = []
    accumulator = 0

    a = ""
    b = 0

    d = {}
    price_d = {}
    purchase_d = {}
    result_d = {}
    purchases = glob.glob('./purchases/purchase_*')
    #print(purchases)

    with open('./purchases/Item List.txt') as myFile:
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]
        for item1 in the_lines:
            temp2 = item1.split()
            temp3 = [temp2[0], (temp2[1])[1:]]
            temp.append(temp3)

        #print(temp)

        for item2 in temp:
            price_d[item2[0]] = item2[1]

        #print(price_d)


    for item1 in purchases: #Iterate through purchases...
        with open(item1) as myFile: #Looking at a certain purchase_xxx
            purchase_num = int(item1[(len(item1) - 7):(len(item1) - 4)])
            #print(purchase_num)
            all_lines = myFile.readlines()
            the_lines = all_lines[2:]
            for item1 in the_lines: #For each fruit/quantity...
                temp4 = item1.split() #Split up into two strings
                temp5 = [temp4[0], (temp4[1])] #Put into list
                temp_a.append(temp5) #Add to a temp list

            #Now temp_a contains list of all item/quantity pairings for purchase_xxx

            for item3 in temp_a: #For each list in temp_a (where each list is an item/quantity pairing)
                purchase_d[item3[0]] = item3[1] #Make a dictionary out of it

            #Now purchase_d is a dictionary of the item:quantity for purchase_xxx.

            for key, value in purchase_d.items():
                #print(accumulator)
                price = float(price_d[key]) #Grab the price from price dictionary using this key (fruit name)
                quantity = int(value)
                #print(price)
                #print(quantity)
                accumulator += round(float("{0:.2f}".format(price * quantity)),2) #This is price of those fruits, added to accum.
                #print(accumulator)

            result_d[purchase_num] = accumulator
            #Now accumulator contains the total price of all these fruits for purchase_xxx.
            #print(accumulator)
        accumulator = 0
        temp.clear()
        temp_a.clear()
        temp2.clear()
        temp3.clear()
        temp4.clear()
        temp5.clear()
        temp6.clear()

    #print(result_d)
    return result_d

def getTotalSold():
#For each purchase_xxx list,
    #Grab the item/quantity, add these to a result_d
        #If the item (key) already exists,
            #Add the value to the existing key's value
        #Else, add the key and value to the dictionary



    temp_a = []
    temp = []
    A = {}
    B = {}


    with open('./purchases/Item List.txt') as myFile:
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]
        for item1 in the_lines:
            temp2 = item1.split()
            temp3 = [temp2[0], (temp2[1])[1:]]
            temp.append(temp3)

        for item3 in temp:
            B[item3[0]] = 0
    #print(B)
    purchases = glob.glob('./purchases/purchase_*')

    for item1 in purchases: #Iterate through purchases...
        with open(item1) as myFile: #Looking at a certain purchase_xxx
            #print(item1)
            purchase_num = int(item1[(len(item1) - 7):(len(item1) - 4)])
            all_lines = myFile.readlines()
            the_lines = all_lines[2:]
            for item4 in the_lines: #For each fruit/quantity...
                temp4 = item4.split() #Split up into two strings
                temp5 = [temp4[0], (temp4[1])] #Put into list
                temp_a.append(temp5) #Add to a temp list
                #print(item4)
            for item2 in temp_a:
                B[item2[0]] += int(item2[1])
    #print(B)
    return B

if __name__ == "__main__":
    s = "ABDBDARWET"
    aSet = {3.12, 5.0, 7.2, 15.24}
    ssp = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    names = ['Spencer', 'Shitij', 'Ayush', 'Akshay', 'Tiger', 'shabam']
    uniqueLetters(s)
    scaleSet(aSet, 2.1)
    printNames(names)
    printSortedMap(ssp)
    getStateName("IN")
    getZipCodes("Indiana")
    switchNames(ssp)
    getPurchaseReport()
    getTotalSold()

    pass





