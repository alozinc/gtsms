import discord
import asyncio
from time import sleep
from requests import get

from sms import SendSms
TOKEN = "MTA5NjEyNTkwOTc0NjA3MzcxMg.Gr4jGu.y0iq2lbTu1Va4gazX010uBmZcTksgHgvo3RIA8"
gif = ""
adet = 50
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name=".gg/1347")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == ".mesaj":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="Mesaj gönderici (+90)", description=(f"{adet} Mesaj Gönderiliyor --> \n{message.author.mention}"), color=0x001eff,)
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(" --> "+str(sms.adet)+f" Mesaj gönderildi. {message.author.mention}")                        
        else:
            await message.channel.send(f"Geçerli komut yazınız!\nYardım için ' .help ' yazınız. {message.author.mention}")
    elif "!help" == message.content:
        await message.channel.send(f"Mesaj göndermek için komutu aşağıdaki gibi yazınız.\n```.mesaj 5051234567 (+90 olmadan.)``` {message.author.mention}")
    else:
        pass
  
client.run(TOKEN)
