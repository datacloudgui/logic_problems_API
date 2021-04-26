from django.test import TestCase
from logic.pingpong import find_second_loser

class FindSecondLoserTestCase(TestCase):
    """
    The next tests evaluate different possible losers
    """
    def test_default_case(self):
        second_loser_name, lost_games = find_second_loser(17, 15, 10)
        self.assertEqual(second_loser_name, "Juan")

    def test_ana_lose_case(self):
        second_loser_name, lost_games = find_second_loser(10, 17, 15)
        self.assertEqual(second_loser_name, "Ana")

class NotPossibleSolution(TestCase):
    """
    The next tests evaluate different not possible solution due the reasons detected in the validation stage
    """
    def test_impossible_case(self):
        second_loser_name, lost_games = find_second_loser(18, 15, 10)
        self.assertEqual(second_loser_name, "Second loser can't be founded: The scores are not possible according to the rules")

    def test_even_case(self):
        second_loser_name, lost_games = find_second_loser(20, 14, 10)
        self.assertEqual(second_loser_name, "Second loser can't be founded: The second loser only can be calculated if the total games is odd")

    def test_too_lost_case(self):
        second_loser_name, lost_games = find_second_loser(20, 12, 2)
        self.assertEqual(second_loser_name, "Second loser can't be founded: Loser games are not possible according to the rules")

    def test_many_options_case(self):
        second_loser_name, lost_games = find_second_loser(17, 15, 14)
        self.assertEqual(second_loser_name, "Second loser can't be founded: Too many options to the second game loser")