import logging
import time
from aiogram import Bot, Dispatcher, executor, types
import Parser
# Включаем логирование, чтобы не пропустить важные сообщения

def PyBot():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="5530067632:AAGl1BTcnfWQPX3N_qQgx9vXc3wKX2KPIDI")  # Объект бота
    dp = Dispatcher(bot)  # Диспетчер
    spisok = [0,0]
    spisok2 = ['0','0']
    @dp.message_handler(commands=['start', 'help'])
    async def process_start_command(message: types.Message):
        await message.reply(
            "Бот отслеживания курса валютной пары \nUSD/RUB на Московской бирже.\nТорги открываются в 7:00 по"
            " московскому времени.\nТорги закрываются в 19:00 по московскому времени.\nВы можете установи"
            "ть границы курса до 4 знаков после запятой, при выходе из которых вы получите уведомление.\nДос"
            "тупные команды:\n/start\n/help\nLimitedCourse\n/CourseOfDollar")
    @dp.message_handler(commands=['LimitedCourse'])
    async def handle_message(message: types.Message):
        await message.reply("Введите верхний предел, а следующим сообщением нижний предел")
        @dp.message_handler()
        async def handle_message(message: types.Message):
            UpperLimit = message.text
            spisok[0] = UpperLimit
        @dp.message_handler()
        async def handle_message(message: types.Message):
            DownLimit = message.text
            spisok[1]= DownLimit

            f = open('limits.txt', 'w')
            for element in spisok:
                f.write(str(element))
                f.write('\n')
            f.close()
            f = open('limits.txt', 'r')
            lines = f.readlines()
            for line in lines:
                spisok2.append(line)
        while (Parser.parse() < float(spisok2[0]) and Parser.parse() > float(spisok2[1])):
            print(Parser.parse())
            time.sleep(2)
        if (Parser.parse() < float(spisok2[1])):
            await message.reply('Курс доллара вышел за нижний предел!')
        else:
            await message.reply('Курс доллара вышел за верхний предел!')
    @dp.message_handler(commands=['CourseOfDollar'])
    async def process_start_command(message: types.Message):
        await message.answer("1 доллар равен " + str(Parser.parse()) + " рублей")
    executor.start_polling(dp, skip_updates=True)