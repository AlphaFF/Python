#!/usr/bin/env python3
# coding=utf-8

# import itchat
#
#
# itchat.auto_login(hotReload=True)
#
#
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
#
# itchat.auto_login()
# itchat.run()
#
# itchat.send_msg('hahaha', toUserName='口水流了一地')


from __future__ import unicode_literals

from wxpy import *
from wechat_sender import listen

bot = Bot('bot.pkl')

my_friend = bot.friends().search('薛文斯')[0]
print(my_friend)


@bot.register(Friend)
def reply_test(msg):
    msg.reply('你个大傻叉')


listen(bot)  # 只需改变最后一行代码


if __name__ == '__main__':
    my_friend.send('你个大傻叉')
