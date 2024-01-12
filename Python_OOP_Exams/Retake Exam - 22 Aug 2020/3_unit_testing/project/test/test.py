from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student = StudentReportCard("name", 4)

    def test_initialization(self):
        self.assertEqual("name", self.student.student_name)
        self.assertEqual(4, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_attributes_types(self):
        self.assertIsInstance(self.student.student_name, str)
        self.assertIsInstance(self.student.school_year, int)
        self.assertIsInstance(self.student.grades_by_subject, dict)

    def test_setter_name_empty_string_raises(self):
        self.assertEqual("name", self.student.student_name)

        with self.assertRaises(ValueError) as ve:
            self.student.student_name = ""

        expected = "Student Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_setter_school_year_less_than_1_and_more_than_12_raises(self):
        self.assertEqual(4, self.student.school_year)

        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 0

        expected = "School Year must be between 1 and 12!"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 13

        expected2 = "School Year must be between 1 and 12!"
        self.assertEqual(expected2, str(ve.exception))

    def test_setter_school_year_boundary_values(self):
        self.assertEqual(4, self.student.school_year)

        self.student.school_year = 1
        self.assertEqual(1, self.student.school_year)

        self.student.school_year = 12
        self.assertEqual(12, self.student.school_year)

    def test_add_grade_non_existing_subject(self):
        self.assertEqual({}, self.student.grades_by_subject)
        self.student.add_grade("math", 6.00)
        self.assertEqual({"math": [6.00]}, self.student.grades_by_subject)

        self.student.add_grade("math", 5)
        self.assertEqual({"math": [6.00, 5]}, self.student.grades_by_subject)

        self.student.add_grade("biology", 6)
        self.assertEqual({"math": [6.00, 5], "biology": [6]}, self.student.grades_by_subject)

    def test_average_grade_by_subject_empty_subjects_dict(self):
        self.assertEqual({}, self.student.grades_by_subject)

        result = self.student.average_grade_by_subject()
        expected = ""

        self.assertEqual(expected, result)

    def test_average_grade_by_subject_existing_subjects(self):
        self.assertEqual({}, self.student.grades_by_subject)
        self.student.add_grade("math", 6)
        self.student.add_grade("math", 6)
        self.student.add_grade("biology", 6)

        result = self.student.average_grade_by_subject()
        expected = ("""math: 6.00"
biology: 6.00""")

        self.assertEqual({"math": [6, 6], "biology": [6]}, self.student.grades_by_subject)
        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects(self):
        self.assertEqual({}, self.student.grades_by_subject)
        self.student.add_grade("math", 6)
        self.student.add_grade("math", 6)
        self.student.add_grade("biology", 6)

        result = self.student.average_grade_for_all_subjects()
        expected = "Average Grade: 6.00"

        self.assertEqual({"math": [6, 6], "biology": [6]}, self.student.grades_by_subject)
        self.assertEqual(expected, result)

    def test_repr_method(self):
        self.assertEqual({}, self.student.grades_by_subject)
        self.student.add_grade("math", 6)
        self.student.add_grade("math", 6)
        self.student.add_grade("biology", 6)

        expected = """Name: name
Year: 4
----------
math: 6.00
biology: 6.00
----------
Average Grade: 6.00"""

        self.assertEqual({"math": [6, 6], "biology": [6]}, self.student.grades_by_subject)
        self.assertEqual(expected, repr(self.student))


if __name__ == '__main__':
    main()
