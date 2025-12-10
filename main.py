_S='desktop'
_R='Discord'
_Q='windows'
_P=''
_O=''
_N='properties'
_M='heartbeat_interval'
_L='Channel ID: '
_K='Server ID: '
_J='tokens.txt'
_I="Don't forget to put your tokens in Tokens.txt"
_H='self_deaf'
_G='self_mute'
_F='channel_id'
_E='guild_id'
_D=False
_C=True
_B='op'
_A='d'

from pystyle import *
import os
from colorama import *
import time, asyncio, json, websockets
from json import loads
from time import sleep
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import random

os.system('clear' if os.name == 'posix' else 'cls')

intro = '''
   _____ ______ _____ ______ _   _  __      ______ _____ _____ ______ 
  / ____|  ____/ ____|  ____| \ | | \ \    / / __ \_   _/ ____|  ____|
 | |    | |__ | |    | |__  |  \| |  \ \  / / |  | || || |    | |__   
 | |    |  __|| |    |  __| | . ` |   \ \/ /| |  | || || |    |  __|  
 | |____| |___| |____| |____| |\  |    \  / | |__| || || |____| |____ 
  \_____|______\_____|______|_| \_|     \/   \____/_____\_____|______|
                                                                      
                                                                      
                                    > Press Enter                                         
'''

Anime.Fade(Center.Center(intro), Colors.red_to_yellow, Colorate.Vertical, interval=.035, enter=_C)

print(f"""{Fore.LIGHTBLUE_EX}
   _____ ______ _____ ______ _   _  __      ______ _____ _____ ______ 
  / ____|  ____/ ____|  ____| \ | | \ \    / / __ \_   _/ ____|  ____|
 | |    | |__ | |    | |__  |  \| |  \ \  / / |  | || || |    | |__   
 | |    |  __|| |    |  __| | . ` |   \ \/ /| |  | || || |    |  __|  
 | |____| |___| |____| |____| |\  |    \  / | |__| || || |____| |____ 
  \_____|______\_____|______|_| \_|     \/   \____/_____\_____|______|
                                                                      
""")
time.sleep(1)

Write.Print('\nWhich option do you want to choose: ', Colors.red_to_yellow)
Write.Print('\n> 1 - join voice ', Colors.red_to_yellow)
Write.Print('\n> 2 - voice spam ', Colors.red_to_yellow)
Write.Print('\n> 3 - exit ', Colors.red_to_yellow)

askim = int(input('\nchoice: '))

# Tokenları toplu işlemek için max bağlantı sayısını sınırla
MAX_WORKERS = 20  # İnterneti korumak için eşzamanlı bağlantı sınırı
RECONNECT_DELAY = 10  # Hata sonrası yeniden bağlanma gecikmesi (saniye)
HEARTBEAT_MULTIPLIER = 1.5  # Heartbeat aralığını artırarak yükü azalt

if askim == 1:
    print(_I)
    with open(_J, 'r') as token_file:
        tokens = [t.strip() for t in token_file.readlines() if t.strip()]
    server_id = input(_K)
    channel_id = input(_L)

    async def connect(token):
        while _C:
            try:
                async with websockets.connect(
                    'wss://gateway.discord.gg/?v=9&encoding=json',
                    ping_interval=30,
                    ping_timeout=60,
                    max_size=2**20,  # Daha düşük veri boyutu
                    max_queue=16  # Kuyruk boyutunu sınırla
                ) as websocket:
                    hello = await websocket.recv()
                    hello_json = json.loads(hello)
                    heartbeat_interval = hello_json[_A][_M] * HEARTBEAT_MULTIPLIER
                    await websocket.send(json.dumps({
                        _B: 2,
                        _A: {'token': token, _N: {'': _Q, _O: _R, _P: _S}}
                    }))
                    await websocket.send(json.dumps({
                        _B: 4,
                        _A: {_E: server_id, _F: channel_id, _G: _D, _H: _D}  # self_mute ve self_deaf False - açık kalacak
                    }))

                    while _C:
                        await asyncio.sleep(heartbeat_interval / 1000)
                        try:
                            await websocket.send(json.dumps({
                                _B: 1,
                                _A: random.randint(1, 1000000)
                            }))
                        except Exception:
                            print(f"Token {token[:10]}... için heartbeat başarısız, yeniden bağlanıyor.")
                            break
            except Exception as e:
                print(f"Token {token[:10]}... bağlantı hatası: {e}, {RECONNECT_DELAY} saniye sonra yeniden deniyor.")
                await asyncio.sleep(RECONNECT_DELAY)

    async def main():
        tasks = []
        for token in tokens[:MAX_WORKERS]:  # Token sayısını sınırla
            task = asyncio.create_task(connect(token))
            tasks.append(task)
            await asyncio.sleep(0.5)  # Rate limit için gecikme
        await asyncio.gather(*tasks, return_exceptions=True)

    asyncio.run(main())

elif askim == 2:
    print(_I)
    tokenlist = [t.strip() for t in open(_J, 'r').read().splitlines() if t.strip()]
    server = input(_K)
    channel = input(_L)
    stream = input('Stream: (y/n) ').lower() == 'y'
    video = input('Video: (y/n) ').lower() == 'y'

    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def run(token):
        while _C:
            try:
                ws = WebSocket()
                ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
                hello = loads(ws.recv())
                heartbeat_interval = hello[_A][_M] * HEARTBEAT_MULTIPLIER
                ws.send(json.dumps({
                    _B: 2,
                    _A: {'token': token, _N: {'': _Q, _O: _R, _P: _S}}
                }))
                ws.send(json.dumps({
                    _B: 4,
                    _A: {
                        _E: server,
                        _F: channel,
                        _G: _D,  # self_mute False - mikrofon açık
                        _H: _D,  # self_deaf False - kulaklık açık
                        'self_stream': stream,
                        'self_video': video
                    }
                }))
                ws.send(json.dumps({
                    _B: 18,
                    _A: {'type': 'guild', _E: server, _F: channel, 'preferred_region': 'singapore'}
                }))

                while _C:
                    sleep(heartbeat_interval / 1000)
                    try:
                        ws.send(json.dumps({
                            _B: 1,
                            _A: random.randint(1, 1000000)
                        }))
                        sleep(1)
                    except Exception:
                        print(f"Token {token[:10]}... için heartbeat veya spam hatası, yeniden bağlanıyor.")
                        break
            except Exception as e:
                print(f"Token {token[:10]}... bağlantı hatası: {e}, {RECONNECT_DELAY} saniye sonra yeniden deniyor.")
                sleep(RECONNECT_DELAY)

    os.system(f"title Total Tokens: {len(tokenlist)}")
    for token in tokenlist[:MAX_WORKERS]:
        executor.submit(run, token)
        print('[+] Joined voice channel')
        sleep(random.uniform(0.5, 1.0))  # Daha uzun rate limit gecikmesi

elif askim == 3:
    print('Exiting the program...')
else:
    print('You have entered invalid. Please try again.')