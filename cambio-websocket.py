import asyncio
import websockets
import os

connected = set()

async def server(websocket, path):
    # register websocket connection
    connected.add(websocket)
    try:
        async for message in websocket:
            print(message)
            #  dont send the message to the sender
            for conn in connected:
                print(conn)
                if conn != websocket:
                    await conn.send(f'{message}')
    finally:
        # when connection finished unregister.
        connected.remove(websocket)

start_server = websockets.serve(server, host="", port=int(os.environ["PORT"]))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()