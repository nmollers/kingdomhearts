import os
#Fight systems
def introFight1():
    print("moves : attack")
    move1 = input("Enter what you will do: ")
    if move1 == "attack":
        print("you damaged the Shadow")
        print("Choose your following move:")
        print("\nmoves : attack")
        move2 = input("Enter what you will do?> ")
        if move2 == "attack":
            print("You defeated the shadow.")
            intro_after_fight()
        else:
            print("invalid input, the fight will be reset.")
            introFight1()        
    else:
        print("invalid choice.")
        introFight1()

def introFight2():
    print("\nmoves : attack, block")
    move1 = input("Enter what you will do?> ")
    if move1 == "attack":
        print("you damaged the Shadow")
        print("\nmoves : attack, block")
        move2 = input("Enter what you will do?> ")
        if move2 == "attack":
            print("You damaged the Shadow")
            print("\nmoves : attack, block")
            move3= input("Enter what you will do?> ")
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
    move1 = input("Enter what you will do?> ")
    if move1 == "attack" or move1 == "magic":
        print("you damaged the Shadow")
        print("\nmoves : attack, block, magic")
        move2 = input("Enter what you will do?> ")
        if move2 == "attack":
            print("You damaged the Shadow")
            print("\nmoves : attack, block, magic")
            move3= input("Enter what you will do?> ")
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
            move3 = input("Enter what you will do?> ")
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
#End Fight Systems

def toy_factory():
    os.system('cls')
    print("""(They run to the second floor
Wrapping Room and find Lock, Shock, and Barrel in amongst the toys)""")
    print("Shock: No!")
    print("(Lock tosses away a sailboat. Barrel looks at a stuffed bear)")
    print("Barrel: This looks good.")
    print("Shock: No!")
    print("Lock: Boooring!")
    print("(Barrel tosses the bear away)")
    print("Lock: This one?")
    print("Shock: No!")
    print("Barrel: No way!")
    print("Donald: Hey!")
    print("(The three miscreants look up and see them)")
    print('Sora: So YOU three took them!')
    print("Shock: Took what?")
    print("""Jack: You stole the presents, didn't you!""")
    print("Lock: It wasn't us!")
    print("Barrel: But...")
    print("Shock (taking off her mask): It really sounds like fun!")
    print("(She puts her mask back on and they start to run away)")
    print("Lock, Shock, & Barrel: Run for it!")
    print("(Sora quickly locks the kids in boxes, then interrogates them)")
    print("Sora: Where'd you put the presents?")
    print("Shock: We told you! We don't have 'em!")
    print("Donald: Then why are you in here!?")
    print("Lock: We're looking for parts for the experiment.")
    print("Jack: Experiment?")
    print("Lock: Dr. Finkelstein's making us a friend!")
    print("Barrel: One we get to boss around!")
    print("Jack: It's true the doctor's been hard at work making SOMETHING lately...")
    print("""Lock: Besides, Christmas presents are boring. Not scary or gross... So what
good are they?""")
    print("Barrel: Yeah!")
    print("Lock: There's nothing fun here. Let's go back to Halloween Town!")

def inside_santa_home():
    os.system('cls')
    print("(They walk in santa's house")
    print("Santa: Oh!")
    print("(They place them on the table)")
    print("Santa: Wherever did you find these?")
    print("(He takes the present from Jack's hands)")
    print("Jack: In Halloween Town. You'll be needing them for Christmas, right, Sandy?")
    print("""Santa: Of course. But these are just a few of the Christmas presents that were
stolen.""")
    print("Sora: Stolen!?")
    print("(They look at Jack, who scratches his head)")
    print("Jack: Oh, Sandy... You don't think it was ME?")
    print("Santa: Still wearing the outfit, I see.")
    print("""Jack: I just thought I'd dress for the occasion. But if you don't believe me,
then we'll just have to find out who really did it!""")
    print("Santa: Very well, I'll leave it to you.")
    print("Jack: All right, Sora, Donald, Goofy! We're off!")
    print("""(He points to the door and starts to leave. Sora, Donald, and Goofy slump in
defeat. They hear a crash from the Toy Factory.)""")
    keuze1 = input("Run to the Toy Factory?> ")
    if keuze1 == 'yes':
        toy_factory()
    elif keuze1 == 'no':
        toy_factory()
    else:
        inside_santa_home()

def snow_world_intro():
    print("(After waking up you wake up in the middle of a snow world)")
    print("(Jack, still in his Sandy Claws outfit, is picking you up)")
    print("""Jack: Perfect timing, gentlemen! Lend me a hand, won't you? These presents must
belong to Sandy Claws. So I thought I'd better return them.""")
    print("Sora (crossing his arms): You just happened to find them?")
    print("Jack: Of course, Sora. I'm finished with Christmas fantasies. You know that.")
    print("Sora: But...You thought you'd hold on to the suit?")
    print("""Jack: What, this? It's just a costume. And Sally worked so very hard making it!
Come on. We've got work to do!""")
    print("(They walk to Santa's House with the presents)")
    keuze1 = input("Want to go in the house of Santa or search around his house?> ")
    if keuze1 == 'go in':
        inside_santa_home()
    elif keuze1 == 'search':
        print("You find a christmas tree with some presents underneath it")
        keuze2 = input("Want to open the presents?> ")
        if keuze2 == 'yes':
            print("You found a potion in a present")
            #Add potion to inventory
            inside_santa_home()
        elif keuze2 == 'no':
            print("You decid to leave the presents")
            inside_santa_home()

def intro_game3():
    print("(You turns around and a large crate and barrel appear.")
    smash = input("Do you 'smash' the crate and barrel or 'leave' them?> ")
    if smash == 'smash':
        print("""(After smashing the items the door opens where there is a flash
of light and the boy wakes up)""")
        snow_world_intro()
    elif smash == 'leave':
        print('There is nothing to do smash the items!')
        intro_game3()
    else:
        print("Please enter a valid input")
        intro_game3()

### After winning the first fight story goes further here
def intro_after_fight():
    print("""(The boy defeats all of the Shadows. A black void appears in the center of 
the platform and he is sucked into it. He bats the darkness away and wakes 
up on a multicolored platform with three silhouettes. He sees a door near 
the platform edge)""")
    print("Will you examin to the door or explor the multicolored platform?")
    choise = input("Make your choise between 'examin' and 'explor'> ")
    if choise == 'examin':
        print("????: I can't open it...")
        intro_after_fight()
    elif choise == 'explor':
        print("(A christmas tree with presents appears)")
        print("Wil you open the present's or leave them there?")
        open = input("'open' or 'leave' the presents?> ")
        if open == 'open':
            print("You opend the presents and find a potion")
            #Potion added to inventory
            intro_game3()#placeholder
        elif open == 'leave':
            print("You decided to leave the presents")
            intro_game3()
        else:
            print("Please enter a valid input")
            intro_after_fight()
    else:
        print("Please enter a valid input")
        intro_after_fight()

### First fight after making the first choise
def intro_game2():
    os.system('cls')
    print("""(The three stones suddenly sink into the floor, knocking the boy back 
onto the platform. The ground rumbles and he looks around. The edges 
of the platform crumble off and the platform shatters. The boy falls 
through darkness and lands on another platform, this time depicting a 
girl in a beautiful silver ball gown. The staff appears in his hand)""")
    print("Voice: You gained the power to fight.")
    print("(He slashes at the air)")
    print("""Voice: All right! You've got it. Use this power to protect yourself and 
others.""")
    print("(Shadows appear)")
    print("Voice: There will be times you have to fight. Keep your light burning strong.")
    introFight1()

### First choise of the player that change the player stats
def choises_intro_game():
    choise = input("Choose between the 'shield', 'blue staff' and 'sword'.> ")
    if choise == 'shield':
        print("(The boy runs over to the shield and holds it in his hands)")
        confurm = input("""Voice: The power of the guardian. Kidness to aid friends. A shield to 
repel all. Is this the power you seek?> """)
        if confurm == 'yes':
            print("(Suddenly, the shield vanished from his hand)")
            intro_game2()
        elif confurm == 'no':
            choises_intro_game()
        else:
            print("Please enter a valid input")
            choises_intro_game()
    elif choise == 'blue staff':
        print("(The boy runs over to the shield and holds it in his hands)")
        confurm = input("""Voice: The power of the mystic. Inner strength. A staff of wonder and 
ruin. Is this the power you seek?> """)
        if confurm == 'yes':
            print("(Suddenly, the staff vanished from his hand)")
            intro_game2()
        elif confurm == 'no':
            choises_intro_game()
        else:
            print("Please enter a valid input")
            choises_intro_game()
    elif choise == 'sword':
        confurm = input("""Voice: The power of the warrior. Invincible courage. A sword of terrible 
destruction. Is this the power you seek?> """)
        if confurm == 'yes':
            print("(Suddenly, the sword disappeared)")
            intro_game2()
        elif confurm == 'no':
            choises_intro_game()
        else:
            print("Please enter a valid input")
            choises_intro_game()

### Game intro
def intro_game():
    os.system('cls')
    print("""(The clouds part and the words rush the screen. A boy awakes, floating 
in a strange abyss, the keychain around his neck waving in the current 
of wind blowing upwards. Gold letters appear in the void)""")
    print("""????: I've been having these weird thoughts lately... Like, is any of this 
for real or not?""")
    print("""(The words fade away. The boy's heart pumps as he falls deeper into the 
abyss, his eyes closed. The empty nothingness becomes water, and bubbles 
form in the wake of his descent. He reaches a barrier and his eyes blink 
open with a flash. He finds himself standing on a sandy beach on a clear 
sunny day. He looks around and sees another boy in the water. Holding his 
hand up to block the glare of the sun, he steps toward the boy in the water 
to get a closer look. Suddenly, the ocean waters recede. He looks up and 
gasps. The boy in the water, turns his head, the breeze billowing through 
his silver hair, as a wave forms beyond. He smirks, holding his hand out 
as the wave reaches its pinnacle behind him. The boy with brown hair runs 
toward the boy in the water, who isn't moving. Time seems to slow down as 
the wave crashes down on top of them. The first boy spins in the water, 
gritting his teeth. He rights himself and stares at the other boy, who is 
unfazed, saying nothing with his arm beckoning. The first boy tries to 
reach him, but is swept away with the current. He eventually surfaces, 
gasping for air, the water dripping off of him as the sun hangs low in 
the sky. He sees a girl on the shore waving to him and calling his name. 
He waves back and starts padding towards shore as she bounces happily on 
her feet. The girl stands with her hands behind her back as he arrives. He 
bends down slightly, catching his breath and smirks up at her. She giggles 
until something in the sky catches her attention, her face forming a 
serious look. He stands up and turns around. A meteor shower rains down 
from the sky, a shadowy figure among them. They stare in awe, and the 
boy realizes the figure is himself. He gasps and feels himself falling. 
He becomes the figure in the sky as he falls below the girl, reaching out 
to her. She reaches out to him until the image of her ripples in water 
reflecting the sky. The boy falls back, eyes closed, sinking deeper as 
bubbles trail him. He stirs awake and manages to right himself before 
settling onto a dark platform. He looks around and takes a step forward. 
There is a flash of blinding light as a large flock of birds rise from 
the platform, flying in all directions and scattering feathers everywhere. 
The boy shields his eyes as the wind whips at him. He watches them leave 
while the last feathers fall. The platform now depicts a girl taking a 
bite out of an apple. The boy turns around seeing no one, yet hearing a voice)""")
    print("""Voice: So much to do, so little time... Take your time. Don't be afraid. 
The door is still shut. Now, step forward. Can you do it?""")
    print("""(The boy takes a few slow steps forward. A light shines down from above 
as a large stone pedestal rises from the platform in a shower of light 
and magic. The boy turns toward it. A red shield blinks into existence, 
floating above it)""")
    print("Voice: Power sleeps within you...")
    print("""(Another pedestal rises from the platform, a blue staff floating above 
it. He turns around to face it)""")
    print("Voice: If you give it form...")
    print("""(A third pedestal appears in front of the boy, who turns toward it. A metal 
sword appears in midair)""")
    print("Voice: It will give you strength.")
    print("(The boy stares ahead at all three)")
    print("Voice: Choose well.")
    choises_intro_game()
            
### Intro if the player want's to start the game or get some help ###
def intro_kingdomhearts():
    os.system('cls')
    print('Welcome to Text-Based Kingdom Hearts Pre-Alpha!') 
    keuze1 = input("Do you wan't to start playing the game, quit or do you want some help?> ")
    if keuze1 == 'play':
        intro_game()    
    elif keuze1 == 'help':
        print("---")
        intro_kingdomhearts()
    elif keuze1 == 'quit':
        quit
    else:
        print('Please make a valid choise')
        keuze1 = input("Do you wan't to start paying the game or do you want some help?> ")

intro_kingdomhearts()