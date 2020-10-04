def get_num_char(string, char):
    return len([x for x in string if x == char])


def win(symbols, who):
    return (symbols[0] == who and symbols[1] == who and symbols[2] == who) or \
           (symbols[3] == who and symbols[4] == who and symbols[5] == who) or \
           (symbols[6] == who and symbols[7] == who and symbols[8] == who) or \
           (symbols[0] == who and symbols[3] == who and symbols[6] == who) or \
           (symbols[1] == who and symbols[4] == who and symbols[7] == who) or \
           (symbols[2] == who and symbols[5] == who and symbols[8] == who) or \
           (symbols[0] == who and symbols[4] == who and symbols[8] == who) or \
           (symbols[2] == who and symbols[4] == who and symbols[6] == who)


def draw(symbols):
    return not win(symbols, 'X') and not win(symbols, 'O') and '_' not in symbols


def not_finished(symbols):
    return not win(symbols, 'X') and not win(symbols, 'O') and '_' in symbols


def impossible(symbols):
    return (win(symbols, 'X') and win(symbols, 'O')) or \
        abs(get_num_char(symbols, 'X') - get_num_char(symbols, 'O')) >= 2


def show_result(symbols):
    if impossible(symbols):
        print('Impossible')
    elif not_finished(symbols):
        print('Game not finished')
    elif draw(symbols):
        print('Draw')
    elif win(symbols, 'X'):
        print('X wins')
    elif win(symbols, 'O'):
        print('O wins')


def render():
    symbols = input('Enter cells: ')
    print('-' * 9)
    print('| ' + ' '.join(symbols[:3]) + ' |')
    print('| ' + ' '.join(symbols[3:6]) + ' |')
    print('| ' + ' '.join(symbols[6:9]) + ' |')
    print('-' * 9)
    show_result(symbols)


render()
