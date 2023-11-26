from unittest import TestCase, main

from worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 7_000, 77)

    def test_correct_initialization(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(7000, self.worker.salary)
        self.assertEqual(77, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_not_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_when_worker_has_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.money + self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_increase_energy_with_one_when_worker_resting(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_valid_string(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.',
                         self.worker.get_info())


if __name__ == '__main__':
    main()