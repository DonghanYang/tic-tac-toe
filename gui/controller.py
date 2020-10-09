from functools import partial
from typing import Tuple

from PyQt5.QtWidgets import QPushButton

from view import GameUI


class GameController:
    def __init__(self, view: GameUI):
        self._view = view
        self._move_next = 'X'
        self._state = {}
        self._end = False
        self._init_state()
        self._connect_signals()

    def _init_state(self):
        for pos, _ in self._view.buttons.items():
            self._state[pos] = ''

    def _set_next_move(self):
        if self._move_next == 'X':
            self._move_next = 'O'
            self._view.set_display_text('O')
        elif self._move_next == 'O':
            self._move_next = 'X'
            self._view.set_display_text('X')

    def _reset_state(self):
        self._move_next = 'X'
        self._view.set_display_text('X')
        self._state = {}
        self._end = False
        self._view.clear_button_text()
        self._init_state()

    def _update_state(self, btn: QPushButton, pos: Tuple):
        if self._end:
            self._reset_state()
            return
        if btn.text() == '':
            self._state[pos] = self._move_next
            btn.setText(self._move_next)
            self._set_next_move()
            self._analyze_state()
        else:
            self._view.set_display_text('Choose another cell')

    def _analyze_state(self):
        if self._not_finished():
            return
        elif self._draw():
            self._end = True
            self._view.set_display_text('Draw')
        elif self._win('X'):
            self._end = True
            self._view.set_display_text('X wins')
        elif self._win('O'):
            self._end = True
            self._view.set_display_text('O wins')
        return

    def _win(self, symbol):
        return (self._state[(0, 0)] == symbol and self._state[(0, 1)] == symbol and self._state[(0, 2)] == symbol) or \
               (self._state[(1, 0)] == symbol and self._state[(1, 1)] == symbol and self._state[(1, 2)] == symbol) or \
               (self._state[(2, 0)] == symbol and self._state[(2, 1)] == symbol and self._state[(2, 2)] == symbol) or \
               (self._state[(0, 0)] == symbol and self._state[(1, 0)] == symbol and self._state[(2, 0)] == symbol) or \
               (self._state[(0, 1)] == symbol and self._state[(1, 1)] == symbol and self._state[(2, 1)] == symbol) or \
               (self._state[(0, 2)] == symbol and self._state[(1, 2)] == symbol and self._state[(2, 2)] == symbol) or \
               (self._state[(0, 0)] == symbol and self._state[(1, 1)] == symbol and self._state[(2, 2)] == symbol) or \
               (self._state[(0, 2)] == symbol and self._state[(1, 1)] == symbol and self._state[(2, 0)] == symbol)

    def _draw(self):
        return not self._win('X') and not self._win('O') and '' not in self._state.values()

    def _not_finished(self):
        return not self._win('X') and not self._win('O') and '' in self._state.values()

    def _connect_signals(self):
        for pos, btn in self._view.buttons.items():
            btn.clicked.connect(partial(self._update_state, btn, pos))
