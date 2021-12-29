import discum, time, os, random, string, httpx, base64
from threading import Thread
from itertools import cycle
from urllib.request import urlopen, Request
#Ur Info
token = "OTIwNDQwMzI3OTgxMTI1NzIy.YcxP8w.RSWDkpXeP3PzsSYCkIuNZlY1C9Y"
serverID = "Server id, right click server "
channelID = "Channel id, must match server id ofc"

bot = discum.Client(token=token, log=False)
def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()
def rc(x):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=x))
def scrape(guild_id, channel_id):
    usernames = []
    pfps = []
    bot.gateway.fetchMembers(guild_id, channel_id, wait=1,reset=False,keep="all") #get all user attributes, wait 1 second between requests
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession() #saves 10 seconds when gateway is run again
    g = bot.gateway.session.guild(guild_id)
    for info in (dict(g.members).items()):
        info2 = list(info)
        usernames.append(info2[1]["username"])
        pfps.append(info2[0]+":"+info2[1]["avatar"])
    with open("data/usernames.txt", "a+") as w:
        for i in usernames:
            if "|" in i:
                pass
            elif "HAPEBEAST" in i:
                pass
            elif "BUSINESS APE" in i:
                pass
            else:
                try:
                    w.write(f"{i}\n")
                except:
                    pass
    with open("data/pfps.txt", "a+") as f:
        for i in pfps:
            i2 = i.split(":")
            if i2[1] == "None":
                pass
            elif i2[1] == None:
                pass
            else:
                try:
                    f.write(f"https://cdn.discordapp.com/avatars/{i2[0]}/{i2[1]}.png?size=512\n")
                except:
                    pass
    input("Scraped {len(pfps)} Avatars and {len(usernames)} Usernames!")
    return bot.gateway.session.guild(guild_id).members

def changer(namepfp, tokenformat):
    tokens = []
    urls = []
    usernames = []
    tokenfile = open("data/tokens.txt", "r").read().splitlines()
    urls = cycle(open("data/pfps.txt", "r").read().splitlines())
    usernames = cycle(open("data/usernames.txt", "r").read().splitlines())
    if tokenformat == "1":
        for i in tokenfile:
            tokens.append(i)
    elif tokenformat == "2":
        for i in tokenfile:
            tokenunformatted = i.split(":")
            token = tokenunformatted[1]
            password = tokenunformatted[0]
            tokens.append(f"{token}:{password}")
    elif tokenformat == "3":
        for i in tokenfile:
            tokenunformatted = i.split(":")
            token = tokenunformatted[2]
            password = tokenunformatted[1]
            tokens.append(f"{token}:{password}")
    elif tokenformat == "4":
        for i in tokenfile:
            tokenunformatted = i.split(":")
            token = tokenunformatted[0]
            password = tokenunformatted[2]
            tokens.append(f"{token}:{password}")
    elif tokenformat == "5":
        for i in tokenfile:
            tokenunformatted = i.split(":")
            token = tokenunformatted[2]
            password = tokenunformatted[0]
            tokens.append(f"{token}:{password}")
    elif tokenformat == "6":
        for i in tokenfile:
            tokenunformatted = i.split(":")
            tokens = tokenunformatted[0]
            password = tokenunformatted[1]
            tokens.append(f"{token}:{password}")
    if namepfp == "1":
        for toucan in tokens:
            token = toucan.split(":")
            headers={'Authorization': token[0],'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}
            req = Request(url=next(urls), headers=headers) 
            b64img = base64.b64encode(urlopen(req).read()).decode('utf-8')
            try:
                httpx.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"username":next(usernames),"avatar":f'data:image/png;base64,{b64img}', "password":token[1]})
            except Exception as err:
                print(err)
        input(f"Succesfully changed the Avatars and Usernames of {len(tokens)}!\nPress enter to rerun the program...")
    elif namepfp == "2":
        for toucan in tokens:
            token = toucan.split(":")
            headers={'Authorization': token[0],'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}
            req = Request(url=next(urls), headers=headers) 
            b64img = base64.b64encode(urlopen(req).read()).decode('utf-8')
            try:
                httpx.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"avatar":f'data:image/png;base64,{b64img}', "password":token[1]})
            except Exception as err:
                print(err)
        input(f"Succesfully changed the Avatars of {len(tokens)}!\nPress enter to rerun the program...")    
    elif namepfp == "3":
        for toucan in tokens:
            token = toucan.split(":")
            headers={'Authorization': token[0],'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}
            try:
                httpx.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"usernames":next(usernames), "password":token[1]})
            except Exception as err:
                print(err)
        input(f"Succesfully changed the Usernames of {len(tokens)}!\nPress enter to rerun the program...")  
try:
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        choice = input("Do you want to scrape Avatars & Userames or change Avatars & Usernames in tokens.txt?\n[1] Scrape\n[2] Changer\nChoice: ")
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username and Avatar scraper")
            serverID = input("Server ID: ")
            channelID = input("Channel ID: ")
            x = Thread(target=scrape, args=(serverID, channelID,))
            x.start()
            x.join()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username and Avatar changer")
            namepfp = input("\n[1] Change Avatars and Usernames\n[2] Change Avatars\n[3] Change Usernames\nChoice: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            tokenformat = input("\nToken format?\n[1] token:password\n[2] password:token\n[3] email:password:token\n[4] token:email:password\n[5] password:email:token\n[6] token:password:email\nChoice: ")
            x = Thread(target=changer, args=(namepfp, tokenformat,))
            x.start()
            x.join()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please only input either '1' or '2'.\n")

except Exception as error:
    print(f"Error: {error}")
