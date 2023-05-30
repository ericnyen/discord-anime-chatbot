import nextcord
from nextcord.ext import commands
import json
import aiohttp
import re

BOT_NAME = "Waifu"
SITUATION = "We are both hella bored"
X_RAPIDAPI_KEY = 'Enter your rapidapi key'
TRANSLATE_FROM = 'en'
TRANSLATE_TO = 'en'

async def waifu_ai_query(query, user_id, user_name):
    
    url = "https://waifu.p.rapidapi.com/path"

    querystring = {

        "user_id": user_id,
        "message": query,
        "from_name": user_name,
        "to_name": BOT_NAME,
        "situation": SITUATION,
        "translate_from": TRANSLATE_FROM,
        "translate_to": TRANSLATE_TO
    }

    my_obj = {

        "key1" : "value",
        "key2" : "value"
        
    }

    payload = json.dumps(my_obj)

    headers = {
    
    'content=type': "application/json",
    'x-rapidapi-host': "waifu.p.rapidapi.com",
    'x-rapidapi-key': X_RAPIDAPI_KEY

    }

    async with aiohttp.ClientSession() as session:

        async with session.post(url, data=payload, headers=headers, params=querystring) as response:
            
            reply = await response.text(
                encoding='utf-8'
            )
        
        return reply


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    elif message.author.bot:
        return
    
    if message.content.startswith("uwu" + " "):

        async with message.channel.typing():

            query = re.sub("uwu" + " ", '', message.content)
            response = await waifu_ai_query(query, message.author.id, message.author.name)
            await message.channel.send(response, reference=message)
            return

bot.run("Enter your discord bot key")