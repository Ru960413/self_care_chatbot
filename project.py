# Goal: build a chatbot with Python, then connect it with Line bot API (and display it using Heroku?)
from data import happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed, excited, movies
import random
import sys

# TODO: add data into SQL database(Cancelled)
# TODO: connect with Line Bot API
    
def greet():
    print("Bot: Hi, there! I'm your self care robot👋 ")
    print("Bot: I'd love to help you with your self care😊 May I know your name? ")
    name = input("You: ")
    print(f"Bot: Hello, {name}! How are you feeling today?") # Question: how to print the conversation using loop?(cancelled)
    print("     (Type in happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed or excited)")



def get_mood():
    moods = ["happy", "overwhelmed", "stressed", "anxious", "sad", "angry", "tired", "depressed", "excited"]
    while True:
        try:
            mood = input("You: ").lower()# How to let user choose what mood they are in?(cancelled)
            if mood == "" or mood not in moods:
                raise ValueError
            else:
                return mood

        except ValueError:
            print("Bot: Please enter one of the emotions listed above")
            if mood in moods:
                return mood
            else:
                continue
            


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


        
# TODO: DONE
def suggest_movie():
    movie = movies[random.randint(0,47)]
    return movie


def main():
    greet()
    mood = get_mood()
    self_care_idea = get_self_care_idea(mood)

    if mood == "happy" or mood == "excited":
        print("Bot: That's awesome!")
        print("Bot: It'll be a good idea to " + self_care_idea + "!")
        print("Bot: Do you like this idea? (Type in Sounds good or try another one)")
    
    elif mood == "overwhelmed":
        print("Bot: Sorry to hear that, it must be tough.")
        print("Bot: How about doing some self care?")
        print("Bot: Perhaps try to " + self_care_idea)
        print("Bot: Do you like this idea? (Type in Sounds good or try another one)")

    elif mood == "stressed" or mood == "anxious" or mood == "sad" or mood == "angry" or mood == "depressed" or mood == "tired":
        print("Bot: Sorry to hear that.")
        print("Bot: Let's do some self care together, shall we?")
        print("Bot: How about " + self_care_idea + "?") # add "Sounds good" or "try another one"
        print("Bot: Do you like this idea? (Type in Sounds good or try another one)")
    reaction = input("You: ").lower()
    if reaction == "sounds good":
        print("Bot: Great!")
    else: 
        self_care_idea = get_self_care_idea(mood)
        print("Bot: How about " + self_care_idea + "?")

    print("Bot: Do you want me to recommend a movie/TV show for you?(Type yes or no)")
    answer = input("You: ").lower()
    if "y" in answer:
        print("Bot: Here is my movie suggestion for you...")
        movie = suggest_movie()
        print("Bot: " + movie)
        print("Bot: Hope you'll like the movie! Bye!")
    else:
        print("Bot: Ok, that's all I have for you today. See you then!")

        
        



if __name__ == "__main__":
    main()