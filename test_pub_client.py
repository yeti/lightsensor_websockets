import asyncio
import aioredis
import websockets

async def publishToRedisWs():
	async with websockets.connect('ws://light.dpmercado.com:8003') as ws:
		while True:
			text = input('>> ')
			await ws.send(text)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(publishToRedisWs())