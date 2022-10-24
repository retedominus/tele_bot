import logging
from calc import excep, operation, rational, complex
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from service_info import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

NUM_TYPE, OPERATION, RESULT, MENU = range(4)

n_type = ''
oper = ''
num = ''
res = ''


def start(update, _):
    reply_keyboard = [['Рациональные', 'Комплексные']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        f'Приветствую, {update.effective_user.first_name}'
        'Добро пожаловать в калькулятор! '
        'Команда /cancel, чтобы прекратить работу.\n\n'
        'Выберите, с какими числами будете работать',
        reply_markup=markup_key, )
    return NUM_TYPE


def num_type(update, _):
    global n_type
    user = update.message.from_user
    n_type = user
    logger.info("Тип числа %s: %s", user.first_name, update.message.text)
    reply_keyboard = [['Сложение', 'Вычетание', 'Умножение', 'Деление',
                       'Возведение в степень', 'Извлечение корня']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Теперь выберите операцию ',
        reply_markup=markup_key, )
    return OPERATION


def operation(update, _):
    global oper
    user = update.message.from_user
    oper = user
    logger.info("Операция %s: %s", user.first_name, update.message.text)
    if n_type == 'Комплексные':
        update.message.reply_text('Комплексное число имеет вид A+Bi, где A и B – действительные числа, '
                                  'i – так называемая мнимая единица'
                                  'Введите 4 действительных числа, по два для каждого комплексного',
                                  reply_markup=ReplyKeyboardRemove(), )
    else:
        update.message.reply_text(
            'Хорошо! Теперь введите 2 числа через пробел',
            reply_markup=ReplyKeyboardRemove(), )
    return RESULT


def result(update, _):
    global num
    global res
    user = update.message.from_user
    num = excep.check_input_data(user)
    logger.info("Пользователь %s ввел:", user.first_name, update.message.text)
    if n_type == 'Рациональные':
        res = rational.calc(oper, num)
    else:
        res = complex.calc(oper, num)

    update.message.reply_text(
        f'Вот, что у меня получилось {res}'
        f'{update.effective_user.first_name} желаете еще что-то посчитать?'
    )
    return MENU


def menu(update, _):
    user = update.message.from_user
    logger.info(
        "Результат %s: %s", res)
    if user.capitalize() == 'Да' or 'Yes':
        return start()
    else:
        cancel()
    return MENU


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s остановил работу калькулятора.", user.first_name)
    update.message.reply_text(
        'Будет необходимо что-то посчитать, заходи.',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NUM_TYPE: [MessageHandler(Filters.regex('^(Рациональные|Комплексные)$'), num_type())],
            OPERATION: [MessageHandler(Filters.regex('^(Сложение|Вычетание|Умножение|Деление|Возведение в степень|'
                                                     'Извлечение корня)$'), operation())],
            RESULT: [
                MessageHandler(Filters.text, result())
            ],
            MENU: [MessageHandler(Filters.text, menu())],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
