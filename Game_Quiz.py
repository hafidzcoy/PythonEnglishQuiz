### English Quiz App ###
import os
import platform
print ('Welcome To The Game')
Score= 0
#Question program
def question(Question, Answerr):
    global continue_or_stop
    #ask user to input answer
    quess=input(Question)
    #i using upper() command to change input from user to capital letters format
    if quess.upper() in Answerr:
        global Score
        Score += 1
    else:
        print ("You Wrong")
        continue_or_stop=input('do you want to continue the game? type yes/no: ')
        if continue_or_stop == "yes":
            #clean the terminal
            os.system('clear')
            #riset score
            Score -= Score
            #recall the program
            looping()
        else:
            print ('Thank You')
            print('Have Done :(')
            #Viwe the score
            print(f"The Score is {Score}")
            #close the programm
            exit()
        


#Questions
quess1= 'What is the meaning of "Desk"? '
quess2= 'what is Indonesian of "Human"? '
quess3= 'what is english of selamat pagi? '
quess4= 'Tuliskan bahasa Inggrisnya "Makan"? '
quess5= 'What is english of "merah"? '
# 6. Grammar: Nouns (Previously Q1)
quess6 = '6. What is the grammatical term for a word that names a person, place, or thing? '

# 7. Grammar: Verbs/Tenses (Previously Q2)
quess7 = '7. What is the simple past tense of the verb "eat"? '

# 8. Grammar: Contractions (Previously Q3)
quess8 = '8. Which two words are combined to form the contraction "don\'t"? '

# 9. Punctuation: End Marks (Previously Q4)
quess9 = '9. What punctuation mark is used at the end of a simple statement or declarative sentence? '

# 10. Vocabulary: Synonyms (Previously Q5)
quess10 = '10. Which word is a synonym for "large": tiny, huge, or small? '


# 11. Vocabulary: Homophones (Previously Q6)
quess11 = '11. What word sounds the same as "see" but means the vast body of salt water? '

# 12. Grammar: Articles (Previously Q7)
quess12 = '12. Which article (a, an, or the) should you use immediately before the word "orange"? '

# 13. Grammar: Subject Identification (Previously Q8)
quess13 = '13. In the sentence "The cat sleeps," what is the subject of the sentence? '

# 14. Grammar: Sentence Types (Previously Q9)
quess14 = '14. What kind of sentence asks a question and always ends with a question mark? '

# 15. Grammar: Prepositions (Previously Q10)
quess15 = '15. Complete the phrase with a basic preposition: The hat is _____ the table. '

#Answerr
ask1= ["MEJA"]
ask2= ["MANUSIA"]
ask3= ["GOOD MORNING"]
ask4= ["EAT"]
ask5= ["RED"]
# 6. Answer (Noun)
ask6 = ["NOUN"]

# 7. Answer (Past tense of eat)
ask7 = ["ATE"]

# 8. Answer (Contraction: do not)
ask8 = ["DO NOT", "DONOT"]

# 9. Answer (End mark)
ask9 = ["PERIOD", "FULL STOP", "DOT"]

# 10. Answer (Synonym for large)
ask10 = ["HUGE"]

# 11. Answer (Homophone of see)
ask11 = ["SEA"]

# 12. Answer (Article before orange)
ask12 = ["AN"]

# 13. Answer (Subject)
ask13 = ["CAT", "THE CAT"]

# 14. Answer (Question sentence)
ask14 = ["INTERROGATIVE", "INTERROGATIVE SENTENCE", "QUESTION SENTENCE"]

# 15. Answer (Basic preposition)
ask15 = ["ON", "UNDER", "IN", "BESIDE", "NEAR"] # Accepting several common simple prepositions


#call and loop program
def looping():
    question(quess1, ask1)
    question(quess2, ask2)
    question(quess3, ask3)
    question(quess4, ask4)
    question(quess5, ask5)
    question(quess6, ask6)
    question(quess7, ask7)
    question(quess8, ask8)
    question(quess9, ask9)
    question(quess10, ask10)
    question(quess11, ask11)
    question(quess12, ask13)
    question(quess13, ask13)
    question(quess14, ask14)
    question(quess15, ask15)
    #result
    print('Have Done :)')
    print(f"The Score is {Score}")
    exit()
    
 
looping()







