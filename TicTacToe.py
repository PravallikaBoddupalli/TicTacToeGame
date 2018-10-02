import time
def DrawBoard(board):    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
board=['0','1','2','3','4','5','6','7','8','9']
print("Hello Players...!!!")
time.sleep(1)
print("Welcome to TIC-TAC-TOE")
time.sleep(1)
print("Here is the board for you....")
time.sleep(2)
DrawBoard(board)
time.sleep(1)
print("Player 1: X")
print("Player 2: O")
t=1
while(t<=9):
 if(t%2!=0):
  print("Player 1's turn...")
  ch=int(input("Where do you place your character???"))
  board[ch]='X'
  DrawBoard(board)
  t=t+1
 else:
  print("Player 2's turn...")
  ch=int(input("Where do you place your character???"))
  board[ch]='O'
  DrawBoard(board)
  t=t+1
 if((board[1]=='X' and board[2]=='X' and board[3]=='X')or(board[4]=='X' and board[5]=='X' and board[6]=='X')or (board[7]=='X' and board[8]=='X' and board[9]=='X') or (board[1]=='X' and board[5]=='X' and board[9]=='X') or (board[3]=='X' and board[5]=='X' and board[7]=='X') or (board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X') or (board[3]=='X' and board[6]=='X' and board[9]=='X')):
  print("Player 1 Won!!!")
  break
 else:
  if(t==10):
   print("Game Draw...!!!")
   break
 if((board[1]=='O' and board[2]=='O' and board[3]=='O')or(board[4]=='O' and board[5]=='O' and board[6]=='O')or (board[7]=='O' and board[8]=='O' and board[9]=='O') or (board[1]=='O' and board[5]=='O' and board[9]=='O') or (board[3]=='O' and board[5]=='O' and board[7]=='O') or (board[1]=='O' and board[4]=='O' and board[7]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O') or (board[3]=='O' and board[6]=='O' and board[9]=='O')):  
  print("Player 2 Won!!!")
  break
 else:
  if(t==10):
   print("Game Draw...!!!")
   break
  
 
 
  


