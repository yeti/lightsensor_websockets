import asyncio
from aioredis import create_connection, Channel
import websockets

async def publish_to_redis(msg):
	conn = await create_connection(('localhost', 6379))
	await conn.execute('publish', 'lightlevel', msg)
	conn.close()

async def server(websocket, path):
	try:
		while True:
			message = await websocket.recv()
			await publish_to_redis(message)
	except websockets.exceptions.ConnectionClosed:
		print('Connection Closed!')


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.set_debug(True)
	ws_server = websockets.serve(server, 'localhost', 8002)
	loop.run_until_complete(ws_server)
	loop.run_forever()
