# Hangman challenge from book 'SelfTaught' supercharged by Sami Kalammallah
# Coded on 27 March 2020 #stayathome
import random
from PrintR import Printer


class HangmanTest(object):

    def __init__(self):
        self.two_legs = ['kuda', 'kucing',
                         'anjing', 'sapi', 'domba', 'keledai',
                         'kerbau', 'kelinci']
        self.four_legs = ['ayam', 'bebek', 'kanguru', 'burung']

        self.clue_1 = "Kuncinya hewan domestik berkaki 4 :)"
        self.clue_2 = "Kuncinya hewan domestik berkaki 2 :)"

        self.chance = ["",
                       "________",
                       "|   |",
                       "|   0",
                       "|  /|\\",
                       "|  / \\",
                       "|",
                       "|"]
        self.stage = 0
        self.starts()

    # random machinee yeaaah!!
    def random_clue(self):
        randnum = random.randint(0, len(self.two_legs) - 1)
        randnum2 = random.randint(0, len(self.four_legs) - 1)

        animals = [self.two_legs[randnum],
                   self.four_legs[randnum2]]
        randnum3 = random.randint(0, len(animals) - 1)

        if randnum3 == 0:
            print(self.clue_1)
        else:
            print(self.clue_2)

        random_words = animals[randnum3]
        return random_words

    # intro coy
    def starts(self):
        Printer('\n>> Coded using python, inspired from books and '
              'SUPERCHARGED by Sami Kalammallah <<\n'
              '\nWazzzaaappp, yuk main HangMan!\n')
        Printer(
            "________\n"
            "|   |\n"
            "|   0\n"
            "|  /|\\\n"
            "|  / \\\n"
            "| \n"
            "|______\n")

        Printer('Lets go, mari kita mainkan!!, ketik apapun untuk memulai.\n'
              'Ketik \'no\' untuk keluar.\n')
        lets_go = input('')
        if lets_go != 'no':
            Printer('\nSilahkan tebak nama hewan domestik ya! kamu punya 7 kesempatan salah!\n'
                  'Ketik \'quit\' untuk keluar\n')
            HangmanTest.main(self)
        else:
            Printer('\nOkayy, silahkan dicoba kembali lain waktu')
            HangmanTest.logout()

    # maincode
    def main(self):
        self.stage = 0
        correct_words = self.random_clue()
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


HangmanTest().main()
