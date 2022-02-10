import discum, time, os, random, string, httpx, json
from threading import Thread
from os import listdir
from itertools import cycle
from base64 import b64encode
from urllib.request import Request
#Ur Info
changed = 0
usernameScraped = 0
pfpScraped = 0
scrapedDone = 0
changerDone = 0
UP = "\x1B[3A"
CLR = "\x1B[0K"

config = json.load(open('config.json'))
token = config.get('token')

ProxyPool = cycle(open("data/proxies.txt", "r").read().splitlines())
bot = discum.Client(token=token, log=False)
def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()
def rc(x):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=x))
def scrape(guild_id, channel_id):
    global usernameScraped
    global pfpScraped
    global scrapedDone
    scrapedDone = 0
    Thread(target=scraperPrint, args=(guild_id,)).start()
    try:
        usernames = []
        pfps = []
        bot.gateway.fetchMembers(guild_id, channel_id, wait=0.01,reset=False,keep="all")
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        g = bot.gateway.session.guild(guild_id)
        for info in (dict(g.members).items()):
            info2 = list(info)
            usernames.append(info2[1]["username"])
            avatar = info2[1]["avatar"]
            pfps.append(f"{info2[0]}:{avatar}")
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
                        usernameScraped+=1
                        w.write(f"{i}\n")
                    except:
                        pass
        threads = []
        for i in pfps:
            
            i2 = i.split(":")
            if i2[1] == "None":
                pass
            elif i2[1] == None:
                pass
            else:
                url = f"https://cdn.discordapp.com/avatars/{i2[0]}/{i2[1]}.png?size=512"
                try:
                    with open("data/pfps.txt", "a+") as f:
                        f.write(f'{url}\n')
                        f.close()
                    x = Thread(target=save, args=(url, i2,))
                    x.start()
                    threads.append(x)
                except Exception as error:
                    print(error)
        for i in threads:
            i.join()
        scrapedDone = 1
        input(f"Scraped {pfpScraped} Avatars and {usernameScraped} Usernames!")
        return bot.gateway.session.guild(guild_id).members
    except Exception as err:
        input(f"Failed to scrape. Error: {err}")
def save(url, i2):
    global pfpScraped
    count=0
    while count < 4: #retries 3 times
        try:
            with open(f'./data/imgs/{i2[0]}.png', 'wb') as f:
                pfpScraped+=1
                f.write(x.content)
            return
        except:
            pass
    
def changer(namepfp, tokenformat, proxyless):
    global changed
    global changerDone
    changerDone = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    tokens = []
    usernames = []
    tokenfile = open("data/tokens.txt", "r").read().splitlines()
    pfps = "data/imgs/"
    usernames = cycle(open("data/usernames.txt", "r").read().splitlines())
    if tokenformat=='1':
        for i in tokenfile:tokens.append(i)
    elif tokenformat=='2':
        for i in tokenfile:tokenunformatted=i.split(':');token=tokenunformatted[1];password=tokenunformatted[0];tokens.append(f"{token}:{password}")
    elif tokenformat=='3':
        for i in tokenfile:tokenunformatted=i.split(':');token=tokenunformatted[2];password=tokenunformatted[1];tokens.append(f"{token}:{password}")
    elif tokenformat=='4':
        for i in tokenfile:tokenunformatted=i.split(':');token=tokenunformatted[0];password=tokenunformatted[2];tokens.append(f"{token}:{password}")
    elif tokenformat=='5':
        for i in tokenfile:tokenunformatted=i.split(':');token=tokenunformatted[2];password=tokenunformatted[0];tokens.append(f"{token}:{password}")
    elif tokenformat=='6':
        for i in tokenfile:tokenunformatted=i.split(':');tokens=tokenunformatted[0];password=tokenunformatted[1];tokens.append(f"{token}:{password}")
    if namepfp == "1":
        Thread(target=changerPrint, args=(tokens, namepfp,)).start()
        for toucan in tokens:
            token = toucan.split(":")
            headers={'Authorization': token[0],'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}
            with open(pfps + random.choice(listdir(pfps)), "rb") as f:
                img = f.read()
            try:
                if proxyless == "1":
                    proxy = f"http://{next(ProxyPool)}"
                else:
                    proxy = None
                httpx.patch('https://discord.com/api/v9/users/@me', proxies=proxy, headers=headers, json={"username":next(usernames),"avatar":f'data:image/png;base64,{b64encode(img).decode("ascii")}', "password":token[1]})
            except Exception as err:
                print(err)
            changed+=1
        changerDone = 1
        input(f"Succesfully changed the Avatars and Usernames of {len(tokens)} tokens!\nPress enter to rerun the program...")
    elif namepfp == "2":
        Thread(target=changerPrint, args=(tokens, namepfp,))
        for toucan in tokens:
            token = toucan.split(":")
            headers={'Authorization': token[0],'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}
            with open(pfps + random.choice(listdir(pfps)), "rb") as f:
                img = f.read()
            try:
                if proxyless == "1":
                    proxy = f"http://{next(ProxyPool)}"
                else:
                    proxy = None
                httpx.patch('https://discord.com/api/v9/users/@me', proxies=proxy, headers=headers, json={"avatar":f'data:image/png;base64,{b64encode(img).decode("ascii")}'})
            except Exception as err:
                print(err)
            changed+=1
        changerDone = 1
        input(f"Succesfully changed the Avatars of {len(tokens)} tokens!\nPress enter to rerun the program...")    
    elif namepfp == "3":
        Thread(target=changerPrint, args=(tokens, namepfp,))
        for toucan in tokens:
            token = toucan.split(":")
            headers={'Authorization': token[0],'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}
            try:
                if proxyless == "1":
                    proxy = f"http://{next(ProxyPool)}"
                else:
                    proxy = None
                httpx.patch('https://discord.com/api/v9/users/@me', proxies=proxy, headers=headers, json={"usernames":next(usernames), "password":token[1]})
            except Exception as err:
                print(err)
            changed+=1
        changerDone = 1
        input(f"Succesfully changed the Usernames of {len(tokens)} tokens!\nPress enter to rerun the program...")
        
def scraperPrint(guild_id):
    global pfpScraped
    global usernameScraped
    global scrapedDone
    os.system('cls' if os.name == 'nt' else 'clear')
    guild_name = httpx.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers={'Authorization':token}).json().get('name')
    print(f"Scraping {guild_name}!\n")
    print('\n\n')
    while scrapedDone == 0:
        print(f"{UP}Usernames Scraped: {usernameScraped}{CLR}\nAvatars Scraped: {pfpScraped}{CLR}\n")
        time.sleep(0.2)
def changerPrint(tokens, mode):
    global changed
    global changerDone    
    print(f"Changing {len(tokens)} tokens!\n\n")    
    while changerDone == 0:
        if mode == "1":
            print(f'{UP}Usernames & Avatars changed: {changed}{CLR}')
        elif mode == "2":
            print(f'{UP}Avatars changed: {changed}{CLR}')
        elif mode == "3":
            print(f'{UP}Usernames changed: {changed}{CLR}')
        time.sleep(0.2)
    
try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
            proxyless = input("Use proxies?\n\n[1] Proxyless\n[2] Proxied")
            x = Thread(target=changer, args=(namepfp, tokenformat, proxyless,))
            x.start()
            x.join()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please only input either '1' or '2'.\n")

except Exception as error:
    print(f"Error: {error}")
