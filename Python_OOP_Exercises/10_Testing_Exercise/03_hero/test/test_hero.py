from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    h_username = "Hero"
    h_level = 2
    h_health = 50.5
    h_damage = 5.5

    e_username = "Enemy"
    e_level = 2
    e_health = 50.5
    e_damage = 5.5

    def setUp(self):
        self.hero = Hero(self.h_username, self.h_level, self.h_health, self.h_damage)
        self.enemy = Hero(self.e_username, self.e_level, self.e_health, self.e_damage)

    def test_init(self):
        self.assertEqual(self.h_username, self.hero.username)
        self.assertEqual(self.h_level, self.hero.level)
        self.assertEqual(self.h_health, self.hero.health)
        self.assertEqual(self.h_damage, self.hero.damage)

    def test_attributes_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle_hero_vs_himself_raises_exception(self):
        with self.assertRaises(Exception) as ex:

            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_equal_to_zero_or_less_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = -1

        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve2.exception))

    def test_enemy_hero_health_equal_to_zero_or_less_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.e_username}. He needs to rest", str(ve.exception))

        self.enemy.health = -1

        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.e_username}. He needs to rest", str(ve2.exception))

    def test_battle_when_hero_and_enemy_health_became_zero_or_less_returned_draw(self):
        self.hero.health = 11
        self.enemy.health = 11
        result_equal_to_zero = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result_equal_to_zero)

        self.hero.health = 10
        self.enemy.health = 10
        result_negative_number = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result_negative_number)

    def test_hero_wins_increases_level_with_one_health_with_five_damage_with_five_returns_win_msg(self):
        self.enemy.health = 11

        expected_level = 3
        expected_health = 44.5
        expected_damage = 10.5

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose_enemy_increases_level_with_one_health_with_five_damage_with_five_returns_hero_lose_msg(self):
        self.hero.health = 11

        expected_level = 3
        expected_health = 44.5
        expected_damage = 10.5

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_represent(self):
        expected = f"Hero {self.h_username}: {self.h_level} lvl\n" \
               f"Health: {self.h_health}\n" \
               f"Damage: {self.h_damage}\n"

        self.assertEqual(expected, str(self.hero))


if __name__ == '__main':
    main()
