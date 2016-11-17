# -*- coding: utf-8 -*-
from application import create_app
from flask_script import Manager, Server

app = create_app('default')

manager = Manager(app)

manager.add_command('runserver', Server(host='127.0.0.1', port=3000))

if __name__ == '__main__':
    manager.run()
