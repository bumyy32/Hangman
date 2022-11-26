import random

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'CASA', 'CAR', 'MONO', 'RISE', 'PYTHON', 'DOWNGRADE',
    'MILTON', 'LION', 'ROAR', 'LOGIC', 'TEST'
]


class Hangman():

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):

        for index in indexes:
            self.game_progress[index] = letter

    @staticmethod
    def is_valid_letter(input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    @staticmethod
    def get_user_input():
        user_input = input('\nPlease, type a letter: ')
        return user_input

    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Check the input
            if self.is_valid_letter(user_input):
                print("The value you choose is not a letter!")
                continue
            # Checking if the letter isn't already guessed
            if user_input in self.game_progress:
                print("You already guessed this letter!")
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)

                # If there's no letters left to find in the word
                if self.game_progress.count('_') == 0:
                    print('You won! Congratulations!')
                    print(f'The word is: ' + self.word_to_guess)
                    quit()
                else:
                    self.failed_attempts += 1
            print("You lost...")


if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()
