import asyncio
from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="🏆 Let's click", web_app=WebAppInfo(
        url="https://0c23-5-130-111-72.ngrok-free.app"
    ))
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(
        "Click! Click! Click!",
        reply_markup=webapp_builder()
    )


async def main() -> None:
    # Инициализируем бота с использованием DefaultBotProperties
    bot = Bot(
        token="7935845098:AAH-ChqONyi9smG6doR8uijqdh8rNbrPmqo",
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=AiohttpSession()
    )

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


# Запускаем асинхронное выполнение
if __name__ == "__main__":
    asyncio.run(main())
