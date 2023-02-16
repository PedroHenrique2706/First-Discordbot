import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)




@bot.event
async def on_ready():
    print('Estou On!')

@bot.event
async def message(message):
  if message.author == bot.user:
    return





@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    response = 'Olá, ' + name

    await ctx.send(response)






#COTAÇÃO DÓLAR
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')

navegador.find_element('xpath',
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')

navegador.find_element('xpath',
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath',
       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(f'Valor do dolar: {cotacao_dolar}')


@bot.command(name='dolar')
async def send_hello(ctx):
    name = ctx.author.name
    response = name  +  ' a cotação do dolar é ' + str(emoji.emojize(':dollar:''R$:')) + cotacao_dolar
    await ctx.send(response)


#COTAÇÃO EURO
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')

navegador.find_element('xpath',
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')

navegador.find_element('xpath',
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath',
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(f'valor do euro:{cotacao_euro}')


@bot.command(name='euro')
async def send_hello(ctx):
    name = ctx.author.name
    response = name  +  ' a cotação do Euro é ' + str(emoji.emojize(':dollar:''R$:')) + cotacao_euro
    await ctx.send(response)




#COTAÇÃO BITCOIN

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')



navegador.get('https://www.google.com/search?q=bitcoin&biw=1365&bih=1007&ei=XKbhY8qMGP_41sQPwoqYoAw&oq=bit&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgQIABBDMgoIABCxAxCDARBDMgQIABBDMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAELEDEIMBMgsIABCABBCxAxCDATIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoLCC4QgAQQxwEQ0QM6BQgAEIAEOgsILhCDARCxAxCABEoECEEYAEoECEYYAFAAWKgEYOwVaABwAXgAgAFyiAHLApIBAzAuM5gBAKABAcABAQ&sclient=gws-wiz-serp')

bitcoin = navegador.find_element('xpath',
                                 '//*[@id="crypto-updatable_2"]/div[3]/div[5]/div[2]/input').get_attribute('value')

print(f'Valor do bitcoin: {bitcoin}')

@bot.command(name='bitcoin')
async def send_hello(ctx):
    name = ctx.author.name
    response = name  +  ' O valor do Bitcoin atualmente é  ' + str(emoji.emojize(':dollar:''R$:')) + bitcoin
    await ctx.send(response)







intents = discord.Intents.default()
client = discord.Client(intents=intents)
bot.run('TOKEN DO BOT')
