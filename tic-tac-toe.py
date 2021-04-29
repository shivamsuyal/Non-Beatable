import time,random,sys
aii=''
ai1_move=0

class Error(Exception):
    pass

class Playererror(Error):
  pass
  
class aierror(Error):
  pass
  
class draw(Error):
  pass

d1={'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
d2={}
theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

d={'n1': 0, 'n2': 0, 'n3': 0, 'n4': 0, 'n5': 0, 'n6': 0, 'n7': 0, 'n8': 0, 'n9': 0}

lis=[1,2,3,4,5,6,7,8,9]

def printBoard(board):
 
 print('      '+'--------+------+--------')
 print('      '+'||'+'      '+'|'+'      '+'|'+'      '+'||')
 print('      '+'||'+'   '+board['1']+'  ' + '|' +'   '+ board['2']+'  ' + '|' + '   '+board['3']+'  '+'||')
 print('      '+'||'+'      '+'|'+'      '+'|'+'      '+'||')
 

 print('      '+'--------+------+--------')
 print('      '+'||'+'      '+'|'+'      '+'|'+'      '+'||')

 print('      '+'||'+'   '+board['4']+'  ' + '|' + '   '+board['5'] +'  '+ '|' +'   '+ board['6']+'  '+'||')
 print('      '+'||'+'      '+'|'+'      '+'|'+'      '+'||')

 print('      '+'--------+------+--------')
 print('      '+'||'+'      '+'|'+'      '+'|'+'      '+'||')
 
 print('      '+'||'+'   '+board['7']+'  ' + '|' +'   '+ board['8']+'  ' + '|' +'   '+ board['9']+'  '+'||')
 print('      '+'||'+'      '+'|'+'      '+'|'+'      '+'||')
 print('      '+'--------+------+--------')

def typeit(mes,t):
  for i in mes:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(t)
  
def ai1():
  global move,ai1_move
  ai1_move=0
  if ((d['n2']+d['n3']==8) | (d['n5']+d['n9']==8) | (d['n4']+d['n7']==8)) and (1 in lis):
    move=1
    ai1_move=1
  elif ((d['n3']+d['n1']==8) | (d['n5']+d['n8']==8)) and (2 in lis):
    move=2
    ai1_move=1
  elif ((d['n2']+d['n1']==8) | (d['n5']+d['n7']==8) | (d['n9']+d['n6']==2)) and (3 in lis):
    move=3
    ai1_move=1
  elif ((d['n7']+d['n1']==8) | (d['n5']+d['n6']==8)) and (4 in lis):
    move=4
    ai1_move=1
  elif ((d['n2']+d['n8']==8) | (d['n4']+d['n6']==8) | (d['n9']+d['n1']==2) | (d['n7']+d['n3']==2)) and (5 in lis):
    move=5  
    ai1_move=1
  elif ((d['n5']+d['n4']==8) | (d['n9']+d['n3']==8)) and (6 in lis):
    move=6
    ai1_move=1
  elif ((d['n4']+d['n1']==8) | (d['n5']+d['n3']==8) | (d['n9']+d['n8']==2)) and (7 in lis):
    move=7
    ai1_move=1
  elif ((d['n2']+d['n5']==8) | (d['n9']+d['n7']==8)) and (8 in lis):
    move=8
    ai1_move=1
  elif ((d['n5']+d['n1']==8) | (d['n8']+d['n7']==8) | (d['n3']+d['n6']==2)) and (9 in lis):
    move=9
    ai1_move=1
    


def ai2 ():
  global move
  
  if ((d['n2']+d['n3']==2) | (d['n5']+d['n9']==2) | (d['n4']+d['n7']==2)) and (1 in lis):
    move=1
    
  
  elif ((d['n3']+d['n1']==2) | (d['n5']+d['n8']==2)) and (2 in lis):
    move=2
    
  
  elif ((d['n2']+d['n1']==2) | (d['n5']+d['n7']==2) | (d['n9']+d['n6']==2)) and (3 in lis):
    move=3
    
  
  elif ((d['n7']+d['n1']==2) | (d['n5']+d['n6']==2)) and (4 in lis):
    move=4
    
  
  elif ((d['n2']+d['n8']==2) | (d['n4']+d['n6']==2) | (d['n9']+d['n1']==2) | (d['n7']+d['n3']==2)) and (5 in lis):
    move=5  
    
  
  elif ((d['n5']+d['n4']==2) | (d['n9']+d['n3']==2)) and (6 in lis):
    move=6
    
  
  elif ((d['n4']+d['n1']==2) | (d['n5']+d['n3']==2) | (d['n9']+d['n8']==2)) and (7 in lis):
    move=7
    
  
  elif ((d['n2']+d['n5']==2) | (d['n9']+d['n7']==2)) and (8 in lis):
    move=8
    
  
  elif ((d['n5']+d['n1']==2) | (d['n8']+d['n7']==2) | (d['n3']+d['n6']==2)) and (9 in lis):
    move=9
    
  else:
    l=random.choice(range(len(lis)-1))
    move=lis[l]

def win():
  k1= d['n1']+d['n2']+d['n3']
  k2= d['n4']+d['n5']+d['n6']
  k3= d['n7']+d['n8']+d['n9'] 
  k4= d['n1']+d['n4']+d['n7'] 
  k5= d['n2']+d['n5']+d['n8'] 
  k6= d['n3']+d['n6']+d['n9'] 
  k7= d['n1']+d['n5']+d['n9'] 
  k8= d['n3']+d['n5']+d['n7'] 
  
  ddd=[k1,k2,k3,k4,k5,k6,k7,k8]
  if 3 in ddd:
    raise Playererror
  else:
    pass
    
def win2():
  global aii
  k1= d['n1']+d['n2']+d['n3']
  k2= d['n4']+d['n5']+d['n6']
  k3= d['n7']+d['n8']+d['n9'] 
  k4= d['n1']+d['n4']+d['n7'] 
  k5= d['n2']+d['n5']+d['n8'] 
  k6= d['n3']+d['n6']+d['n9'] 
  k7= d['n1']+d['n5']+d['n9'] 
  k8= d['n3']+d['n5']+d['n7'] 
  
  ddd=[k1,k2,k3,k4,k5,k6,k7,k8]
  if 12 in ddd:
    aii='win'
  else:
    pass

def play():
           try:
            global lis,move,theBoard,d1,aii,ai1_move
            
            print('Turn for ' + 'X' + '. Move on which space?')
            move = str(input())
            while theBoard[move]!=' ':
              printBoard(theBoard)
              print('\n','The place had already been aquried')
              print('Type something new')
              move = str(input())
            
            theBoard[move] = 'X'
            d['n'+move] = 1
            lis.pop(lis.index(int(move)))
            d1[move] = 'O'
            win()
            
            ai1()
            if ai1_move==0:
                ai2()
            print('Computer marked ')
            theBoard[str(move)] = 'O'
            d['n'+str(move)] = 4
            d2[str(move)]='X'
            lis.pop(lis.index(move))
            win2()
            if len(lis)==0:
              raise draw
            else:
              pass
          
              
            print('\n','~'*30,'\n')
            printBoard(theBoard)
            if aii=='win':
              raise aierror
            else:
              pass
           except KeyError:
              printBoard(theBoard)
              print('This Letters is not allowed')
              
              play()
              
printBoard(theBoard)
while True:  
 try:
            play()
              
 except Playererror:
   typeit("The end\n\n\nYOU W",0.2)
   print('O'*209)
   time.sleep(2)
   typeit('Game crashed\n',0.1)
   time.sleep(1)
   typeit('reopening the game\n',0.1)
   time.sleep(1)
   typeit('retriving the data\n',0.1)
   time.sleep(1)
   typeit('showing result\n',0.1)
   time.sleep(2)
   d1.update(d2)
   print('\033c')
   printBoard(d1)
   time.sleep(0.9)
   print('    You lost from a brainless machine   hahaha ')
   break
 except aierror:
   print('    You lost from a brainless machine    hahahahahahahahaha       ')
   break
 except KeyError:
   print('Letters not allowed')
   play()
 except draw:
   print('No one won')
   break
 except:
  print('Game Over')
  break
