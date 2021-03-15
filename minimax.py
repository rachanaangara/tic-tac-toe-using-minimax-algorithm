import sys
import random 
def game_player(game_board,chance,game_is_on):
    
    if(game_is_on==True):
          
            if(chance%2==0):
                ec=check_empty_slot(game_board)
                if(len(ec)==0):
                    msg="DRAW"
                    return [game_board,chance,False,"DRAW"]
                else: 
                    msg="Waiting for Bot 1's move"
                    for i in ec:
                        game_board[i]='x'
                        flag=check_winning_moves('x',game_board)
                        if(flag==1):                          
                            msg="BOT 2 WON!!"
                            return [game_board,chance,False,msg]
                        game_board[i]='e'
                    if(flag!=1):
                        r=random.choice(ec)
                        game_board[r]='x'
                        chance=chance+1
                        return [game_board,chance,game_is_on,'']
            else:
                ec=check_empty_slot(game_board)
                if(len(ec)==0):
                    return [game_board,chance,False,'DRAW']
                else:    
                    msg="Waiting for Bot 2's move"
                    for i in ec:
                        game_board[i]='o'
                        flag=check_winning_moves('o',game_board)
                        if(flag==1):
                            msg="BOT 1 WON!!"
                            return [game_board,chance,False,msg]
                        game_board[i]='e'
                    if(flag!=1):
                        r=random.choice(ec)
                        game_board[r]='o'
                        chance=chance+1
                        return [game_board,chance,game_is_on,'']
def check_empty_slot(game_board):
    empty_cells=[]
    for i in game_board.keys():
            if game_board[i]=='e':
                empty_cells.append(i)
    return empty_cells

def check_winning_moves(a,game_board):
    if (game_board['1']==a and game_board['2']==a and game_board['3']==a):
        return 1
    if game_board['4']==a and game_board['5']==a and game_board['6']==a:
        return 1 
    if game_board['7']==a and game_board['8']==a and game_board['9']==a:
        return 1
    #checking verals
    
    if game_board['1']==a and game_board['4']==a and game_board['7']==a:
        return 1 
    if game_board['2']==a and game_board['5']==a and game_board['8']==a:
        return 1 
    if game_board['3']==a and game_board['6']==a and game_board['9']==a:
        return 1 
    
    #checking diaognals
    if game_board['1']==a and game_board['5']==a and game_board['9']==a:
        return 1 
    if game_board['3']==a and game_board['5']==a and game_board['7']==a:
        return 1     
                    