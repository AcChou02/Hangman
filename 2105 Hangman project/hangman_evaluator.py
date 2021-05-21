from eng import *
import pandas as pd
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
eng_fp='C:/Users/andre/Downloads/eng.txt'
eng_data=pd.read_csv(eng_fp, names = ["Word"]).Word.tolist()
eng_data=list(map(str, eng_data))

def evalute_guess(correct, guess, current):
    for i in range(len(current)):
        if current[i]=='_' and correct[i]==guess:
            current=current[:i]+guess+current[i+1:]
    return current

def hangman_auto(word):
    #print('來玩hangman吧！你出題')
    possible_words=eng_data
    not_guessed=letters.copy()
    #print('想好請輸入與題目長度相同的底線')
    score=0

    clues='_'*len(word)
    #print(clues)

    while True:
        possible_words=filter_by_clues(possible_words, clues, not_guessed)
        to_guess=guess_letter(possible_words, not_guessed)
            
        if len(possible_words)==1:
            break
        #print(f'有沒有{to_guess}？')
        not_guessed.remove(to_guess)
        
        if evalute_guess(word, to_guess, clues)==clues:
            score+=1
        clues=evalute_guess(word, to_guess, clues)
        #print(clues)
        
    #print(f'我知道了！答案是{possible_words[0]}')
    return score

def hangman_evaluate(AI):
    total=0
    samples=200
    losses=0
    for i in range(samples):
        word=eng_data[random.randint(0,len(eng_data)-1)]
        game=AI(word)
        total+=game
        if game>5:
            losses+=1
    return (total/samples, 1-(losses/samples))

def hangman_evaluate_all(AI):
    total=0
    losses=0
    for i in range(len(eng_data)):
        game=AI(eng_data[i])
        total+=game
        if game>5:
            losses+=1
        if i%200==0:
            print(i)
    return (total/len(eng_data), 1-(losses/len(eng_data)))
    
print(hangman_evaluate_all(hangman_auto))

