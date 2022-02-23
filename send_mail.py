import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'loginRegister2.settings'

if __name__ == '__main__':

    send_mail(
        '来自问道的测试邮件',
        '欢迎访问www.liujiangblog.com，这里是问道的博客站点，总能给你带来惊喜',
        'zengzhiqi365@126.com',
        ['1374968273@qq.com'],
    )