from tictactoe import board
import pytest

def test_row_win():
    b = board()
    b.setValue(0,0,'X')
    assert b.setValueAndCheckWin(0,1,'X') == False
    assert b.setValueAndCheckWin(0,2,'X') == True

def test_col_win():
    b = board()
    b.setValue(0,0,'X')
    assert b.setValueAndCheckWin(1,0,'X') == False
    assert b.setValueAndCheckWin(2,0,'X') == True

def test_col_fail():
    b = board()
    b.setValue(0,0,'X')
    assert b.setValueAndCheckWin(1,0,'X') == False
    assert b.setValueAndCheckWin(2,1,'X') == False
