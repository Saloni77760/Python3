# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:19:56 2020

@author: LENOVO
"""

import numpy 
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p='X'
ps='O'

def place(symbol):
    print(numpy.matrix(board))
    while(1):
         row=int(input("Enter row :- 1 or 2 or 3: "))
         col=int(input("Enter column :- 1 or 2 or 3: "))
         if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_':
             board[row-1][col-1] = symbol
             break
         else:
             print("Invalid input! please enter again.")
         

def cheak_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol, "won")
            return True
    return False

def cheak_columm(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol, "won")
            return True
    return False

def cheak_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol, "won")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol, "won")
        return True
    return False

def won(symbol):
    return cheak_rows(symbol) or cheak_columm(symbol) or cheak_diagonals(symbol)
    
    
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn :")
            place(p)
            if won(p):
                break
        else:
            print("O turn :")
            place(ps)
            if won(ps):
                break
    if not(won(p)) and not(won(ps)):
        print("DRAW")
play()
    