# -*- coding: utf-8 -*-
from application import create_app, db
from flask_script import Manager, Server, Shell

app = create_app('default')

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(host='127.0.0.1', port=3000))

if __name__ == '__main__':
    manager.run()
