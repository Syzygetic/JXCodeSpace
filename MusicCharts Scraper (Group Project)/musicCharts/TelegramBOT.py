import telebot
import logging
import configOOP
import time
from csv import reader
from telebot import types

# Bot Token
bot = telebot.TeleBot(configOOP.telegram_key)

# Store temporary user information (user ID)
dic_user = []

# Icons
dice = u"\U0001f3b2"
mahjong = u"\U0001F000"
mahjongm = u"\U0001f004"
musicNote = u"\U0001F3B6"
heart = u"\u2764"
man = u"\U0001f9cd"
woman = u"\U0001f9cd\u200D\u2640\uFE0F"

# keyboard buttons lists
startList = ["Spotify", "Billboard", "Spotify VS Billboard"]
spotifylist = ["Top 10 Ranking", "Top Artist Statistic",
               "Top 10 Stream", "Weekly Stream"]
billboardList = ["Top 10 Ranking", "Top Artist Statistic"]

# Open Billboard file and write value to array
songNameBillboard = []
artistNameBillboard = []
top = 0
with open("exports/billboard.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            songNameBillboard.append(row[2])
            artistNameBillboard.append(row[3])
            top += 1
            if top == 10:
                break

# Open Spotify file and write value to array
spotsongName = []
spotsongNameFeq = []
spotartistName = []
spotartistNameFeq = []
with open("exports/spotifyFeq.csv", "r", encoding="utf-8") as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            spotsongName.append(row[0])
            spotsongNameFeq.append(row[1])
            spotartistName.append(row[2])
            spotartistNameFeq.append(row[3])

# Open Spotify weekly file and write value to array


def spotifyStreamWeekly(week):
    week = int(week)
    if week > 1:
        week = 3 * week + (week - 1)
    else:
        week = 3
    spotstreamWeekly = []
    with open("exports/spotifyTop.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                spotstreamWeekly.append(row[week])
    return spotstreamWeekly


# logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def startKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in startList:
        markup.add(types.InlineKeyboardButton(text=value, callback_data=value))
    return markup


def billboardchoiceKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in billboardList:
        markup.add(types.InlineKeyboardButton(
            text=value, callback_data=value + " B"))
    return markup


def spotifychoiceKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in spotifylist:
        markup.add(types.InlineKeyboardButton(
            text=value, callback_data=value + " S"))
    return markup


def comparechoiceKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in billboardList:
        if value == "Top Artist Statistic":
            break
        markup.add(types.InlineKeyboardButton(
            text=value, callback_data=value + " C"))
    return markup


def rankspotifyKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(
                   text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Artist " + woman, callback_data="none"))
    for value in spotsongName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(
                           text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=spotartistName[count-1], callback_data="none"))
        else:
            break
    return markup


def rankBillboardKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(
                   text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Artist " + woman, callback_data="none"))
    for value in songNameBillboard:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(
                           text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=artistNameBillboard[count-1], callback_data="none"))
        else:
            break
    return markup


def rankVSKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(
                   text=musicNote + " Spotify " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Billboard " + woman, callback_data="none"))
    for value in songNameBillboard:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(
                           text=spotsongName[count-1], callback_data="none"),
                       types.InlineKeyboardButton(text=value, callback_data="none"))
        else:
            break
    return markup


def streamSpotifyKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(
                   text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Stream " + woman, callback_data="none"))
    for value in spotsongName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(
                           text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=spotsongNameFeq[count-1], callback_data="none"))
        else:
            break
    return markup


def weeklystreamSpotifyKeyboardButtons(week):
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    stream = spotifyStreamWeekly(week)
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(
                   text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Stream " + woman, callback_data="none"))
    for value in songNameBillboard:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(
                           text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=stream[count-1], callback_data="none"))
        else:
            break
    return markup


@bot.message_handler(commands=["start"])
def _start(message):
    msg = dice*8 + "\n\nData Science Music Bot!\n\n" + dice*8
    bot.send_message(message.chat.id, msg,
                     reply_markup=startKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["billboardchoice"])
def billboardchoice(message):
    msg = dice*8 + \
        "\n\n [Billboard]\nChoose one of the following: \n\n" + dice*8
    bot.send_message(message.chat.id, msg,
                     reply_markup=billboardchoiceKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["spotifychoice"])
def spotifychoice(message):
    msg = dice*8 + "\n\n [Spotify]\nChoose one of the following: \n\n" + dice*8
    bot.send_message(message.chat.id, msg,
                     reply_markup=spotifychoiceKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["comparechoice"])
def comparechoice(message):
    msg = dice*8 + "\n\n Spotify VS Billboard\n\n" + dice*8
    bot.send_message(message.chat.id, msg,
                     reply_markup=comparechoiceKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["toprankspot"])
def toprankSpotify(message):
    msg = dice + " Spotify Top Rank " + dice
    bot.send_message(message.chat.id, msg,
                     reply_markup=rankspotifyKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["toprankbillboard"])
def toprankBillboard(message):
    msg = dice + " Top 10 Songs for the week! " + dice
    bot.send_message(message.chat.id, msg,
                     reply_markup=rankBillboardKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["topvs"])
def toprankvs(message):
    msg = "Top 10 Songs for the week!"
    bot.send_message(message.chat.id, msg,
                     reply_markup=rankVSKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["artiststatsbillboard"])
def topartiststatsBillboard(message):
    bot.send_message(message.chat.id, dice +
                     " Top 5 Artists for the week! " + dice)
    bot.send_photo(message.chat.id, photo=open(
        "exports/images/topArtistbillboard.png", "rb"))


@bot.message_handler(commands=["topartiststatsspotify"])
def topartiststatsSpotify(message):
    bot.send_message(message.chat.id, dice +
                     " Top 5 Songs for the week! " + dice)
    bot.send_photo(message.chat.id, photo=open(
        "exports/images/topSongspotify.png", "rb"))
    bot.send_message(message.chat.id, dice +
                     " Top 5 Artists for the week! " + dice)
    bot.send_photo(message.chat.id, photo=open(
        "exports/images/topArtistspotify.png", "rb"))


@bot.message_handler(commands=["topstreamspotify"])
def topStreamSpotify(message):
    msg = "Top 10 Streaming for past 10 weeks"
    bot.send_message(message.chat.id, msg,
                     reply_markup=streamSpotifyKeyboardButtons(), parse_mode="HTML")


@bot.message_handler(commands=["topweeklystreamspotify"])
def topWeeklyStreamSpotify(message, week):
    msg = "Week " + week + " Streaming"
    bot.send_message(message.chat.id, msg, reply_markup=weeklystreamSpotifyKeyboardButtons(
        week), parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith("Spotify VS Billboard"):
        comparechoice(query.message)
    elif data.startswith("Spotify"):
        spotifychoice(query.message)
    elif data.startswith("Billboard"):
        billboardchoice(query.message)
    elif data.startswith("Top 10 Stream S"):
        topStreamSpotify(query.message)
    elif data.startswith("Weekly Stream"):
        msg = "Please select which week"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            text="Current Week 1", callback_data="1"))
        for i in range(2, 5):
            markup.add(types.InlineKeyboardButton(text="Week " + str(i), callback_data=str(i)),
                       types.InlineKeyboardButton(
                           text="Week " + str(i+3), callback_data=str(i+3)),
                       types.InlineKeyboardButton(text="Week " + str(i+6), callback_data=str(i+6)))
        bot.send_message(query.message.chat.id, msg,
                         reply_markup=markup, parse_mode="HTML")
    elif data.startswith("Top 10 Ranking S"):
        toprankSpotify(query.message)
    elif data.startswith("Top 10 Ranking B"):
        toprankBillboard(query.message)
    elif data.startswith("Top 10 Ranking C"):
        toprankvs(query.message)
    elif data.startswith("Top Artist Statistic S"):
        topartiststatsSpotify(query.message)
    elif data.startswith("Top Artist Statistic B"):
        topartiststatsBillboard(query.message)
    else:
        for i in range(1, 11):
            if data == str(i):
                topWeeklyStreamSpotify(query.message, str(i))


while True:
    try:
        bot.infinity_polling(True)
    except:
        time.sleep(1)
