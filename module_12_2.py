import unittest


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        self.distance += self.speed

    def walk(self):
        self.distance += self.speed // 2


class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants
    # Дополнительно:
    # В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
    # В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее,
    # чем бегун с большей.
    # Попробуйте решить эту проблему и обложить дополнительными тестами.
    def start(self):
        # Рассчитываем время для каждого бегуна
        times = {runner.name: self.distance / runner.speed for runner in self.participants}

        # Сортировка по времени финиша
        sorted_runners = sorted(times.items(), key=lambda x: x[1])

        # Результаты
        results = {i + 1: runner[0] for i, runner in enumerate(sorted_runners)}
        return results


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Usain", 10)
        self.runner_andrey = Runner("Andrey", 9)
        self.runner_nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, [self.runner_usain, self.runner_nick])
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, [self.runner_andrey, self.runner_nick])
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, [self.runner_usain, self.runner_andrey, self.runner_nick])
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_correct_order_with_three_runners(self):
        # Дополнительный тест для проверки порядка
        tournament = Tournament(90, [self.runner_usain, self.runner_andrey, self.runner_nick])
        results = tournament.start()
        expected_order = {1: "Usain", 2: "Andrey", 3: "Nick"}
        self.assertEqual(results, expected_order)

    def test_same_speed(self):
        # Тест для бегунов с одинаковой скоростью
        runner1 = Runner("Runner1", 5)
        runner2 = Runner("Runner2", 5)
        tournament = Tournament(90, [runner1, runner2])
        results = tournament.start()
        expected_order = {1: "Runner1", 2: "Runner2"}  # Порядок определяется порядком добавления
        self.assertEqual(results, expected_order)


if __name__ == "__main__":
    unittest.main(verbosity=2)
