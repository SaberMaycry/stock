import wxpy as wx


def init_wx(name):
    """ 初始化微信通讯 """
    bot = wx.Bot(cache_path=True)
    global receiver
    receiver = bot.search(name)[0]
    return receiver


def send_msg(msg):
    """ 发送消息 """
    receiver.send(msg)
