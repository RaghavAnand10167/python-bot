
import requests,re
from hh import keep_alive
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from GATEAU import Tele
from colorama import Fore
sto = {"stop":True}
dollar=10
token = "6615542930:AAH0uFl1lgloDmhhwbCmPjW5Jl-3bADbxgk" 
id =  5173016128
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["stop"])
def start(message):
    sto.update({"stop":True})
    bot.reply_to(message,'𝐼 𝑠𝑡𝑜𝑝𝑝𝑒𝑑 𝑡𝒉𝑒 𝑐𝑜𝑚𝑏𝑜 𝑓𝑜𝑟 𝑦𝑜𝑢, 𝑤𝑖𝑡𝒉 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛. 𝑊𝑎𝑖𝑡 10𝑠')
@bot.message_handler(commands=["start"])
def start(message):
 bot.send_message(message.chat.id,"   ဘော့တ်မှကြိုဆိုပါတယ်။ \n  𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗕𝗼𝘁  \n  𝐘𝐨𝐮 𝐚𝐫𝐞 𝐂𝐨𝐦𝐛𝐨 𝐭𝐱𝐭 𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝 𝐍𝐨𝐰".format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
@bot.message_handler(content_types=["document"])
def main(message):
 first_name = message.from_user.first_name
 last_name = message.from_user.last_name
 name=f"{first_name} {last_name}"
 fe=0
 bad=0
 nok=0
 ok = 0
 last=0
 risk=0
 ko = (bot.reply_to(message,f" 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 {name} 𝙄 𝙒𝙄𝙇𝙇 𝙉𝙊𝙒 𝙎𝙏𝘼𝙍𝙏 𝘾𝙃𝙀𝘾𝙆").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":True})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == True:
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
           	req=requests.get(url).json()
           except:
           	pass
           try:
           	inf = req['scheme']
           except:
           	inf = "------------"
           try:
           	type = req['type']
           except:
           	type = "-----------"
           try:
           	brand = req['brand']
           except:
           	brand = '-----'
           try:
           	info = inf + '-' + type + '-' + brand
           except:
           	info = "CREDIT-CORPORATE"
           try:
           	ii = info.upper()
           except:
           	ii = "----------"
           try:
           	bank = req['bank']['name'].upper()
           except:
           	bank = "CAPITAL ONE"
           try:
           	do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
           	do = "-----------"
           mes = types.InlineKeyboardMarkup(row_width=1)
           JOKER1 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u8')
           res = types.InlineKeyboardButton(f"• {last} •",callback_data='u1')
           JOKER3 = types.InlineKeyboardButton(f"• 𝗛𝗜𝗧𝗦 ✅: : [ {ok} ] •",callback_data='u2')
           JOKER4 = types.InlineKeyboardButton(f"• 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  : [ {bad} ] •",callback_data='u1')
           risk6 = types.InlineKeyboardButton(f"• 𝗖𝗖𝗡 ❎: [ {fe} ] •",callback_data='u1')
           JOKER5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 🇲🇲  : [ {total} ] •",callback_data='u1')
           mes.add(res,JOKER1,JOKER3,JOKER4,risk6,JOKER5)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=f''' 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ  {name}, 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗰𝗮𝗿𝗱...⌛💸
    ''',parse_mode='markdown',reply_markup=mes)
           
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"𝑪𝑨𝑹𝑫 𝑰𝑺 𝑫𝑬𝑨𝑫 𝑨𝑵𝑫 𝑰 >> {cc}")
           if "risk" in last:
           	risk += 1
           	print(Fore.YELLOW+cc+"->"+Fore.CYAN+last)
           elif "Your card has insufficient funds." in last or "success" in last:
               ok +=1
               respo = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ <code>{cc}</code>
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ {dollar}$</code>
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{ii}</code>
[↯] 𝗕𝗮𝗻𝗸: <code>{bank}</code>
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{do}</code>
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: <a href='t.me/X1_H9'> </a>
[↯] 𝗣𝗥𝗢𝗫𝗬 : <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
──────────────────
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ <code>{cc}</code>
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ {dollar}$</code>
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{ii}</code>
[↯] 𝗕𝗮𝗻𝗸: <code>{bank}</code>
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{do}</code>
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: <a href='t.me/X1_H9'> </a>
[↯] 𝗣𝗥𝗢𝗫𝗬 : <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
──────────────────
''')
           elif "Your card's security code is" in last:
               fe +=1
               ggg = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ <code>{cc}</code>
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>CCN CHARGE {dollar}$</code>
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{ii}</code>
[↯] 𝗕𝗮𝗻𝗸: <code>{bank}</code>
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{do}</code>
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: <a href='t.me/X1_H9'> </a>
[↯] 𝗣𝗥𝗢𝗫𝗬 : <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
──────────────────
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,ggg)
               with open("hit.txt", "a") as f:
               	f.write(f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ <code>{cc}</code>
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>CCN CHARGE {dollar}$</code>
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{ii}</code>
[↯] 𝗕𝗮𝗻𝗸: <code>{bank}</code>
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{do}</code>
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: <a href='t.me/X1_H9'> </a>
[↯] 𝗣𝗥𝗢𝗫𝗬 : <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
──────────────────
''')
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.RED+last)
       if sto["stop"] == False:
           bot.reply_to(message,'🇲🇲')
 else:
     bot.reply_to(message,'𝗬𝗼𝘂 𝗡𝗼𝘁 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗨𝘀𝗲𝗿 😢😢              /   💸𝗣𝗮𝗶𝗱 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗣𝗹𝗮𝗻  \n DM @X1_H9')
keep_alive()
print("STARTED BOT @X1_H9")
bot.infinity_polling()
