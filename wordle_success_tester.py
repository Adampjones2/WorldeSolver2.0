# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:45:35 2022

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

def reduce_possibilities(comp_results, word_list, guess):
    possible_comparisons = dict()
    for word in word_list:
        possible_comparisons[word] = compare_guess_answer(word, guess)
    possible_words = [word for word in possible_comparisons if possible_comparisons[word] == comp_results]
    return possible_words

def word_chooser(possible_answers: list, possible_guesses: list) -> str:
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
                rem_possible_words = reduce_possibilities(guess_results, possible_answers, guess)
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
    
    for i in range(6):
        if guesses[i] == answer:
            return ("Correct", answer, i+1, guesses)
        guess_results = compare_guess_answer(answer, guesses[i])
        possible_words = reduce_possibilities(guess_results, possible_words, guesses[i])
        next_guess = word_chooser(possible_words, initial_possible_words)
        guesses.append(next_guess)
    return ("Failed", answer, None, guesses)


initial_possible_words = []
fin = open('C:\\Users\\adamp\\Downloads\\words.txt')
for line in fin:
    word = line.strip()
    if len(word) == 5:
        initial_possible_words.append(word)

wordle_solutions = []
bar = Bar('Processing', max = len(initial_possible_words))
for word in initial_possible_words:
    wordle_solutions.append(wordle_solver(word, 'lares', initial_possible_words))
    bar.next()
bar.finish()

failed_wordles = [wordle for wordle in wordle_solutions if wordle[0] == 'Failed']
successful_wordles = [wordle for wordle in wordle_solutions if wordle[0] == 'Correct']


plt.bar(["Successful", "Failed"], [len(successful_wordles), len(failed_wordles)])

guess_freq = dict()
for item in wordle_solutions:
    if str(item[2]) not in guess_freq:
        guess_freq[str(item[2])] = 1
    else:
        guess_freq[str(item[2])] += 1

plt.bar(list(guess_freq.keys()), list(guess_freq.values()))

failed_words = [word[1] for word in failed_wordles]































