import discord
import re
#emoji = re.compile('[\\-U26CF\\-U2694\\-U1F3F9\\-U1F52B\\-U1FA93\\-U1F527\\-U1F374\\-U1F9CA\\-U1F525\\-U1F691\\-U1F5E1\\-U1fa9b]')
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
from keep_alive import keep_alive
import os
import requests
import json
from replit import db
import csv
from datetime import datetime
from discord.ext import commands, tasks
#Roles-and-ranks channel = 921280925646602241
#Introduce self channel = 922127429588361246
# test channel = 920602720241590322
##************************Google Creds Start***************************************
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#*************************Google Creds Stop**************



client = discord.Client()
weprolemessageid = int()
craftrolemessageid = int()

@client.event
async def on_ready():
  print('We have logged in as {0.user})'.format(client))
  channel = client.get_channel(921280925646602241)

  #*********Create New Wep Role Message********************
  #await channel.purge(limit=10, check=lambda message: message.author == client.user)
  #sent_message = await channel.send(content= 'React to this message for the following weapon builds\nShield: š”ļø\n Sword: #āļø\n Hatchet: šŖ\n Bow: š¹\n Hammer: šØ\n Great Axe: š§\n Spear: š“\n Rapier: šŖ\n Musket: š«\n Ice Gauntlet: š§\n Fire #staff: š„\n Life Staff: š\n Void Guantlet: š”\n')
  #reactions = ['š”ļø', 'āļø', 'šŖ', 'š¹', 'šØ', 'š§', 'š“', 'šŖ', 'š«', 'š§', 'š„', 'š','š”']
  #for emoji in reactions: 
  #  await sent_message.add_reaction(emoji)
  #for x in reactions:
  #  await sent_message.add_reaction(x)
  #*********************************************************

  #************Create New Crafting Role Message***********************
  #channel = client.get_channel(920602720241590322)
  #sent_message = await channel.send(content= 'React to this message to claim max in the following Professions \nāļø : #Weaponsmithing	\nš”ļø : Armoring	\nāļø: Engineering	\nš: Jewelcrafting	\nāļø: Arcana	\nš: Cooking	\nšŖ: Furnishing	#\nāļø: Mining	\nš§āš¾: Harvesting	\nšŖ: Logging	\nš„: Smelting	\nšŖØ: Stonecutting	\nšŖµ: Woodworking	\nš: #Leatherworking	\nš§µ: Weaving' )
  #reactions = ['āļø', 'š”ļø', 'āļø', 'š', 'āļø', 'š', 'šŖ', 'āļø', 'š§āš¾', 'šŖ', 'š„', 'šŖØ', 'šŖµ', 'š', 'š§µ']
  #for x in reactions:
  #  await sent_message.add_reaction(x)
  #********************************************************************

  global weprolemessageid  
  weprolemessageid= 922938296613609573 #sent_message.id
  craftrolemessageid = 922931227995021343
  #for testing, deletes db entries
  #for key in db.keys():
    #del db[key]


@client.event
async def on_message(message):
  rolelist = []
  if message.channel == client.get_channel(921280925646602241) and '!export' in message.content:
    channel = client.get_channel(921280925646602241)
    await message.delete()
   
    title = ['Name', 'Spear', 'Bow', 'Tank', 'Sword', 'Hatchet', 'Hammer', 'GreatAxe', 'Rapier', 'Musket', 'IceGauntlet', 'FireStaff', 'LifeStaff', 'VoidGauntlet'] 
  if message.channel == client.get_channel(922127429588361246):
    await msg.add_reaction('š')



    


@client.event
async def on_raw_reaction_add(payload):

  if payload.message_id == weprolemessageid:
      user = await client.fetch_user(payload.user_id)
      weproles(user, payload)






#************************* Code for adding Crafting Roles ********************************************
#************************* end code for crafting Roles ***********************************************


#************************* Code for adding weapon roles **********************************************
def weproles(username, payload):   
  name = username.name
  emoji = payload.emoji.name
  print(name)
  print(emoji)

  if emoji == 'š“':
    ifuserexistsindb(name,'Spear')
  elif emoji == 'š¹':
    ifuserexistsindb(name,'Bow')
  elif emoji == 'š”ļø':
    ifuserexistsindb(name,'Tank')
  elif emoji == 'āļø':
    ifuserexistsindb(name,'Sword')
  elif emoji == 'šŖ':
    ifuserexistsindb(name,'Hatchet')
  elif emoji == 'šØ':
    ifuserexistsindb(name,'Hammer')
  elif emoji == 'š§':
    ifuserexistsindb(name,'GreatAxe')
  elif emoji == 'šŖ':
    ifuserexistsindb(name,'Rapier')
  elif emoji == 'š«':
    ifuserexistsindb(name,'Musket')
  elif emoji == 'š§':
    ifuserexistsindb(name,'IceGauntlet')
  elif emoji == 'š„':
    ifuserexistsindb(name,'FireStaff')
  elif emoji == 'š':
    ifuserexistsindb(name,'LifeStaff')
  elif emoji == 'š”':
    ifuserexistsindb(name,'VoidGauntlet')

  #****import data from the database to the google sheet
  updatedb()
    
def ifuserexistsindb(user,newitem):
  try:
    dbinfo = db[user].value  
    if dbinfo[newitem] == False:
      dbinfo[newitem] = True
      db[user] = dbinfo
      return
    else:
      return
  except KeyError:
    userdict = { 
      'Name' : user, 
      'Spear' : False, 
      'Bow' : False, 
      'Tank' : False, 
      'Sword' : False, 
      'Hatchet' : False, 
      'Hammer' : False, 
      'GreatAxe' : False, 
      'Rapier' : False, 
      'Musket' : False, 
      'IceGauntlet' : False, 
      'FireStaff' : False, 
      'LifeStaff' : False, 
      'VoidGauntlet' : False }

    userdict[newitem] = True

    db[user] = userdict
    return
#***************************************** end code weapon roles********************************************************


  
  
@client.event
async def on_raw_reaction_remove(payload):
   if payload.message_id == weprolemessageid:
    user = await client.fetch_user(payload.user_id)
    name = user.name
    emoji = payload.emoji.name

    if emoji == 'š“':
      removeRole(name,'Spear')
    elif emoji == 'š¹':
      removeRole(name,'Bow')
    elif emoji == 'š”ļø':
      removeRole(name,'Tank')
    elif emoji == 'āļø':
      removeRole(name,'Sword')
    elif emoji == 'šŖ':
      removeRole(name,'Hatchet')
    elif emoji == 'šØ':
      removeRole(name,'Hammer')
    elif emoji == 'š§':
      removeRole(name,'GreatAxe')
    elif emoji == 'šŖ':
      removeRole(name,'Rapier')
    elif emoji == 'š«':
      removeRole(name,'Musket')
    elif emoji == 'š§':
      removeRole(name,'IceGauntlet')
    elif emoji == 'š„':
      removeRole(name,'FireStaff')
    elif emoji == 'š':
      removeRole(name,'LifeStaff')
    elif emoji == 'š”':
      removeRole(name,'VoidGauntlet')

def removeRole(user,newitem):
  try:
    dbinfo = db[user].value  
    if dbinfo[newitem] == True:
      dbinfo[newitem] = False
      db[user] = dbinfo
      updatedb()
      return
    else:
      return
  except KeyError:
    return


def updatedb():
  rolelist = []
  for key in db.keys():
    rolelist.append(db[key].value)
          
  title = ['Name', 'Spear', 'Bow', 'Tank', 'Sword', 'Hatchet', 'Hammer', 'GreatAxe', 'Rapier', 'Musket', 'IceGauntlet', 'FireStaff', 'LifeStaff', 'VoidGauntlet'] 
  #export files to csv
  with open("output.csv","w") as csvfile:  
    cw = csv.DictWriter(csvfile, fieldnames = title)
    cw.writeheader()
    cw.writerows(rolelist)


  scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
  jsoncreds = os.environ['googleapi']
  File_object = open("./api.json", "w")
  File_object.write(jsoncreds)
  File_object.close()

  credentials = ServiceAccountCredentials.from_json_keyfile_name("./api.json", scope)
  gclient = gspread.authorize(credentials)

  spreadsheet = gclient.open('Roster and Weapon')

  with open('output.csv', 'r') as file_obj:
    content = file_obj.read()
    gclient.import_csv(spreadsheet.id, data=content)

  os.remove("api.json")


#db.keys
#del.db['']
#for key in db.keys()


#payload objects
# message_id
# user_id
# channel_id
# guild_id
# emoji.name




keep_alive()
client.run(os.environ['TOKEN'])







