def beach_puzzle():
    print("BEACH")
    print("""(Now your standing on the beach and have three options:
'run along the beach'
'go to the small treehut'
'run to the high boards'
'run into the sea'
'talk to Kairi'""")
    keuze = input("What are you gone do?> ")
    if keuze == 'run along the beach':
        print("You run along the beach and find a log")
        beach_puzzle()
    elif keuze == 'go to the small treehut':
        print("You walk to the small threehut")
        print("You'r standing in front of the small treehut")
        keuze2 = input("Go 'in' or 'leave'?> ")
        if keuze2 == 'in':
            print("You enter the small treehouse where you find one cloth")
            print("(After finding the cloth you leave the small threehouse)")
            beach_puzzle()
    elif keuze == 'run to the high boards':
        print("You run to the hight boards")
        print("You find a coil of rope")
        beach_puzzle()
        
def beach_intro2():
    print("????: Hey!")
    print("(They turn to see a silver-haired boy carrying a log)")
    print("""Riku: Aren't you guys forgetting about me? So, I guess I'm the only one 
working on the raft.""")
    print("""(He tosses the log to Sora, who falls over with a yelp, and walks over 
to Kairi)""")
    print("Riku: And you're just as lazy as he is!")
    print("Kairi (giggling): So you noticed. Okay, we'll finish it together.")
    print("""Kairi: So, can you gather the rest of the supplies? Sora, are you listening 
to me?""")
    print("Sora: Yeah, I heard you.")
    print("""Kairi: Okay, here's what you need to go find: One Logs, One Cloth, One 
Rope. Bring everything back here. If you need help, just ask. I'm counting 
on you!""")
    beach_puzzle()#Placeholder

### ???
def beach_intro():
    print("""(You wake up on a bright sandy beach, the sun shines warmly on the same spiky-haired 
boy, who opens his sleepy eyes and sits up. He yawns, starting to lay back 
down again, when suddenly: a girl’s face)""")
    print("????: Whoa!")
    print("""(The boy jumps back up and turns around, kneeling in the sand. The girl 
giggles, hovering over him)""")
    print("????: Gimme a break, Kairi.")
    print("Kairi: Sora, you lazy bum. I knew that I'd find you snoozing down here.")
    print("""Sora: No! This huge, black THING swallowed me up! I couldn't breathe! I couldn't--""")
    print("(She smacks you)")
    response = input("After smacking you in the face what is your response? 'Ow!'/'Why'> ")
    if response == 'Ow!':
        print("Sora: Ow!")
        print("Kairi: Are you still dreaming?")
        print("Sora: It wasn't a dream! Or was it? I don't know.")
        print("(He looks off toward the ocean, seeing the clouds billow in the sky)")
        print("Sora: What was that place? So bizarre...")
        print("Kairi: Yeah, sure.")
        beach_intro2()#Placeholder
    elif response == 'Why':
        print("Sora: Why did you do that?")
        print("Kairi: To see if you are still dreaming?")
        print("Sora: It wasn't a dream! Or was it? I don't know.")
        print("(He looks off toward the ocean, seeing the clouds billow in the sky)")
        print("Sora: What was that place? So bizarre...")
        print("Kairi: Yeah, sure.")
        beach_intro2()#Placeholder
    else:
        print("Please enter a valid input")
        beach_intro()

### ???
def intro_game3():
    print("(You turns around and a large crate and barrel appear.")
    smash = input("Do you 'smash' the crate and barrel or 'leave' them?> ")
    if smash == 'smash':
        print("""(After smashing the items the door opens where there is a flash
of light and the boy wakes up)""")
        beach_intro()#Placeholder
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
    ### Fight with the shadows needs to come here after winning story continues otherwise repeat the fight
    intro_after_fight()#placeholder

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
            intro_game2()#placeholder
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
    print('Welcome to Text-Based Kingdom Hearts!')
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