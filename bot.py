import discord
from discord.ext import tasks

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "start:confirm":
        channel = client.get_channel(channel_id)
        client.channel = channel
        if message.channel == client.channel:
            await client.channel.send("message recieved")
            send_mes.start()

    if message.content == "stop:confirm":
        if message.channel == client.channel:
            await message.channel.send("stopped")
            send_mes.stop()

@tasks.loop(seconds=60)
async def send_mes():
    await client.channel.send("pls beg")

client.run(token, bot=False)