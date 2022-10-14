# Goal: build a chatbot with Python, then connect it with Line bot API (and display it using Heroku?)
from data import happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed, excited, movies
import tkinter as tk
import random

# TODO: add data into SQL database(Cancelled)
# TODO: connect with Line Bot API
# happy = data.happy
# overwhelmed = data.overwhelmed
# stressed = data.stressed
# anxious = data.anxious
# sad = data.sad
# angry = data.angry
# tired = data.tired
# depressed = data.depressed
# excited = data.excited
# movies = data.movies
    


 
def greet_and_get_mood():
    print("Bot: Hi, there! I'm your self care robot👋 ")
    print("Bot: I'd love to help you with your self care😊 May I know your name? ")
    name = input("You: ")
    print(f"Bot: Hello, {name}! How are you feeling today?") # Question: how to print the conversation using loop?(cancelled)
    print("     (Type in happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed or excited)")
    mood = input("You: ").lower()# How to let user choose what mood they are in?
   
    return mood


def get_self_care_idea(mood):
    if mood == "happy":
        self_care_idea = random.choice(happy)
        return self_care_idea
    
    elif mood == "overwhelmed":
        self_care_idea = random.choice(overwhelmed)
        return self_care_idea
    
    elif mood == "stressed":
        self_care_idea = random.choice(stressed)
        return self_care_idea
    
    elif mood == "anxious":
        self_care_idea = random.choice(anxious)
        return self_care_idea
    
    elif mood == "sad":
        self_care_idea = random.choice(sad)
        return self_care_idea

    elif mood == "angry":
        self_care_idea = random.choice(angry)
        return self_care_idea
    
    elif mood == "depressed":
        self_care_idea = random.choice(depressed)
        return self_care_idea

    elif mood == "excited":
        self_care_idea = random.choice(excited)
        return self_care_idea
    
    elif mood == "tired":
        self_care_idea = random.choice(tired)
        return self_care_idea
    else:
        return "Bot: Please type in one of the emotions listed above"


# TODO: DONE
def suggest_movie():
    movie = movies[random.randint(0,47)]
    return "Bot: " + movie


def main():
    mood = greet_and_get_mood()
    self_care_idea = get_self_care_idea(mood)

    if mood == "happy" or mood == "excited":
        print("Bot: That's awesome!")
        print("Bot: It'll be a good idea to " + self_care_idea + "!")

    elif mood == "overwhelmed":
        print("Bot: Sorry to hear that, it must be tough.")
        print("Bot: How about doing some self care?")
        print("Bot: Perhaps try to " + self_care_idea)

    elif mood == "stressed" or mood == "anxious" or mood == "sad" or mood == "angry" or mood == "depressed" or mood == "tired":
        print("Bot: Sorry to hear that.")
        print("Bot: Let's do some self care together, shall we?")
        print("Bot: How about " + self_care_idea + "?") # add "Sounds good" or "try another one"
    else:
        print(get_self_care_idea(mood))

    print("Bot: Do you want me to recommend a movie/TV show for you?(Type yes or no)")
    answer = input("You: ").lower()
    if "y" in answer:
        print("Bot: Here are our movie suggestions for you...")
        # movie = suggest_movie()
        print(suggest_movie())
    else:
        print("Bot: Ok, that's all I have for you today. See you!")

        
        









if __name__ == "__main__":
    main()