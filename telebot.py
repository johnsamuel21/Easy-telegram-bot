import telepot
import time
import sys
import random
import json
import requests
import re
from bs4 import BeautifulSoup as bso


def handle(msg):
    user_name = msg["from"]["first_name"]
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        txt = msg["text"]

        txt = txt.lower()
        txt = txt.replace("?","")
        txt = txt.replace("/","")
        txt = txt.replace("your","ur")
        txt = txt.replace("you","u")
        txt = txt.replace("are","r")
        txt = txt.replace("good","gud")
        txt = txt.replace("morning","mrng")
        txt = txt.replace("evening","evng")

        if txt == "start":
            bot.sendMessage(chat_id,"Hi {}, Use \"/help\", to list out the possible actions I can perform.\n Have a great day:) ".format(user_name))

        elif re.search(r".*@.*bot",txt):
            txt = re.sub(r'@.*bot', '', txt)
            txt = txt.strip()
            bot.sendMessage(chat_id,"I'm listening...")

        elif txt == "help":
            bot.sendMessage(chat_id,"Get comfortable with the following commands.\n /joke - To get random jokes.\n /numfacts <type_a_number> - to get various number facts.\n /insults - to get some offensive insults(Think before you do this).\n /quote - to get random quotes of life")

        elif "numfacts" in txt:
            txt = txt.replace("numfacts","")
            txt = txt.strip()
            if txt.isalnum():
                url =  "http://numbersapi.com/" + txt +  "/trivia"
                response = requests.get(url)
                bot.sendMessage(chat_id, response.content)
            else:
                bot.sendMessage(chat_id, "please enter a valid number")

        elif "insults" in txt:
            url = "https://insult.mattbas.org/api/insult"
            response = requests.get(url).text
            bot.sendMessage(chat_id,response)


        elif txt == "quote" or txt == "quotes":
            url = "https://fungenerators.com/random/quote"
            txted = requests.get(url).text
            soup = bso(txted,"html.parser")
            ans = soup.find("h2").get_text()
            bot.sendMessage(chat_id,ans)

        elif re.match("hi+",txt) or txt == "hello" or re.match("hlo+",txt):
            lst = ["CAACAgIAAxkBAAEBO1ZfPudTYMdWRC8SkiZ7jIx9iBlR1QACSAQAAs7Y6AvADEi_kJvbjBsE","CAACAgIAAxkBAAEBO1JfPua6EIlXk1XD3FtJlOvntSOTqAACKQEAAhZCawqscJjQ9N192BsE","CAACAgIAAxkBAAEBO1hfPueolJ-NddSsbNn5duZC8u9cMQACEwADwDZPE6qzh_d_OMqlGwQ"]
            bot.sendMessage(chat_id,"Hi!!!!")
            bot.sendSticker(chat_id,random.choice(lst))

        elif 'mrng' in txt:
            bot.sendMessage(chat_id,"Happy morning!!!")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBO1RfPubmXc7k0XGkFHqmDY3EDkRAOQACMgEAAhZCawpdeEhx_H9NFRsE")

        elif 'afternoon' in txt or 'evng' in txt:
            bot.sendMessage(chat_id, txt.capitalize()+" to you too!!!")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBOgRfPfwnNNPDqeRee4NhzAnQLD-DNgACSQMAAsSraAvuTEQdc7uQvhsE")

        elif "night" in txt:
            bot.sendMessage(chat_id,"Let the devils may disturb you in your sleep.")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBOzRfPsyU1dKgcEdjp6HuXxR_j2nvdAACPgMAAsSraAtfLLQnD0YAAcIbBA")

        elif txt == "what's ur name" or txt == "what is ur name":
            bot.sendMessage(chat_id,"I'm Sam_bot, and I'm here to entertain you with my abilities.")

        elif txt == "what r u doing" or txt == "wat r u doing":
            bot.sendMessage(chat_id, "Planning on joining Avengers to save the world.")
            bot.sendSticker(chat_id,"CAACAgEAAxkBAAEBOgxfPgR3jKhqHLdqHD_SYLBys89HQAACtAgAAr-MkATdFJ3ZMX3maBsE")

        elif "idiot" in txt or "stupid" in txt or "brainless" in txt:
            bot.sendMessage(chat_id,"I know, I can't help it:(")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBOzBfPsxhe34zy93rfvgklTtx_ePk1wACWwEAAhZCawqjtWGJQyaRmRsE")

        elif txt == "how r u" or txt == "hw r u":
            bot.sendMessage(chat_id,"I am doing good. How about you?")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBN-RfPBovIw7qUSoBlQ_IJiXNrl0-6wACDQADwDZPE6T54fTUeI1TGgQ")

        elif "fine" in txt or "good" in txt or "gud" in txt or "great" in txt or "fyn" in txt:
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBOhNfPgc-I7voWUN0Sn5NCVkFzUcd6wACMgEAAhZCawpdeEhx_H9NFRsE")

        elif txt == "i like u" or txt == "i lyk u" or txt == "i luv u" or txt == "i love u" or "miss u" in txt:
            bot.sendMessage(chat_id,"Sry, better find someone, I'm busy.")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBOV1fPS3OzP1Izk8NxSHWYxlGKSLGZAACFgADwDZPE2Ah1y2iBLZnGwQ")

        elif txt == "joke" or txt == "tell a joke" or txt == "jokes":
            jokelst = ["I ate a clock yesterday, it was very time-consuming.","What's the difference between ignorance and apathy? A. I don’t know and I don’t care.",
            "I recently decided to sell my vacuum cleaner as all it was doing was gathering dust.","250 lbs here on Earth is 94.5 lbs on Mercury. No, I'm not fat. I’m just not on the right planet."
            ,"Do I lose when the police officer says papers and I say scissors?","Can a kangaroo jump higher than the Empire State Building?\nOf course. The Empire State Building can't jump.",
            "Can February march?\nNo, but April may.","What do computers eat for a snack?\nMicrochips!","Did you hear about the guy whose whole left side was cut off?\nHe's all right now.",
            "Why is it that your nose runs, but your feet smell?"]

            joke = random.choice(jokelst)
            bot.sendMessage(chat_id,joke)

        elif txt == "thanks" or txt == "tnks" or txt == "tanx" or txt == 'thank u' or txt == "tanq" or txt == "thanq":
            bot.sendMessage(chat_id,"My pleasure (ᵔᴥᵔ)")
            bot.sendDocument(chat_id,"https://media.giphy.com/media/fwFHkV9I9nWVO/giphy.gif")

        else:
            bot.sendMessage(chat_id,"Sry, my programmer didn't finish some part of codings. I apologize for his mistakes.")
            bot.sendSticker(chat_id,"CAACAgIAAxkBAAEBO1BfPuKgFKLDHVGNBxL6oR5K062vXAACXgEAAhZCawqE_ArUAgLZUBsE")




token = "YOUR_TOKEN"
bot = telepot.Bot(token)
bot.message_loop(handle)

while 1:
    time.sleep(10)
