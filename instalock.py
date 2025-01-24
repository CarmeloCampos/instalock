from valclient.client import Client
import time

print('Valorant Agent instalocker')
print('')
print('All regions: LATAM - BR - NA - EU - AP - KR')
playerRegion = input('Enter your region (e.g latam): ').lower()

try:
    client = Client(region=playerRegion)
    client.activate()
except Exception as e:
    print('No tienes valorant abierto.')
    exit()

valid = False
agents = {
    "jett": "add6443a-41bd-e414-f6ad-e58d267f4e95",
    "reyna": "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
    "raze": "f94c3b30-42be-e959-889c-5aa313dba261",
    "yoru": "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
    "phoenix": "eb93336a-449b-9c1b-0a54-a891f7921d69",
    "neon": "bb2a4828-46eb-8cd1-e765-15848195d751",
    "breach": "5f8d3a7f-467b-97f3-062c-13acf203c006",
    "skye": "6f2a04ca-43e0-be17-7f36-b3908627744d",
    "sova": "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
    "kayo": "601dbbe7-43ce-be57-2a40-4abd24953621",
    "killjoy": "1e58de9c-4950-5125-93e9-a0aee9f98746",
    "cypher": "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
    "sage": "569fdd95-4d10-43ab-ca70-79becc718b46",
    "chamber": "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
    "omen": "8e253930-4c05-31dd-1b6c-968525494517",
    "brimstome": "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
    "astra": "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
    "viper": "707eab51-4836-f488-046a-cda6bf494859",
    "fade": "dade69b4-4f5a-8528-247b-219e5a1facd6",
    "harbor": "95b78ed7-4637-86d9-7e41-71ba8c293152",
    "gekko": "e370fa57-4757-3604-3648-499e1f642d3f",
    "deadlock": "cc8b64c8-4b25-4ff9-6e7f-37b4da43d235",
    "iso":"0e38b510-41a8-5780-5e8f-568b2a4f2d6c",
    "clove":"1dbf2edd-4729-0984-3115-daa5eed44993",
    "vyse":"efba5359-4016-a1e5-7626-b1ae76895940",
    "tejo":"b444168c-4e35-8076-db47-ef9bf368f384"
}
seenMatches = []

while not valid:
    try:
        preferredAgent = input("Preferred Agent (e.g Gekko): ").lower()
        if preferredAgent in agents.keys():
            valid = True
        else:
            print("Invalid Agent")
    except:
        print("Input Error")

timeToPick = int(input("Tiempo antes de pickear (Recomendado 5): "))
AutoFind = input("Autobuscar partida: Si - No: ").lower()
print("Waiting for Agent Select")
while True:
    try:
        time.sleep(1)
        valorantInfo = client.fetch_presence(client.puuid)
        sessionState = valorantInfo['sessionLoopState']
        if (AutoFind == "si") and (valorantInfo['partyState'] == "DEFAULT") and (sessionState == "MENUS") and \
                valorantInfo['isPartyOwner']:
            time.sleep(1)
            client.party_enter_matchmaking_queue()
            print('Buscando partida')

        elif (sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches):
            print('Agent Select Found')
            time.sleep(timeToPick)
            client.pregame_select_character(agents[preferredAgent])
            time.sleep(1)
            client.pregame_lock_character(agents[preferredAgent])
            seenMatches.append(client.pregame_fetch_match()['ID'])
            print('Successfully Locked ' + preferredAgent.capitalize())
    except Exception as e:
        print('', end='')
