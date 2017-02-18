import asyncio
from websockets import serve
from aioredis import create_connection

# Consumer sub-routine
async def store_redis_data(data):
    redis_conn = await create_connection(('localhost', 6379))
    await redis_conn.execute('SET', 'light', data)
    redis_conn.close()

async def light_socket(websocket, path):
    '''
    Server Pattern: consumer
    Input: light data from Pi Client
    Output: store light data into Redis async store 
    '''
    while True:
        light_level = await websocket.recv()
        await store_redis_data(light_level)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    # Sets server to port 8765
    start_server = serve(light_socket, 'localhost', 8765)
    # Websocket server boilerplate
    loop.run_until_complete(start_server)
    loop.run_forever()


