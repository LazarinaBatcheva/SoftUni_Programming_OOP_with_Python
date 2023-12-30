from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("A")

    def test_initialization(self):
        self.assertEqual("A", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_name_not_isalpha_raises(self):
        self.assertEqual("A", self.team.name)

        expected = "Team Name can contain only letters!"

        with self.assertRaises(ValueError) as ve:
            self.team.name = "a b"

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.team.name = "a12"

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.team.name = " "

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.team.name = "012"

        self.assertEqual(expected, str(ve.exception))

    def test_add_member_non_existing_name_success(self):
        self.assertEqual({}, self.team.members)

        result = self.team.add_member(Ivan=20, Maria=21)
        expected = "Successfully added: Ivan, Maria"

        self.assertEqual({"Ivan": 20, "Maria": 21}, self.team.members)
        self.assertEqual(expected, result)

    def test_add_member_existing_name_failure(self):
        self.assertEqual({}, self.team.members)
        self.team.members = {"Ivan": 20, "Maria": 21}

        result = self.team.add_member(Ivan=25)
        expected = "Successfully added: "

        self.assertEqual({"Ivan": 20, "Maria": 21}, self.team.members)
        self.assertEqual(expected, result)

    def test_add_member_non_existing_and_existing_name_added_only_non_existing_name(self):
        self.assertEqual({}, self.team.members)
        self.team.members = {"Ivan": 20, "Maria": 21}

        result = self.team.add_member(Mitko=22, Ivan=23)
        expected = "Successfully added: Mitko"

        self.assertEqual({"Ivan": 20, "Maria": 21, "Mitko": 22}, self.team.members)
        self.assertEqual(expected, result)

    def test_add_member_invalid_name_and_non_existing_name_added_only_non_existing_name(self):
        self.assertEqual({}, self.team.members)
        self.team.members = {"Ivan": 20, "Mitko": 21}

        result = self.team.add_member(Maria=22, Ivan12=23)
        expected = "Successfully added: Maria"

        self.assertEqual({"Ivan": 20, "Mitko": 21, "Maria": 22}, self.team.members)
        self.assertEqual(expected, result)

    def test_remove_member_empty_dict_members_failure(self):
        self.assertEqual({}, self.team.members)

        result = self.team.remove_member("Ivan")
        expected = "Member with name Ivan does not exist"

        self.assertEqual(expected, result)

    def test_remove_member_non_existing_name_failure(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Maria=21)

        result = self.team.remove_member("Mitko")
        expected = "Member with name Mitko does not exist"

        self.assertEqual({"Ivan": 20, "Maria": 21}, self.team.members)
        self.assertEqual(expected, result)

    def test_remove_member_existing_name_success(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Mitko=22, Maria=21)

        result = self.team.remove_member("Mitko")
        expected = "Member Mitko removed"

        self.assertEqual({"Ivan": 20, "Maria": 21}, self.team.members)
        self.assertEqual(expected, result)

    def test_team_members_greater_than_another_one(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Maria=21, Mitko=22)

        another_team = Team("B")
        another_team.add_member(Gosho=30, Petar=25)

        self.assertEqual(self.team > another_team, True)

    def test_team_members_lower_than_another_one(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Maria=21)
        another_team = Team("B")
        another_team.add_member(Gosho=30, Petar=25, Mitko=22)

        self.assertEqual(self.team > another_team, False)

    def test_team_members_equal_to_another_one(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Petar=21)

        another_team = Team("B")
        another_team.add_member(Gosho=30, Mitko=22)

        self.assertEqual(self.team > another_team, False)

    def test_len_dict_members(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Maria=21)

        result = len(self.team)

        self.assertEqual(2, result)

    def test_len_dict_members_no_members(self):
        self.assertEqual({}, self.team.members)

        result = len(self.team)

        self.assertEqual(0, result)

    def test_add_method(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Ivan=20, Gosho=25)

        another_team = Team("B")
        another_team.add_member(Maria=20, Petar=30)

        new_team = self.team + another_team
        self.assertEqual("AB", new_team.name)
        self.assertEqual({"Ivan": 20, "Gosho": 25, "Maria": 20, "Petar": 30}, new_team.members)

    def test_string_method(self):
        self.assertEqual({}, self.team.members)
        self.team.add_member(Gosho=30, Petar=25, Mitko=22)

        expected = """Team name: A
Member: Gosho - 30-years old
Member: Petar - 25-years old
Member: Mitko - 22-years old"""

        result = str(self.team)

        self.assertEqual({"Gosho": 30, "Petar": 25, "Mitko": 22}, self.team.members)
        self.assertEqual(expected, result)

    def test_string_method_empty_dict_of_members(self):
        self.assertEqual({}, self.team.members)

        expected = """Team name: A"""

        result = str(self.team)

        self.assertEqual({}, self.team.members)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
