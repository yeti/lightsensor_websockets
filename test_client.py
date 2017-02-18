from websockets import connect
import asyncio
from random import randrange
from os import getenv

async def client():
	'''
	Stubbed out functional client
	'''
	async with connect(getenv('LIGHT_SENSOR_ENV')) as connection:
		while True:
			light_level = "{}".format(randrange(0, 1001))
			await connection.send(light_level)
			await asyncio.sleep(1)

if __name__ == '__main__':
	import logging
	logger = logging.getLogger('websockets')
	logger.setLevel(logging.INFO)
	logger.addHandler(logging.StreamHandler())
	loop = asyncio.get_event_loop()
	loop.set_debug(True)
	loop.run_until_complete(client())
