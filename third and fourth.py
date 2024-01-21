import datetime
import sqlite3
import telebot

bot = telebot.TeleBot('6644961310:AAFOQDHbqBVoYH9C3PKGv6n0nrz1ltPR7JI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f"Hello!{message.from_user.username} it's my trial bot.\nSend me message which starting with <Strattonbot+>")
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS information(id auto_increment primary key,bot_text text,data_del date)')
    conn.commit()
    cur.close()
    conn.close()
@bot.message_handler()
def echo(message):
    if message.text.startswith("Strattonbot+"):
        reply_text = f"{message.text.replace('Strattonbot+','')}"
        cur_date = datetime.datetime.now().strftime("%Y-%m-%d")
        bot.send_message(message.chat.id,f" your text: {reply_text} date: {cur_date}")
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO information(bot_text,data_del) VALUES(?,?)",
                    (reply_text,
                     cur_date))
        conn.commit()
        cur.close()
        conn.close()
    else:
        bot.send_message(message.chat.id,'Your text dont start with <Strattonbot+>,so try again')


bot.polling(none_stop=True)