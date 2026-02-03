import discord
from discord.client import Client
from discord.message import Message
from backend.Globals import log

intents = discord.Intents.default()
intents.message_content = True

rawToken = open(".token")
token = rawToken.read()
prefix:str = "!"

bot:Client = Client(intents=intents)

@bot.event
async def on_ready():
    log.log_info(f"Krill You Bot is ready as {bot.user} | ID: {bot.user.id}", True, "BotHandler.py", 16)
    
@bot.event
async def on_message(message:Message):
    if message.author == bot.user: return
    content = message.content
    contentL = content.lower()

    if contentL.startswith("/krill"):
        from cmds.KrillCommand import processCommand
        print(processCommand(content))
        
    if contentL.startswith(prefix):
        from cmds.SettingManager import changeSetting
        print(changeSetting(content, prefix))
    
def runBot():
    log.log_info("Starting Bot!", True, "BotHandler.py", 33)
    bot.run(token=token)