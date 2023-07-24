import discord
from discord.ext import commands

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'O {bot.user.name}  foi iniciado com sucesso!  ')

# Comando !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Comando !vacuum
@bot.command()
async def vacuum(ctx):
    embed = discord.Embed(
        title='Vacuum Discord',
        description='Acesse o link para entrar no servidor Vacuum Discord:',
        color=0x6E1BD8
    )
    embed.add_field(name='Link', value='[Vacuum Discord](https://discord.gg/vacuum)', inline=True)
    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1666236069677809666/c529cWQ3_400x400.jpg')
    embed.set_image(url='https://media.discordapp.net/attachments/1090814148964778014/1131012391493181511/Red_and_Black_Full_Photo_Night_Sky_Aesthetic_Quote_Twitter_Header_1440_300_px.gif?width=1024&height=213')
    embed.set_footer(text='Bot Vacuum - Desenvolvido por yashirof', icon_url='https://pbs.twimg.com/profile_images/1666236069677809666/c529cWQ3_400x400.jpg')

    await ctx.send(embed=embed)


bot.run('TOKEN_DO_BOT')

