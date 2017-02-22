import websockets
import asyncio
from random import randrange


async def client():
	while True:
		try:
			async with websockets.connect('ws://light.dpmercado.com:8001') as connection:
				while True:
					msg = await connection.recv()
					print(msg)
		except websockets.exceptions.ConnectionClosed:
			pass

if __name__ == '__main__':
	import logging
	logger = logging.getLogger('websockets')
	logger.setLevel(logging.INFO)
	logger.addHandler(logging.StreamHandler())
	loop = asyncio.get_event_loop()
	loop.set_debug(True)
	loop.run_until_complete(client())
