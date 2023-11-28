from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Um", "dolphin", "dolphin sound")

    def test_init(self):
        self.assertEqual("Um", self.mammal.name)
        self.assertEqual("dolphin", self.mammal.type)
        self.assertEqual("dolphin sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}",
                         self.mammal.make_sound())

    def test_get_kingdom(self):
        expected_result = self.mammal._Mammal__kingdom

        self.assertEqual(expected_result, self.mammal.get_kingdom())

    def test_info_about_animal(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}",
                         self.mammal.info())


if __name__ == "__main__":
    main()
