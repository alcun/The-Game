print("Hello there. Welcome to The-Game. I hope you are sitting comfortably.")

name = input("What name do you go by? ")
age = int(input("A strong name. And for how many years have you existed? "))



print("Greetings", name,"- it's a pleasure to meet you.", "I see that you are", age, "years old.")

health = 10

print("And of the vigourous type too! I see you have a whole", health, "health")

if age >= 18:
  print("Many fine years. You are old enough to play.")
  
  wants_to_play = input("That is, if you want to play of course? ").lower()
  if wants_to_play =="yes":
    print("Jolly good! Let us continue.")
    
    print("You wake up. You were dreaming.")

    wants_to_sleep = input("Go back to sleep? ") .lower()
    if wants_to_sleep == "no":
     ans = input("You've slept enough. You get up from a firm bed and feel about a dark room for a door handle. The door is a ajar, do you open or close it? ")

     if ans == "open":
       print("The heavy wooden door swings on its hinges and you step out into a corridor flickering in dim candle light.")
     elif ans == "close":
       print("You slam the door forcefully and a spider falls down the back of your shirt. Yuck! It bites you for 5 health. You, in turn, stamp it into a paste. You hear the scurrying of hundreds more and quickly open the door and scarper into the dim candle lit corridor.")
       health -= 5
       print("Your health is now", health, "- act accordingly!")

       left_or_right = input("You look about. Down the hall to your right is a window open with its blinds flapping in the breeze. To the left you hear a murmur of voices and footsteps. Which way do you head? ")       
       if ans == "right":
        print("You hurry towards the window, getting a good run up before flinging yourself through.")
       else:
        print("In an act of curiosity, bravery or foolhardiness (take your picK) you walk towards the voices. 'Oi!' You are clobbered on the noggin. Lights out.")

      
  

    
    



    else:
     print("You close your eyes and go back to sleep... ") 

elif age >= 14:
  print("This game is not for the faint hearted. You may continue only with the supervision of a trusted guardian.")
else: print("I admire your efforts young whippersnapper! Come back when you are a little longer in the tooth.")


delay = 5



'''
string "hello", "hi"

int 8, 2, 48, 3200

float 37.5, 6.0, 54.2

bool True, False
'''

'''

if health<= 0:
  print("You now have 0 health and you lost the game...")
else:
 print("You win!")
'''

'''
demonstrates python branching paths, nesting, if/else, running var health mechanics