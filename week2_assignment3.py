# let the user know what's going on
print ("Welcome to Paula's story!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
yourName1 = raw_input("What's your name?: ")
adjective1 = raw_input("Enter an adjective: ")
transport1 = raw_input("Name a transportation: ")
place1 = raw_input("Name a place you go often: ")
famousPerson1 = raw_input("A famous person you really like: ")
object1 = raw_input("What's your favorite object: ")
verb1 = raw_input("Enter a verb on past tense: ")
adjective2 = raw_input("Enter one more adjective: ")

# this is the story. it is made up of strings and variables.
story = "It was a " + adjective1 + " day " + ". " + yourName1 + " took the " + transport1 + " to " + place1 + ". " \
"" + yourName1 + " lost her/his " + object1 + " in her/his way to " + place1 + ". " \
"" + famousPerson1 + " found " + yourName1 + "'s " + object1 + " and followed her/him to " + place1 + " to give it/them back to her/him. " \
"When they met for the first time, they " + verb1 + ". " \
"" + yourName1 + " was very " + adjective2 + " to get her/his " + object1 + " back. " \


# finally we print the story
print (story)