# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:50:14 2022

@author: adamp
"""

from progress.bar import Bar
import matplotlib.pyplot as plt
import statistics


def compare_guess_answer(answer: str, guess: str) -> list[list[str, int, str]]:
    results = []
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            results.append([guess[i], i, 'green'])
            guess = guess[:i] + ',' + guess[i+1:]
            answer = answer[:i] + '.' + answer[i+1:]
    for i in range(len(guess)):
        if guess[i] in answer:
            results.append([guess[i], i, 'orange'])
            answer = answer.replace(guess[i], '.', 1)
            guess = guess[:i] + ',' + guess[i+1:]
        elif guess[i] in 'abcdefghijklmnopqrstuvwxyz':
            results.append([guess[i], i, 'grey'])
    results.sort(key = lambda x:x[1])
    return results

def reduce_possibilities(comp_results, word_list, green_letters, guess):
    possible_comparisons = dict()
    for word in word_list:
        possible_comparisons[word] = compare_guess_answer(word, guess)
    possible_words = [word for word in possible_comparisons if possible_comparisons[word] == comp_results]
    return possible_words, green_letters

def word_chooser(possible_answers: list, possible_guesses: list, green_letters: dict) -> str:
    """
    After inputting todays wordle answer and your starting guess, along with 
    the list of valid words this function returns the answer along with the
    number of guesses taken and a list of the guesses made.
    """
    if len(possible_answers) == 1:
        return possible_answers[0]
    else:
        no_reduced = dict()
        for guess in possible_guesses:
            no_ruled_out = []
            for ans in possible_answers:
                guess_results = compare_guess_answer(ans, guess)
                rem_possible_words, green_letters = reduce_possibilities(guess_results, possible_answers, green_letters, guess)
                no_ruled_out.append(len(possible_answers) - len(rem_possible_words))
            no_reduced[guess] = statistics.mean(no_ruled_out)
        return max(no_reduced, key = no_reduced.get)


def wordle_solver(answer: str, starting_guess: str, valid_words: list) -> tuple():
    """
    After inputting todays wordle answer and your starting guess, along with 
    the list of valid words this function returns the answer along with the
    number of guesses taken and a list of the guesses made.

    """
    guesses = [starting_guess]
    initial_possible_words = valid_words
    possible_words = valid_words
    green_letters = dict()
    
    possible_answers_tracker = [initial_possible_words]
    
    for i in range(6):
        if guesses[i] == answer:
            return ("Correct", answer, i+1, guesses, possible_answers_tracker)
        guess_results = compare_guess_answer(answer, guesses[i])
        possible_words, green_letters = reduce_possibilities(guess_results, possible_words, green_letters, guesses[i])
        next_guess = word_chooser(possible_words, initial_possible_words, green_letters)
        guesses.append(next_guess)
        possible_answers_tracker.append(possible_words)
    return ("Failed", answer, None, guesses, possible_answers_tracker)

initial_possible_words = []
fin = open('C:\\Users\\adamp\\Downloads\\words.txt')
for line in fin:
    word = line.strip()
    if len(word) == 5:
        initial_possible_words.append(word)
        
x = wordle_solver('label', 'lares', initial_possible_words)