import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import json
import Verb as v
import sqlite3 as lite
import os
import sys

verbs = {}

S = requests.Session()

def get_verb(c, q):
    """ Parse a section of a page, fetch its table data and save it to a CSV file
    """

    url = 'https://en.wiktionary.org/w/api.php?action=parse&format=json&prop=text&disabletoc=true&page=' + q
    try:
        res = S.get(url=url)
    except:
        return False

    data = res.json()
    try:
        text = data['parse']['text']['*']
    except:
        return False

    title = data['parse']['title']
    html = BeautifulSoup(text, "html.parser")
    tables = html.findAll('table')

    translation = ''

    # lis = html.ol.findAll('li', limit=4)
    # for i, li in enumerate(lis):
    #     if li.a != None:
    #         translation += 'to ' + str(li.a.contents[0])
    #         if lis[-1] != li:
    #             translation += '\n'
    #     elif type(li.contents) == NavigableString:
    #         translation += 'to ' + str(li.a.contents[0])
    #         if lis[-1] != li:
    #             translation += '\n'


    subverb = v.new_sub_verb()
    subverb['title'] = title
    subverb['english'] = translation

    if subverb['english'] == '':
        subverb['english'] = input('No English translation found, please enter it here: ')

    for i, table in enumerate(tables):
        if table['class'][0] == 'inflection':
            spans = table.findAll('span')
            for span in spans:
                if len(span['class']) > 3:
                    form = span['class'][3]
                    if form in v.forms:
                        a = span.contents[0]
                        subverb[form] = a.contents[0]
            break

    query = ''
    columns = ''
    for x, y in subverb.items():
        columns += '\'' + str(v.htmltodb[str(x)]) + '\','
        query += '\'' + str(y) + '\','


    qu = 'INSERT INTO verbs (' + columns[:-1] + ') VALUES(' + query[:-1] + ')'
    try:
        c.execute(qu)
    except:
        return False

    return title

def create_table(c):
    c.execute("""CREATE TABLE verbs(
    title TEXT NOT NULL PRIMARY KEY,
    english TEXT,
    inf TEXT,
    pres_act_part TEXT,
    past_act_part TEXT,
    pres_pass_part TEXT,
    past_pass_part TEXT,
    pres_adv_part TEXT,
    past_adv_part TEXT,
    _1_s_pres_ind TEXT,
    _2_s_pres_ind TEXT,
    _3_s_pres_ind TEXT,
    _1_p_pres_ind TEXT,
    _2_p_pres_ind TEXT,
    _3_p_pres_ind TEXT,
    _2_s_imp TEXT,
    _2_p_imp TEXT,
    m_s_past_ind TEXT,
    p_past_ind TEXT,
    f_s_past_ind TEXT,
    n_s_past_ind TEXT
    )""")



if __name__ == '__main__':
    os.system('clear')
    q = input('what is the name of this dataset?')
    con = lite.connect(q + '.db')

    cur = con.cursor()
    cur.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table';")
    if cur.fetchone()[0] == 0:
        create_table(cur)


    with con:
        cont = True
        while cont:
            q = input("verb to search for:")
            if q in verbs:
                print('you have already added the verb: ' + q)
            elif q == '#':
                con.close()
                cont = False
            else:
                a = get_verb(cur, q)
                if a:
                    con.commit()
                    os.system('clear')
                    print('The verb ' + a + ' has been added to the database')
                    print('To stop entering more verbs pres ctrl + c')
                else:
                    print('Something went wrong, try again')
