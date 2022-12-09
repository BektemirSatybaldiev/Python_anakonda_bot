from aiogram import Dispatcher, types


async def set_main_menu(dp: Dispatcher):
    # Создаем список с командами для кнопки menu
    main_menu_commands = [
        types.BotCommand(command='/help', description='Справка по работе бота'),
        types.BotCommand(command='/support', description='Поддержка'),
        types.BotCommand(command='/contacts', description='Другие способы связи'),
        types.BotCommand(command='/payments', description='Платежи')
    ]
    await dp.bot.set_my_commands(main_menu_commands)