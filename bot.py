import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import asyncio
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
from discord import Game
 
 
bot = commands.Bot(command_prefix='.')
Snapchot='328062252420694026'
start=time.time()
bot.remove_command('help')
status = ('$help for commands', 'https://discord.gg/Zpzd34X', "Bitch Lasagna 🎶 | $help")

players = {}


async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name =current_status, type=1))
        await asyncio.sleep(10)





@bot.event
async def on_ready():
        print("later")





@bot.command(pass_context=True)
async def help(ctx):

        commands={}
        commands['$help']='`Show bot command list`'
        commands['$website']='***Official server!***'
        commands['$nuke']='***Nuke!!!***'
        commands['$lucky']='***Lucky!!***'
        commands['$invite']='***How to invite***'
        commands['$dm']='***Dm user***'
        commands['$ping']='***Pong!***'
        commands['$whogay]='***Who is gay?***'
        commands['$imgay']='***Gay or no?***'
        commands['$info']='***Show my information***'
        commands['$userinfo']='***Show user info `$userinfo <user>`'
        commands['$uptime']='***Bot up status!***'
        commands['$botcount']='***Count bot***'
        commands['$avatar']='***Show user avatar!***'
        commands['$world']='***Find world in Growtopia!***'
        commands['$purge:']='***clear message*** `$purge <value>`'
        commands['$warn']='***Warn a user!***'
        commands['$mute']='***Mute a user!***'
        commands['$unmute']='***Unmute user!***'
        commands['$kick']='***Kick user from server!***'
        commands['$ban']='***Ban user from server!***'
        commands['$presence:']='***Change Bot Presence***'

        msg=discord.Embed(title='******COMMAND LIST!******', description="***Create By Christ*** ",color=0xF35353)
        for command,description in commands.items():
            msg.add_field(name=command,value=description, inline=False)
        msg.add_field(name='******INFORMATION!******',value='_Thanks Add If You Added My Bot!_', inline=False)
        await bot.whisper(embed=msg)
        await bot.say('***Check*** ___Dm___ ***For Information*** :mailbox:')
        

@bot.command(pass_context=True)
async def invite():
	await bot.say('___HOW TO INVITE___ ***Invite Many People To Join My Discord Official*** : https://discord.gg/Zpzd34X')

@bot.command()
async def website():
	await bot.say('***Check DM For Information :mailbox:***')
	await bot.whisper('||@everyone|| `This Is My Official Server About How To Add My Bot` https://discord.gg/Zpzd34X')

@bot.command(pass_context = True)
async def nuke(ctx, type):
	if ctx.message.author.id==(Snapchot):

	    t = await bot.say('Nuking World ***Be Patient***')
	    await bot.edit_message(t,f'***{type}*** ***>>***  ***was nuked from orbit , it the only way to be sure . play nice everybody!***')

@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
        
@bot.command(pass_context = True)
async def dm(ctx, member : discord.Member, *, content: str):
    await bot.send_message(member, content)
    await bot.say('***User Get Dm From Me!***')
    
@bot.command()
async def bdm():
	   await bot.say('@everyone If You New Here Can U Sub My Creator Channel : ***See GT***')

@bot.command()
async def ping():
	await bot.say('`999+ MS`')

@bot.command()
async def whogay():
	whogay = random.choice(['***YOUR MOM***','***YOUR FATHER***','***YOUR GF / BF***'])
	await bot.say(whogay)

@bot.command()
async def imgay():
	imgay = random.choice(['*1%*','*2%*','*3%*','*4%*','*5%*','6%','7%','8%','9%','10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','*100%*'])
	await bot.say(imgay)

@bot.command()
async def info():
	await bot.say('Created By : Ꮯʜʀɪsᴛ')
	await bot.say('`Make with love <3`')

@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def uptime(ctx):
	now=time.time()
	sec=int(now-start)
	mins=int(sec//60)
	await bot.say('***Uptime is*** ___{sec}___ ***seconds!***')

@bot.command()
async def botcount():
  	"""Bot Guild Count"""
  	await bot.say("***I'm in {} Servers!***".format(len(bot.servers)))
  	
@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))
    
@bot.command(pass_context = True)
async def world(ctx, type):
    await bot.say('***Successfully!!***')
    await bot.say('https://growtopiagame.com/worlds/'f'{type}.png')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx,num:int):
	if ctx.message.author.id==(Snapchot):
		await bot.purge_from(ctx.message.channel,limit=num)
		await bot.say('***Text Has Been Cleared From Me***')
	else:
		await bot.say('___No Perms!___')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def warn(ctx,target:discord.Member):
	if ctx.message.author.id==(Snapchot):
	  await bot.say(':white_check_mark:***User Has been Warned!***')
	else:
		await bot.say('***No Perms!***')
	await bot.send_message(target,'***Pls See The Rules Madafaqa***:mailbox:')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx,target:discord.Member):
	if ctx.message.author.id==(Snapchot):
    	        role=discord.utils.get(ctx.message.author.server.roles,name='Muted')

	await bot.add_roles(target,role)
	await bot.say(target.mention +'***Was Muted!***')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unmute(ctx,target:discord.Member):
	if ctx.message.author.id==(Snapchot):

    	        role=discord.utils.get(ctx.message.author.server.roles,name='Muted')

	await bot.remove_roles(target,role)
	await bot.say(target.mention +'***Has been unmuted!***')

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def kick(ctx, target: discord.Member):	
    await bot.kick(target)
    await bot.say(terget,':white_check_mark: ***User Has Been Kick From Discord!***')
 
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def ban(ctx, userName: discord.Member):
    await bot.ban(userName)
    await bot.say('***User Has Been Banned From Discord!***')
    
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
	if ctx.message.author.id==(Snapchot):
		await bot.change_presence(game=discord.Game(name=text,type=type))
		await bot.say('**Succesfully Presence Got Changed!**')
	else:
		await bot.say('***No Perms!***')
        
 
bot.loop.create_task(change_status())
client.run(str(os.environ.get('TOKEN')))
