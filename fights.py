def introFight1():
    print("moves : attack")
    move1 = input("Enter what you will do: ")
    if move1 == "attack":
        print("you damaged the Shadow")
        print("Choose your following move:")
        print("\nmoves : attack")
        move2 = input("Enter what you will do; ")
        if move2 == "attack":
            print("You defeated the shadow.")
            #   continues with the story
        else:
            print("invalid input, the fight will be reset.")
            introFight1()
        
    else:
        print("invalid choice.")
        introFight1()

def introFight2():
    print("\nmoves : attack, block")
    move1 = input("Enter what you will do: ")
    if move1 == "attack":
        print("you damaged the Shadow")
        print("\nmoves : attack, block")
        move2 = input("Enter what you will do: ")
        if move2 == "attack":
            print("You damaged the Shadow")
            print("\nmoves : attack, block")
            move3= input("Enter what you will do: ")
            if move3 == "attack":
                print("You attacked the Shadow and killed it.")
                #   continues with the story
            elif move3 == "block":
                print("You blocked the incoming attack, attack him once to kill it.") 
                print("\nMoves : attack")  
            else:
                print("invalid input, the fight will be reset.")
                introFight2()
        elif move2 == "block":
            print("You blocked the incoming attack")
            print("\nmoves : block, attack")
            move3= input("Enter what you will do: ")
            if move3 == "attack":
                print("You attacked the Shadow and killed it.")
                #   continues with the story
            elif move3 == "block":
                print("You blocked the incoming attack, attack him once to kill it.") 
                print("\nMoves : attack")
                move4 = input("enter what you will do: ")
                if move4 == "attack":
                    print("You damaged the Shadow and killed it!")
                    #   continues with the story
                else:
                    print("Invalid input, the fight will be reset.")
                    introFight2()
            else:
                print("Invalid input, the fight will be reset.")
                introFight2()
        else:
            print("invalid input, the fight will be reset.")
            introFight2()
    elif move1 == "block":
        print("You blocked the incoming attack")
        introFight2()
    else:
        print("invalid input, The fight will be reset")
        introFight2()

def introFight3():
    print("\nmoves : attack, block, magic")
    move1 = input("Enter what you will do: ")
    if move1 == "attack" or move1 == "magic":
        print("you damaged the Shadow")
        print("\nmoves : attack, block, magic")
        move2 = input("Enter what you will do: ")
        if move2 == "attack":
            print("You damaged the Shadow")
            print("\nmoves : attack, block, magic")
            move3= input("Enter what you will do: ")
            if move3 == "attack":
                print("You attacked the Shadow and killed it.")
                #   continues with the story
            elif move3 == "block":
                print("You blocked the incoming attack, attack him once to kill it.") 
                print("\nMoves : attack")  
            else:
                print("invalid input, the fight will be reset.")
                introFight3()
        elif move2 == "block":
            print("You blocked the incoming attack")
            print("\n")
            move3= input("Enter what you will do: ")
            if move3 == "attack":
                print("You attacked the Shadow and killed it.")
                #   continues with the story
            elif move3 == "block":
                print("You blocked the incoming attack, attack it once to kill it.") 
                print("\nMoves : attack")   
            else:
                print("Invalid input, the fight will be reset.")
                introFight3()
        elif move2 == "magic":
            print("You damaged the shadow")
            print("\nmoves : attack, block, magic")
            move3 = input("Enter what you will do: ")
            if move3 == "attack":
                print("you damaged the Shadow and killed it!")
                #   continues with the story
            elif move3 == "block":
                print("you blocked the incoming attack, attack now!")
                print("\nmoves : attack, magic")
                move4 = input("Enter what you will do: ")
                if move4 == "attack" or move4 == "magic":
                    print("You attacked the Shadow and killed it!")
                    #   continues with the story
                else:
                    print("Invalid input, the fight will be reset.")
                    introFight3()
            elif move3 == "magic":
                print("You damaged the shadow")
                print("\nMoves : attack, block, magic")
                move4 == input("Enter what you will do: ")
                if move4 == "attack" or move4 == "magic":
                    print("You damaged the Shadow and killed it!")
                    #   continues with the story
                elif move4 == "block":
                    print("you blocked the attack, attack it once to kill it")
                    print("\nmoves : attack, magic")
                    move5 = input("Enter what you will do: ")
                    if move5 == "attack" or move5 == "magic":
                        print("You damaged the Shadow and killed it")
                        #   continues with the story
                    else:
                        print("Invalid input, the fight will be reset.")
                        introFight3()
                else:
                    print("Invalid input, the fight will be reset.")
                    introFight3()

            else:
                print("Invalid input, the fight will be reset")
                introFight3()
        else:
            print("invalid input, the fight will be reset.")
            introFight3()
    elif move1 == "block":
        print("You blocked the incoming attack")
        introFight3()

def restFights():
    pass


# introFight1()
# introFight2()
introFight3()