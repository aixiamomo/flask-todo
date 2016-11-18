# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, \
    flash, render_template, url_for, Blueprint
from application.extensions import db
from application.models import Todo


# 初始化蓝本
todo_bp = Blueprint('todo', __name__, template_folder='../templates')


# 主页
@todo_bp.route('/', methods=['GET', 'POST'])
def index():
    todo = Todo.query.order_by('-id')

    if request.method == 'POST':
        _form = request.form
        # 添加任务
        title = _form['title']
        td = Todo(title=title)
        try:
            td.store_to_db()  # 将数据保存到数据库
            flash("add task successfully!")
            return redirect(url_for('todo.index'))
        except Exception as e:
            print e
            flash("fail to add task!")
    return render_template('index.html', todo=todo)


# 删除任务
@todo_bp.route('/<int:todo_id>/del', methods=['GET'])
def del_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.delete_todo()
        flash('delete task successfully!')
    return redirect(url_for('todo.index'))


# 编辑（更新）任务
@todo_bp.route('/<int:todo_id>/edit', methods=['GET', 'POST'])
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    if request.method == 'POST':
        todo.title = request.form['title']
        db.session.commit()
        flash("update successfully!")
        return redirect(url_for('todo.index'))

    return render_template('edit.html', todo=todo)


# 标记任务完成
@todo_bp.route('/<int:todo_id>/done', methods=['GET'])
def done(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.status = True
        db.session.commit()
        flash('task is completed!')
    return redirect(url_for('todo.index'))


# 重置任务
@todo_bp.route('/<int:todo_id>/redo', methods=['GET'])
def redo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.status = False
        db.session.commit()
        flash('redo successfully!')
    return redirect(url_for('todo.index'))


# 404处理
@todo_bp.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
