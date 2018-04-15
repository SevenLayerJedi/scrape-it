import sqlite3
import datetime

dbFileName = 'lib/PASTEBIN.db'

def db_create():
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS TBL_PASTEBINKEYS
             (PASTE_KEY text, DATE_TIME_ADDED text)''')
    
    conn.commit()
    conn.close()


def db_insert(pasteKey, dateTime):
    # Check to see if the db is created
    # If not then create it
    db_create()
    
    # Connect to the db
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    
    c.execute("INSERT INTO TBL_PASTEBINKEYS VALUES (?, ?)", (pasteKey, dateTime))
    conn.commit()
    conn.close()


def db_show_all():
    # Check to see if the db is created
    # If not then create it
    db_create()
    
    # Connect to the db
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    
    sql_cmd = '''SELECT * FROM TBL_PASTEBINKEYS'''
    
    sqlResults = c.execute(sql_cmd)
    for i in sqlResults:
        print(i)
    
    conn.commit()
    conn.close()

def db_return_all():
    # Check to see if the db is created
    # If not then create it
    db_create()
    
    # Connect to the db
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    
    sql_cmd = '''SELECT * FROM TBL_PASTEBINKEYS'''
    
    newList = []
    
    sqlResults = c.execute(sql_cmd)
    for i in sqlResults:
        newList.append(i)
    
    conn.commit()
    conn.close()
    
    return newList


def db_clean():
    # Check to see if the db is created
    # If not then create it
    db_create()
    
    epoch = int(datetime.datetime.now().strftime("%s")) * 1000
    
    # Connect to the db
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    c2 = conn.cursor()
    
    sql_cmd = '''SELECT * FROM TBL_PASTEBINKEYS'''
    
    newList = []
    t = 0
    sqlResults = c.execute(sql_cmd)
    
    for i in sqlResults:
        timeInDB = int(epoch)- int(i[1])
        if timeInDB > 600000:
            oldKey = i[0]
            t += 1
            #print('Deleting ' + str(i[0]))
            c2.execute("DELETE FROM TBL_PASTEBINKEYS WHERE PASTE_KEY = ?;", (oldKey,))
            conn.commit()
    conn.close()
    
    print(' [+] Deleted ' + str(t) + ' rows from DB')
