# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, \
    flash, render_template, url_for, Blueprint
from application.extensions import db
from application.models import Todo


# 初始化蓝本
todo_bp = Blueprint('todo', __name__, template_folder='../templates')
