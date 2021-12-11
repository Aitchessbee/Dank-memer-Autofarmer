import discord
from discord.ext import tasks
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "start:aitchessbee:confirm":
        channel = client.get_channel(751701811810795551)
        client.channel = channel
        if message.channel == client.channel:
            await client.channel.send("message recieved")
            send_mes.start()

    if message.content == "stop:aitchessbee:confirm":
        if message.channel == client.channel:
            await message.channel.send("stopped")
            send_mes.stop()

@tasks.loop(seconds=60)
async def send_mes():
    await client.channel.send("pls beg")
    #await asyncio.sleep(3)
    #await client.channel.send("pls share <@!664401331250921473> max")

client.run(token, bot=False)  #disctest1 account