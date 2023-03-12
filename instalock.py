import json
from requests import session
from valclient.client import Client
import time
print('Valorant Agent instalocker by ZEROv20')
print('Modificado por CarmeloCampos')
print('')
print('Todas las regiones: LATAM - BR - NA - EU - AP - KR')
playerRegion = input('Enter your region (e.g latam): ').lower()

try:
    client = Client(region=playerRegion)
    client.activate()
except Exception as e:
    print('No tienes valorant abierto.')
    exit()

valid = False
agents = {}
seenMatches = []

with open('data.json', 'r') as f:
    agents = json.load(f)

while valid == False:
    try:
        preferredAgent = input("Preferred Agent (e.g Gekko): ").lower()
        if (preferredAgent in agents['agents'].keys()):
            valid = True
        else:
            print("Invalid Agent")
    except:
        print("Input Error")

timeToPickear = int(input("Tiempo antes de pickear (Recom 5): "))
AutoBuscar = input("Autobuscar partida: Si - No: ").lower()
print("Waiting for Agent Select")
while True:
    try:
        time.sleep(1)
        valorantInfo    =   client.fetch_presence(client.puuid)
        sessionState    =   valorantInfo['sessionLoopState']
        if ((AutoBuscar == "si") and (valorantInfo['partyState'] == "DEFAULT") and (sessionState == "MENUS") and valorantInfo['isPartyOwner']):
            time.sleep(1)
            client.party_enter_matchmaking_queue()
            print('Buscando partida')

        elif ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
            print('Agent Select Found')
            time.sleep(timeToPickear)
            client.pregame_select_character(agents['agents'][preferredAgent])
            time.sleep(1)
            client.pregame_lock_character(agents['agents'][preferredAgent])
            seenMatches.append(client.pregame_fetch_match()['ID'])
            print('Successfully Locked ' + preferredAgent.capitalize())
    except Exception as e:
        print('', end='') # Using pass caused weird behavior
