# -*- coding:utf-8 -*-
# @Author:ðRedBalloon
# @Time:2022/10/29-13:24
# @File:6-éææä»¶01.py

# éææä»¶ï¼css, js, å¾ç, è§é¢, é³é¢ç­ã
# éææä»¶çå¤çï¼
#     ææçéææä»¶é½é»è®¤ä¿å­å¨é¡¹ç®æä»¶å¤¹ä¸­ç static æä»¶å¤¹ä¸­ï¼å¨è®¿é®éææä»¶æ¶éè¦éè¿ /static/èµæºè·¯å¾ æ¥è¿è¡è®¿é®
# éææä»¶çè·¯å¾ååè§£æ
#     url_for('static', filename='ahri.jpg')


from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    # ååè§£ææ¹å¼ä¸
    # link=url_for('static', filename='images/ahri.jpg')
    return render_template('static-01.html', test_data=locals())


if __name__ == '__main__':
    app.run(debug=True)