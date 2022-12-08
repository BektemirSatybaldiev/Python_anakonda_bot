from aiogram import Bot, Dispatcher, executor
from config_data.config import load_config
from handlers.user_handlers import process_start_command, process_toyota_ist_answer, process_honda_fit_answer, \
    process_toyota_raum_answer, process_toyota_prius_answer

config = load_config('E:\Python_anakonda_bot\.env')

API_TOKEN: str = config.tg_bot.token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_toyota_ist_answer, text='toyota_ist')
dp.register_message_handler(process_honda_fit_answer, text='honda_fit')
dp.register_message_handler(process_toyota_raum_answer, text='toyota_raum')
dp.register_message_handler(process_toyota_prius_answer, text='toyota_prius')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)