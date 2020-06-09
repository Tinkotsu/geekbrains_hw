import random


pull = [i for i in range(1, 91)]


def game_over():
    print('Игра закончена! Проигрыш!')
    exit()


def victory():
    print('Победа!')
    exit()


class Player:
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.to_win = 15

    def __str__(self):
        res = '\n'.join([' '.join(self.card[i]) for i in range(3)])
        return res

    def close_num(self, num):
        item = str(num)
        if len(item) == 1:
            item += ' '
        for i in range(3):
            if item in self.card[i]:
                self.card[i][self.card[i].index(item)] = '- '
                self.to_win -= 1
                break

    def check(self, num):
        item = str(num)
        if len(item) == 1:
            item += ' '
        for i in range(3):
            if item in self.card[i]:
                return i
        return -1

    def ask_user(self, num):
        answer = input('Зачеркнуть цифру? (y/n) ')
        while answer != 'y' and answer != 'n':
            answer = input('Зачеркнуть цифру? (y/n) ')
        checked = self.check(num)
        if answer == 'y' and checked == -1:
            game_over()
        elif answer == 'n' and checked != -1:
            game_over()
        if answer == 'y':
            self.close_num(num)
            if self.to_win == 0:
                victory()


def generate_card():
    gen_pull = pull.copy()
    index_array = [i for i in range(9)]
    gen_card = [['  ' for _ in range(9)] for _ in range(3)]
    for i in range(3):
        new_i_array = index_array.copy()
        for _ in range(5):
            random.shuffle(gen_pull)
            random.shuffle(new_i_array)
            item = str(gen_pull.pop())
            gen_card[i][new_i_array.pop()] = item + ' ' if len(item) == 1 else item
    return gen_card


player = Player('Player', generate_card())
computer = Player('Computer', generate_card())

while True:
    if computer.to_win == 0:
        game_over()
    random.shuffle(pull)
    new_num = pull.pop()
    print(f'Новый бочонок: {new_num} (осталось {len(pull)})\n')
    print('------ Ваша карточка -----')
    print(player)
    print('--------------------------')
    print('-- Карточка компьютера ---')
    print(computer)
    print('--------------------------')
    player.ask_user(new_num)
    computer.close_num(new_num)
    print('')
