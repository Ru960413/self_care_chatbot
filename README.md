# Self care chatbot

#### Video Demo: <https://youtu.be/kfDNm_bembs>

#### Usage:
Download the repository and open it up in your terminal. If you already have Python installed in your computer, cd into the folder and then type "python3 project.py" to run the project. If not, download Python via visiting <https://www.python.org/downloads/>

#### Description:
This is a chat robot which works in user's command line.

It stores a variety of self care ideas, which are categorized in 8 different moods, in a file called data.py. Those moods are: happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed, and excited. In data.py, there's also a list of movie stored.

In project.py, it prompts the user to enter the mood she/he is in and provides user with a self care idea based on user's mood, it then ask the user whether she/he is satisfied with the idea provided or not. If not, then it will provide one more self care idea to user. Afterwards, chatbot ask the user if she/he needs a movie recommendation, and recommends a movie randomly from the downloaded IMDB Top 250 movie list. If not, then the project ends here.