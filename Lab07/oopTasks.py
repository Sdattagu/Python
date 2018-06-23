import math

class Course:
#Member variables:
    #courseID - string that represents the course name
    #fst - float representing the grade for the first midterm
    #snd - float representing the grade for the second midterm
    #final - float representing the grade for the final grade
    #total - float representing the total grade obtained for that course
        #total = 0.25 * fst + 0.25 * snd + 0.59 * final
    #letter - One letter string representing the letter grade for this course based on scale.

    def __init__(self, courseID, fst, snd, final):
        #Init a course instance with the given params and sets member vars
        #Calculates and sets "total" and "letter" variables
        self.courseID = courseID
        self.fst = fst
        self.snd = snd
        self.final = final
        self.total = (0.25 * self.fst + 0.25 * self.snd + 0.50 * self.final)
        self.letter = self.getLetterGrade()


    def __str__(self):
        #result += format(item1, '.2f')
        result = ""
        result += str(self.courseID)
        result += ": ("
        result += format(self.fst, '.2f')
        result += ", "
        result += format(self.snd, '.2f')
        result += ", "
        result += format(self.final, '.2f')
        result += ") = ("
        result += format(self.total, '.2f')
        result += ", "
        result += format(self.letter)
        result += ")"

        return result

    def getLetterGrade(self):
        if(self.total >= 90):
            return "A"
        elif(self.total >= 80 and self.total < 90):
            return "B"
        elif(self.total >= 70 and self.total < 80):
            return "C"
        elif(self.total >= 60 and self.total < 90):
            return "D"
        elif(self.total < 60):
            return "F"

class Student:
#Member variables
    #name - A string that represents the student's name, e.g. 'Purdue University'
    #courses - A dictionary that maps a course ID (which is a string) to an instance of the Course class

    def __init__(self, name):
        #Takes a string as an argument and sets the name member variable to this value.
        #Init courses to be an empty dictionary
        if(type(name) == str):
            self.name = name

        self.courses = dict()


    def __str__(self):
        #Returns a string in the following format:
        #StudentName: (courseID1: letterGrade), (courseID2: letterGrade)
        #The course IDs must be listed in a "sorted" order.
        result = ""
        result += str(self.name) + ": "
        for item1 in sorted(self.courses):
            result += "("
            result += item1 + ": "
            result += self.courses[item1].letter
            result += "), "

        #result = result.rstrip(", ")
        r = result[:len(result) - 2]

        return r

    def addCourse(self, course):
        #Adds/updates the courses dictionary with an entry
            #Update the entry if the key courseID exists, or create a new one if it does not
            #Input parameter is an instance of the Course class
                #Course class has fst, snd, letter, etc...


        self.courses[course.courseID] = course



    def generateTranscript(self):
        #Return a string with information about the student's grade.
        #Returned multi-line string should be in the format:
            #StudentName
            #CourseID1: (fst, snd, final) = (total, letter)
            #...
        result = ""
        result += self.name
        result += "\n"
        for item1 in sorted(self.courses):
            result += str(self.courses[item1])
            result += "\n"

        return result


class School:
#Member variables
    #name - A string that represents the school's name, e.g. 'Purdue University'
    #students - A dictionary that maps a student's name to an instance of the Student class

    def __init__(self, name):
        #Take a string as an argument and sets the "name" member variable to this value.
        #Initialize "students" to be an empty dictionary
        if(type(name) == str):
            self.name = name

        self.students = dict()


    def __str__(self):
        #Returns a string containing the school name, and the number of students in the internal dictionary
            #Along with their names, in following format:
                #SchoolName: ## Students
                #StudentName1
                #StudentName2
                #...
        result = ""
        result += self.name
        result += ": " + str(len(self.students))
        result += "\n"
        for item1 in sorted(self.students):
            result += str(item1)
            result += "\n"

        return result

    def loadStudentsInfo(self, filename):
        #Populates the "students" dictionary by reading the specified input file. The format of the file is as follows:
            #StudentName1
            #---------------
            #CourseID1: fst, snd, final
            #...
        #The file contains an arbitrary number of students
            #Each student has an arbitrary number of courses listed
        #For each student, create a new instance of Student class
            #Populate it with the info
            #Add an entry into the School.students dictionary
                #This, in turn, requires you to create an instance of the Course class for every course listed, to populate the Students.courses dictionary,
                #before you assign it to School.students
        with open (filename) as myFile:
            lines = myFile.read()

        entries = lines.split("\n\n")
        for item1 in entries:
            entry_nl = item1.split("\n")
            #print(entry_nl)
            student = Student(entry_nl[0])
            for courseInfo in entry_nl[2:]:
                courseInfo.strip()
                getCourse = courseInfo.split(":")[0].strip()
                #print(getCourse)
                getGrades = (courseInfo.split(", "))
                getLastGrade = getGrades[0].split(" ")[-1]
                #print(getGrades)
                #print(getLastGrade)
                course = Course(getCourse, float(getLastGrade), float(getGrades[1]), float(getGrades[2]))
                student.addCourse(course)
            self.students[student.name] = student

        #print(entries)

        pass

    def saveSchoolInfo(self, filename):
        #builds and saves a file containing the transcripts of all students, sorted by the student name. Each transcript should be separated by two new lines.
        #For an example of expected format, refer to "school_data_target.txt"
        result = ""
        for student in sorted(self.students):
            current_student = self.students[student]
            result += current_student.generateTranscript()
            result += "\n\n"

        with open(filename, "w") as myFile:
            myFile.write(result[:-2])

        #return result


if __name__ == "__main__":
    course_364 = Course("ECE364", 80, 80, 90)
    course_208 = Course("ECE208", 80, 80, 90)
    student = Student("Shounak")
    student.addCourse(course_364)
    student.addCourse(course_208)
    #print(student.generateTranscript())
    #print(str(student))
    school = School("Purdue University")

    print(school.loadStudentsInfo("school_data_source.txt"))
    #print(school.saveSchoolInfo("school_data_source.txt"))
    school.saveSchoolInfo("output.txt")