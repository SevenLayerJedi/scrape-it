from lib.tweet_it import *
from lib.check_paste_exist import *
from lib.regexes import *
from lib.paste_db import *
import re
import requests
import json
import datetime
import time
from datetime import datetime
from time import sleep
import io
import os
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def scrape_pastebin():
    response = requests.get('https://pastebin.com/api_scraping.php?limit=250')
    jsonOutput = response.json()
    #timenow = time.time()
    for eachPaste in jsonOutput:
        outputString = ''
        numEmail = 0
        numSSN = 0
        numHash32 = 0
        numCiscoHash = 0
        numCiscoPass = 0
        numGoogleAPIKey = 0
        numPGPKeys = 0
        numSSHKeys = 0
        numKeywords = 0
        isAntiSecGlobal = 0
        isInDB = False
        isInDB = check_pastekey(eachPaste['key'])
        
        if not isInDB:
            try:
                epoch = int(datetime.now().strftime("%s")) * 1000
                db_insert(eachPaste['key'], epoch)
            except Exception as e:
                print(' [ERROR TRY REQUEST] ' + str(e.message) + ' ' + str(e.args))
            
            try:
                resp = requests.get('https://pastebin.com/api_scrape_item.php?i={}'.format(eachPaste['key']))
            except Exception as e:
                print(' [ERROR TRY REQUEST] ' + str(e.message) + ' ' + str(e.args))
            
            for line in resp.text.splitlines():
                numEmail += len(regexes['email'].findall(line))
                SSNData = regexes['ssn'].findall(line)
                numHash32 += len(regexes['hash32'].findall(line))
                numCiscoHash += len(regexes['cisco_hash'].findall(line))
                numCiscoPass += len(regexes['cisco_pass'].findall(line))
                numGoogleAPIKey += len(regexes['google_api'].findall(line))
                numPGPKeys += len(regexes['pgp_private'].findall(line))
                numSSHKeys += len(regexes['ssh_private'].findall(line))
                isAntiSecGlobal += len(regexes['lulz'].findall(line))
                
                for regex in regexes['db_keywords']:
                    numKeywords += len(regex.findall(line))
            
            outputString += '[http://pastebin.com/' + eachPaste['key'] + '] '
            
            if numEmail > 0:
                outputString += '[EMAIL: ' + str(numEmail) + '] '
            if numSSN > 0:
                outputString += '[SSN: ' + str(numSSN) + '] '
            if numHash32 > 0:
                outputString += '[HASH: ' + str(numHash32) + '] '
            if numCiscoHash > 0:
                outputString += '[CISCO_HASH: ' + str(numCiscoHash) + '] '
            if numCiscoPass > 0:
                outputString += '[CISCO_PASS: ' + str(numCiscoPass) + '] '
            if numGoogleAPIKey > 0:
                outputString += '[GOOGLE_API: ' + str(numGoogleAPIKey) + '] '
            if numPGPKeys > 0:
                outputString += '[PGP_PRIV: ' + str(numPGPKeys) + '] '
            if numSSHKeys > 0:
                outputString += '[SSH_PRIV: ' + str(numSSHKeys) + '] '
            if isAntiSecGlobal > 0:
                outputString += '[ANTISECGLOBAL: YES] '
            if numEmail > 12:
                outputString += ' #infoleak #passwords'
            
            if len(outputString) > 32:
                print(bcolors.FAIL + ' [-] ' + outputString + bcolors.ENDC)
            
            if numEmail > 12 or isAntiSecGlobal > 0:
                try:
                    tweet_it(outputString)
                    print(bcolors.OKBLUE + '    [+] [TWEETING] http://www.pastebin.com/' + eachPaste['key'] + bcolors.ENDC)
                except Exception as e:
                    print(bcolors.FAIL + ' [-] [DUPLICATE TWEET] ' + e.message + bcolors.ENDC)
            
            if numEmail > 12 or isAntiSecGlobal > 0:
                if ( not os.path.isfile('/mnt/d/toolshed/scrape-it/pastes/' + eachPaste['key'] + '.txt')):
                    print(bcolors.HEADER + '    [+] [SAVING] /mnt/d/toolshed/python_scripts/scrape-it/pastes/' + eachPaste['key'] + '.txt' + bcolors.ENDC)
                    f = open ('/mnt/d/toolshed/python_scripts/scrape-it/pastes/' + eachPaste['key'] + '.txt', 'a')
                    for line in resp.text.splitlines():
                        try:
                            line = u' '.join((line)).encode('utf-8').trim()
                        except:
                            line = line
                        
                        f.write(line + '\r' + '\n')
                    print(bcolors.HEADER + '    [+] [CLOSING] /mnt/d/toolshed/python_scripts/scrape-it/pastes/' + eachPaste['key'] + '.txt' + bcolors.ENDC)
                    f.close()
                else:
                    print(bcolors.WARNING + '    [+] [FILE EXISTS] /mnt/d/toolshed/python_scripts/scrape-it/pastes/' + eachPaste['key'] + '.txt' + bcolors.ENDC)
    
    db_clean()
    
    print(bcolors.OKGREEN + ' --- zzz sleeping 60 seconds zzz ---' + bcolors.ENDC)
    time.sleep(60)

