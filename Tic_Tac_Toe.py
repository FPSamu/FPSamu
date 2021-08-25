tablero = [' ',' ',' ',
           ' ',' ',' ',
           ' ',' ',' ']

player1 = 'X'
player2 = 'O'

# winner = None

# Dibujar tablero
def draw_board(): 
    print(tablero[0],'|',tablero[1],'|',tablero[2])
    print('--+---+--')
    print(tablero[3],'|',tablero[4],'|',tablero[5])
    print('--+---+--')
    print(tablero[6],'|',tablero[7],'|',tablero[8])    
draw_board()


# Colocar ficha X
def place_x():
    position = int(input('Enter a number: '))
    place = position-1
    if tablero[place] != ' ':
        place_x()
    else:
        tablero[place] = player1 
        draw_board()

# Colocar ficha O
def place_o():
    position = int(input('Enter a number: '))
    place = position-1
    if tablero[place] != ' ':
        place_o()
    else:
        tablero[place] = player2
        draw_board()


# Revisar ganador 
def play():
    winner = None
    while winner == None:
        place_x()
        if tablero[0] == tablero[1] and tablero[1] == tablero[2] and tablero[2] == tablero[0]:
            if tablero[0] != ' ':
                if tablero[0] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[0] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        
        if tablero[3] == tablero[4] and tablero[4] == tablero[5] and tablero[5] == tablero[3]:
            if tablero[3] != ' ':
                if tablero[3] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[3] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
                
        if tablero[6] == tablero[7] and tablero[7] == tablero[8] and tablero[8] == tablero[6]:
            if tablero[6] != ' ':
                if tablero[6] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[6] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[0] == tablero[3] and tablero[3] == tablero[6] and tablero[6] == tablero[0]:
            if tablero[0] != ' ':
                if tablero[0] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[0] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[1] == tablero[4] and tablero[4] == tablero[7] and tablero[7] == tablero[1]:
            if tablero[1] != ' ':
                if tablero[1] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[1] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[2] == tablero[5] and tablero[5] == tablero[8] and tablero[8] == tablero[2]:
            if tablero[2] != ' ':
                if tablero[2] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[2] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[0] == tablero[4] and tablero[4] == tablero[8] and tablero[8] == tablero[0]:
            if tablero[0] != ' ':
                if tablero[0] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[0] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[2] == tablero[4] and tablero[4] == tablero[6] and tablero[6] == tablero[2]:
            if tablero[2] != ' ':
                if tablero[2] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[2] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[0] != ' ' and tablero[2] != ' ' and tablero[3] != ' ' and tablero[4] != ' ' and tablero[5] != ' ' and tablero[6] != ' 'and tablero[7] != ' ' and tablero[8] != ' ':
            if winner == None:
                print('tie')
                break
                
        place_o()
        if tablero[0] == tablero[1] and tablero[1] == tablero[2] and tablero[2] == tablero[0]:
            if tablero[0] != ' ':
                if tablero[0] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[0] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        
        if tablero[3] == tablero[4] and tablero[4] == tablero[5] and tablero[5] == tablero[3]:
            if tablero[3] != ' ':
                if tablero[3] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[3] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
                
        if tablero[6] == tablero[7] and tablero[7] == tablero[8] and tablero[8] == tablero[6]:
            if tablero[6] != ' ':
                if tablero[6] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[6] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[0] == tablero[3] and tablero[3] == tablero[6] and tablero[6] == tablero[0]:
            if tablero[0] != ' ':
                if tablero[0] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[0] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[1] == tablero[4] and tablero[4] == tablero[7] and tablero[7] == tablero[1]:
            if tablero[1] != ' ':
                if tablero[1] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[1] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[2] == tablero[5] and tablero[5] == tablero[8] and tablero[8] == tablero[2]:
            if tablero[2] != ' ':
                if tablero[2] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[2] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[0] == tablero[4] and tablero[4] == tablero[8] and tablero[8] == tablero[0]:
            if tablero[0] != ' ':
                if tablero[0] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[0] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[2] == tablero[4] and tablero[4] == tablero[6] and tablero[6] == tablero[2]:
            if tablero[2] != ' ':
                if tablero[2] == player1:
                    winner = 'Player 1 won'
                    print(winner)
                    break
                if tablero[2] == player2:
                    winner = 'Player 2 won'
                    print(winner)
                    break
        if tablero[0] != ' ' and tablero[2] != ' ' and tablero[3] != ' ' and tablero[4] != ' ' and tablero[5] != ' ' and tablero[6] != ' 'and tablero[7] != ' ' and tablero[8] != ' ':
            if winner == None:
                print('tie')
                break

play()
