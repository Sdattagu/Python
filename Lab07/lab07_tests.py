import os
import sys
import uuid
import unittest
from oopTasks import *


def loadTextFiles(path1, path2):

    with open(path1, 'r') as firstFile:
        first = firstFile.read()

    with open(path2, 'r') as secondFile:
        second = secondFile.read()

    return first, second


class Lab07TestSuite(unittest.TestCase):

    def test_course_initializer(self):

        c = Course("ECE638", 63, 94, 81)
        self.assertIsNotNone(c)

    def test_course_attributesExist(self):

        c = Course("ECE337", 77, 67, 80)

        with self.subTest(key="ID"):
            self.assertEqual("ECE337", c.courseID)

        with self.subTest(key="First"):
            self.assertEqual(77, c.fst)

        with self.subTest(key="Second"):
            self.assertEqual(67, c.snd)

        with self.subTest(key="Final"):
            self.assertEqual(80, c.final)

        with self.subTest(key="Total"):
            self.assertEqual(76, c.total)

        with self.subTest(key="Total"):
            self.assertEqual("C", c.letter)

    def test_course_letterGrade(self):

        c = Course("ECE638", 80, 95, 99)

        expectedValue = "A"
        actualValue = c.getLetterGrade()

        self.assertEqual(expectedValue, actualValue)

    def test_course_representation(self):

        c = Course("ECE364", 80, 95, 99)

        expectedValue = "ECE364: (80.00, 95.00, 99.00) = (93.25, A)"
        actualValue = str(c)

        self.assertEqual(expectedValue, actualValue)

    def test_student_initializer(self):

        student = Student("Elizabeth Rogers")
        self.assertIsNotNone(student)

    def test_student_attributesExist(self):

        student = Student("Sarah Carter")

        with self.subTest(key="Name"):
            self.assertEqual("Sarah Carter", student.name)

        with self.subTest(key="Courses"):
            self.assertDictEqual({}, student.courses)

    def test_student_representation(self):

        c1 = Course("ECE264", 99, 72, 74)
        c2 = Course("ECE638", 89, 86, 79)
        c3 = Course("ECE464", 96, 90, 67)
        c4 = Course("ECE337", 64, 86, 79)

        student = Student("Margaret Cook")

        for course in [c1, c2, c3, c4]:
            student.addCourse(course)

        expectedValue = "Margaret Cook: (ECE264: C), (ECE337: C), (ECE464: B), (ECE638: B)"
        actualValue = str(student)

        self.assertEqual(expectedValue, actualValue)

    def test_student_addCourse(self):

        c1 = Course("ECE264", 99, 72, 74)
        c2 = Course("ECE638", 89, 86, 79)
        c3 = Course("ECE638", 96, 90, 67)

        student = Student("Margaret Cook")

        with self.subTest(key="Add"):

            student.addCourse(c1)

            self.assertEqual(c1, student.courses["ECE264"])

        with self.subTest(key="Update"):

            student.addCourse(c2)
            student.addCourse(c3)

            self.assertNotEqual(c2, student.courses["ECE638"])

    def test_student_generateTranscript(self):

        c1 = Course("ECE264", 99, 72, 74)
        c2 = Course("ECE638", 89, 86, 79)
        c3 = Course("ECE464", 96, 90, 67)
        c4 = Course("ECE337", 64, 86, 79)

        student = Student("Margaret Cook")

        for course in [c1, c2, c3, c4]:
            student.addCourse(course)

        expectedValue = "Margaret Cook\n"
        expectedValue += "ECE264: (99.00, 72.00, 74.00) = (79.75, C)\n"
        expectedValue += "ECE337: (64.00, 86.00, 79.00) = (77.00, C)\n"
        expectedValue += "ECE464: (96.00, 90.00, 67.00) = (80.00, B)\n"
        expectedValue += "ECE638: (89.00, 86.00, 79.00) = (83.25, B)"

        actualValue = student.generateTranscript()

        self.assertEqual(expectedValue, actualValue)

    def test_school_initializer(self):

        school = School("Purdue University")
        self.assertIsNotNone(school)

    def test_school_attributesExist(self):

        school = School("Purdue University")

        with self.subTest(key="Name"):
            self.assertEqual("Purdue University", school.name)

        with self.subTest(key="Students"):
            self.assertDictEqual({}, school.students)

    def test_school_representation(self):

        school = School("Purdue University")
        school.loadStudentsInfo("school_data_source.txt")

        expectedValue = ['Purdue University: 20 Students', 'Aaron Miller', 'Anne Harris', 'Beverly Hall',
                         'Brenda Phillips', 'Deborah Sanchez', 'Donna Murphy', 'Doris Jackson', 'Elizabeth Rogers',
                         'Evelyn Bryant', 'George Richardson', 'Howard Wilson', 'Johnny Evans', 'Joyce Kelly',
                         'Kimberly Gonzalez', 'Margaret Cook', 'Martin Watson', 'Mary Williams', 'Nancy Bennett',
                         'Sandra Ward', 'Sarah Carter']
        expectedValue = "\n".join(expectedValue)

        actualValue = str(school)

        self.assertEqual(expectedValue, actualValue)

    def test_school_loadStudentsInfo(self):

        school = School("Purdue University")
        school.loadStudentsInfo("school_data_source.txt")

        with self.subTest(key="StudentCount"):
            self.assertEqual(20, len(school.students))

        with self.subTest(key="CourseCount"):
            studentName = "Donna Murphy"
            studentCourses = school.students[studentName].courses
            self.assertEqual(3, len(studentCourses))

        with self.subTest(key="LetterGrade"):
            studentName = "Evelyn Bryant"
            studentCourses = school.students[studentName].courses
            letterGrade = studentCourses["ECE437"].getLetterGrade()
            self.assertEqual("B", letterGrade)

    def test_school_saveSchoolInfo(self):

        school = School("Purdue University")
        school.loadStudentsInfo("school_data_source.txt")

        expectedFileName = "school_data_target.txt"
        actualFileName = str(uuid.uuid4()) + '.txt'

        school.saveSchoolInfo(actualFileName)
        actualValue, expectedValue = loadTextFiles(actualFileName, expectedFileName)
        os.remove(actualFileName)

        self.assertEqual(actualValue, expectedValue)

if __name__ == '__main__':
    unittest.main()
