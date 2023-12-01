from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Maria", {})
        self.student2 = Student("Maria", {"course1": ["n1", "n2"]})

    def test_init(self):
        self.assertEqual(self.student.name, "Maria")
        self.assertEqual(self.student.courses, {})

        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

    def test_enroll_existing_course(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})
        result = self.student2.enroll("course1", ["n3", "n4"], add_course_notes="")

        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2", "n3", "n4"]})
        self.assertEqual(result, "Course already added. Notes have been updated.")

        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2", "n3", "n4"]})
        result = self.student2.enroll("course1", ["n5", "n6"], add_course_notes="L")

        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2", "n3", "n4", "n5", "n6"]})
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_not_existing_course(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        result = self.student2.enroll("course2", ["n1", "n2"])

        self.assertTrue("course2" in self.student2.courses)
        self.assertEqual(self.student2.courses["course2"], ["n1", "n2"])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_not_existing_course_with_y(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        result = self.student2.enroll("c2", ["n1", "n2"], add_course_notes="Y")

        self.assertTrue("c2" in self.student2.courses)
        self.assertEqual(self.student2.courses["c2"], ["n1", "n2"])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_not_existing_course_with_empty_string(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        result = self.student2.enroll("c2", ["n1", "n2"], add_course_notes="")

        self.assertTrue("c2" in self.student2.courses)
        self.assertEqual(self.student2.courses["c2"], ["n1", "n2"])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_not_existing_course_no_adding_notes(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        result = self.student2.enroll("c2", ["n1", "n2"], add_course_notes="P")

        self.assertTrue("c2" in self.student2.courses)
        self.assertEqual(self.student2.courses["c2"], [])
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_existing_course(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        result = self.student2.add_notes("course1", "n3")

        self.assertEqual(self.student2.courses["course1"], ["n1", "n2", "n3"])
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_to_not_existing_course_raises_exception(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("c2", "n10")

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        result = self.student2.leave_course("course1")

        self.assertFalse("course1" in self.student2.courses)
        self.assertEqual(result, "Course has been removed")

    def test_leave_not_existing_course_raises_exception(self):
        self.assertEqual(self.student2.courses, {"course1": ["n1", "n2"]})

        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("alabala")

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    main()
