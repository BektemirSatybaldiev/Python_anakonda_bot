from aiogram import Bot, Dispatcher, executor
from config_data.config import load_config
from handlers.user_handlers import process_start_command, process_car_answer, process_main_menu

config = load_config('E:\Python_anakonda_bot\.env')

API_TOKEN: str = config.tg_bot.token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_car_answer, text=['тойота_приус', 'хонда_фит',
                                                      'тойота_раум', 'тойота_ист'])
dp.register_message_handler(process_main_menu, commands=['help', 'support',
                                                         'contacts', 'payments'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
