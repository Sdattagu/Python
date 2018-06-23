#===============

#Shounak Dattagupta
#12/4/2016
#HomographyGUI

#===============

import sys

from PySide.QtGui import *
from PySide.QtCore import *
from scipy.misc import *

from Homography import *
from HomographyGUI import *


class HomographyApp(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(HomographyApp, self).__init__(parent)
        #First set up the UI calling HomographyGUI's setupUI() function
        self.setupUi(self)

        #NOTES:
        #clicked is an indicator that this function should be called since GUI button has been "clicked"
        #connect() maps the button click to call the function that is passed in as the parameter.

        print("Initializing defaults...")

        #GLOBALS for ease of access
        self.target_pixel_map = None
        self.point_ind = 0
        self.readyFlag = 0
        self.transformedFlag = 0
        self.target_bu = None
        self.fp = ""
        self.homography_image = None
        self.source_image = None #For Homography
        self.target_image = None #For Homography

        self.acq_points_pb.setDisabled(True)
        self.reset_pb.setDisabled(True)
        self.save_pb.setDisabled(True)
        self.transform_pb.setDisabled(True)
        self.Effect_option_cb.setDisabled(True)
        self.source_image_gv.setDisabled(True)
        self.target_image_gv.setDisabled(True)
        self.sourceLoaded = 0
        self.targetLoaded = 0
        #self.load_source_pb.setDisabled(True)
        self.up_left_le.setDisabled(True)
        self.up_right_le.setDisabled(True)
        self.low_left_le.setDisabled(True)
        self.low_right_le.setDisabled(True)
        #self.load_target_pb.setDisabled(True)

        self.load_source_pb.clicked.connect(self.loadSourceImageFunction)
        self.load_target_pb.clicked.connect(self.loadTargetImageFunction)
        self.acq_points_pb.clicked.connect(self.acq_evaluate)
        self.save_pb.clicked.connect(self.saveDiagBoxFunction)
        self.transform_pb.clicked.connect(self.applyHomography)
        self.reset_pb.clicked.connect(self.resetFunction)

        self.keyPressEvent = self.rm_point

        self.initialState()


    def initialState(self):

        print("Initial State.")
       #When you first run the application;
            #- it should start with all widgets disabled.
                #- EXCEPT for load source and load target images.

        #Force the user to load the source AND target images to continue.
            #- Clicking on these buttons will pop up a file select dialog box.
                #- Allow user to select an image.
                #- Once an image is selected, it should display on the widget below the button.
                    #- The source_image_gv or target_image_gv boxes, respectively.

        #Assume both images will either be gray-scale or color images.


        #LD_SRC / LD_TARG
        self.load_source_pb.setEnabled(True)
        self.load_target_pb.setEnabled(True)

        #If Reset Button is Pushed
        #self.reset_pb.clicked.connect(self.resetForm)

    def loadedState(self):

        print("Loaded State.")
        """LOADED STATE"""
        """
            In this state means source and target have been verified as loaded.

            The acquire points button + the text boxes have been enabled to collect target coordinates.

            Three possible actions:
                - Reload a different source image
                    - Click again on the Load Source button
                - Reload a different target image
                    - Click again on the Load Target button
                - Select the target points, via clicking on the Acquire Points button
                    - Change application state to point selection state.
        """


        self.load_source_pb.setEnabled(True)
        self.load_target_pb.setEnabled(True)
        self.acq_points_pb.setEnabled(True)
        self.Effect_option_cb.setEnabled(False)
        self.transform_pb.setEnabled(False)
        self.reset_pb.setEnabled(False)
        self.save_pb.setEnabled(False)

        pass


    def pointSelectState(self):

        print("Point-Selection State.")
        """ POINT SELECTION STATE"""
        """
            Disable the loading buttons (src and target)
                - Prevent reloading while selecting target points.

            Procedure:
                1) Using the mouse, user hovers over TARGET image and clicks to select first point
                2) Once point is selected, populate first text box with coordinates of that point.
                    - Register 4 clicks, populate boxes in order
                        - up_left, up_right, low_left, low_right
                    - Selection behavior is repeated until all points are selected
                3) Backspace -> prior point is deleted
                    - Backspace deletes most recent point
                    - pointInd = 1,2,3,4 -> check which point was just populated to know which to delete.

                4) If acq_points_pb is hit (toggled) BEFORE all four points are selected (pointInd != 4)
                    - reset all text boxes (coordinates all moot)
                    - Enable loading buttons (src / target pbs)
                    - Send application to Loaded State.

                5) ELSE IF acq_points_pb is hit (toggled) AFTER all four points are selected (pointInd == 4)
                    - Enable everything
                    - send app into Ready State.
        """
        self.point_ind += 1

        self.up_left_le.setEnabled(True)
        self.up_right_le.setEnabled(True)
        self.low_left_le.setEnabled(True)
        self.low_right_le.setEnabled(True)

        self.load_source_pb.setDisabled(True)
        self.load_target_pb.setDisabled(True)
        self.transform_pb.setDisabled(True)
        #self.reset_pb.setDisabled(True)
        self.save_pb.setDisabled(True)
        self.Effect_option_cb.setDisabled(True)
        self.Effect_label.setDisabled(True)

        self.target_pixel_map.mousePressEvent = self.assign_point

        pass

    def readyState(self):
        print("Ready State.")

        """ READY STATE"""
        """
            Application now has all the information it needs to perform the homography as shown in Figure 6.

            Clicking on "Load Source ..." pb will allow for reloading a new source image

            Clicking on "Load Target ..." pb will allow for reloading a new target image
                - If this happens, reset text boxes, send application into Loaded state.

            Clicking on "Acquire Points" will send app into Point-Select state

            Changing the option in "Effect" drop-down has no additional side-effects
                - will not affect any other part of the GUI.

            Clicking "Reset" will have no effect

            Clicking "Save ..." will pop up a dialog box to select a target file name to save the target image to a
            different file

            Clicking on "Transform" will apply homography, with selected effect, and show results.
                - Disable point selection mechanism
                    - Bring application into "Transformed" state.
        """

        self.readyFlag = 1
        self.load_source_pb.setEnabled(True)
        self.load_target_pb.setEnabled(True)
        self.acq_points_pb.setEnabled(True)
        self.save_pb.setEnabled(True)
        self.transform_pb.setEnabled(True)
        self.reset_pb.setEnabled(True)
        pass

    def applyHomography(self):
        #Applies the Homography using the pre-built Homography class.
        #First determine if we are doing a color transform or regular transform
            #Accomplished by checking dimensions of source_image
                #If 2 -> regular, if 3 -> color

        if(self.source_image.ndim == 2):
            if(self.target_image.ndim == 2):
                trans = Transformation(self.source_image)
            elif(self.target_image.ndim == 3):
                self.source_image = np.dstack((self.source_image, self.source_image, self.source_image))
                trans = ColorTransformation(self.source_image)
        elif(self.source_image.ndim == 3):
            if(self.target_image.ndim == 2):
                self.target_image = np.dstack((self.target_image, self.target_image, self.target_image))
                trans = ColorTransformation(self.source_image)
            elif(self.target_image.ndim == 3):
                trans = ColorTransformation(self.source_image)

        #Second, compile the target points using the line edit boxes for coordinates
            # 4x2 float64 array
            #representing four (x', y') points

        targetPoints = np.array([[0 for x in range(2)] for y in range(4)], dtype=np.float64)

        targetPoints[0][0] = self.up_left_le.text().split(', ')[0]
        targetPoints[0][1] = self.up_left_le.text().split(', ')[1]

        targetPoints[1][0] = self.up_right_le.text().split(', ')[0]
        targetPoints[1][1] = self.up_right_le.text().split(', ')[1]

        targetPoints[2][0] = self.low_left_le.text().split(', ')[0]
        targetPoints[2][1] = self.low_left_le.text().split(', ')[1]

        targetPoints[3][0] = self.low_right_le.text().split(', ')[0]
        targetPoints[3][1] = self.low_right_le.text().split(', ')[1]

        #Third, figure out which Effect (if any) is selected from combo box
            #currentIndex() and hard-coded comparison

        effect = None
        if(self.Effect_option_cb.currentIndex() == 1):
            effect = Effect.rotate90
        elif(self.Effect_option_cb.currentIndex() == 2):
            effect = Effect.rotate180
        elif(self.Effect_option_cb.currentIndex() == 3):
            effect = Effect.rotate270
        elif(self.Effect_option_cb.currentIndex() == 4):
            effect = Effect.flipHorizontally
        elif(self.Effect_option_cb.currentIndex() == 5):
            effect = Effect.flipVertically
        elif(self.Effect_option_cb.currentIndex() == 6):
            effect = Effect.transpose

        #Finally, perform transform
            #setupTransformation(target_points, effect=effect)
            #transformImageOnto(self.target_image)

        trans.setupTransformation(targetPoints, effect=effect)
        self.homography_image = trans.transformImageOnto(self.target_image)

        #Save the transformed image as a .png and pixel map it onto target_image_gv
            #Similar process to before.
        #Save as a .png image
        imsave("Homography_GUI_out.png", self.homography_image)
        #Create a pixel map for the object
            #Create an instance of QGraphicsScene()
                #Surface for managing 2D objects (an image)
        scene = QtGui.QGraphicsScene() #new instance of scene, displays 2D item.

        #Get a pixel map of the image the user loaded.
            #Assigns a pixel map property to the loaded image.
            #Sets the item's current pix map.
        item = QtGui.QGraphicsPixmapItem(QPixmap("Homography_GUI_out.png"))

        #Add the pixel mapped item to the scene.
        scene.addItem(item)
        self.target_image_gv.setScene(scene)
        self.target_image_gv.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.target_pixel_map = item

        #Transition to transformedState.
        self.transformedState()

    def transformedState(self):

        print("Transformed State.")
        self.transformedFlag = 1
        self.save_pb.setEnabled(True)
        self.reset_pb.setEnabled(True)
        self.transform_pb.setEnabled(True)
        self.Effect_option_cb.setEnabled(True)
        self.acq_points_pb.setEnabled(False)
        self.load_source_pb.setEnabled(True)
        self.load_target_pb.setEnabled(True)

        self.up_left_le.setEnabled(False)
        self.up_right_le.setEnabled(False)
        self.low_left_le.setEnabled(False)
        self.low_right_le.setEnabled(False)


    def resetFunction(self):
        self.up_left_le.setText("")
        self.up_right_le.setText("")
        self.low_right_le.setText("")
        self.low_left_le.setText("")

        self.homography_image = None

        scene = QtGui.QGraphicsScene()
        item = QtGui.QGraphicsPixmapItem(QPixmap(self.target_bu))
        scene.addItem(item)
        self.target_image_gv.setScene(scene)
        self.target_image_gv.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.target_pixel_map = item

        self.target_image = imread(self.fp)
        #self.target_bu = imread(self.fp)

        self.readyState()
        print("Reset")


    def saveDiagBoxFunction(self):
        #Similar to loading an image dialog box, but for saving. duh.
        self.fp, _ = QFileDialog.getSaveFileName(self, caption='Save Target to ...')
        if not self.fp:
            return
        imsave(self.fp, self.target_image, "png")

    def loadTargetImageFromReadyFunction(self):
        #Will just clear the text boxes before loading a new target image
        self.up_left_le.setText("")
        self.up_right_le.setText("")
        self.low_right_le.setText("")
        self.low_left_le.setText("")
        self.loadTargetImageFunction()
        self.readyFlag = 0
        self.loadedState()

    def acq_evaluate(self):
        #This function is called when the acq_points_pb is pushed
        #It is required in order to work with "toggling" the acq button.
        #When the acq button is pushed, before moving to the Ready state,
            #We have to check if four points have been collected

        print(self.point_ind)
        print("in eval")
        if(self.point_ind == 0 or self.point_ind == 1 or self.readyFlag == 1):
            if(self.readyFlag == 1):
                self.readyFlag = 0
                self.point_ind = 0
            self.point_ind = 0
            self.low_left_le.setText("")
            self.low_right_le.setText("")
            self.up_right_le.setText("")
            self.up_left_le.setText("")
            self.pointSelectState()


        elif(self.point_ind > 0 and self.point_ind <= 4):

            print(self.point_ind)

            self.point_ind = 1

            self.low_left_le.setText("")
            self.low_right_le.setText("")
            self.up_right_le.setText("")
            self.up_left_le.setText("")

            self.load_source_pb.setEnabled(True)
            self.load_target_pb.setEnabled(True)

            #self.loadedState()

        elif(self.point_ind == 5):
            self.point_ind = 1
            self.acq_points_pb.setEnabled(True)
            self.reset_pb.setEnabled(True)
            self.source_image_gv.setEnabled(True)
            self.target_image_gv.setEnabled(True)
            self.sourceLoaded = 0
            self.targetLoaded = 0
            self.load_source_pb.setEnabled(True)
            self.Effect_option_cb.setEnabled(True)
            self.save_pb.setEnabled(True)
            self.up_left_le.setEnabled(True)
            self.up_right_le.setEnabled(True)
            self.low_left_le.setEnabled(True)
            self.low_right_le.setEnabled(True)
            self.load_target_pb.setEnabled(True)
            self.transform_pb.setEnabled(True)
            self.readyState()

    def assign_point(self, event):
        #This is an event based function
            #If mouse is clicked inside of the pixel map,
            #Grab the tuple coordinates of the click, unpack into x and y
        #Depending on point_index,
            #If point_index == 0
                #Assign the x and y coordinates to up_left as formatted string.
            #If point_index == 1
                #Assign the x and y coordinates to up_right as formatted string.
            #If point_index == 2
                #Assign the x and y coordinates to bottom_left as formatted string.
            #If point_index == 3
                #Assign the x and y coordinates to bottom_right as formatted string.
        x = event.pos().x()
        y = event.pos().y()

        print(event.pos().x())
        print(x)

        if(self.point_ind >= 4):
            self.point_ind = 4

        print("Click : " + str(self.point_ind))
        if self.point_ind == 1:
            #Assign the x and y coordinates to up_left as formatted string.
            self.up_left_le.setText("{0:.0f}.0, {1:.0f}.0".format(x, y))
            self.point_ind += 1

        elif self.point_ind == 2:
            #Assign the x and y coordinates to up_right as formatted string.
            self.up_right_le.setText("{0:.0f}.0, {1:.0f}.0".format(x, y))
            self.point_ind += 1

        elif self.point_ind == 3:
            #Assign the x and y coordinates to bottom_left as formatted string.
            self.low_left_le.setText("{0:.0f}.0, {1:.0f}.0".format(x, y))
            self.point_ind += 1

        elif self.point_ind == 4:
            #Assign the x and y coordinates to bottom_right as formatted string.
            self.low_right_le.setText("{0:.0f}.0, {1:.0f}.0".format(x, y))
            self.point_ind += 1


    def rm_point(self, event):
        #This is an event based function
            #If a key is pressed, we default to this function
            #We need to check if the key that was pressed (event) is the BACKSPACE key
                #If so, depending on current point_ind, we set text input to empty.

        self.point_ind -= 1
        if(self.point_ind <= 0):
            self.point_ind = 1

        print("Rm stage : " + str(self.point_ind))
        if(event.key() == QtCore.Qt.Key_Backspace):
            if(self.point_ind == 1):
                self.up_left_le.setText("")

            elif(self.point_ind == 2):
                self.up_right_le.setText("")
                #self.point_ind -= 1

            elif(self.point_ind == 3):
                self.low_left_le.setText("")
                #self.point_ind -= 1

            elif(self.point_ind == 4):
                self.low_right_le.setText("")
                #self.point_ind -= 1



    """ LD_SRC / LD_TARG """


    def loadSourceImageFunction(self):
        #This function is called when user presses "Load Source" pb

        print("Load Source")
        #Set the load_pb_ind flag to source
        load_pb_ind = "Source_load"
        #File select dialog box should pop up
            #Use the getOpenFileName function in QFileDialog Class
                #First arg refers to calling class
                #Second is name of the dialog box that pops up
                #Third filters it to only show the .png files.
        self.fp, _ = QFileDialog.getOpenFileName(self, caption="Source Image Select ...", filter="Image Files (*.png)" )
        if not self.fp:
            #If there isn't any relevant fp, then just return from the function
            #Here for error handling
            return

        #Call function to actually populate the widget box
            #Source load flag is set.
        self.loadImageFileFunction(self.fp, load_pb_ind)

    def loadTargetImageFunction(self):
        #This function is called when user presses "Load Source" pb

        print("Load Target")
        #Set the load_pb_ind flag to source
        load_pb_ind = "Target_load"
        #File select dialog box should pop up
            #Use the getOpenFileName function in QFileDialog Class
                #First arg refers to calling class
                #Second is name of the dialog box that pops up
                #Third filters it to only show the .png files.
        #I put whatever in there to absorb whatever the second output is, makes it work

        self.fp, whatever = QFileDialog.getOpenFileName(self, caption="Target Image Select ...", filter="Image Files (*.png)")
        self.target_bu = self.fp
        if not self.fp:
            #If there isn't any relevant fp, then just return from the function
            #Here for error handling
            return

        #Call function to actually populate the widget box
            #Target load flag is set.
        self.loadImageFileFunction(self.fp, load_pb_ind)

    """ LD_IMG """

    def loadImageFileFunction(self, fp, load_pb_ind):

        #print("Load Image")
        #This function actually gets the .png and put it into the appropriate widget.
        #Check which widget (source or target) graphics view we're loading
            #Check the load_pb_ind flag
                #Depending on which it is, set the source/targetLoaded member variable flags.
                #Enable the appropriate gv widget based on flag
                    #self.source_image_gv.setEnabled(True), etc...
            if(load_pb_ind == "Source_load"):
                #target_bu = fp
                self.source_image = imread(self.fp)
                self.sourceLoaded = 1
                self.source_image_gv.setEnabled(True)
            elif(load_pb_ind == "Target_load"):
                self.target_image = imread(self.fp)
                self.targetLoaded = 1
                self.target_image_gv.setEnabled(True)


            #print(self.sourceLoaded)
            #print(self.targetLoaded)

            #Create a pixel map for the object
                #Create an instance of QGraphicsScene()
                    #Surface for managing 2D objects (an image)
            scene = QtGui.QGraphicsScene() #new instance of scene, displays 2D item.

            #Get a pixel map of the image the user loaded.
                #Assigns a pixel map property to the loaded image.
                #Sets the item's current pix map.
            item = QtGui.QGraphicsPixmapItem(QPixmap(self.fp))

            #Add the pixel mapped item to the scene.
            scene.addItem(item)


            #Write the newly created scene to the appropriate window
            if(load_pb_ind == "Source_load"):
                self.source_image_gv.setScene(scene)
                self.source_image_gv.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
            elif(load_pb_ind == "Target_load" and self.transformedFlag == 0):
                self.target_image_gv.setScene(scene)
                self.target_image_gv.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
                self.target_pixel_map = item

            if(self.transformedFlag == 1):
                scene = QtGui.QGraphicsScene()
                item = QtGui.QGraphicsPixmapItem(QPixmap(self.target_bu))
                scene.addItem(item)
                self.target_image_gv.setScene(scene)
                self.target_image_gv.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
                self.target_pixel_map = item

            if(self.readyFlag == 1 or self.transformedFlag == 1):
                print("in")
                self.up_left_le.setText("")
                self.up_right_le.setText("")
                self.low_right_le.setText("")
                self.low_left_le.setText("")
                self.sourceLoaded = 1
                self.targetLoaded = 1

            #TRANSITION TO LOADED STATE
            if(self.sourceLoaded and self.targetLoaded):
                print("point ind" + str(self.point_ind))
                self.sourceLoaded = 0
                self.targetLoaded = 0
                self.acq_points_pb.setEnabled(True)
                self.up_left_le.setEnabled(True)
                self.up_right_le.setEnabled(True)
                self.low_left_le.setEnabled(True)
                self.low_right_le.setEnabled(True)
                self.loadedState()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = HomographyApp()

    currentForm.show()
    currentApp.exec_()
