import pandas as pd

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
eng_fp='C:/Users/andre/Downloads/eng.txt'
eng_data=pd.read_csv(eng_fp, names = ["Word"]).Word.tolist()
eng_data=list(map(str, eng_data))

def filter_by_len(word_list, length):
    return list(filter(lambda x: len(x)==length, word_list))

def letter_percent(word_list, letter):
    return len(list(filter(lambda x: letter in x, word_list)))/len(word_list)

def guess_letter(word_list, available_letters):
    min_entropy=1
    guess=''
    for i in available_letters:
        entropy=abs(letter_percent(word_list, i)-1)
        if entropy<min_entropy:
            guess=i
            min_entropy=entropy
    return guess

def filter_by_clues(word_list, clues, not_guessed):
    LEN=len(clues)
    new=filter_by_len(word_list, LEN)
    used=[]
    for letter in clues:
        if letter!='_' and letter not in used:
            used.append(letter)
    ans=[]
    for word in new:
        satisfy=True
        for i in range(LEN):
            if clues[i]=='_':
                if word[i] in used:
                    satisfy=False
                if word[i] not in not_guessed:
                    satisfy=False
            else:
                if word[i]!=clues[i]:
                    satisfy=False
        if satisfy:
            ans.append(word)
    return ans
    
def hangman():
    print('來玩hangman吧！你出題')
    possible_words=eng_data
    not_guessed=letters.copy()
    print('想好請輸入與題目長度相同的底線')
    while True:
        clues=input()
        possible_words=filter_by_clues(possible_words, clues, not_guessed)
        to_guess=guess_letter(possible_words, not_guessed)
            
        if len(possible_words)==1:
            break
        print(f'有沒有{to_guess}？')
        not_guessed.remove(to_guess)
        
    print(f'我知道了！答案是{possible_words[0]}')

def search(clues):
    return filter_by_clues(eng_data, clues, letters)
