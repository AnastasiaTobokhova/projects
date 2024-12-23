import unittest

def frozen_test(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f'Тесты в этом кейсе заморожены')
            return
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        # Ваш код теста
        self.assertTrue(True)

    def test_run(self):
        # Ваш код теста
        self.assertTrue(True)

    def test_walk(self):
        # Ваш код теста
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @frozen_test
    def test_first_tournament(self):
        # Ваш код теста
        self.assertTrue(True)

    @frozen_test
    def test_second_tournament(self):
        # Ваш код теста
        self.assertTrue(True)

    @frozen_test
    def test_third_tournament(self):
        # Ваш код теста
        self.assertTrue(True)
