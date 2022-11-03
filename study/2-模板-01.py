# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/10/24-20:28
# @File:2-模板-01.py

# 模板 - MTV 中的 Templates
# 模板创建动态的网页  包含响应文本的文件（html）该文件中允许包含 “占位变量” 用动态的方式来传递内容，其具体内容只要在请求后才可知。
# ”占位变量“最终会被真实的值所替换  模板最终也会被解析成响应的字符串, 这一过程即为"渲染"


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('sss.html',)


if __name__ == '__main__':
    app.run(debug=True)


# 2.模板的设置
# 默认情况下, Flask会在程序文件夹中的 templates 子文件夹中寻找模板

# 所以需要手动在程序目录下创建 templates 文件夹

# 3. 渲染模板
# 在视图函数中,通过 return render_template() 将模板渲染成字符串再响应给客户端
#
# render_template(): 语法
#     render_template('index.html', arg1=value1, arg2=value2)
#     第一个参数: xxx.html  要渲染给客户端的html模板
#     参数1 - 参数n :   要传递给模板动态显示的变量占位符,如果没有动态的变量占位符, 则可以省略  有点像format方法-_-
#     返回值 是字符串
