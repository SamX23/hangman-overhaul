class Init(object):
    def __init__(self):
        self.four_legs = ['kuda', 'kucing',
                          'anjing', 'sapi', 'domba', 'keledai',
                          'kerbau', 'kelinci']
        self.two_legs = ['ayam', 'bebek', 'kanguru', 'burung']

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

        self.intro_1 = """>> Coded using python, inspired from books and SUPERCHARGED by Sami Kalammallah <<
        \nWazzzaaappp, yuk main HangMan!
        ________
        |   |
        |   0
        |  /|\\
        |  / \\
        | 
        |______
        \nLets go, mari kita mainkan!!, ketik apapun untuk memulai.\nKetik \'no\' untuk keluar.\n"""
        self.intro_2 = '\nSilahkan tebak nama hewan domestik ya! kamu punya 7 kesempatan salah!\nKetik \'quit\' untuk ' \
                      'keluar.\n'
