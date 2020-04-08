# Hangman challenge from book 'SelfTaught' supercharged by Sami Kalammallah
# Coded on 27 March 2020 #stayathome
from Randomizer import RandomClue
from PrintR import Printer


class HangmanTest(RandomClue):

    def __init__(self):
        super().__init__()
        self.stage = 0
        self.starts()

    # intro coy
    def starts(self):
        Printer(self.intro_1)
        lets_go = input('')
        if lets_go != 'no':
            Printer(self.intro_2)
            HangmanTest.main(self)
        else:
            Printer('\nOkayy, silahkan dicoba kembali lain waktu')
            HangmanTest.logout()

    # maincode
    def main(self):
        Printer(RandomClue().clue)
        print()
        self.stage = 0
        correct_words = RandomClue().words
        correct_list = list(correct_words)
        score_brd = [' _ '] * len(correct_words)
        win = False
        Printer(''.join(score_brd))
        # Loop question
        while self.stage < len(self.chance) - 1:
            print()
            guess = input('Masukan Huruf :\n')
            guess_len = len(guess)
            correct_len = len(correct_list)

            if guess_len <= correct_len:
                if guess == 'quit':
                    break
                else:
                    for i in range(len(guess)):
                        list_guess = list(guess)
                        indexing = list_guess[i]
                        if guess == 'quit':
                            break
                        elif indexing in correct_list:
                            char_index = correct_list.index(indexing)
                            score_brd[char_index] = indexing
                            correct_list[char_index] = '$'
                        else:
                            self.stage += 1
            elif guess_len == 0:
                print('Masukan sebuah huruf saja !!')
            else:
                print('Jangan diembat semua gan, mana salah lagi!')
                self.stage += 1

            print(''.join(score_brd).upper())

            if ' _ ' not in score_brd:
                print('')
                print('YESS!!')
                Printer('\nKamu menang!!')
                win = True
                break
            else:
                Printer('\n'.join(self.chance[0: self.stage + 1]))
                print('\n')

        # closing
        if not win:
            # print('\n'.join(wrong_gs[0:stage]))
            Printer('\nTetoooot! Jawabannya adalah: ')
            Printer(correct_words.upper())
        Printer('\nTerima kasih, apakah kamu masih ingin bermain lagi?')
        again = input('\nKetik \'yes\' untuk lanjut atau enter untuk keluar:\n')
        if again == 'yes':
            Printer('\nAyo bermain lagi!\n')
            HangmanTest.main(self)
        else:
            HangmanTest.logout()

    # logout
    @staticmethod
    def logout():
        Printer('\nWassalam !!!\n')
        exit()


HangmanTest()
