from aiogram.utils.keyboard import ReplyKeyboardBuilder


def type_buttons():
    btn = ReplyKeyboardBuilder()
    btn.button(text='🇺🇸 1 AQSH dollori , USD')
    btn.button(text='🇷🇺 1 ROSSIYA rubli , RUB')
    btn.button(text='🇪🇺 1 Yevro , EUR')
    btn.button(text='🇬🇧 1 Angliya funt sterlingi, GBP')
    btn.button(text='🇯🇵 1 Japoniya iyenasi , JPY')
    btn.button(text='🇨🇳 1 Xitoy yuani , CNY')
    btn.button(text='🇰🇷 Korea respublikasi voni , KRW')
    btn.button(text='🇹🇷 Turkiya lirasi , TRY')
    btn.adjust(2)
    return btn.as_markup(resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Valyutani tanlang:')
