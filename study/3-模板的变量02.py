# -*- coding:utf-8 -*-
# @Author:ðRedBalloon
# @Time:2022/10/26-17:26
# @File:3-æ¨¡æ¿çåé02.py

"""è±éæè½ä¿¡æ¯çæ¡ä¾"""
from flask import Flask, render_template

app = Flask(__name__)


# è¿éè±éä¸ºäºç´¢
@app.route('/hero/<hero_name>')
def hero_info(hero_name=None):
    # return render_template('heroInformation.html', title='{}çæè½åç§°'.format(hero_name),
    #                        name=hero_name, skill1='æ©é¢éª', skill2='é£ä¹å£é', skill3='è¸åæ©', skill4='çé£ç»æ¯æ©')
    # ç®åç²æ´çä¼ å,æè½ç°å¨ååæ­»

    # dic_data = {
    #     'title': f'{hero_name}çæè½åç§°',
    #     'name': hero_name,
    #     'skill1': 'æ©é¢éª',
    #     'skill2': 'é£ä¹å£é',
    #     'skill3': 'è¸åæ©',
    #     'skill4': 'çé£ç»æ¯æ©',
    # }
    # return render_template('heroInformation.html', hero_data=dic_data)

    # æ´æ¹ä¾¿çæ¹æ³
    title = f'{hero_name}çæè½åç§°'
    name = hero_name
    skill1 = 'æ©é¢éª'
    skill2 = 'é£ä¹å£é'
    skill3 = 'è¸åæ©'
    skill4 = 'çé£ç»æ¯æ©'
    # print(locals())
    # {'hero_name': 'äºç´¢', 'title': 'äºç´¢çæè½åç§°', 'name': 'äºç´¢' ...}
    # locas() ä½ç¨ä»¥å­å¸çæ¹å¼åå»ºåé å±é¨çåéåä¸ºkey,å¼ä¸ºvalue.
    return render_template('heroInformation.html', hero_data=locals())


if __name__ == '__main__':
    app.run(debug=True)