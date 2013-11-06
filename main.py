#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function check if squares make the player winner
def checkWinner(player , squares):
    if(squares[0]==player and squares[3]==player and squares[6]==player or\
       squares[1]==player and squares[4]==player and squares[7]==player or\
       squares[2]==player and squares[5]==player and squares[8]==player or\
       squares[0]==player and squares[1]==player and squares[2]==player or\
       squares[3]==player and squares[4]==player and squares[5]==player or\
       squares[6]==player and squares[7]==player and squares[8]==player or\
       squares[0]==player and squares[4]==player and squares[8]==player or\
       squares[2]==player and squares[4]==player and squares[6]==player):
        return True
    else:
        return False


c = 9 # counter squars 
turn = 0 # 0 for player X , 1 for player O

squares = ["1","2","3",
           "4","5","6",
           "7","8","9"]

strsq = squares[0]+" | "+squares[1]+" | "+squares[2]+"\n----------\n"+\
        squares[3]+" | "+squares[4]+" | "+squares[5]+"\n----------\n"+\
        squares[6]+" | "+squares[7]+" | "+squares[8]+"\n"
    
print strsq

playerXs = []
playerOs = []

while c > 0:
    
    
    # turn player X
    if(turn == 0):
        try:
            
            inp = int(input("Message >> Input number of squar as X player (1-9):")) # input squar X from squares 1-9
            
        except SyntaxError: # if input is empty
            inp = 0
        
        # if the player entered number other than 1-9 or empty
        if( not (1 <= inp <= 9) or inp == 0):
            print "Error >> X player did not enter integer (1-9)"
            break
        
        # if there is signal where the player entered
        if(playerOs.count(inp) > 0 or playerXs.count(inp) > 0):
            print "Error >> there is signal at",inp,"square!"
            break
        
        squares[squares.index(str(inp))] = "X" # replace number square by X
        playerXs.append(inp) # add X in squares where the player enter
        turn = 1 # turn to player O
    
    # turn player O
    else:
        try:
            inp = input("Message >> Input number of squar as O player (1-9):") # input squar O from squares 1-9
            
        except SyntaxError: # if input is empty
            inp = 0
        
        # if the player entered number other than 1-9 or empty
        if( not (1 <= inp <= 9) or inp == 0):
            print "Error >> O player did not enter integer (1-9)"
            break
        
        # if there is signal where the player entered
        if(playerOs.count(inp) > 0 or playerXs.count(inp) > 0):
            print "Error >> there is signal at",inp,"square!"
            break
        
        squares[squares.index(str(inp))] = "O" # replace number square by O
        playerOs.append(inp) # add O in squares where the player enter
        turn = 0 # turn to player X
    
    
    strsq = squares[0]+" | "+squares[1]+" | "+squares[2]+"\n----------\n"+\
            squares[3]+" | "+squares[4]+" | "+squares[5]+"\n----------\n"+\
            squares[6]+" | "+squares[7]+" | "+squares[8]+"\n"
    
    print strsq
    
    c-=1 # decrement the squares
    
    if(checkWinner("X",squares)):
        print "Message >> player X win !"
        break
    
    if(checkWinner("O",squares)):
        print "Message >> player O win !"
        break
    
    # if the game end
    if(c == 0):
        print "Message >> the Game end as draw"


