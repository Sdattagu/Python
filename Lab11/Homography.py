#Shounak Dattagupta
#Homography

"""
Implement the Homography class that holds the homography matrix details and the logic that is associated with it.
The member definitions below represent the public interface that your class should conform to.

MEMBER VARIABLES
    forwardMatrix
        #A 3x3 numpy array of type float64 containing the forward projection matrix.
    inverseMatrix
        #A 3x3 numpy array of type float64 containing the inverse projection matrix.
    n_degree
        #Used for initializing the A_n 8x2 matrix.
            #n_degree++ after each successful creation of an A_n matrix.
    A
        #8x8 Matrix used to calculate homography (h) matrix
            #Ah = b
    b
        #8x1 Matrix used to calculate homography (h) matrix
            #Ah = b

"""

import numpy as np
import scipy as sp
from enum import Enum
#from Transformation import *
#from ColorTransformation import *
from scipy.interpolate import RectBivariateSpline

"""
EFFECT Enum CLASS
"""

class Effect(Enum):

    #Enum class has the following options:
        rotate90 = 1
        rotate180 = 2
        rotate270 = 3
        flipHorizontally = 4
        flipVertically = 5
        transpose = 6

"""
HOMOGRAPHY CLASS
"""

class Homography:
    def __init__(self, **kwargs):
        #Initializes the instance of the Homography class and populates the member variables using one of the following two options
            #homographyMatrix
                #A 3x3 numpy array of type float64
            #sourcePoints
                #A 4x2 float64 array, representing four correspondences.
            #targetPoints
                #A 4x2 float64 array, representing four correspondences.
            #"Optional" effect
                #instance of Effect Enum.


        #IF homographyMatrix is a key in kwargs
            #If array does not have expected dimensions OR not correct type
                #Raise a ValueError with an appropriate message.
        #ELIF sourcePoints AND targetPoints are keys in kwargs
            #IF sourcePoints or targetPoints does not have 4x2 dims or float64 type
                #raise ValueError with an appropriate message.
            #ELSE
                # invoke the method computeHomography()
        #ELSE
            # Raise ValueError if missing an expected keyword.

        #IF effect is provided but is not instance of Effect enum
            #raise TypeError with an appropriate message.

        listOfKeys = list(kwargs.keys())

        self.n_degree = 0

        if("homographyMatrix" not in listOfKeys and ("sourcePoints" not in listOfKeys and "targetPoints" not in listOfKeys)):
            raise ValueError("Missing expected keyword: homographyMatrix OR source+targetPoints.")
        else:
            if("homographyMatrix" in listOfKeys):

                hoMat = kwargs["homographyMatrix"]
                type64Flag = True

                for row in hoMat:
                    for index in range(2):
                        if(type(row[index]) != np.float64):
                            type64Flag = False

                if((len(hoMat) == 3 and len(hoMat[0] == 3))):
                    if(type64Flag == True):
                        self.forwardMatrix = kwargs["homographyMatrix"]
                        self.inverseMatrix = np.linalg.inv(self.forwardMatrix)
                    else:
                        raise ValueError("Homography matrix must be a 3x3 numpy array of float64.")
                else:
                    raise ValueError("Homography matrix must be a 3x3 numpy array.")


            elif("sourcePoints" in listOfKeys and "targetPoints" in listOfKeys):
                sPoints = kwargs["sourcePoints"]
                tPoints = kwargs["targetPoints"]
                type64FlagSource = True
                type64FlagTarget = True

                sourcePointsGood = False
                targetPointsGood = False

                effectGood = False

                for row in sPoints:
                    for index in range(2):
                        if(type(row[index]) != np.float64):
                            type64FlagSource = False

                for element in tPoints:
                    for index in range(2):
                        if(type(row[index]) != np.float64):
                            type64FlagTarget = False

                if((len(sPoints) == 4 and len(sPoints[0]) == 2)):
                    if(type64FlagSource == True):
                        self.sourcePoints = kwargs["sourcePoints"]
                        sourcePointsGood = True
                    else:
                        raise ValueError("sourcePoints must be a 4x2 array of float64.")
                else:
                    raise ValueError("sourcePoints must be 4x2 array.")

                if((len(tPoints) == 4 and len(tPoints[0] == 2))):
                    if(type64FlagTarget == True):
                        self.targetPoints = kwargs["targetPoints"]
                        targetPointsGood = True
                    else:
                        raise ValueError("taretPoints must be a 4x2 array of float64.")
                else:
                    raise ValueError("targetPoints must be 4x2 array.")

                if("effect" in listOfKeys):
                    #eList = ["rotate90", "rotate180", "rotate270", "flipHorizontally", "flipVertically", "transpose"]
                    if (kwargs["effect"] == None or type(kwargs["effect"]) == Effect):
                        self.effect = kwargs["effect"]
                        effectGood = True
                    else:
                        raise TypeError("Provided effect is not an instance of Effect enum.")

                if(sourcePointsGood == True and targetPointsGood == True and effectGood == True):
                    self.computeHomography(self.sourcePoints, self.targetPoints, self.effect)
                elif(sourcePointsGood == True and targetPointsGood == True):
                    self.computeHomography(self.sourcePoints, self.targetPoints, None)

            else:
                raise ValueError("Missing expected keyword: sourcePoints or targetPoints.")




    def computeHomography(self, sourcePoints, targetPoints, effect=None):
        #Takes in the two arrays
            #computes and returns the homography from the given correspondences.
            #IF effect is provided
               #Apply the pair re-ordering BEFORE constructing the homography matrix

        if(effect != None):
            newSourcePoints = None
            if(effect == Effect.rotate90):
                newSourcePoints = self.rotate90(sourcePoints)
            if(effect == Effect.rotate180):
                newSourcePoints = self.rotate180(sourcePoints)
            if(effect == Effect.rotate270):
                newSourcePoints = self.rotate270(sourcePoints)
            elif(effect == Effect.flipHorizontally):
                newSourcePoints = self.flipHorizontally(sourcePoints)
            elif(effect == Effect.flipVertically):
                newSourcePoints = self.flipVertically(sourcePoints)
            elif(effect == Effect.transpose):
                newSourcePoints = self.transpose(sourcePoints)
            #Start process of finding homography matrix with modified source and target points arrays.
            self.calcHomographyMatrix(newSourcePoints, targetPoints)

        else:
            #Start process of finding homography matrix with unmodified source and target points arrays.
            self.calcHomographyMatrix(sourcePoints, targetPoints)


    def calcHomographyMatrix(self, sourcePoints, targetPoints):
        #calculate A_n and B_n matrices
        A_1 = self.initA_nMatrix(sourcePoints, targetPoints, self.n_degree)
        B_1 = self.initB_nMatrix(targetPoints, self.n_degree)
        A_2 = self.initA_nMatrix(sourcePoints, targetPoints, self.n_degree)
        B_2 = self.initB_nMatrix(targetPoints, self.n_degree)
        A_3 = self.initA_nMatrix(sourcePoints, targetPoints, self.n_degree)
        B_3 = self.initB_nMatrix(targetPoints, self.n_degree)
        A_4 = self.initA_nMatrix(sourcePoints, targetPoints, self.n_degree)
        B_4 = self.initB_nMatrix(targetPoints, self.n_degree)
        #Stack A_n and B_n matrices
        A = self.compile_A_matrix(A_1, A_2, A_3, A_4)
        b = self.compile_B_matrix(B_1, B_2, B_3, B_4)
        #Compute "h" column vector
        h = np.linalg.solve(A, b)
        #print(h)
        #Rearrange into homography matrix H
        H = self.rearrangeHMatrix(h)
        self.forwardMatrix = H
        self.inverseMatrix = np.linalg.inv(self.forwardMatrix)

    def initA_nMatrix(self, sourcePoints, targetPoints, n_degree):
    #Creates A_n matrix for given source and target correspondence point
        #Return this A_n to merge to larger A matrix.
        #Use "n_degree" to init A_n.

        A_n = np.array([[0 for x in range(8)] for y in range(2)], dtype=np.float64)
        x = 0 #Internal index
        y = 1 #Internal index

        #FIRST ROW OF A_n
        A_n[0][0] = sourcePoints[n_degree][x]
        A_n[0][1] = sourcePoints[n_degree][y]
        A_n[0][2] = np.float64(1)
        A_n[0][-1] = -targetPoints[n_degree][x] * sourcePoints[n_degree][y]
        A_n[0][-2] = -targetPoints[n_degree][x] * sourcePoints[n_degree][x]

        #SECOND ROW OF A_n
        A_n[1][3] = sourcePoints[n_degree][x]
        A_n[1][4] = sourcePoints[n_degree][y]
        A_n[1][5] = np.float64(1)
        A_n[1][-1] = -targetPoints[n_degree][y] * sourcePoints[n_degree][y]
        A_n[1][-2] = -targetPoints[n_degree][y] * sourcePoints[n_degree][x]

        #printA_n(A_n)
        return A_n

    def initB_nMatrix(self, targetPoints, n_degree):
        #Creates B_n matrix for given source and target correspondence point
            #Return this B_n to merge to larger B matrix.
            #Use "n_degree" to init B_n.

        B_n = np.array([[0 for x in range(1)] for y in range(2)])
        x = 0 #Internal index
        y = 1 #Internal index

        B_n[0] = targetPoints[n_degree][x]
        B_n[1] = targetPoints[n_degree][y]

        #printB_n(B_n)
        self.incN_degree(self.n_degree)

        return B_n

    def compile_A_matrix(self, A_1, A_2, A_3, A_4):
        #Stack all of the A_n matrices
        A = np.concatenate((A_1, A_2, A_3, A_4), axis=0)

        #print_A(A)

        return A

    def compile_B_matrix(self, B_1, B_2, B_3, B_4):
        #Stack all of the B_n matrices
        B = np.concatenate((B_1, B_2, B_3, B_4), axis=0)

        #print_B(B)

        return B

    def rearrangeHMatrix(self, h):
        #Re-arrange column vector into homography matrix H
        H = np.array([[0 for x in range(3)] for y in range(3)], np.float64)

        H[0][0] = h[0]
        H[0][1] = h[1]
        H[0][2] = h[2]
        H[1][0] = h[3]
        H[1][1] = h[4]
        H[1][2] = h[5]
        H[2][0] = h[6]
        H[2][1] = h[7]
        H[2][2] = np.float64(1)

        print(H)
        return H

    def incN_degree(self, n_degree):
        #Increment the n_degree member variable.
        self.n_degree += 1

#==== EFFECT ENUM OPS ====

    #==== ROTATE ====
    def rotate90(self, sourcePoints):

        rotatedSourcePoints = np.float64(np.array([[0 for x in range(2)] for y in range(4)]))

        #1 => 2
        rotatedSourcePoints[1][0] = sourcePoints[0][0]
        rotatedSourcePoints[1][1] = sourcePoints[0][1]
        #2 => 4
        rotatedSourcePoints[3][0] = sourcePoints[1][0]
        rotatedSourcePoints[3][1] = sourcePoints[1][1]
        #3 => 1
        rotatedSourcePoints[0][0] = sourcePoints[2][0]
        rotatedSourcePoints[0][1] = sourcePoints[2][1]
        #4 => 3
        rotatedSourcePoints[2][0] = sourcePoints[3][0]
        rotatedSourcePoints[2][1] = sourcePoints[3][1]

        return rotatedSourcePoints

    def rotate180(self, sourcePoints):

        rotatedSourcePoints = np.float64(np.array([[0 for x in range(2)] for y in range(4)]))

        #1 => 4
        rotatedSourcePoints[3][0] = sourcePoints[0][0]
        rotatedSourcePoints[3][1] = sourcePoints[0][1]
        #2 => 3
        rotatedSourcePoints[2][0] = sourcePoints[1][0]
        rotatedSourcePoints[2][1] = sourcePoints[1][1]
        #3 => 2
        rotatedSourcePoints[1][0] = sourcePoints[2][0]
        rotatedSourcePoints[1][1] = sourcePoints[2][1]
        #4 => 1
        rotatedSourcePoints[0][0] = sourcePoints[3][0]
        rotatedSourcePoints[0][1] = sourcePoints[3][1]

        return rotatedSourcePoints

    def rotate270(self, sourcePoints):

        rotatedSourcePoints = np.float64(np.array([[0 for x in range(2)] for y in range(4)]))

        #1 => 3
        rotatedSourcePoints[2][0] = sourcePoints[0][0]
        rotatedSourcePoints[2][1] = sourcePoints[0][1]
        #2 => 1
        rotatedSourcePoints[0][0] = sourcePoints[1][0]
        rotatedSourcePoints[0][1] = sourcePoints[1][1]
        #3 => 4
        rotatedSourcePoints[3][0] = sourcePoints[2][0]
        rotatedSourcePoints[3][1] = sourcePoints[2][1]
        #4 => 2
        rotatedSourcePoints[1][0] = sourcePoints[3][0]
        rotatedSourcePoints[1][1] = sourcePoints[3][1]

        return rotatedSourcePoints

    #==== FLIP ====
    def flipHorizontally(self, sourcePoints):
    #flipHorizontally

        flippedSourcePoints = np.float64(np.array([[0 for x in range(2)] for y in range(4)]))

        #1 => 3
        flippedSourcePoints[2][0] = sourcePoints[0][0]
        flippedSourcePoints[2][1] = -sourcePoints[0][1]
        #2 => 4
        flippedSourcePoints[3][0] = sourcePoints[1][0]
        flippedSourcePoints[3][1] = -sourcePoints[1][1]
        #3 => 1
        flippedSourcePoints[0][0] = sourcePoints[2][0]
        flippedSourcePoints[0][1] = sourcePoints[2][1]
        #4 => 2
        flippedSourcePoints[1][0] = sourcePoints[3][0]
        flippedSourcePoints[1][1] = sourcePoints[3][1]

        return flippedSourcePoints

    def flipVertically(self, sourcePoints):
    #flipVertically

        flippedSourcePoints = np.float64(np.array([[0 for x in range(2)] for y in range(4)]))

        #1 => 2
        flippedSourcePoints[1][0] = sourcePoints[0][0]
        flippedSourcePoints[1][1] = -sourcePoints[0][1]
        #2 => 1
        flippedSourcePoints[0][0] = sourcePoints[1][0]
        flippedSourcePoints[0][1] = -sourcePoints[1][1]
        #3 => 4
        flippedSourcePoints[3][0] = sourcePoints[2][0]
        flippedSourcePoints[3][1] = sourcePoints[2][1]
        #4 => 3
        flippedSourcePoints[2][0] = sourcePoints[3][0]
        flippedSourcePoints[2][1] = sourcePoints[3][1]

        return flippedSourcePoints

    #==== TRANSPOSE ====
    def transpose(self, sourcePoints):
    #transpose

        transposedSourcePoints = np.float64(np.array([[0 for x in range(2)] for y in range(4)]))

        #1 => 1
        transposedSourcePoints[0][0] = sourcePoints[0][0]
        transposedSourcePoints[0][1] = -sourcePoints[0][1]
        #2 => 3
        transposedSourcePoints[2][0] = sourcePoints[1][0]
        transposedSourcePoints[2][1] = -sourcePoints[1][1]
        #3 => 2
        transposedSourcePoints[1][0] = sourcePoints[2][0]
        transposedSourcePoints[1][1] = sourcePoints[2][1]
        #4 => 4
        transposedSourcePoints[3][0] = sourcePoints[3][0]
        transposedSourcePoints[3][1] = sourcePoints[3][1]

        return transposedSourcePoints

#==== DEV SECTION ====
#The functions in this section are isolated functions that can be tested
#for standalone functionality. May be merged into Homography class.
    #Need to add reflexive "self" to parameter list.

"""
TRANSFORMATION CLASS

Implement the Transformation class that manages the mechanics of applying a homography. It holds a
source image, and transforms it based on the homography provided to a given target image.

MEMBER VARIABLES
    #==== Variables that define range of iteration =====
    minXPoint
        #Minimum bounding X coordinate of containerImage.
    minYPoint
        #Minimum bounding Y coordinate of containerImage.
    maxXPoint
        #Maximum bounding X coordinate of containerImage.
    maxYPoint
        #Maximum bounding Y coordinate of containerImage.
    sourcePoints
        #source points array, for global and ease of access

    #==== Source image bounds =====
    columnCount
        #Defines maximum range of X in the source image.
    rowCount
        #Defines maximum range of Y in the source image.

"""

class Transformation:
    def __init__(self, sourceImage, homography=None):
        #Initializes an instance of the Transformation class using:
            # a specific sourceImage,
                # an instance of numpy array
            # an OPTIONAL instance of the Homography class.

        #IF sourceImage is not of correct type (instance of numpy array)
            #raise TypeError
        #ELIF homography is not instance of Homography class
            #raise TypeError

        self.maxXPoint = 0
        self.maxYPoint = 0
        self.minXPoint = 0
        self.minYPoint = 0

        if (type(sourceImage) != np.ndarray):
            raise TypeError("Source image is not an instance of numpy array.")
        elif(type(sourceImage) == np.ndarray):
            self.sourceImage = sourceImage
            self.findSourceImageBounds(sourceImage)

        if(homography != None):
            if (type(homography) != Homography):
                raise TypeError("homography is not an instance of Homography class")
            elif (type(homography) == Homography):
                self.homography = homography
        elif(homography == None):
            self.homography = homography

    def setupTransformation(self, targetPoints, effect=None):
        #Takes in targetPoints
            # 4x2 float64 array
            #representing four (x', y') points
        #optional instance of Effect class

        #Must ALWAYS be invoked before you apply the homography.
        #Two ways:
            #IF a Homography instance was passed to this Transformation instance when instantiated
                #use targetPoints to identify range of iteration in target image.
            #IF a Homography instance was NOT passed to this Transformation instance when instantiated
                #use targetPoints, as well as effect, to instantiate a new Homography instance.
                #compute homography matrix.
                #Then targetPoints can be used to identify the range of iteration.

        if (self.homography):
            self.computeRangeOfIteration(targetPoints)
        elif(self.homography == None):
            self.sourcePoints = self.computeSourcePointsFromSourceImage(self.sourceImage)
            if(effect != None):
                self.homography= Homography(sourcePoints=self.sourcePoints, targetPoints=targetPoints, effect=effect)
            elif(effect == None):
                self.homography = Homography(sourcePoints=self.sourcePoints, targetPoints=targetPoints)
            self.computeRangeOfIteration(targetPoints)

    def transformImageOnto(self, containerImage):
        #Takes in containerImage
            #instance of numpy array.
            #Homography target image.
        #If containerImage not correct type (instance of numpy array)
            #raise TypeError

        #This method uses the homography to transform the source image onto the container image
            #STEPS
                # Identify the target bounding box
                # For every point within the box,
                        #perform an inverse projection of the coordinates.
                        # IF the result of the inverse projection falls within bounds of source image
                            #read that value (potentially using 2D interpolation.)
                        # ELIF the result falls outside of the source image
                            #ignore that value.
        if(type(containerImage) != np.ndarray):
            raise TypeError("Container image is not instance of numpy array.")
        elif(type(containerImage) == np.ndarray):

            u = np.arange(0, (self.sourcePoints[1][0] + 1))
            v = np.arange(0, (self.sourcePoints[2][1] + 1))

            rect_B_spline = RectBivariateSpline(v, u, self.sourceImage, kx=1, ky=1)

            for a in np.arange(self.minXPoint, self.maxXPoint + 1):
                for b in np.arange(self.minYPoint, self.maxYPoint + 1):
                    invProject = self.performInverseProjection(a, b, (self.homography).inverseMatrix)
                    x = invProject[0]
                    y = invProject[1]
                    if(0 <= x <= (self.columnCount-1) and 0 <= y <= (self.rowCount-1)):
                        containerImage[b][a] = np.uint8(np.round(rect_B_spline(y, x)))

        #Return the result
        return containerImage

    def findSourceImageBounds(self, sourceImage):
        #Takes in a source image
            #Finds the columnCount and rowCount member variables
            #Used to determine if inverse projection falls within bounds of source image.

        row = sourceImage.shape[0]
        columns = sourceImage.shape[1]

        """
        for point in sourceImage:
            x = point[0]
            y = point[1]

            if(x > maxYPoint):
                maxXPoint = x

            if(y > maxYPoint):
                maxYPoint = y
        """

        self.columnCount = columns
        self.rowCount = row

    def performInverseProjection(self, x, y, inverseMatrix):
        #Perform the inverse projection of coordinates in the containerImage.
            #STEPS
                #Set up product matrix with x, y, 1.
                #inverseMatrix (3x3) dot productMatrix (3x1) = invProjectUnscaled (3x1).
                #round(invProjectScaled) = invProjectUnscaled / invProjectUnscaled[2], scalar division.
                #Verify invProjectScaled[2] is 1.
                    #This is result.
        #Return the resultant 3x1 matrix.

        productMatrix = np.array([[x], [y], [1]], np.float64)

        invProjectUnscaled = np.dot(inverseMatrix, productMatrix)
        x_3 = invProjectUnscaled[2]
        invProjectScaled = np.round(np.divide(invProjectUnscaled, x_3), decimals = 3)

        if(invProjectScaled[2] == np.float64(1)):
            return invProjectScaled
        else:
            raise ValueError("x_3 is not 1 in scaled matrix.")

    def computeRangeOfIteration(self, targetPoints):
        #Computes the range of iteration from the targetPoints.
            #Min X, Min Y, Max X, Max Y.
                #Member variables that can be accessed later for iteration.

        """
        minXPoint = 999999.9999
        minYPoint = 999999.9999
        maxXPoint = -999999.9999
        maxYPoint = -999999.9999

        for row in range(targetPoints.shape[0]):
            x = targetPoints[row][0]
            y = targetPoints[row][1]

            if(x < minXPoint):
                self.minXPoint = x
            elif(x > maxYPoint):
                self.maxXPoint = x

            if(y < minYPoint):
                self.minYPoint = y
            elif(y > maxYPoint):
                self.maxYPoint = y
        """
        self.maxXPoint = targetPoints[:,0].max()
        self.maxYPoint = targetPoints[:,1].max()
        self.minXPoint = targetPoints[:,0].min()
        self.minYPoint = targetPoints[:,1].min()

    def computeSourcePointsFromSourceImage(self, sourceImage):
        #Computes the sourcePoints from the sourceImage
            #Gather the min/max X and Y coordinates
                #Return a sourcePoints 4x2 float64 array.

        rows = sourceImage.shape[0]
        columns = sourceImage.shape[1]

        #minXPoint = 999999.9999
        #minYPoint = 999999.9999
        #maxXPoint = -999999.9999
        #maxYPoint = -999999.9999

        sourcePoints = np.array([[0 for x in range(2)] for y in range(4)], dtype=np.float64)
        #print(np.shape(sourcePoints))

        """
        for point in sourceImage:
            x = point[0]
            y = point[1]

            if(x < minXPoint):
                minXPoint = x
            elif(x > maxYPoint):
                maxXPoint = x

            if(y < minYPoint):
                minYPoint = y
            elif(y > maxYPoint):
                maxYPoint = y
        """

        sourcePoints[0][0] = 0
        sourcePoints[0][1] = 0

        sourcePoints[1][0] = columns - 1
        sourcePoints[1][1] = 0

        sourcePoints[2][0] = 0
        sourcePoints[2][1] = rows - 1

        sourcePoints[3][0] = columns - 1
        sourcePoints[3][1] = rows - 1

        return sourcePoints

"""
COLOR_TRANSFORMATION CLASS

Inherit and extend the Transformation class that you implemented above to include the functionality of applying
a homography to a color image.

"""

class ColorTransformation(Transformation):
    def __init__(self, sourceImage, homography=None):
        #Init an instance of the ColorTransformation class using a specific sourceImage
        #and a homography instance.
        # After invoking the base initializer,
            #Verify that the image provided is a color image
                #Check its dimensions.

        if(homography != None):
            Transformation.__init__(self, sourceImage, homography)
        elif(homography == None):
            Transformation.__init__(self, sourceImage)

        if(len(sourceImage.shape) != 3):
            raise ValueError("Provided image is not a color image.")


    def transformImageOnto(self, containerImage):
        #Override this method to provide the same functionality as its base, but for color images.
        red = self.sourceImage[:,:,0] #Grab the red part of the container image.
        green = self.sourceImage[:,:,1] #Grab the blue part of the container image.
        blue = self.sourceImage[:,:,2] #Grab the green part of the container image.


        z = 0
        for channel in [red, green, blue]:
            if(type(containerImage) != np.ndarray):
                raise TypeError("Container image is not instance of numpy array.")
            elif(type(containerImage) == np.ndarray):

                u = np.arange(0, (self.sourcePoints[1][0] + 1))
                v = np.arange(0, (self.sourcePoints[2][1] + 1))

                rect_B_spline = RectBivariateSpline(v, u, channel, kx=1, ky=1)

                for a in np.arange(self.minXPoint, self.maxXPoint + 1):
                    for b in np.arange(self.minYPoint, self.maxYPoint + 1):
                        invProject = self.performInverseProjection(a, b, (self.homography).inverseMatrix)
                        x = invProject[0]
                        y = invProject[1]
                        if(0 <= x <= (self.columnCount-1) and 0 <= y <= (self.rowCount-1)):
                            containerImage[b][a][z] = np.uint8(np.round(rect_B_spline(y, x)))
            z += 1

        #Return the result
        return containerImage

"""
ADVANCED TRANSFORMATION CLASS
Contains the operations needed to perform "V" and "A" effects.
"""

class AdvancedTransformation:
    def __init__(self, sourceImage, v, h1, h2):
        #Init the instance of the AdvancedTransformation class.
            #The parameter sourceImage is an instance of numpy array.
            #v is an integer >= 0.
            #h1 is an integer >= 0.
            #h2 is an integer >= 0.
        #IF sourceImage is not a numpy array:
            #Raise a TypeError with appropriate message
        #ELIF sourceImage is not a color image:
            #Raise a ValueError with appropriate message.
        #IF number of columns in sourceImage is not an even number
            #Raise ValueError.

        if(type(sourceImage) != np.ndarray):
            raise TypeError("Source image is not an instance of numpy array.")
        elif(len(sourceImage.shape) != 3):
            raise ValueError("Provided image is not a color image.")

        if(sourceImage.shape[1]%2 != 0):
            raise ValueError("sourceImage does not have an even number of columns.")
        else:
            self.sourceImage = sourceImage
            self.columns = self.sourceImage.shape[0]
            self.rows = self.sourceImage.shape[1]

        if(v >= 0 and h1 >= 0 and h2 >= 0):
            self.v = v
            self.h1 = h1
            self.h2 = h2

    def applyEffectV(self):
        pass
    """
      #Apply effect "V" on the image provided to this instance and return the result.
        self.boundingBoxFromSourceImage(self.sourceImage)
        #Transform Left Side
        #Base changes to the abcdmn box
        self.constructRectImageBase()
        x_range = self.c / 2
        y_range = self.r + self.v
        containerImage = np.array([[[0 for x in range(1200)] for y in range(1600)] for z in range(3)], dtype=np.float64)
        #Use the changed abcdmn box to calculate new target points (to pass into setup Transform)
        targetPoints = self.constructNewTargetImageLeft()
        color_t = ColorTransformation(self.sourceImage, None)
        self.setupTransformation(targetPoints, None)
        color_t.transformImageOnto(containerImage)

        pass

    """
    def boundingBoxFromSourceImage(self, sourceImage):
        self.maxXPoint = sourceImage[:,0].max()
        self.maxYPoint = sourceImage[:,1].max()
        self.minXPoint = sourceImage[:,0].min()
        self.minYPoint = sourceImage[:,1].min()

    def constructRectImageBase(self):
        self.m = np.array([[0 for x in range(1)] for y in range(2)], dtype=np.float64)
        self.n = np.array([[0 for x in range(1)] for y in range(2)], dtype=np.float64)
        self.a = np.array([[0 for x in range(1)] for y in range(2)], dtype=np.float64)
        self.d = np.array([[0 for x in range(1)] for y in range(2)], dtype=np.float64)
        self.b = np.array([[0 for x in range(1)] for y in range(2)], dtype=np.float64)
        self.e = np.array([[0 for x in range(1)] for y in range(2)], dtype=np.float64)

        self.m[0] = (self.maxXPoint - self.minXPoint) / 2
        self.m[1] = 0
        self.n = self.m
        self.a[0] = self.minXPoint
        self.a[1] = 0
        self.d[0] = self.maxXPoint
        self.d[1] = 0
        self.b[0] = self.minXPoint
        self.b[1] = self.minYPoint
        self.e[0] = self.maxXPoint
        self.e[1] = self.minYPoint

        self.c = self.d[0] - self.a[0]
        self.r = self.b[1] - self.a[1]

    def constructNewTargetImageLeft(self):
        #LEFT SIDE OF IMAGE

        #Change b
        self.b[0] += self.h1
        self.b[1] += self.v

        #Change m
        self.m[0] -= self.h2
        self.m[1] -= self.v

        self.n[1] -= self.v

        targetPoints = np.array([[0 for x in range(2)] for y in range(4)], dtype=np.float64)

        targetPoints[0][0] = self.a[0]
        targetPoints[0][1] = self.a[1]

        targetPoints[1][0] = self.m[0]
        targetPoints[1][1] = self.m[1]

        targetPoints[2][0] = self.n[0]
        targetPoints[2][1] = self.n[1]

        targetPoints[3][0] = self.b[0]
        targetPoints[3][1] = self.b[1]

        return targetPoints

    def constructNewTagetImageRight(self):
        #RIGHT SIDE OF IMAGE
        #Change e
        self.e[0] -= self.h1
        self.e[1] += self.v

        #Change m
        self.m[0] += self.h2
        self.m[1] -= self.v


    def setupTransformation(self, targetPoints, effect=None):
        #Takes in targetPoints
            # 4x2 float64 array
            #representing four (x', y') points
        #optional instance of Effect class

        #Must ALWAYS be invoked before you apply the homography.
        #Two ways:
            #IF a Homography instance was passed to this Transformation instance when instantiated
                #use targetPoints to identify range of iteration in target image.
            #IF a Homography instance was NOT passed to this Transformation instance when instantiated
                #use targetPoints, as well as effect, to instantiate a new Homography instance.
                #compute homography matrix.
                #Then targetPoints can be used to identify the range of iteration.

        if (self.homography):
            self.computeRangeOfIteration(targetPoints)
        elif(self.homography == None):
            self.sourcePoints = self.computeSourcePointsFromSourceImage(self.sourceImage)
            if(effect != None):
                self.homography= Homography(sourcePoints=self.sourcePoints, targetPoints=targetPoints, effect=effect)
            elif(effect == None):
                self.homography = Homography(sourcePoints=self.sourcePoints, targetPoints=targetPoints)


"""
"""
#==== UTILITY FUNCTIONS =====
#These functions are here for main testing
#These probably won't be merged into the homography class.
"""

def testInitSourcePoints(cp_arr):
    #Inits a sample of sourcePoints using given array of four sample correspondence points.
    sourcePoints = np.array([[0 for x in range(2)] for y in range(4)])

    sourcePoints[0][0] = cp_arr[0][0]
    sourcePoints[0][1] = cp_arr[0][1]
    sourcePoints[1][0] = cp_arr[1][0]
    sourcePoints[1][1] = cp_arr[1][1]
    sourcePoints[2][0] = cp_arr[2][0]
    sourcePoints[2][1] = cp_arr[2][1]
    sourcePoints[3][0] = cp_arr[3][0]
    sourcePoints[3][1] = cp_arr[3][1]

    printSourcePoints(sourcePoints)

    return sourcePoints

def testInitTargetPoints(cp_arr):
    #Inits a sample of sourcePoints using given array of four sample correspondence points.
    targetPoints = np.array([[0 for x in range(2)] for y in range(4)])

    targetPoints[0][0] = cp_arr[0][0]
    targetPoints[0][1] = cp_arr[0][1]
    targetPoints[1][0] = cp_arr[1][0]
    targetPoints[1][1] = cp_arr[1][1]
    targetPoints[2][0] = cp_arr[2][0]
    targetPoints[2][1] = cp_arr[2][1]
    targetPoints[3][0] = cp_arr[3][0]
    targetPoints[3][1] = cp_arr[3][1]

    printTargetPoints(targetPoints)

    return targetPoints

def printSourcePoints(sourcePoints):

    print("sourcePoints is a " + format(str(len(sourcePoints))) + "x" + format(str(len(sourcePoints[1]))) + ":")
    print(sourcePoints)

def printTargetPoints(targetPoints):

    print("targetPoints is a " + format(str(len(targetPoints))) + "x" + format(str(len(targetPoints[1]))) + ":")
    print(targetPoints)

def printA_n(A_n):

    print("A_n is a " + format(str(len(A_n))) + "x" + format(str(len(A_n[1]))) + ":")
    print(A_n)

def printB_n(B_n):

    print("B_n is a " + format(str(len(B_n))) + "x" + format(str(len(B_n[1]))) + ":")
    print(B_n)

def print_A(A):

    print("A is " + str(A.shape[0]) + "x" + str(A.shape[1]))
    print(A)

def print_B(B):

    print("B is " + str(B.shape[0]) + "x" + str(B.shape[1]))
    print(B)

#==== MAIN ====
"""
if __name__ == "__main__":
    """
    kwargs = dict()
    sampleSourcePointsArray = np.array([[4,3], [1,5], [9,7], [6,1]], np.float64)
    sampleTargetPointsArray = np.array([[9,6], [4,8], [0,0], [9,1]], np.float64)
    kwargs["sourcePoints"] = sampleSourcePointsArray
    kwargs["targetPoints"] = sampleTargetPointsArray
    #kwargs["effect"] = Effect.rotate90
    homography = Homography(**kwargs)

    #print(type(sampleTargetPointsArray))
    #n_degree = 0
    """
    """
    print("Isolated Test Cases (not part of homography class yet")
    print("Testing init of source and target arrays with sample arrays")
    print("===================")
    sourcePoints = testInitSourcePoints(sampleSourcePointsArray)
    print("===================")
    targetPoints = testInitTargetPoints(sampleTargetPointsArray)
    print("===================")


    print("CREATING A_n")
    print("Testing init of homography matrix using source and target arrays")
    print("Calling initA_nMatrix with source and target points [[n=" + format(str(n_degree)) + "]...")
    A_1 = initA_nMatrix(sourcePoints, targetPoints, n_degree)
    B_1 = initB_nMatrix(sourcePoints, targetPoints, n_degree)
    n_degree += 1
    print("===================")
    print("Testing init of homography matrix using source and target arrays")
    print("Calling initA_nMatrix with source and target points [n=" + format(str(n_degree)) + "]...")
    A_2 = initA_nMatrix(sourcePoints, targetPoints, n_degree)
    B_2 = initB_nMatrix(sourcePoints, targetPoints, n_degree)
    n_degree += 1
    print("===================")
    print("Testing init of homography matrix using source and target arrays")
    print("Calling initA_nMatrix with source and target points [n=" + format(str(n_degree)) + "]...")
    A_3 = initA_nMatrix(sourcePoints, targetPoints, n_degree)
    B_3 = initB_nMatrix(sourcePoints, targetPoints, n_degree)
    n_degree += 1
    print("===================")
    print("Testing init of homography matrix using source and target arrays")
    print("Calling initA_nMatrix with source and target points [n=" + format(str(n_degree)) + "]...")
    A_4 = initA_nMatrix(sourcePoints, targetPoints, n_degree)
    B_4 = initB_nMatrix(sourcePoints, targetPoints, n_degree)
    print("===================")
    print("Creating A")
    print("Using the four A_n matrices, compile into A")
    A = compile_A_matrix(A_1, A_2, A_3, A_4)
    print("Creating B")
    print("Using the four B_n matrices,compile into B")
    b = compile_B_matrix(B_1, B_2, B_3, B_4)
    print("===================")
    print("Calculate column vector h")
    h = np.linalg.solve(A, b)
    print(h)
    """