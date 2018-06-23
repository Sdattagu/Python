#Shounak Dattagupta
#10/16/2016

#Import math library
import math
#Import system library
import sys
import operator

#Class: PointND: represents a point in an n-dimensional Cartesian space.
class PointND:
    def __init__(self, *args):
        #Constructs a new PointND object with N float values.
        #If any of the values is not a float, raise the following error
        list_floats = []
        for item1 in args:
            if(type(item1) == float):
                list_floats.append(item1)
            else:
                raise ValueError("Cannot instantiate an object with non-float values.")

        self.t = args
        self.n = len(args)
        tuple(list_floats)


    def __str__(self):
        #Returns a string representation of the PointND in the format (0.00, ...)
            #Format each coordinate with two decimal digits
            #DO NOT round values, just display with two decimals using string format specifiers.
        result = "("
        for item1 in self.t:
            result += format(item1, '.2f')
            result += ", "
        #Remove whitespace character at end of last entry, based on ","
        result = result.rstrip(", ")
        result += ")"
        return result

    def __hash__(self):
        #Returns hash(self.t). This function is needed for the next part.
            #A hash value is an integer that is unique to the object.
        return hash(self.t)

    def distanceFrom(self, other):
        #Computes, and returns, the Euclidean distance between the point and another point.
        #Raise value error if "other" had a different cardinality.
            #raise ValueError("Cannot calculate distance between points of different cardinality.")

        accum = 0

        if not (self.n == other.n):
            raise ValueError("Cannot calculate distance between points of different cardinality.")

        else:
            for item1 in range(self.n):
                difference_squared = (self.t[item1] - other.t[item1])**2
                accum += difference_squared
            result = math.sqrt(accum)

        return result

    def nearestPoint(self, points):
        #Returns the point that is closest to this point from the list of points.
        #IF points is empty, raise an error:
            #raise ValueError("Input cannot be empty.")
        #You can use distanceFrom(point) to calculate distance
        #Assume first point as default return
        #Set initial distance to max int

        initDistance = sys.maxsize

        if (len(points) == 0):
            raise ValueError("Input cannot be empty.")
        else:
            result = points[0]
            for item1 in points:
                if self.distanceFrom(item1) < initDistance:
                    initDistance = self.distanceFrom(item1)
                    result = item1

        return result

    def clone(self):
        #Returns a new unique copy of this point.
        pointTup = self.t
        card = self.n
        result = PointND(*self.t)
        return result

    def __add__(self, other):
        pointCalc_list = []
        if (type(other) == PointND):
            if not (self.n == other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
        if not (type(other) == float):
            #Case for adding respective coordinates of each object
            for item1 in range(self.n):
                pointCalc_list.append(self.t[item1] + other.t[item1])
            resultPoint = tuple(pointCalc_list)
        if (type(other) == float):
            for item1 in range(self.n):
                print(self.t[item1])
                print(other)
                pointCalc_list.append(self.t[item1] + other)
            resultPoint = tuple(pointCalc_list)

        return PointND(*resultPoint)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        pointCalc_list = []
        if(type(other) == PointND):
            if not (self.n == other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
        if not (type(other) == float):
            #Case for subtracting respective coordinates of each object
            for item1 in range(self.n):
                pointCalc_list.append(self.t[item1] - other.t[item1])
            resultPoint = tuple(pointCalc_list)
        if (type(other) == float):
            for item1 in range(self.n):
                pointCalc_list.append(self.t[item1] - other)
            resultPoint = tuple(pointCalc_list)

        return PointND(*resultPoint)

    def __mul__(self, other):
        pointCalc_list = []
        if (type(other) == float):
            for item1 in self.t:
                pointCalc_list.append(item1 * other)
            resultPoint = tuple(pointCalc_list)

        return PointND(*resultPoint)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __truediv__(self, other):
        pointCalc_list = []
        if(type(other) == float):
            for item1 in self.t:
                pointCalc_list.append(item1 / other)
            #resultPoint = tuple(pointCalc_list)

        return PointND(*(tuple(pointCalc_list)))

    #NEGATION:
    def __neg__(self):
        pointCalc_list = []
        for item1 in self.t:
            pointCalc_list.append(-item1)
        resultPoint = tuple(pointCalc_list)

        return PointND(*resultPoint)

    #INDEXING
    def __getitem__(self, item):
        return self.t[item]

    #COMPARISON
    #For all: raise ValueError("Cannot operate on points with different cardinalities.") when necessary.
    def __eq__(self, o):
        #Return true IFF each coordinate from first point is equal to its counterpart in second.
        check_list = []
        if not (self.n == o.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        else:
            for item1 in range(self.n):
                check_list.append(self.t[item1] == o.t[item1])

        return all(check_list)

    def __ne__(self, o):
        #Computes and returns inverse of the == operator.
            #return not self.__eq__(o)
        check_list = []
        if not (self.n == o.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        else:
            for item1 in range(self.n):
                check_list.append(self.t[item1] != o.t[item1])

        return all(check_list)

    def __gt__(self, o):
        #Return True IFF distance of first point from origin is greater than distance of second from origin.
        result = False
        if not (self.n == o.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        else:
            selDistance = self.distanceFrom(PointND(*[0.0]*self.n))
            othDistance = o.distanceFrom(PointND(*[0.0]*self.n))
            if(selDistance > othDistance):
                result = True

        return result

    def __ge__(self, o):
        #Same as gt, but also check for equality.
            #return self.__gt__(o) or self.__eq__(o)
        if not (self.n == o.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        else:
            selDistance = self.distanceFrom(PointND(*[0.0]*self.n))
            othDistance = o.distanceFrom(PointND(*[0.0]*self.n))
            if(selDistance >= othDistance):
                result = True

        return result

    def __lt__(self, o):
        #Returns True IFF distance of first point from origin is less than distance of second.
        result = False
        if not (self.n == o.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        else:
            selDistance = self.distanceFrom(PointND(*[0.0]*self.n))
            othDistance = o.distanceFrom(PointND(*[0.0]*self.n))
            if(selDistance < othDistance):
                result = True

        return result

    def __le__(self, o):
        #Same as gt, but also check for equality.
            #Return self.__lt__(o) or self.__eq__(o)
        result = False
        if not (self.n == o.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        else:
            selDistance = self.distanceFrom(PointND(*([0.0]*self.n)))
            othDistance = o.distanceFrom(PointND(*([0.0]*self.n)))
            if(selDistance <= othDistance):
                result = True

        return result

class Point3D(PointND):
    #Class that represents a point in a 3-dimensional Cartesian space.
        #Only defining a new constructor
            #All member functions and variables in base class are accessible here.

    def __init__(self, x=0.0, y=0.0, z=0.0):
        PointND.__init__(self, x, y, z)
        self.x = x
        self.y = y
        self.z = z

class PointGroup:
    #Class that represents a "unique" group of PointND entries, where each point is accessed via its hash.
        #This class is similar to a standard dictionary, but it constrains the points that can be added
        #to be of similar cardinality and adds some additional member functions.

    def __init__(self, **kwargs):
        #Construct new PointGroup object with following options:
            #If no args passed, init self._pointMap to an empty dictionary, and set self.n = 0.
            if not kwargs:
                #print("in init not kwargs")
                self._pointMap = dict()
                self.n = 0
            #If list is empty
            elif not kwargs["pointList"]:
                raise ValueError("'pointList' input parameter cannot be empty.")
            #If any other keyword argument is passed
            elif "pointList" not in kwargs:
                raise KeyError("'pointList' input parameter not found.")
            #If key "pointList" is passed (CORRECT CASE)
            else:
                self._pointMap = dict()
                #add all elements from list of PointND passed in the value
                for point in kwargs["pointList"]:
                    print(point)
                    self.addPoint(point)
                #Set self.n to cardinality of the first PointND
                self.n = kwargs["pointList"][0].n
                #Confirm that each point added has the same cardinality. Raise value error if not.
                for point in kwargs["pointList"]:
                    if(point.n != self.n):
                        raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))



    def addPoint(self, point):
        #Adds a PointND to the internal dictionary self._pointMap.
        #Confirm that cardinality of new point matches cardinality of instance
            #Raise error given above, otherwise.

        if (len(self._pointMap) != 0):
            #print(list(self._pointMap.values()))
            if point.n != list(self._pointMap.values())[0].n:
                raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, list(self._pointMap.values())[0].n))
        self._pointMap[hash(point)] = point

    def count(self):
        #Return number of points contained in the internal dictionary
        return len(self._pointMap)

    def computeBoundingHyperCube(self):
        #Return a (minPoint, maxPoint) tuple of two PointND, representing the coordinates of the bounding hyper-cube
        # that surrounds all of the points in the internal dictionary.
        result = []
        minPoint = [999999.9999] * self.n
        maxPoint = [-999999.9999] * self.n
        a = PointND(*minPoint)
        b = PointND(*maxPoint)

        for point in iter(self):
            cardCount = 0
            #print("Min and Max points for this iteration are:")
            #print(minPoint)
            #print(maxPoint)
            #[print("Point in consideration is:")]
            #print(str(point))
            #print("Starting comparisons...")
            for cardCount in range(self.n):
                if point[cardCount] > maxPoint[cardCount]:
                    maxPoint[cardCount] = point[cardCount]
                if point[cardCount] < minPoint[cardCount]:
                    minPoint[cardCount] = point[cardCount]
            #print("UPDATED Min and Max points for this iteration are:")
            #print(minPoint)
            #print(maxPoint)

        result.append(PointND(*minPoint))
        result.append(PointND(*maxPoint))
        return(tuple(result))

    def computeNearestNeighbors(self, otherPointGroup):
        #Takes in another PointGroup and returns a sorted list of tuples
            #For each tuple
                # the first element is a point from the current PointGroup instance
                # the second element is its corresponding nearest neighbor from otherPointGroup.

        #otherPointGroup has a set of points accessible by otherPointGroup.points
            #Convert to list of points so we can call nearestPoint() of PointND class, compare to current point.
        result_T = []
        result = []
        otherPointGroupList = list(otherPointGroup._pointMap.values())
        #print(type(list(otherPointGroup._pointMap.values())))
        #for point in otherPointGroupList:
            #print(str(point))

        for point in iter(self):
            #print(point)
            result_T.append(point)
            result_T.append(point.nearestPoint(otherPointGroupList))
            result.append(tuple(result_T))
            result_T = []

        #print("The results are:")
        #for item1 in result:
        #    print(str(item1[0]))
        #    print("is closest to:")
        #    print(str(item1[1]))
        return(sorted(result))

    def __iter__(self):
        #Returns an iterator over the points present in the dictionary.
        return iter(self._pointMap.values())

    def __add__(self, o):
        #PointGroup + PointND
            #Adds a new PointND to the group
            #Returns reference to the current PointGroup instance (i.e. self)
        #Confirm that cardinalities match, raise error given above otherwise.
        if(self.n != o.n):
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(o, self.n))
        else:
            self.addPoint(o)

        return self

    def __sub__(self, o):
        #PointGroup - PointND
            #Removes the given PointND from the dictionary
            #Returns reference to the current PointGroup instance (i.e. self)
        #If point does not exist in the instance, jut return a reference with no errors.
        if(self.n != o.n):
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(o, self.n))
        else:
            del self._pointMap[hash(o)]

        return self

    def __contains__(self, o):
        #PointND in PointGroup
        #Returns True is given point is in the dictionary, False otherwise.
        retVal = False
        if o in iter(self):
            retVal = True

        return retVal

if __name__ == "__main__":
    #Point3D object coordinates
    x = 0.4
    y = 0.5
    z = 0.6
    #Initialize two Point3D objects
    print("-------------------")
    print("initializing Point3D object A")
    A = PointND(0.3, 0.2, 0.8)
    print("initializing Point3D object B w/ x={}, y={}, z={}".format(x, y, z))
    B = PointND(1.4, 0.5, 0.6)
    C = Point3D(0.3, 0.5)
    D = Point3D(1.0, 4.0, 7.0)
    E = 1.0
    print("Creating list of point objects...")
    listOfPoints = [Point3D(0.3, 0.4, 0.5), Point3D(0.6, 0.7, 0.8), Point3D(0.1, 0.2, 0.3)]

#TEST SUIT FOR PointGroup CLASS
    """print("-------------------")
    print("Testing no arg case.")
    print("Creating PointGroup instance...")
    kwargs = {}
    point_group = PointGroup(**kwargs)
    print("Done.")
    if(point_group.n == 0):
        print("No arg case success")
    print("-------------------")
    print("Testing if key 'pointList' is passed.")
    print("Creating PointGroup instance...")"""
    #kwargs = {"pointList" : [Point3D(1.0, 4.0, 7.0), Point3D(6.0, 3.0, 4.0), Point3D(9.0, 0.0, 5.0), PointND(1.0, 2.0, 4.0, 5.0)]}
    point_group = PointGroup(pointList = [Point3D(1.0, 4.0, 7.0), Point3D(6.0, 3.0, 4.0), Point3D(9.0, 0.0, 5.0)])
    """kwargs = {"pointList" : [Point3D(1.0, 1.0, 1.0), Point3D(7.0, 3.0, 4.0), Point3D(9.0, 1.0, 5.0)]}
    point_group_two = PointGroup(**kwargs)
    print("Done.")
    print("PointGroup has following points:")
    for point in point_group:
        print(str(point))
    #print("Testing if pointList is not input parameter")"""
    #kwargs = {"blahList" : [Point3D(0.1, 0.2, 0.3), Point3D(0.2, 0.3, 0.4), Point3D(0.3, 0.4, 0.5), Point3D(0.5, 0.6, 0.7), Point3D(0.7, 0.8, 0.9)]}
    #print("blahList created.")
    #point_group = PointGroup(**kwargs)
    #print("Done.")
    #print("-------------------")
    print("Testing addPoint")
    print("Adding custom point to point group...")
    point_group.addPoint(Point3D(0.4, 0.2, 0.01))
    print("Point added.")
    print("PointGroup has following points:")
    for point in point_group:
        print(str(point))
    """print("-------------------")
    print("Testing count")
    print(point_group.count())
    print("-------------------")
    print("Testing computeBoundingHyperCube")
    b = point_group.computeBoundingHyperCube()
    print("Bounding hyper cube computed:")
    print(b[0])
    print(b[1])
    print("-------------------")
    print("Testing computeNearestNeighbors")
    a = point_group_two.computeNearestNeighbors(point_group)
    print("-------------------")
    print("Testing add to pointGroup")
    print(point_group + Point3D())
    for point in point_group:
        print(str(point))
    print("-------------------")
    print("Testing sub from pointGroup")
    print(point_group - Point3D())
    for point in point_group:
        print(str(point))
    print("-------------------")
    print("Testing exist contains from pointGroup")
    print(D in point_group)
    print("Testing non-exist contains from pointGroup")
    print(C in point_group)"""

#TEST SUITE FOR Point3D/ND CLASS
    #Return string rep of A and B
    #print("-------------------")
    #print(str(A))
    #print(str(B))
    #print(str(C))
    #Test hash functions for both A and B objects
    #print("-------------------")
    #print("Print hash A:")
    #print(hash(A))
    #print("Print hash B:")
    #print(hash(B))
    #Test distance from A to B
    #print("-------------------")
    #print("Distance from A to B:")
    #print(A.distanceFrom(B))
    #Test nearest point
    #print("-------------------")
    #print("Nearest point to A is:")
    #print(A.nearestPoint(listOfPoints))
    #print("Nearest point to B is:")
    #print(B.nearestPoint(listOfPoints))
    #Test Clone
    #print("-------------------")
    #print("Testing Clone of A")
    #print(A.clone())
    #Testing overloaded add
    #print("-------------------")
    #print("Testing: A + B")
    """print(A+B)
    print("-------------------")
    print("Testing: A + E")
    print(A+E)
    print("-------------------")
    print("Testing: E + A")
    print(E+A)
    print("-------------------")
    print("Testing: A <= B")
    print(A<=B)"""
    print("-------------------")
    print("Testing: A <= B")
    print(A / E)
    #Testing overloaded sub
    #print("-------------------")
    #print("Testing: A - B")
    #print(A-B)
    #Testing overloaded mul
    #print("-------------------")
    #print("Testing: A|B * 0.5")
    #print(A*0.5)
    #print(B*0.5)
    #Testing overloaded div
    #print("-------------------")
    #print("Testing A|B / 0.5")
    #print(A/0.5)
    #print(B/0.5)
    #Testing negation
    #print("-------------------")
    #print("Testing negation")
    #print(-A)
    #print(-B)
    #Testing indexing
    #print("-------------------")
    #print("Testing indexing")
    #print(A[0])
    #print(B[1])
    #Testing equality with different cardinalities
    #print("Testing equality w/ same cardinality")
    #print(A == C)