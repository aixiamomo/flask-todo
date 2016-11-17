# -*- coding: utf-8 -*-
import todo

# controllers里新增的蓝图都可以添加到这里，然后传给app.py注册到应用
blueprints = [
    todo.todo_bp
]