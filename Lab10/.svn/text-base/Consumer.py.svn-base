import sys

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        #Functionality for clear button
        self.clearButton.clicked.connect(self.clearButtonAction)
        self.lastNameLineEdit.textChanged.connect(self.dataEntryAction)
        self.firstNameLineEdit.textChanged.connect(self.dataEntryAction)
        self.addressLineEdit.textChanged.connect(self.dataEntryAction)
        self.cityLineEdit.textChanged.connect(self.dataEntryAction)
        self.stateLineEdit.textChanged.connect(self.dataEntryAction)
        self.zipLineEdit.textChanged.connect(self.dataEntryAction)
        self.emailLineEdit.textChanged.connect(self.dataEntryAction)

        #Save to target button
        self.saveToTargetButton.clicked.connect(self.validationAction)
        #load button
        self.loadButton.clicked.connect(self.loadData)

        self.myArr = [self.firstNameLineEdit, self.lastNameLineEdit, self.addressLineEdit, self.cityLineEdit, self.stateLineEdit, self.zipLineEdit, self.emailLineEdit]

    def validationAction(self):
        #Validation
            #If you click on Save (once you are done populating the text widgets), you need to perform the following validation
            #on the QLineEdit widget's content:
                #All entries must be populated
                #The State must be one of the valid US states
                #ZIP code must be a 5-digit number (any 5 digits ok)
                #Email must be valid format (regex: \w+@\w+\.\w+
            #If any not met, display an error.
            #If more than one, display any one of them.

            import re
            expr = r"\w+@\w+\.\w+"

            textFieldBool = True #Def fields populated
            validState = True
            zipBool = True
            emailBool = False
            for item1 in self.myArr:
                if(item1.text() == ""):
                    textFieldBool = False #Entry not populated

            if(self.stateLineEdit.text() not in self.states):
                validState = False

            if(len(self.zipLineEdit.text()) > 5):
                zipBool = False

            if(re.match(expr, self.emailLineEdit.text())):
                emailBool = True

            if(not textFieldBool):
                if(self.firstNameLineEdit):
                    self.errorInfoLabel.setText("Error: Text entry is empty, cannot save.")

            elif(not validState):
                self.errorInfoLabel.setText("Error: Not a valid state.")

            elif(not zipBool):
                self.errorInfoLabel.setText("Error: Not a valid zip code.")

            elif(not emailBool):
                self.errorInfoLabel.setText("Error: Not a valid email.")

            else:
                self.saveToTarget()
                self.errorInfoLabel.setText("")

    def saveToTarget(self):

        #print("in")
        with open("target.xml", 'w') as myFile:
            myFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            myFile.write('<user>\n')
            myFile.write('\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n')
            myFile.write('\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n')
            myFile.write('\t<Address>' + self.addressLineEdit.text() + '</Address>\n')
            myFile.write('\t<City>' + self.cityLineEdit.text() + '</City>\n')
            myFile.write('\t<State>' + self.stateLineEdit.text() + '</State>\n')
            myFile.write('\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n')
            myFile.write('\t<Email>' + self.emailLineEdit.text() + '</Email>\n')
            myFile.write("</user>\n")

    def clearButtonAction(self):
        #At any point in the app lifetime, clicking on Clear must reset the form to the initial state.
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.firstNameLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.zipLineEdit.setText("")
        #self.firstNameLineEdit.setText(" ")
        self.emailLineEdit.setText("")

        self.loadButton.setEnabled(True)
        self.saveToTargetButton.setEnabled(False)
        self.clearButton.setEnabled(True)
        self.errorInfoLabel.setText("")

    def dataEntryAction(self):
        #When data starts getting entered
            #Disable the Save button
            #Disable the Load button

            self.saveToTargetButton.setEnabled(True)
            self.loadButton.setEnabled(False)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        import re
        exprFirstName = r"<FirstName>(.+)</FirstName>"
        exprLastName = r"<LastName>(.+)</LastName>"
        exprAddressName = r"<Address>(.+)</Address>"
        exprCityName = r"<City>(.+)</City>"
        exprStateName = r"<State>(.+)</State>"
        exprZIP = r"<ZIP>(.+)</ZIP>"
        exprEmail = r"<Email>(\w+@\w+\.\w+)</Email>"

        with open(filePath, "r") as myFile:
            all_lines = myFile.read()

        m = re.search(exprFirstName, all_lines)
        if m:
            self.firstNameLineEdit.setText(m.group(1))

        m = re.search(exprLastName, all_lines)
        if m:
            self.lastNameLineEdit.setText(m.group(1))

        m = re.search(exprAddressName, all_lines)
        if m:
            self.addressLineEdit.setText(m.group(1))

        m = re.search(exprCityName, all_lines)
        if m:
            self.cityLineEdit.setText(m.group(1))

        m = re.search(exprStateName, all_lines)
        if m:
            self.stateLineEdit.setText(m.group(1))

        m = re.search(exprZIP, all_lines)
        if m:
            self.zipLineEdit.setText(m.group(1))

        m = re.search(exprEmail, all_lines)
        if m:
            self.emailLineEdit.setText(m.group(1))



    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
