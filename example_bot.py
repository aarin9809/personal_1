import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTEzMjE4MTgzODI0NTQxNzAyMA.GANpcl.ZVa8HOwZHWIYZRI97dGEaEpuR_gMv6wj-0ughY')
