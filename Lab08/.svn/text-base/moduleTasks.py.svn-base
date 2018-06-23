
def isIdValid(pin):
    #Takes a Verilog identifier as its argument.
    #A valid identifier is any combination of letters, numbers, or underscores.
    #You should check each character in this string to make sure it meets this condition
        #If every character is a letter, number OR underscore, return True.
        #Else, return False.

    boolResult = True

    from string import ascii_letters
    from string import digits


    for character in pin:

        if(character not in ascii_letters and character not in digits and character != "_"):
            boolResult = False

    return boolResult

def parseAssignment(assignment):
    #Takes a Verilog assignment string as its argument
    #A valid Verilog assignment has the form:
        #.PORT_NAME(PIN_NAME)
            #starts with a period, followed by a valid port name then a valid pin name in parentheses
            #Use isIdValid to check if the pin and port names are valid
        #Return a tuple consisting of the port name and the pin name if assignment is valid
            #If assignment is not valid, raise a ValueError exception
                #Use the passed in string as the argument for the exception.

    tupList = []
    result = tuple()

    import re
    assignment_expr = r"\.(.+)\(([^(]+)\)"

    m = re.match(assignment_expr, assignment, re.DOTALL)
    if(m):
        print(m.group(0))
        print(m.group(1))
        print(m.group(2))

        port_name = m.group(0).split("(")[0][1:]
        pin_name = assignment.split("(")[1][:-1]

        #print(port_name)
        #print(pin_name)

        port_name_vld = isIdValid(port_name)
        pin_name_vld = isIdValid(pin_name)


        if(port_name_vld == True and pin_name_vld == True):
            print("both vld")
            tupList.append(port_name)
            tupList.append(pin_name)
            result = tuple(tupList)
        else:
            raise ValueError(assignment)


    return result

def parseLine(line):
    #Takes a line of text as its argument.
    #Line of text is checked to make sure it follows the format of a line from a netlist
        #COMP_NAME INSTANCE_NAME (ASSIGNMENT_LIST)
        #Make sure component and instance name is valid
            #isIdValid
        #Also check to make sure that an assignment list is provided
            #Check within parentheses
        #Check that each assignment in the assignment list is valid
            #Each assignment is separated by commas

    #If line is valid
        #Return a tuple with three parts:
            #Component name
            #Instance name
            #Another tuple that contains all pin assignments
    #If line is invalid
        #raise ValueError using entire line of text as argument
    #If any individual assignment is invalid
        #raise ValueError using assignment string as the argument

    import re
    list_expr = r"[\w]+\s+([\w]+)\s+\((.+\))\s*\)"
    tupList = []
    assignment_list_expr = r"\(.+\)"

    m = re.search(list_expr, line, re.DOTALL)
    #print(m.group(0))
    if(m):

        print(m.group(0))
        print(m.group(1))
        print(m.group(2))

        vld_line_list = m.group(0)
        print(vld_line_list)

        instance_name = m.group(1)
        print(instance_name)

        assignments = m.group(2)
        print(assignments)

        print(vld_line_list.split(" "))
        comp_name = vld_line_list.split(" ")[0]
        #print(comp_name)

        #instance_name = vld_line_list.split(" ")[1]
        #print(instance_name)

        #all_parts = assignment_list.split("( ")
        assignment_list = assignments.split(",")
        #print(assignment_list)

        #assignment_list = all_parts[1].split(" )")[0].strip().split(",")

        print(comp_name)
        print(instance_name)
        #print(assignment_list)


        comp_name_vld = isIdValid(comp_name)
        instance_name_vld = isIdValid(instance_name)

        for item1 in assignment_list:
            #print(item1.strip())
            print(item1)
            blah = parseAssignment(item1.strip())
            print(blah)
            tupList.append(blah)

        result = tuple(tupList)
        blah2 = (comp_name, instance_name, result)
        #print(type(blah2))
        #print(comp_name, instance_name, result)
        return blah2

    else:
        raise ValueError(line)

    pass

if __name__ == "__main__":
    #print(isIdValid("b1932_"))
    #print(parseAssignment(".D(n30)"))
    print(parseLine("OAI21X1 U19 ( .A(n31), .B(n32), .C(n11), .Y(n13) "))
    pass