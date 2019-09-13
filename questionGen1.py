from textblob import TextBlob
from textblob.en import tag as pattern_tag, tag
from textblob.decorators import requires_nltk_corpus
from textblob.base import BaseTagger
import os

# importing a text:
text1 = filehandle = open('corpus1.txt')
text = filehandle.read()

# text = '''Timmie Willie is a country mouse who is accidentally transported
# to a city in a vegetable basket. When he wakes up, he finds himself in a
# party and makes a friend. When he is unable to bear the city life,
# he returns to his home but invites his friend to the village. When his friend visits him,
# something similar happens.'''

# removes \n from the text and adds each line to lines_list
lines_list = text.splitlines()
# joins the elements of lines_list and makes raw text
text_raw = "".join(lines_list)
# implement raw text to textblob
blob = TextBlob(text_raw)
# parsing sentences
sentences = blob.split('.')
# tag senteces
tags = blob.tags
# print the sentences
print('\n\n{:-^160}'.format(' Parsed Sentences ') + '\n\n')
for i in range(0, len(sentences)):
    print(sentences[i])
# put tags into a list
list3_tags = []
for i in range(0, len(sentences)):
    list3_tags.append(tag(sentences[i]))
tags_list_final = []
tags_final = []
# separate tags by sentence
for i in range(0, (len(list3_tags) - 1)):
    for j in range(0, len(list3_tags[i])):
        tags_list_final.append(list3_tags[i][j][1])
    tags_final.append(tags_list_final)
    tags_list_final = []

# put words into a list
# put tags into a list
list3_words = []
for i in range(0, len(sentences)):
    list3_words.append(tag(sentences[i]))
words_list_final = []
words_final = []
# separate tags by sentence
for i in range(0, (len(list3_words) - 1)):
    for j in range(0, len(list3_words[i])):
        words_list_final.append(list3_words[i][j][0])
    words_final.append(words_list_final)
    words_list_final = []

print('\n\n{:-^160}'.format(' Tags and Words ') + '\n\n')
for i in range(0, len(tags_final)):
    print(tags_final[i])
    print(words_final[i])

#print('\n\n{:-^160}'.format(' Words ') + '\n\n')
#for i in range(0, len(tags_final)):
#    print(words_final[i])

for i in range(0, len(tags_final)):
    for j in range(0, len(tags_final[i])):
        if tags_final[i][j] == 'DT':
            pass

print('\n\n{:-^160}'.format(' Questions Test: ') + '\n\n')

# lists for tags to compare
li1 = ['DT', 'VBN', 'VBZ', 'DT']
li2 = ['DT', 'NN', 'VBZ', 'DT']
li3 = ['DT', 'VBN', 'MD', 'VB', 'VBN']
li4 = ['DT', 'JJ', 'VBN', 'VBZ', 'DT']
li5 = ['DT', 'NN', 'VBN', 'VBZ', 'DT']
li6 = ['PRP', 'VBZ', 'DT']
li7 = ['DT', 'VBD', 'NN', 'VBZ', 'RB', 'DT']
li8 = ['VBD', 'NNS', 'VBP', 'RB', 'VBN']
li9 = ['NN', 'NN', 'VBZ', 'DT']
li10 = ['NN', 'NN', 'VBZ', 'JJ']
li11 = ['DT', 'VBG', 'NNS', 'VBP', 'JJ']
li12 = ['DT', 'VBZ', 'DT', 'VBN', 'JJ']

# make lists to add questions and answers
questions = []
answers = []

for i in range(0, len(tags_final)):
    if tags_final[i][0:4] == li1[0:4]:
        questions.append(f'What {words_final[i][2]} {words_final[i][0].lower()} {words_final[i][1]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:5] == li5[0:5]:
        questions.append(
            f'What {words_final[i][3]} {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:5] == li4[0:5]:
        questions.append(
            f'What {words_final[i][3]} {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:5] == li3[0:5]:
        questions.append(f'How {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} {words_final[i][3]} '
                         f'{words_final[i][4]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:4] == li2[0:4]:
        questions.append(f'What {words_final[i][2]} {words_final[i][0].lower()} {words_final[i][1]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:3] == li6[0:3]:
        questions.append(f'{words_final[i][0]} {words_final[i][1]} what ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:6] == li7[0:6]:
        questions.append(
            f'What {words_final[i][3]} {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:6] == li7[0:6]:
        questions.append(
            f'What {words_final[i][3]} {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:5] == li8[0:5]:
        questions.append(
            f'What {words_final[i][2]} {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][4]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:4] == li9[0:4]:
        questions.append(f'What {words_final[i][2]} {words_final[i][0].lower()} {words_final[i][1]}  ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:4] == li10[0:4]:
        questions.append(
            f'Why {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} {words_final[i][3]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:5] == li11[0:5]:
        questions.append(
            f'How {words_final[i][3]} {words_final[i][0].lower()} {words_final[i][1]} {words_final[i][2]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

    if tags_final[i][0:5] == li12[0:5]:
        questions.append(
            f'What {words_final[i][0].lower()} {words_final[i][1]} ?')
        answers.append(f'{" ".join(words_final[i])}.')

for i in range(0, len(questions)):
    print(f'{questions[i]}  {answers[i]}')
