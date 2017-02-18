from websockets import serve
import asyncio
from random import randrange
from aioredis import create_connection

# Producer subroutine
async def get_from_redis():
	redis_conn = await create_connection(('localhost', 6379))
	result = await redis_conn.execute('GET', 'light')
	redis_conn.close()
	return result

async def browser_server(websocket, path):
	'''
	Server Pattern: producer
	Input: Gets data from redis server
	Output: Sends data to browser
	'''
	print('Connection established')

	while True:
		data = await get_from_redis()
		await websocket.send(data.decode('utf-8'))
		await asyncio.sleep(1)

if __name__ == '__main__':

	import logging
	logger = logging.getLogger('websockets')
	logger.setLevel(logging.INFO)
	logger.addHandler(logging.StreamHandler())

	start_server = serve(browser_server, 'localhost', 8767)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()

