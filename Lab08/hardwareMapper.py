

#Given the module you created, you now need to convert Verilog netlists to VHDL netlists.
#Each line in a VHDL netlist is of the following form:
    #INSTANCE_NAME: COMP_NAME PORT MAP(PORT=>PIN, PORT2=>PIN2);

#The COMP_NAME and INSTANCE_NAME are switched. Second, this format includes a colon (':') after the
#instance name, includes the words PORT MAP before the assignment list, and uses '=>' for assignments.
#Finally, it ends with a semicolon (';'). Your script should use your moduleTasks module to convert Verilog
#netlists into VHDL netlists.

def mapHardwareLine(line):
    #Takes in a Verilog netlist string and returns a VHDL netlist string.
    #If the input line is invalid, i.e. produces an exception, return the string:
        #Error: Bad Line.

    import moduleTasks
    errorString = "Error: Bad Line."
    vhdlNetListString = ""
    try:
        verilogListUnpacked = moduleTasks.parseLine(line)
        print(verilogListUnpacked)
    except (ValueError, IOError, OSError, IndexError, KeyError, TypeError):
        return errorString
    else:

        vhdlNetListString += verilogListUnpacked[1]
        vhdlNetListString += ": "
        vhdlNetListString += (verilogListUnpacked[0] + " PORT MAP(")

        #print(verilogListUnpacked)
        #print(verilogListUnpacked[2])
        for item1 in verilogListUnpacked[2]:
            port = item1[0]
            pin = item1[1]
            vhdlNetListString += (port + "=>" + pin + ", ")

            #print(port)
            #print(pin)


        vhdlNetListString = vhdlNetListString[:-2]
        vhdlNetListString += ");"
        #print(vhdlNetListString)
        return vhdlNetListString

def mapFile(sourceFile, targetFile):
    #Takes in two file paths.
        #The first one is a source Verilog netlists file, containing netlist lines
        #The second is the target VHDL netlists file to save to.
    #This function should convert each line in the source file using the mapHardwareLine() function.

    with open(sourceFile) as myFile:
        all_lines = myFile.readlines()

    for item1 in all_lines:
        vhdl_netlist = mapHardwareLine(item1)
        with open(targetFile, 'a') as myFile:
            myFile.write(vhdl_netlist)
            myFile.write("\n")


if __name__ == "__main__":
    #mapHardwareLine("DFFSR present_val_reg  ( .D(n30), .CLK(clk), .R(n33), .S(1), .Q(stop_bit) )")
    mapFile('verilog_test.v', "vhdl.v")