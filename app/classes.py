'''
Quizzicle App 
Written by Mandy Kopelke and Anne Holman for CSB2019

API & Flask Team Project, Term 2
Uses the Open Trivia Database API, more info at: https://opentdb.com/

This classes module defines the classes required to receive the question and
answer data returned from the API. These object classes are used to pass data
into the index page, for the user to interact with.

'''
import requests

API_URL = "https://opentdb.com/api.php?amount=10&category=9&type=boolean"

class Questions():
    '''
    Questions Class defines the blueprint for a questions object
    '''

    def __init__(self):
        self.question = ""
        self.correct_answer = ""

    def get_questions(self):
        '''
        This method retrieves the set of random questions from the API
        '''
        data_found = False
        questions_retrieve = requests.get(f"{API_URL}")
        questions = questions_retrieve.json()
        status_code = questions["response_code"]
        if status_code == 0:
            data_found = True
            for loop in range(10):
                self.question = questions['results'][loop]['question']
                self.correct_answer = questions['results'][loop]['correct_answer']
        return data_found, status_code
