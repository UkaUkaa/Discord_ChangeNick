import subprocess
import random

def getTokenAndPass():
    token_user = []
    pass_user = []
    
    file = open('account.txt', 'r', encoding="utf8")
    for line in file.readlines():
        information = line.replace('\n', '').split(':')
        pass_user.append(information[1])
        token_user.append(information[2])

    return token_user, pass_user


def getNickname():
    nickname_user = []

    file = open('nickname.txt', 'r', encoding='utf8')
    for line in file.readlines():
        nickname_user.append(line.replace('\n', ''))

    return nickname_user

def startChangeNick(nickname,token_user, pass_user):
    nickname = sorted(nickname, key=lambda *args: random.random())
    len_token = 0
    for token in token_user:
        subprocess.Popen(['python', 'main.py', token, pass_user[len_token], nickname[len_token]])
        len_token += 1

allNickname = getNickname()
allTokens, allPassword = getTokenAndPass()

print('Start change nickname')
startChangeNick(allNickname, allTokens, allPassword)