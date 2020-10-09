class TicTacToeGameManager:
    def __init__(self):
        self.state = '_' * 9
        self.move_next = 'X'
        self.end = False
        self.end_message = ''
        self.coordinates_map = {
            (1, 1): 6, (2, 1): 7, (3, 1): 8,
            (1, 2): 3, (2, 2): 4, (3, 2): 5,
            (1, 3): 0, (2, 3): 1, (3, 3): 2
        }

    def run(self):
        self.render_empty_state()
        while not self.end:
            self.update_state()
            self.render_state()
            self.analyze_state()
        print(self.end_message)

    @staticmethod
    def render_empty_state():
        print('-' * 9)
        print('|' + ' ' * 7 + '|')
        print('|' + ' ' * 7 + '|')
        print('|' + ' ' * 7 + '|')
        print('-' * 9)

    def render_state(self):
        print('-' * 9)
        print('| ' + ' '.join(self.state[:3]) + ' |')
        print('| ' + ' '.join(self.state[3:6]) + ' |')
        print('| ' + ' '.join(self.state[6:9]) + ' |')
        print('-' * 9)

    def update_state(self):
        [a, b] = input('Enter the coordinates: ').split()
        if not a.isnumeric() or not b.isnumeric():
            print('You should enter numbers!')
            self.update_state()
        elif int(a) > 3 or int(a) < 1 or int(b) > 3 or int(b) < 1:
            print('Coordinates should be from 1 to 3!')
            self.update_state()
        elif self.state[self.coordinates_map[(int(a), int(b))]] != '_':
            print('This cell is occupied! Choose another one!')
            self.update_state()
        else:
            state_lst = list(self.state)
            state_lst[self.coordinates_map[(int(a), int(b))]] = self.move_next
            self.state = ''.join(state_lst)
            if self.move_next == 'X':
                self.move_next = 'O'
            else:
                self.move_next = 'X'
            return

    def analyze_state(self):
        if self.not_finished():
            return
        elif self.draw():
            self.end = True
            self.end_message = 'Draw'
        elif self.win('X'):
            self.end = True
            self.end_message = 'X wins'
        elif self.win('O'):
            self.end = True
            self.end_message = 'O wins'
        return

    @staticmethod
    def get_num_char_in_str(string, char):
        return len([x for x in string if x == char])

    def win(self, symbol):
        return (self.state[0] == symbol and self.state[1] == symbol and self.state[2] == symbol) or \
               (self.state[3] == symbol and self.state[4] == symbol and self.state[5] == symbol) or \
               (self.state[6] == symbol and self.state[7] == symbol and self.state[8] == symbol) or \
               (self.state[0] == symbol and self.state[3] == symbol and self.state[6] == symbol) or \
               (self.state[1] == symbol and self.state[4] == symbol and self.state[7] == symbol) or \
               (self.state[2] == symbol and self.state[5] == symbol and self.state[8] == symbol) or \
               (self.state[0] == symbol and self.state[4] == symbol and self.state[8] == symbol) or \
               (self.state[2] == symbol and self.state[4] == symbol and self.state[6] == symbol)

    def draw(self):
        return not self.win('X') and not self.win('O') and '_' not in self.state

    def not_finished(self):
        return not self.win('X') and not self.win('O') and '_' in self.state

    # def impossible(self):
    #     return (self.win('X') and self.win('O')) or \
    #            abs(self.get_num_char_in_str(self.state, 'X') - self.get_num_char_in_str(self.state, 'O')) >= 2


if __name__ == '__main__':
    game = TicTacToeGameManager()
    game.run()
