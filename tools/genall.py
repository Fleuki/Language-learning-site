import asyncio, ssl, json, os
import edge_tts.communicate as C
C._SSL_CTX = ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
import edge_tts
m = json.load(open('texts.json'))
V = {'f':'it-IT-IsabellaNeural','m':'it-IT-DiegoNeural'}
sem = asyncio.Semaphore(6)
async def one(k, voice, text, h):
    out = f'audio/{k}/{h}.mp3'
    if os.path.exists(out) and os.path.getsize(out) > 0: return
    async with sem:
        for i in range(4):
            try:
                await edge_tts.Communicate(text.replace('…',''), voice, rate='-5%').save(out); return
            except Exception as e:
                await asyncio.sleep(2**i)
        print('FAIL', k, text)
async def main():
    for k in V: os.makedirs(f'audio/{k}', exist_ok=True)
    await asyncio.gather(*[one(k, v, t, h) for k, v in V.items() for t, h in m.items()])
asyncio.run(main())
