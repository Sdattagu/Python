import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class Calculator(Ui_Calculator, QMainWindow):
#Calculator class implements the basic functionality of a calculator by extending the QMainWindow GUI Library
#From QtCore and extending the Ui_Calculator class in calculator.py.

#Member variables for this class are basically all the GUI buttons in the Ui_Calculator class
#Also two operands that are updated with the information that is input by the user
    #These are strings
    #Access user input on button press using sender().text()
        #sender() tells you who is sending the button press information
        #text() converts it to a string that can be appended to the operand.
#Also an operator which is initially empty (null)
    #The operator is updated when a function button is pressed (/, *, -, +).

#Finally, there is a result variable which stores the final result when = GUI button is pressed
    #Can be a string or an int that gets converted to string on display.
        #self.Display(self.result)

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        #First set up the UI calling Ui_calculator's setupUI() function
        self.setupUi(self)

        #Set up operators
        self.a = "0"
        self.b = "0"
        self.op = None
        self.result = 0

        #Set up function (/, *, -, +) GUI buttons
        #self refers to Calculator object
        #btn(...) references name of widget name
            #From QtGui library, QPushButton object
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.
        self.btnDivide.clicked.connect(self.opClickedAction)
        self.btnMultiply.clicked.connect(self.opClickedAction)
        self.btnMinus.clicked.connect(self.opClickedAction)
        self.btnPlus.clicked.connect(self.opClickedAction)

        #Set up number (0-9) GUI buttons
        #self refers to Calculator object
        #btn(...) references name of widget name
            #From QtGui library, QPushButton object
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.
        self.btn0.clicked.connect(self.digitClickedAction)
        self.btn1.clicked.connect(self.digitClickedAction)
        self.btn2.clicked.connect(self.digitClickedAction)
        self.btn3.clicked.connect(self.digitClickedAction)
        self.btn4.clicked.connect(self.digitClickedAction)
        self.btn5.clicked.connect(self.digitClickedAction)
        self.btn6.clicked.connect(self.digitClickedAction)
        self.btn7.clicked.connect(self.digitClickedAction)
        self.btn8.clicked.connect(self.digitClickedAction)
        self.btn9.clicked.connect(self.digitClickedAction)

        #Set up DOT button
        #self refers to Calculator object
        #btn(...) references name of widget name
            #From QtGui library, QPushButton object
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.
        self.btnDot.clicked.connect(self.digitClickedAction)

        #Set up CLEAR button
        #self refers to Calculator object
        #btn(...) references name of widget name
            #From QtGui library, QPushButton object
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.
        self.btnClear.clicked.connect(self.clearClickedAction)

        #Set up EQUAL button
        #self refers to Calculator object
        #btn(...) references name of widget name
            #From QtGui library, QPushButton object
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.
        self.btnEqual.clicked.connect(self.calcPrevResult)

        #Set up SEPARATOR button
        #self refers to Calculator object
        #btn(...) references name of widget name
            #From QtGui library, QPushButton object
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.
        self.chkSeparator.stateChanged.connect(self.separatorChk)

    def clearClickedAction(self):
        #When equal button is clicked
        self.txtDisplay.setText("0.")
        self.a = "0"
        self.b = "0"
        self.op = None

    def digitClickedAction(self):
        #A number (0-9) was clicked so we have to add it as an operand.
        #Display it to the screen, as long as the digit input is not 0.
        #Two cases
            #This is the first operator if the text currently in the box is "0."
                #Otherwise, the first operator is updated in calcPrevResult()
            #This is the second operator if self.op != None

        if(self.txtDisplay.text() == "0." and self.sender().text() != "0"):
            self.txtDisplay.setText(self.sender().text())
        elif (self.txtDisplay.text() != "0."):
            if(self.op == None):
                self.txtDisplay.setText(self.txtDisplay.text() + self.sender().text())
            elif(self.op != None):
                self.txtDisplay.setText(self.sender().text())

        if(self.op == None):
            self.a += self.sender().text()
        elif (self.op == "+" or self.op == "-" or self.op == "/" or self.op == "x"):
            self.b += self.sender().text()

    def opClickedAction(self):
        #Two cases
            #3 + 2
                #Operator "+" is pressed, operand1 has been stored as "3" but operand2 is not yet founded.
                #self.op == None (since this is the first operator!)
                    #self.op = operator pressed, return
            #3 + 2 - 6
                #Operator "-" is pressed, operand 1 and 2 have been stored.
                #self.op != None
                    #Calculate the previous result (using the current operator)
                    #Update the operator (+ -> -).

        if(self.op == None):
            self.op = self.sender().text()

        elif(self.op == "+" or self.op == "-" or self.op == "/" or self.op == "x"):
            self.calcPrevResult()
            self.op = self.sender().text()

    def calcPrevResult(self):
        #In this state to calculate the result
            #Can assume that the operands have been given and we just want to calc and display.
        #Account for Division by 0.
        #Calculate Result
            #Display result
            #Set operand 1 to the result (so we can update with further ops for Immediate Result mode)
            #Reset operand 2
            #Reset the operator

        if(self.op == "+"):
            self.result = float(self.a) + float(self.b)
        elif(self.op == "-"):
            self.result = float(self.a) - float(self.b)
        elif(self.op == "/"):
            if(float(self.b) != 0 or float(self.b) != 0.0):
                self.result = float(self.a) / float(self.b)
            elif(float(self.b) == 0 or float(self.b) == 0.0):
                self.txtDisplay.setText("DIV 0 ERROR.")
        elif(self.op == "x"):
            self.result = float(self.a) * float(self.b)

        self.decimalRange(self.result)
        self.a = self.result
        self.b = "0"
        self.op = None

    def decimalRange(self, fullNumber):
        if(type(fullNumber) == float):
            decOption = int(self.cboDecimal.currentText())
            if(decOption == 0):
                self.txtDisplay.setText(str(format(round(number))))
            elif(decOption != 0):
                if(fullNumber.is_integer() == False):
                    form = "." + str(decOption) + "f"
                    self.txtDisplay.setText(str(format(fullNumber, form)))
                elif(fullNumber.is_integer() == True):
                    self.txtDisplay.setText(str(fullNumber)[:-2])

    def separatorChk(self):
        if(self.chkSeparator.isChecked() == 1):
             #temp = self.txtDisplay.text()
             #for i in range(3):
             #    if(i == 2):

             #self.txtDisplay.setText()
            form = "{0:,}"
            flot = float(self.txtDisplay.text())
            self.txtDisplay.setText(form.format(flot))
        else:
            commaChar = ","
            if commaChar in self.txtDisplay.text():
                repT = self.txtDisplay.text()
                repT = repT.replace(",","")
                self.txtDisplay.setText(repT)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Calculator()
    form.show()
    app.exec_()
    pass