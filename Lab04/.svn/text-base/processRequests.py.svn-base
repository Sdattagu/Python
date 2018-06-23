def processRequests():
#Analyze log file, returns a list of tuples of the form (string, string, string, string, bool)
#Where the first 4 elements of the tuple are:
    #The user ID
    #The URL
    #The controller
    #The action
    #Final element is a Boolean indicating whether the user is to be granted access to that URL or not.
#Ex.: 'bphillips', 'http://www.purdue.com/Forums/Page1', 'Forums', 'Page1', True)

    temp = []
    result = []
#Parse "ServerRequests.txt" to get the lines
#For item1 in lines:
    #Parse item1 to grab the userid, URL, controller, and action.
    #Use the userID and URL and call isAccessAllowedFor(userID, url)
        #Assign this result to boolVal
    #Create a tuple with the above elements
    #Add this tuple to a result list

    with open('ServerRequests.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()

    for item1 in all_lines:
        temp = []
        #Get rid of whitespace
        stripped = item1.strip()
        #Separate into userID and URL fields
        serverRequestsArray = item1.split(':', 1)
        #print(serverRequestsArray)
        #Break into userID and URL
        userID = serverRequestsArray[0].strip()
        url = serverRequestsArray[1].strip()
        #Grab the controller and action.
        urlSplit = url.split('/')
        #print(urlSplit)
        controller = urlSplit[3]
        action = urlSplit[4]
        #Now you have 4/5 fields
        #print(userID, url, controller, action)
        boolVal = isAccessAllowedFor(userID, url)
        temp.append(userID)
        temp.append(url)
        temp.append(controller)
        temp.append(action)
        temp.append(boolVal)
        T = tuple(temp)
        #print(T)
        result.append(T)

    #print("processRequests: ")
    #print(result)
    return result

    # TODO: Remove the "pass" before you add any code to this block.
    pass


def getAccessControlByLogin():
#Open the AccessControl.txt file using with command
#Parse the AccessControl.txt
    #Separate into User and Controller Fields
        #For each user, check if they exist in the dictionary
            #If they don't exist, add them and add the controller field to the set
            #If they do exist, append the controller field to the set

    result_d = {}
#controllers = set()

    with open('AccessControl.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]

    for item1 in the_lines:
        #Separate into User and Controller Field for that line
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        user_controller_array = stripped.split(':')
        #Break into user and controller fields
        user = user_controller_array[0].strip()
        controller = user_controller_array[1].strip()
        #Do the checks; if user key exists?
        if(user in result_d):
            #Add the controller to the user's set
            result_d[user].add(controller)
        elif(user not in result_d):
            #Create new user, and a set associated with him/her
            result_d[user] = set()
            #Add the controller to that user's list
            result_d[user].add(controller)

    #print("getAccessControlByLogin")
    #print(result_d)
    return result_d

def getAccessControlByController():
#Open the Logins.txt file, grab the Last/First name and ID combination
    #Throw into a reference dictionary

#Parse the AccessControl.txt file
    #For each controller, check if they exist in the result
        #If they don't exist, add them and the user field to the set
        #If they do exist, append the user field to the set.

    result_d = {}
    reference_d = {}

    with open('Logins.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]
        #Throw into a ref dictionary
    for item1 in the_lines:
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        logins_array = stripped.split('|')
        #Break into fields
        name = logins_array[0].strip()
        id = logins_array[1].strip()
        #Add to the dictionary
        reference_d[id] = name

    with open('AccessControl.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]

    for item1 in the_lines:
        #Separate into User and Controller Field for that line
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        user_controller_array = stripped.split(':')
        #Break into user and controller fields
        user = user_controller_array[0]
        user = user.strip()
        controller = user_controller_array[1].strip()
        #Do the checks; if user key exists?
        if(controller in result_d):
            #Look up the name in the reference_d
            nameVal = reference_d[user]
            #Add the controller to the user's set
            result_d[controller].add(nameVal)
        elif(controller not in result_d):
            #Create new user, and a set associated with him/her
            result_d[controller] = set()
            #Look up the name in the reference_d
            nameVal = reference_d[user]
            #Add the controller to the user's set
            result_d[controller].add(nameVal)
            #Add the controller to that user's list
            #result_d[controller].add(user)
    #print(result_d)

    return result_d

def getActionsOfController():
#Open up ServerRequests.txt
    #Grab the relevant lines

    result_d = {}
    reference_d = {}

    with open('ServerRequests.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
#       #the_lines = all_lines[2:]
        #Throw into a ref dictionary
    for item1 in all_lines:
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into fields
        logins_array = stripped.split(':')
        #Break into fields
        name = logins_array[0].strip()
        URL = logins_array[2].strip()
        #Split up the URL into Controller and Action
        URL_array = URL.split('/')
   #     print(URL_array)
        controller = URL_array[3].strip()
    #    print(controller)
        action = URL_array[4].strip()
        if(controller in result_d):
            result_d[controller].add(action)
        elif(controller not in result_d):
            result_d[controller] = set()
            result_d[controller].add(action)

    return result_d

def isAccessAllowedFor(userID, url):
#Use getAccessControlByLogin output to get a dictionary of what userID can access
#Pull out the Controller from the URL
#See if userID is in the dictionary,
    # if not, return false
    # If they are, then check if they have access to the controller
        #If true, return true
        #If false, return false

    user_controller_d = getAccessControlByLogin()
    #Strip the whitespace off
    stripped = url.strip()
    #Split into fields
    logins_array = stripped.split('/')
    #Break into fields
    name = logins_array[0].strip()
    controller = logins_array[3].strip()
    #print(controller)
    if(userID in user_controller_d):
        listOfControllers = user_controller_d[userID]
        if(controller in listOfControllers):
            return True
        else:
            return False
    elif(userID not in user_controller_d):
        return False


def getRequestsBy(userID):
#Create a reference dictionary using ServerRequests.txt

    result_d = []
    temp = []
    reference_d = {}

    with open('ServerRequests.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
    for item1 in all_lines:
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        requests_array = stripped.split(':', 1)
        #print(requests_array)
        #Break into fields
        name = requests_array[0].strip()
        request = requests_array[1].strip()
        #Add to the dictionary
        if(name in reference_d):
            reference_d[name].add(request)
        elif(name not in reference_d):
            reference_d[name] = set()
            reference_d[name].add(request)

    #print(reference_d)

    for item2 in reference_d[userID]:
        temp = []
        boolVal = isAccessAllowedFor(userID, item2)
        temp.append(item2)
        temp.append(boolVal)
        T = tuple(temp)
        result_d.append(T)

    #print(result_d)
    B = tuple(result_d)
    #print(B)
    return B

def aggregateUserRequests():
#Create a reference dictionary using ServerRequests.txt
#For each entry in reference_d,
    #Break up into username and List of URL's attempted access
    #Get number of URL's attempted access using len
        #For each username
            #For each URL in the list of URLs,
                #Call isAccessAllowed to check.
                #If true, accessAllow++
                #else if false, accessDenied++

        #Make a tuple of accessAllow, accessDenied
        # if, else...
        # result_d[username] = tuple

    result_d = {}
    temp = []
    numberOfAccessTried = {}
    reference_d = {}
    reference_id_name = {}
    accessAllowed = 0
    accessDenied = 0

    with open('Logins.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]
        #Throw into a ref dictionary
    for item1 in the_lines:
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        logins_array = stripped.split('|')
        #Break into fields
        name = logins_array[0].strip()
        id = logins_array[1].strip()
        #Add to the dictionary
        reference_id_name[id] = name

    with open('ServerRequests.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
    for item1 in all_lines:
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        requests_array = stripped.split(':', 1)
        #print(requests_array)
        #Break into fields
        name = requests_array[0].strip()
        request = requests_array[1].strip()
        #print(request)
        #Add to the dictionary
        if(name in reference_d):
            reference_d[name].add(request)
        elif(name not in reference_d):
            reference_d[name] = set()
            reference_d[name].add(request)

    #print(reference_d)
    for key, value in reference_d.items():
        numberOfAccessTried = len(value)
        for item1 in value:
            if(isAccessAllowedFor(key, item1) == True):
                accessAllowed += 1
            elif(isAccessAllowedFor(key, item1) == False):
                accessDenied += 1

        temp.append(accessAllowed)
        temp.append(accessDenied)
        T = tuple(temp)
        #print(T)
        result_d[reference_id_name[key]] = T
        temp = []
        accessAllowed = 0
        accessDenied = 0

    #print(result_d)
    return result_d

def aggregateControllerRequests():
#Returns a dictionary of the form {string: (int, int)}
    #Key is a string (Controller), value is a tuple of two ints.
        #First int: number of URLs, containing the given controller, which have been granted access
        #Second int: number of URLs, containing the given controller, which have NOT been granted access

#Parse ServerRequests.txt to get the lines
#Get a dictionary of Controller:Name using getAccessControlByController()
#Get a dictionary of userID:Name
#For each controller in controller:name dictionary
    #For each line in the_lines
        #If controller is in the URL (request)
            #Using controller:name dictionary, get a set of names that have access
            #Using userID:Name dictionary, get the Name (as a string)
            #Check if the Name is in the list
                #If exists, accessAllowed++
                #Else, accessDenied++
    #Make a tuple of accessAllowed/Denied
    #result_d[controller]:new_tuple

    controller_name_d = {}
    userID_name_d = {}
    namesWithAccess = {}
    accessAllowed = 0
    accessDenied = 0
    temp = []
    result_d = {}

    with open('ServerRequests.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()

    controller_name_d = getAccessControlByController()
    userID_name_d = userID_Name_d()
    #print(controller_name_d)
    #print(userID_name_d)

    for controller in controller_name_d.keys():
        temp = []
        accessAllowed = 0
        accessDenied = 0
        for line in all_lines:
            stripped = line.strip()
            url = stripped.split(':', 1)[1].strip()
            userID = stripped.split(':', 1)[0].strip()
            #print(userID, url)
            if(controller in url):
                namesWithAccess = controller_name_d[controller]
                fullName = userID_name_d[userID]
                if(fullName in namesWithAccess):
                    accessAllowed += 1
                else:
                    accessDenied += 1

        temp.append(accessAllowed)
        temp.append(accessDenied)
        T = tuple(temp)
        result_d[controller] = T


    #print(result_d)
    return result_d

def userID_Name_d():

    reference_d = {}

    with open('Logins.txt') as myFile:
        #Grab the valid data
        all_lines = myFile.readlines()
        the_lines = all_lines[2:]
        #Throw into a ref dictionary
    for item1 in the_lines:
        #Strip the whitespace off
        stripped = item1.strip()
        #Split into two fields
        logins_array = stripped.split('|')
        #Break into fields
        name = logins_array[0].strip()
        id = logins_array[1].strip()
        #Add to the dictionary
        reference_d[id] = name

    return reference_d

if __name__ == "__main__":

    print(getAccessControlByLogin())
    print(getAccessControlByController())
    print(getActionsOfController())
    print(isAccessAllowedFor("jkelly", "http://www.purdue.com/Proceedings/Page14"))
    print(getRequestsBy("hwilson"))
    print(aggregateUserRequests())
    print(processRequests())
    print(aggregateControllerRequests())