# Self care chatbot

![Demo photo](demo.png)

## Video Demo: <https://youtu.be/kfDNm_bembs>


## Brief Introduction about the project:  

This is a chatting robot which runs in user's command line.

### Prerequisites:

Python.

Download this repository to your local environment and open it up in your terminal. If you already have Python installed in your computer, just cd into the folder and then type "python3 project.py" to run the project. If not, it is required to download Python via visiting <https://www.python.org/downloads/>

## Description:

It stores a variety of self care ideas, which are categorized in 8 different moods, in a file called data.py. Those moods are: happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed, and excited respectively. Each mood has their own list of self care ideas. In data.py, there's also a list of [IMDB Top 250 movies](https://www.imdb.com/chart/top/?ref_=nv_mv_250) (DictReader were used to read WATCHLIST.csv and append the movie title to the "movies" list ).

In project.py, the first function greet() greets the user and asks the user to enter her/his name, then get_mood() prompts the user to enter the mood she/he is in , which must be one of the eight moods, or it will being viewed as invalid, and it will re-prompt.

If the input is valid, the ChatBot randomly provides user with a self care idea based on user's mood, after that asks the user whether she/he is satisfied with the idea provided or not. If not, it will provide one more self care idea to user.

Following the self care idea suggestion, chatbot asks the user if she/he wants a movie recommendation, and then recommends a movie randomly from the movie list, and then reaches the end of the project. If not, then the project ends without any movie recommendation.

Lastly, test_project.py tests the functions implemented in project.py, using unittest module.

## License

This project is licensed under the MIT License.

## Acknowledgments:

This project is inspired by all the lovely therapists who provide self care tips on instagram!