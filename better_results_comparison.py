# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:48:44 2022

@author: adamp
"""
                   

guess = 'mamma'
ans = 'madam'
results = []
for i in range(len(guess)):
    if guess[i] == ans[i]:
        results.append([guess[i], i, 'green'])
        guess = guess[:i] + ',' + guess[i+1:]
        ans = ans[:i] + '.' + ans[i+1:]
for i in range(len(guess)):
    if guess[i] in ans:
        results.append([guess[i], i, 'orange'])
        ans = ans.replace(guess[i], '.', 1)
        guess = guess[:i] + ',' + guess[i+1:]
    elif guess[i] in 'abcdefghijklmnopqrstuvwxyz':
        results.append([guess[i], i, 'grey'])
results.sort(key = lambda x:x[1])


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

compare_guess_answer('madam', 'daddy')



def reduce_possibilities(comp_results, word_list, green_letters, guess):
    possible_comparisons = dict()
    for word in word_list:
        possible_comparisons[word] = compare_guess_answer(word, guess)
    possible_words = [word for word in possible_comparisons if possible_comparisons[word] == comp_results]
    return possible_words













































