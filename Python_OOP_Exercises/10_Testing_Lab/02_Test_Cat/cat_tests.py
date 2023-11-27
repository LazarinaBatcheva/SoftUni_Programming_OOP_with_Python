from unittest import TestCase, main

# from cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Garfild')

    def test_when_cat_fed_can_not_eat_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_when_cat_not_fed_can_eat_became_sleepy_and_increase_size_with_one(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_can_not_sleep_if_it_is_hungry_raises_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_fed_and_can_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
