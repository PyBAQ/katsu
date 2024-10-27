from collections import namedtuple
import unittest
import give_away;

class TestStringMethods(unittest.TestCase):
    def test_winner_should_return_random_user(self):
        w: str = give_away.winner(give_away.cvsReader('participants_test_data'))
        assert isinstance(w, str) and w is not ''

    def test_winner_handle_empty_param(self):
        with self.assertRaises(ValueError):
           give_away.winner([])

    def test_winner_should_handle_type_error(self):
        with self.assertRaises(TypeError):
           give_away.winner("not a list")

        with self.assertRaises(TypeError):
           give_away.winner(1)

        with self.assertRaises(TypeError):
           give_away.winner({'test': 1})

    def test_winner_with_tuple_missing_attribute(self):
        ParticipantWithoutName = namedtuple('ParticipantWithoutName', ['lastname'])
        ParticipantWithoutLasName = namedtuple('ParticipantWithoutName', ['name'])

        participants = [ParticipantWithoutName('Orozco'), ParticipantWithoutName('Herdenez')]
        with self.assertRaises(AttributeError):
            give_away.winner(participants)

        participants = [ParticipantWithoutLasName('Pedro'), ParticipantWithoutName('Carlos')]
        with self.assertRaises(AttributeError):
            give_away.winner(participants)

    def test_winner_with_tuple_different_attribute(self):
        ParticipantWithoutName = namedtuple('ParticipantWithoutName', ['lastName', 'firstName'])

        participants = [ParticipantWithoutName('Orozco', 'Pedro'), ParticipantWithoutName('Perez', 'Jose')]

        with self.assertRaises(AttributeError):
            give_away.winner(participants)

    def test_winner_should_remove_winners_of_data(self):
        give_away.participants = give_away.cvsReader('participants_test_data');
        initial_len = len(give_away.participants)
        give_away.winner(give_away.cvsReader('participants_test_data'))
        self.assertNotEqual(initial_len, len(give_away.participants))


if __name__ == '__main__':
    unittest.main()