# -*- coding:utf-8 -*-
# @Author:ðRedBalloon
# @Time:2022/10/26-22:32
# @File:3-æ¨¡æ¿çåé03.py

# å°è¯ä¼ å¥ä¸åçæ°æ®ç±»å

from flask import Flask, render_template

app = Flask(__name__)


class LOLHero(object):
    def __init__(self):
        self.name = None

    def say(self):
        return 'è¿æ¯è±éä¿¡æ¯~'


@app.route('/index')
def index():
    # å­ç¬¦ä¸²ç±»å
    title = 'ä¸åæ°æ®ç±»åçæ¨¡æ¿ä¼ å'
    # åè¡¨ç±»å
    lists_data = ['æè«', 'çç', 'å°æ³å¸', 'å°ç®æ', 'æ³¢æ¯']
    # åç»ç±»å
    tuples_data = ('ç¾é£åè±ª', 'æè£åé­', 'æ ååå§¬', 'æ æåå£')
    # å­å¸ç±»å
    dicts_data = {
        'ç¾é£åè±ª': 'äºç´¢',
        'æè£åé­': 'äºæåæ¯',
        'æ ååå§¬': 'è²å¥¥å¨',
        'æ æåå£': 'æ',
    }
    # ç±»æ¹æ³ ï¼å¯¹è±¡ï¼
    hero = LOLHero()
    hero.name = 'æ«ç²é¾é¾'

    return render_template('differentDataTemplate.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)
