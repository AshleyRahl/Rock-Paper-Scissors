import unittest
import rock_paper_scissors

class TestRockPaperScissors(unittest.TestCase):

    def test_ties(self):
        self.assertEqual(rock_paper_scissors.determine_winner("rock", "rock"), "Its a tie")
        self.assertEqual(rock_paper_scissors.determine_winner("paper", "paper"), "Its a tie")
        self.assertEqual(rock_paper_scissors.determine_winner("scissors", "scissors"), "Its a tie")

    def test_user_wins(self):
        self.assertEqual(rock_paper_scissors.determine_winner("rock", "scissors"), "You win! Rock beats Scissors.")
        self.assertEqual(rock_paper_scissors.determine_winner("paper", "rock"), "You win! Paper beats Rock.")
        self.assertEqual(rock_paper_scissors.determine_winner("scissors", "paper"), "You win! Scissors beats Paper.")

    def test_computer_wins(self):
        # swap conditions to test computer wins
        self.assertEqual(rock_paper_scissors.determine_winner("rock", "paper"), "Computer wins! Paper beats Rock.")
        self.assertEqual(rock_paper_scissors.determine_winner("paper", "scissors"), "Computer wins! Scissors beats Paper.")
        self.assertEqual(rock_paper_scissors.determine_winner("scissors", "rock"), "Computer wins! Rock beats Scissors.")



if __name__ == '__main__':
    unittest.main()
        