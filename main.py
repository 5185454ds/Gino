import discord
from discord.ext import commands
import requests as req
import re


intents = discord.Intents.default()  # Alapértelmezett intents beállítása
intents.messages = True  # Engedélyezzük a Message eseményeket

# Discord bot token
TOKEN = 'MTE1ODA1MDQyNTM0MjI2MzM5Nw.GfwY-R.ER07O9RyEjS_EDpy8edzIdi1Vg2GozZsu-2Pi4'

# Bot példány létrehozása az intents paraméterrel
bot = commands.Bot(command_prefix='!', intents=intents)

# Eseménykezelő, amely akkor hívódik meg, amikor a bot csatlakozik a Discordhoz


@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Eseménykezelő, amely akkor hívódik meg, amikor a bot egy üzenetet kap


@bot.event
async def on_message(message):
    # Ellenőrizzük, hogy az üzenetet a bot küldte-e, hogy ne válaszoljon magának
    if message.author == bot.user:
        return

    # Ellenőrizzük, hogy az üzenet tartalmazza-e a "hello" szót
    if 'hello' in message.content.lower():
        # Küldjük a választ
        channel = bot.get_channel(1158148726242689044)
        await message.channel.send('Hello!')

    if 'port' in message.content.lower():           
        await message.channel.send('Szerver portok:')
        await message.channel.send('GypsyCraft:25565, HellCraft: Nem üzemel., Teamspeak3:9987')

    if 'ip' in message.content.lower():
        # Küldjük a választ
        url: str = 'http://checkip.dyndns.org'
        request = req.get(url)
        html_content: str = request.text


        # Regular expression pattern to match IP address
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

        # Keresés az IP-címekben a HTML tartalomban
        ip_addresses = re.findall(ip_pattern, html_content)

        # Az összes megtalált IP-címet kiírjuk
        for ip_address in ip_addresses:
            print("IP cím: " + ip_address)
            await message.channel.send("IP cím: " + ip_address)
            

# Bot futtatása a Discordhoz való csatlakozással
bot.run(TOKEN)
