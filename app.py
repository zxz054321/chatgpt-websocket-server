import asyncio
import json
import random

import openai
from websockets import serve

with open("pool.txt", "r") as f:
    txt = f.read()
secrets = [l for l in txt.split("\n") if l]


async def echo(websocket):
    async for data in websocket:
        conversation = [{"role": msg[0], "content": msg[1]} for msg in json.loads(data)]
        openai.api_key = random.choice(secrets)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            stream=True,
        )
        for chunk in response:
            if "choices" in chunk:
                choice = chunk.choices[0]
                if choice.finish_reason == "stop":
                    return
                elif "content" in choice.delta:
                    piece = choice.delta.content
                    await websocket.send(piece)


async def main():
    async with serve(echo, "0.0.0.0", 9000):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
