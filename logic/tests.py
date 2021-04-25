from django.test import TestCase
from logic.pingpong import find_second_loser

# Create your tests here.
class FindSecondLoserTestCase(TestCase):
    def test_default_case(self):
        second_loser_name, lost_games = find_second_loser(17, 15, 10)
        self.assertEqual(second_loser_name, "Player 3")