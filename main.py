import discord
import os
import Webscrape as ws
from keep_alive import keep_alive
from replit import db

my_secret = os.environ['CODINGS']

client = discord.Client()

if "responding" not in db.keys():
    db["responding"] = True

if "items" not in db.keys():
    db["items"] = ['Avatar']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("&add_item"):
        item = msg.split("&add_item ", 1)[1]
        ws.update_items(item)
        await message.channel.send(item + " added to list.")

    if msg.startswith("&del_item"):
        items = []
        if "items" in db.keys():
            index = int(msg.split("&del_item", 1)[1])
            ws.delete_item(index)
            items = db["items"]
            string = ", ".join(str(i) for i in items)
        await message.channel.send(items)

    if msg.startswith("&list_items"):
        items = []
        if "items" in db.keys():
            items = db["items"]
            string = ", ".join(str(i) for i in items)
        await message.channel.send(string)

    if msg.startswith("&help"):
        help_message = ws.get_helpmessage()
        await message.channel.send(help_message)

    if msg.startswith("&funkome"):
        msg = str(ws.checkfilbarstore()) + str(ws.checkbigboys())
        await message.channel.send(msg)


keep_alive()
client.run(my_secret)
