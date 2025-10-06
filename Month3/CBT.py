score = 0 
while True:
    print("1. What is 2 + 2?\n a) 3\n b) 4\n c) 5\n d) 6")
    choice1 = input("Enter an option from a to d: ")
    if choice1 == 'b':
        score += 20
    else:
        score += 0

    
    print("\n2. What color is the sky on a clear day?\n a) Red\n b) Blue c) Green\n d) Yellow")
    choice2 = input("Enter an option from a to d: ")

    if choice2 == 'b':
        score += 20
    else:
        score += 0
    
    print("\n3. How many legs does a spider have?\n a) 6\n b) 7\n c) 8\n d) 9")
    choice3 = input("Enter an option from a to d: ")
    if choice3 == 'c':
        score += 20
    else:
        score += 0


    print("\n4. What sound does a cow make?\n a) Meow\n b) Bark\n c) Moo\n d) Quack")
    choice4 = input("Enter an option from a to d: ")
    if choice4 == 'c':
        score += 20
    else:
        score += 0

    print("\n5. What is the opposite of 'hot'?\n a) Warm\n b) Cold\n c) Cool\n d) Boiling")
    choice5 = input("Enter an option from a to d: ") 
    if choice5 == 'b':
        score += 20
    else:
        score += 0
        print(f'\nAt the end of the CBT exam, you scored {score} points.')
        break


    # 
    # 
    # 
    # 
    


    
    
    
    
    
    
    
    
    
    
    
    
