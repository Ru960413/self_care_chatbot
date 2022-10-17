# Question: How to test random?
from project import get_mood, get_self_care_idea, suggest_movie
from data import happy, overwhelmed, stressed, anxious, sad, angry, tired, depressed, excited, movies
import random
import pytest


def test_get_mood():
    ...



def test_get_self_care_idea():
    assert get_self_care_idea("happy") == random.choice(happy)
    assert get_self_care_idea("sad") == random.choice(sad)


def test_suggest_movie():
    assert suggest_movie() == movies[random.randint(0,47)]