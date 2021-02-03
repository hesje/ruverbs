import os
import Verb as v
import sqlite3 as lite
import random

def choose_file():
    os.system('clear')
    dir = os.listdir('./')
    files = []
    for els in dir:
        if els[-3:] == '.db':
            files.append(els)

    for i, file in enumerate(files):
        print('[' + str(i) + '] ' + file)

    j = input('Which file do you want to practice with? (enter the nr.)')
    return load_file(files[int(j)])


def load_file(file):
    c = lite.connect(file)
    return c

def preferences():
    os.system('clear')
    preferences = {
        'enru' : 'with the English translation(y) or the Russan infinitive(n)? ',
        'pres' : 'present tense? (y/n) ',
        'past' : 'past tense? (y/n) ',
        'part' : 'participles? (y/n) ',
        'imp' : 'imperatives? (y/n) '
    }

    forms = v.dbtohum.copy()
    chosen_prefs = {}

    for x, y in preferences.items():
        enable = (input('Would you like to practice ' + y) == 'y')
        if (x == 'enru' and enable):
            chosen_prefs['inf'] = 'infinitive'
        for i, f in forms.items():
            if (i.find(x) > 0 and enable):
                chosen_prefs[i] = f

    return chosen_prefs

def rand_verb(c, pr):
    w = ''
    while w == '':
        rf = random.choice(list(p.keys()))
        cur.execute('SELECT title, english, inf, ' + rf + ' FROM verbs ORDER BY RANDOM() LIMIT 1;')
        row = cur.fetchone()
        w = row[3]

    enru = 1 if 'inf' in p.keys() else 2

    return p[rf], row[enru], row[3]

def removeaccents(a):
    accentletters = {'а́' : 'а', 'у́' : 'у', 'о́' : 'о', 'е́' : 'е', 'и́' : 'и'}
    for x, y in accentletters.items():
        a = a.replace(x, y)
    return a

def correct(uans, cans, form):
    os.system('clear')
    if uans == removeaccents(cans):
        print('\n\n\nCorrect!')
    else:
        print('\n\n\nNot correct')
        print('the correct translation is: ' + removeaccents(cans))

    input('\n\nPress Enter to continue')


while True:
    conn = choose_file()
    cur = conn.cursor()

    p = preferences()

    for i in range(10):
        os.system('clear')
        form, h, answer = rand_verb(cur, p)
        print('please give the ' + form + ' of the verb: \n\n' + h + '\n')
        a = input('Answer: ')
        correct(a, answer, form)
