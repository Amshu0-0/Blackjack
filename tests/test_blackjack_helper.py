from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 10), "Drew a 10\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 15), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, -1), "BAD CARD\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([2], draw_card), 2)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([15], draw_card), 15)
    self.assertEqual(mock_random([0], draw_card), 0)
    self.assertEqual(mock_random([-1], draw_card), -1)
  
  def test_print_header(self):
    self.assertEqual(get_print(print_header, "HI"), "-----------\nHI\n-----------\n")
    self.assertEqual(get_print(print_header, ""), "-----------\n\n-----------\n")
    self.assertEqual(get_print(print_header, "p1ease w8rk"), "-----------\np1ease w8rk\n-----------\n")
    self.assertEqual(get_print(print_header, " oh noGAME OVER !"), "-----------\n oh noGAME OVER !\n-----------\n")

  def test_draw_starting_hand(self):
    output = mock_random([13, 12], draw_starting_hand, "PLAYER")
    self.assertEqual(output, 20)
    output = mock_random([1, 12], draw_starting_hand, "DEALER")
    self.assertEqual(output, 21)
    output = mock_random([4, 6], draw_starting_hand, "PLAYER")
    self.assertEqual(output, 10)
    output = mock_random([3, 1], draw_starting_hand, "DEALER")
    self.assertEqual(output, 14)
  
  def test_print_end_turn_status(self):
    expected_output = "Final hand: 18.\n"
    self.assertEqual(get_print(print_end_turn_status, 18), expected_output)
    expected_output = "Final hand: 17.\n"
    self.assertEqual(get_print(print_end_turn_status, 17), expected_output)
    expected_output = "Final hand: 21.\nBLACKJACK!\n"
    self.assertEqual(get_print(print_end_turn_status, 21), expected_output)
    expected_output = "Final hand: 25.\nBUST.\n"
    self.assertEqual(get_print(print_end_turn_status, 25), expected_output)
    expected_output = "Final hand: 2.\n"
    self.assertEqual(get_print(print_end_turn_status, 2), expected_output)

  def test_print_end_game_status(self):
    expected_output = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 20, 19), expected_output)  
    expected_output = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 22, 19), expected_output)
    expected_output = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 19, 19), expected_output)
    expected_output = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 23, 24), expected_output)
         
if __name__ == '__main__':
    unittest.main()