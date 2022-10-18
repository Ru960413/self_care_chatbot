# Question: How to test random? using unittest.mock.patch

from project import get_mood, get_self_care_idea, suggest_movie
from data import happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed, excited, movies
import random
import pytest
from unittest.mock import patch


def test_get_mood():
    with patch("builtins.input", return_value="happy"):
        assert get_mood() == "happy"
    


# using unittest.mock.patch to insert my version of random to return a known value when running test
def test_get_self_care_idea():
    # pass in a lambda function into side effect so that the third element will be chose
    with patch("random.choice", side_effect=lambda seq: seq[3]) as mock_random:
        choice = get_self_care_idea("happy")
        assert choice == "do some workout to feel more alive"

    with patch("random.choice", side_effect=lambda seq: seq[5]) as mock_random:
        choice = get_self_care_idea("sad")
        assert choice == "cuddle with your animal"


        
def test_suggest_movie():
    # patch the function so that it'd choose the 0th index of element form the movie list
    with patch("random.randint", return_value=0) as mock_random:
        movie = suggest_movie()
        assert movie == "Eternal Sunshine of the Spotless Mind"

        

# Reference 1: https://stackoverflow.com/questions/18463173/can-i-patch-random-using-unittest-mock-patch
# Reference 2: https://realpython.com/lessons/what-side-effect/
# What is a Side Effect?
# A side effect of a function is something that happens—for example, printing to standard output, making a request to a web server, raising an exception—something beyond just the return value can be considered a side effect of a function.