from khl import *
from random import randint

bot = Bot(token='1/MjI3NTE=/fjEPJ0zRImyYGvhdb/9eCw==')


@bot.command(name='投骰子')
async def rollDice(msg: Message):
    randNumber = randint(1, 6)
    await msg.reply('您掷出的点数是：' + str(randNumber))

bot.run()
