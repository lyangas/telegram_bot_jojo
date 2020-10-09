import telebot
from telebot import apihelper
import pandas as pd

replicas = [
    'ты проходишь возле рынка.\nпройти мимо?',
    'ты проходишь мимо, но тут тебя подозвал к себе какой-то неперсточник-цыган. \nсыграть с ним?',
    'опаа, а тут на самом входе сидит некоторый тип цыганской наружности и играет в наперстки! \nсыграть с ним?',
    'он сказал что у тебя плохая прическа. но ты гребаный Жоский Жоске и у тебя просто не осталось выбора после такой дерзости!',
    'он кладет шарик под 3-й стаканчик. затем меняет местами 2 и 1. \nшарик в стаканчике номер 3?',
    'ай маладца! какой красавчик у нас играит!\n\nты поставил на кон мамку.\n\nтеперь он кладет шарик под 1-й стаканчик. затем меняет местами 1 и 2. \nшарик в стаканчике номер 1?',
    'ха, лох.\n\nно ты не отчаиваешься и ставишь на кон мамку.\n\nтеперь он кладет шарик под 1-й стаканчик. затем меняет местами 1 и 2. \nшарик в стаканчике номер 1?',
    'ШТООО?! невозможно!ты жулик! - кричит тебе маэстро наперстков, - вызываю тебя на бой! он разъяренно разбивает бутылку водяры о голову и несется на тебя!\n\nударим его своим стояком по лицу?',
    'а нет, не угадал :) давай сыграем еще разочек, дорогой? ну, золотой раунд как-никак ;)\n\nтеперь он кладет шарик под 2-й стаканчик. затем меняет местами 3 и 2. \n\nшарик в стаканчике номер 2?',
    'ты проиграл. гони мамашу ;) - сказала эта крыса. мы такое не прощаем, Жоске такое не прощает. ты вызываешь его на бой!\n\nоднако, цыган не сильно расстроен и полный напора и уверенности разбивает бутылочку водяры об голову и уже мчится на тебя в своей тельняшке\n\nударим его своим стояком по лицу?',

    'я призываю свой стояк! Коцаный Янтарь - удар кула.....КХ!\nтебя ударили в поддых прежде чем ты завершил свою великолепную атакующую фразу! как он успел??\n\nи тут ты заметил, что рядом валяется бита - схватить ее для удара? из альтернатив - ты можешь рассказать шарлотану о его мамаше...',
    'я призываю свой стояк! Коцаный Янтарь - удар кулаком!!! \n\nнаперсточник говорит:\nУХ, мать, как большо ты шлепнул мне по щеке своим стояком! ты опасный поц!\n\nи тут ты заметил, что рядом валяется бита - схватить ее для удара? из альтернатив - ты можешь рассказать шарлотану о его мамаше...',
    'ты хорошенько погладил его битой по голове\n\nКАК ТЫ ЭТО ДЕЛАЕШЬ???!! прекрати немедленно! - кричит шуллер\n\nты всего на секунду отвлекся на аквариум с черепахами в соседнем прилавке, как вдруг - машенник пропал!\n\nобернуться назад?',
    '...но и тут он оказывается быстрее тебя и мнгновенно хватает эту биту и бъет тебя в поддых!\n\nты всего на секунду отвлекся на аквариум с черепахами в соседнем прилавке, как вдруг - машенник пропал!\n\nобернуться назад?',
    'твоя мамка-цыганка! - крикнул ты этому типу и его лицо залилось красным цветом! переполняемый эмоциями, он кричит тебе: \n\nвообще-то, это расизм, больной ты ублюдок! и как ты посмел такое сказать про эту великолепную женщину, которая с детства дает мне столько заботы, добра и побоев! она взрастила из меня законопослушного гражданина, который встает каждый день с одной мысью: надо нести людям счастье... не по 1000р за грамм, а за 900р! а ну забери слова обратно!\n\nты всего на секунду отвлекся на аквариум с черепахами в соседнем прилавке, как вдруг - машенник пропал!\n\nобернуться назад?',
    'ты обернулся и видишь как он берет биту из отдела "все для домашнего уюта", и со всей силы бъешь его  МУДА-МУДА-МУДА!\nон лежит на асфальте перед тобой, напуганный...\n\nспросишь его о силе его стояка?',
    'ты обернулся и тут же получил удар по голове! откуда он взялся? - эта мысль уже не проскочит в твоей голове, так как ты лежишь без сознания. THE END',
    'ты видишь, как он выскакивает из-за соседнего прилавка и летит не тебя с испуганными глазами! ты не растерялся: бъешь его что есть мочи - теперь он лежит на асфальте.\n\nспросишь его о силе его стояка?',
    'внезапный удар по голове сзади кладет тебя не только на асфальт, но и в больницу на ближайшие пол года.',
    'ты накланяешься к нему, чтобы разобрать что он там бормочит... и... УДАР В ТВОЙ НОС! - он вырубил тебя и скрылся',
    'только не надо больше меня избивать! да, сила моего стояка "Золотые Купола" в том, что после удара по голове я предвижу ближайшие 30 секунд и знаю, что будет происходить наперед...\n\nай да маладца ты! все разгадал, жижафаг! THE END',
    'он молит о пощаде и убегает в даль... THE END',
    'не верный ответ - Жоские Жоски не покидают поле битвы просто так\n\nударим его своим стояком по лицу?'
]
relations = {
    0: {'да': 1,'нет':2},
    1: {'да': 4,'нет':3},
    2: {'да': 4,'нет':3},
    3: {'да': 4,'нет':3},
    4: {'да': 5,'нет':6},
    5: {'да': {'да': 7,'нет':8},'нет':{'да': 7,'нет':8}},
    6: {'да': {'да': 7,'нет':9},'нет':{'да': 7,'нет':9}},
    7: {'да': {'да': 11,'нет':10},'нет':{'да': 22,'нет':22}},
    8: {'да': {'да': 7,'нет':9},'нет':{'да': 7,'нет':9}},
    9: {'да': {'да': 11,'нет':10},'нет':{'да': 22,'нет':22}},
    10: {'да': {'да': 12,'нет':13},'нет':{'да': 14,'нет':14}},
    11: {'да': {'да': 12,'нет':13},'нет':{'да': 14,'нет':14}},
    12: {'да': {'да': 15,'нет':16},'нет':{'да': 17,'нет':18}},
    13: {'да': {'да': 15,'нет':16},'нет':{'да': 17,'нет':18}},
    14: {'да': {'да': 15,'нет':16},'нет':{'да': 17,'нет':18}},
    15: {'да': {'да': 20,'нет':19},'нет':21},
    16: None,
    17: {'да': {'да': 20,'нет':19},'нет':21},
    18: None,
    19: None,
    20: None,
    21: None,
    22: {'да': {'да': 11,'нет':10},'нет':{'да': 22,'нет':22}}
}

import time

class MyTimer():
    def __init__(self):
        self.last_time_moment = time.time()
        self.threshhold = 30

    def get_time_delta(self, last_time):
        return int(time.time() - last_time)

    def update_last_time_moment(self, dialogue):
        dialogue['time'] = time.time()

    def delta_smaller_then_threshold(self, dialogue):
        last_time = dialogue['time']
        if self.get_time_delta(last_time) > self.threshhold:
            dialogue['time'] = time.time()
            return 'да'
        else:
            dialogue['time'] = time.time()
            return 'нет'

def get_next_replic(index, choice, dialogue):

    next_index = relations[index]

    if next_index == None:
        return 0

    user_input = choice

    if type(next_index[user_input]) == dict:
        delta_smaller_then_threshold = my_timer.delta_smaller_then_threshold(dialogue)
        index = next_index[user_input][delta_smaller_then_threshold]
    else:
        index = next_index[user_input]
    my_timer.update_last_time_moment(dialogue)

    return index


my_timer = MyTimer()
attempt_count = 0
index_of_ip = 0


bot = telebot.TeleBot('1215716564:AAEhpwiQgSMX912DUmPBrutF-o2DaywpG0U')

dialogues = {}

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Да', 'Нет', 'Начать с начала')

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        dialogues[message.chat.id]
    except Exception:
        dialogues[message.chat.id] = {}
        pass
    dialogues[message.chat.id]['index'] = 0
    dialogues[message.chat.id]['time'] = time.time()
    dialogues[message.chat.id]['score'] = 0
    bot.send_message(message.chat.id, 'ну, начнем :)', reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'ты проходишь возле рынка.\nпройти мимо?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        # если решил начать чат с начала по своей воле
        if 'начать с начала' in message.text.lower():
            bot.send_message(message.chat.id, 'ты проходишь возле рынка.\nпройти мимо?', reply_markup=keyboard1)
            dialogues[message.chat.id] = {}
            dialogues[message.chat.id]['index'] = 0
            dialogues[message.chat.id]['time'] = time.time()
            dialogues[message.chat.id]['score'] = 0
            return

        # если оказался в начале истроии так как закончил ее
        if dialogues[message.chat.id]['index'] == 0:
            dialogues[message.chat.id]['score'] = 0

        if 'да' in message.text.lower():
            if dialogues[message.chat.id]['index'] in [5, 7, 11, 12, 15, 17]:
                dialogues[message.chat.id]['score'] += 1

            if dialogues[message.chat.id]['index'] in [15, 17]:
                if dialogues[message.chat.id]['score'] < 4:
                    dialogues[message.chat.id]['time'] = time.time()
            
            choice = 'да'
        if 'нет' in message.text.lower():
            choice = 'нет'
        if choice in ['да','нет']:
            index = dialogues[message.chat.id]['index']
            dialogue = dialogues[message.chat.id]
            dialogues[message.chat.id]['index'] = get_next_replic(index, choice, dialogue)
            
            answer = replicas[dialogues[message.chat.id]['index']]
            bot.send_message(message.chat.id, answer)
        '''for answer_msg in answer.split('\n\n'):
            bot.send_message(message.chat.id, answer_msg)'''
    except KeyError:
        dialogues[message.chat.id] = {}
        dialogues[message.chat.id]['index'] = 0
        dialogues[message.chat.id]['time'] = time.time()
        dialogues[message.chat.id]['score'] = 0

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True)
