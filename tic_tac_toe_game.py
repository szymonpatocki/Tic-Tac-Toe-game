def create_game_board():
    for i in range(width):
        index.append([i+1])
    if level != 3:
            print('     '+ str(index))     

    for i in range(length):
            game_board.append(['O']*width)

    for i in range(len(game_board)):
        if level != 3:
            if  i+1<10:
                print(' '+ str([i+1]) + ' '+ str(game_board[i]))
            elif i+1>9:
                print(str([i+1]) + ' '+ str(game_board[i]))
def choose_position():
#Środkowa część planszy
 if 1<n<length and  1<m<width:
    if game_board[n-1][m-1] != '*':
        if  game_board[n-1][m-1] == 'O':    #środkowy
            game_board[n-1][m-1] = 'X'
        else:
            game_board[n-1][m-1] = 'O'

    if game_board[n-2][m-1] != '*':
        if  game_board[n-2][m-1] == 'O':   #góra
            game_board[n-2][m-1] = 'X' 
        else:
            game_board[n-2][m-1] = 'O'    

    if game_board[n][m-1] != '*':
        if  game_board[n][m-1] == 'O':    #dół
            game_board[n][m-1] = 'X'
        else:
            game_board[n][m-1] = 'O'

    if game_board[n-1][m] != '*':
        if  game_board[n-1][m] == 'O':   #prawy
            game_board[n-1][m] = 'X'
        else:
            game_board[n-1][m] = 'O'
  
    if game_board[n-1][m-2] != '*':
        if  game_board[n-1][m-2] == 'O':   #lewy 
            game_board[n-1][m-2] = 'X'
        else:
            game_board[n-1][m-2] = 'O'

#Warunki brzegowe planszy 
 if n == 1 and m == 1:                               #lewy górny
    if game_board[0][0] != '*':
        if  game_board[0][0] == "O":
            game_board[0][0] = "X"
        else:
            game_board[0][0] = "O"

    if game_board[0][1] != '*':
        if  game_board[0][1] == "O":
            game_board[0][1] = "X"
        else:
            game_board[0][1] = "O" 

    if game_board[1][0] != '*':
        if  game_board[1][0] == "O":
            game_board[1][0] = "X"
        else:
            game_board[1][0] = "O"

 if n == length and m == width:                 #prawy dolny
    if game_board[length-1][width-1] != '*':
        if  game_board[length-1][width-1] == "O":
            game_board[length-1][width-1] = "X"
        else:
            game_board[length-1][width-1] = "O"

    if game_board[length-1][width-2] != '*':    
        if  game_board[length-1][width-2] == "O":
            game_board[length-1][width-2] = "X"
        else:
            game_board[length-1][width-2] = "O"

    if game_board[length-2][width-1] != '*':
        if  game_board[length-2][width-1] == "O":
            game_board[length-2][width-1] = "X"
        else:
            game_board[length-2][width-1] = "O"

 if n == 1 and m ==width:                      #prawy górny
    if game_board[0][width-1] != '*':
        if  game_board[0][width-1] == "O":
            game_board[0][width-1] = "X"
        else:
            game_board[0][width-1] = "O"

    if game_board[0][width-2] != '*':        
        if  game_board[0][width-2] == "O":
            game_board[0][width-2] = "X"
        else:
            game_board[0][width-2] = "O"

    if game_board[1][width-1] != '*':
        if  game_board[1][width-1] == "O":
            game_board[1][width-1] = "X"
        else:
            game_board[1][width-1] = "O"

 if n == length and m == 1:                    #lewy dolny
    if game_board[length-1][0] != '*':
        if  game_board[length-1][0] == "O":
            game_board[length-1][0] = "X"
        else:
            game_board[length-1][0] = "O"

    if game_board[length-1][1] != '*':
        if  game_board[length-1][1] == "O":
            game_board[length-1][1] = "X"
        else:
            game_board[length-1][1] = "O"

    if game_board[length-2][0] != '*':
        if  game_board[length-2][0] == "O":
            game_board[length-2][0] = "X"
        else:
            game_board[length-2][0] = "O"

#Górna krawędź planszy
 if n == 1 and 1<m<width:
    if game_board[n-1][m-1] != '*':
        if  game_board[n-1][m-1] == 'O':    #środkowy
            game_board[n-1][m-1] = 'X'
        else:
            game_board[n-1][m-1] = 'O'

    if game_board[n-1][m] != '*':
        if  game_board[n-1][m] == 'O':      #prawy
            game_board[n-1][m] = 'X'
        else:
            game_board[n-1][m] = 'O'  

    if game_board[n-1][m-2] != '*':
        if  game_board[n-1][m-2] == 'O':    #lewy
            game_board[n-1][m-2] = 'X'
        else:
            game_board[n-1][m-2] = 'O'

    if game_board[n][m-1] != '*':
        if  game_board[n][m-1] == 'O':      #dół
            game_board[n][m-1] = 'X'
        else:
            game_board[n][m-1] = 'O'

#Dolna krawędź planszy
 if n ==length and 1<m<width:
    if game_board[n-1][m-1] != '*':
        if  game_board[n-1][m-1] == 'O':   #środkowy
            game_board[n-1][m-1] = 'X'
        else:
            game_board[n-1][m-1] = 'O'
    
    if game_board[n-1][m-2] != '*':
        if  game_board[n-1][m-2] == 'O':  #lewy
            game_board[n-1][m-2] = 'X'
        else:
            game_board[n-1][m-2] = 'O'  

    if game_board[n-2][m-1] != '*':
        if  game_board[n-2][m-1] == 'O':  #góra
            game_board[n-2][m-1] = 'X' 
        else:
            game_board[n-2][m-1] = 'O'  

    if game_board[n-1][m] != '*':
        if  game_board[n-1][m] == 'O':  #prawy
            game_board[n-1][m] = 'X'
        else:
            game_board[n-1][m] = 'O'
            
#Lewa krawędź planszy
 if 1<n<length and m == 1:
    if game_board[n-1][m-1] != '*':
        if  game_board[n-1][m-1] == 'O':  #środkowy
            game_board[n-1][m-1] = 'X'
        else:
            game_board[n-1][m-1] = 'O'

    if game_board[n-2][m-1] != '*':
        if  game_board[n-2][m-1] == 'O':  #góra
            game_board[n-2][m-1] = 'X' 
        else:
            game_board[n-2][m-1] = 'O'    

    if game_board[n][m-1] != '*':
        if  game_board[n][m-1] == 'O':   #dół
            game_board[n][m-1] = 'X'
        else:
            game_board[n][m-1] = 'O'

    if game_board[n-1][m] != '*':
        if  game_board[n-1][m] == 'O':  #prawy
            game_board[n-1][m] = 'X'
        else:
            game_board[n-1][m] = 'O'
    
#Prawa krawędź planszy
 if 1<n<length and m ==width:
    if game_board[n-1][m-1] != '*':
        if  game_board[n-1][m-1] == 'O':  #środkowy
            game_board[n-1][m-1] = 'X'
        else:
            game_board[n-1][m-1] = 'O'
  
    if game_board[n-2][m-1] != '*':
        if  game_board[n-2][m-1] == 'O':  #góra
            game_board[n-2][m-1] = 'X' 
        else:
            game_board[n-2][m-1] = 'O'  

    if game_board[n][m-1] != '*':
        if  game_board[n][m-1] == 'O':   #dół
            game_board[n][m-1] = 'X'
        else:
            game_board[n][m-1] = 'O'

    if game_board[n-1][m-2] != '*':
        if  game_board[n-1][m-2] == 'O': #lewy
            game_board[n-1][m-2] = 'X'
        else:
            game_board[n][m-2] = 'O'  
def forbidden_position():
    import random
    random_length = random.randrange(1,length+1)
    random_width = random.randrange(1,width+1)
    game_board[random_length-1][random_width-1] = "*"
    
game_board = []
index = []
width = -1
length = -1
forbidden = -1
step = 0
amount_of_X = 0
amount_of_forbidden = 0
choice=0

print("Gra rozpoczęta!")
while choice != 5:
    print("\nWybierz poziom trundności: ")
    print("1. Normalny")                #Żadnych utrudnień
    print("2. Średni")                  #większa plansza
    print("3. Trudny")                  #zakazane pozycje 
    print("4. Stwórz własną plansze")   #Uytkownik sam tworzy plansze
    level = int(input())
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("5. Potwierdź")
    print("6. Cofnij")
    choice=int(input())
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

if level ==1:
    width = 4
    length = 4
    create_game_board()

elif level ==2:
    width = 8
    length = 8
    create_game_board()

elif level ==3:
    width = 8
    length = 8
    create_game_board()

    #Uzupełnanie planszy niędostępnymi polami
    while amount_of_forbidden != 10:
        forbidden_position()
        amount_of_forbidden = 0
        for i in range(0,length,1):
            for j in range(0,width,1):
                if game_board[i][j] == "*":
                    amount_of_forbidden = amount_of_forbidden + 1

    print('     '+ str(index))
    for i in range(len(game_board)): 
        if i+1<10:
            print(' '+ str([i+1]) + ' '+ str(game_board[i]))
        elif i+1>9:
            print(str([i+1]) + ' '+ str(game_board[i]))  

elif level ==4:
    #Wybór szerokości planszy
    while width<0:
        try:
            width = int(input("Podaj szerokość planszy: ")) 
        except ValueError:  
            print("\nSzerokość planszy musi być liczbą dodatnią!") 

    #Wybró długości planszy
    while length<0:     
        try:
            length = int(input("Podaj długość planszy: "))
        except ValueError: 
            print("\nDługość planszy musi być liczbą dodatni!")

    create_game_board()
    print("")

    #Wybór liczby niedostępnych pól
    while forbidden<0:
        try:
            forbidden = int(input("Podaj ilość zakazanych pozycji na planszy: "))
        except ValueError:  
            print("\nIlość zakazanych pozycji na planszy musi być liczbą dodatnią!") 

    #Uzupełnanie planszy niędostępnymi polami 
    while amount_of_forbidden != forbidden:
        forbidden_position()
        amount_of_forbidden = 0
        for i in range(0,length,1):
            for j in range(0,width,1):
                if game_board[i][j] == "*":
                    amount_of_forbidden = amount_of_forbidden + 1

    #Wyświetlanie planszy
    print('     '+ str(index))
    for i in range(len(game_board)): 
        if i+1<10:
            print(' '+ str([i+1]) + ' '+ str(game_board[i]))
        elif i+1>9:
            print(str([i+1]) + ' '+ str(game_board[i]))

#Blok opisujący logię gry
while amount_of_X != length*width - amount_of_forbidden:

    n = -1
    m = -1

    #Wybór wiersza 
    while n<0:
        try:
            n= int(input("Podaj numer wierszu z zakresu planszy: "))
        except:
            print("\nNumer wierszu musi być liczbą dodatnią!") 

    while n>length:
        try:
            n= int(input("Podaj numer wierszu z zakresu planszy: "))
        except:
            print("\nNumer wierszu musi być liczbą dodatnią!") 

    #Wybór kolumny        
    while m<0: 
        try:   
            m= int(input("Podaj numer kolumny z zakresu planszy: "))
        except:
            print("\nNumer kolumny musi być liczbą dodatanią!") 

    while m>width:
        try:   
            m= int(input("Podaj numer kolumny z zakresu planszy: "))
        except:
            print("\nNumer kolumny musi być liczbą dodatanią!") 
 
    step = step + 1
    amount_of_X = 0
    amount_of_forbidden = 0
    choose_position()

    #Zlicznie liczby X na planszy
    for i in range(0,length,1):
        for j in range(0,width,1):
            if game_board[i][j] == "X":
                 amount_of_X = amount_of_X + 1

    #Zlicznie liczby niedostępnych pól na planszy
    for i in range(0,length,1):
        for j in range(0,width,1):
            if game_board[i][j] == "*":
                 amount_of_forbidden = amount_of_forbidden + 1

    #Wyświetlanie planszy do gry
    print('     '+ str(index))
    for i in range(len(game_board)): 
        if i+1<10:
            print(' '+ str([i+1]) + ' '+ str(game_board[i]))
        elif i+1>9:
            print(str([i+1]) + ' '+ str(game_board[i]))

    #Wyświetlanie liczby X na planszy oraz wykoanynych ruchów
    print("Ilość X na planszy: " + str(amount_of_X)+"/"+ str(length*width - amount_of_forbidden))
    print("Ilość ruchów: " + str(step))
    
 #Warunek konieczny do wygrania gry
if amount_of_X == length*width - amount_of_forbidden:
     print("Wygrałeś")
        

