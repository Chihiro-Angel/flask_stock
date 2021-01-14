# -*- coding: utf-8 -*-
# author:yang  time:19-8-7 上午10:25
from flask import render_template, current_app, request, jsonify
from info.models import Stock, Focus, db
from info.modules.index import index_blu


@index_blu.route('/')
def index():

    # stock_list = []
    # try:
    #     stock_list = Stock.query.all()
    # except BaseException as e:
    #     current_app.logger.error(e)
    infos = Stock.query.all()
    for info in infos:
        f = Focus.query.filter_by(relationship_id=info.id).all()
        # print(f)
        if f:
            info.is_focus = True
        else:
            info.is_focus = False

    return render_template('index.html', data=infos)


@index_blu.route('/center')
def center():

    focus_list = []
    try:
        focus_list = Focus.query.all()
    except BaseException as e:
        current_app.logger.error(e)

    data = {
        'focus': [focus.to_dict() for focus in focus_list]
    }
    # print(data)

    return render_template('center.html', data=data)


@index_blu.route('/add/<code>.html')
def add(code):
    code = int(code)
    # print(code)
    focus = Focus.query.all()

    focu_list = [focu.to_dict() for focu in focus]
    list_ = []
    for i in focu_list:
        print(i['relationship_id'])
        list_ .append(i['relationship_id'])

    if code not in list_:
        focus_re_id = Focus(relationship_id=code)
        try:
            db.session.add(focus_re_id)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return "添加失败"
        return "添加成功"
    else:
        # print("已存在")
        return "数据已存在"


@index_blu.route('/del/<code>.html')
def delete(code):
    code = int(code)
    print(code)
    focus_re_id = Focus.query.filter_by(id=code).first()
    try:
        db.session.delete(focus_re_id)
        db.session.commit()
    except BaseException as e:
        db.session.rollback()
        current_app.logger.error(e)
        return "删除失败"

    return "删除成功"


@index_blu.route('/update/<int:code>/')
def alter(code):
    code = int(code)
    print("这是修改")
    notestail = request.args.get("notestail")
    try:
        focu = Focus.query.get(code)
        focu.note = notestail
        db.session.commit()
        return "修改成功"
    except BaseException as e:
        db.session.rollback()
        current_app.logger.error(e)
        return "修改失败"


@index_blu.route('/update')
def refresh():
    if request.method == "GET":
        try:
            refresh_data = request.args.get('p')
            print(refresh_data)
            focu = Focus.query.get(refresh_data)
            print(focu)
            return render_template("update.html", focu=focu)
        except BaseException as e:
            current_app.logger.error(e)
            return "刷新失败"



