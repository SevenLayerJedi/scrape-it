from lib.paste_db import *


def check_pastekey(pasteKey):
    allPasteKeys = db_return_all()
    isInDB = False
    
    for i in allPasteKeys:
        if pasteKey in i:
            isInDB = True
    
    return isInDB

