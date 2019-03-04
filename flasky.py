# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-2-26 下午2:36
@Desc :
'''
import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, Permission, Post
from app import fake

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


# shell创建数据库
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


# 注册shell上下文处理函数
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Role=Role, User=User, Permission=Permission, Post=Post)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# 生成模拟数据
@app.cli.command()
def fakes():
    fake.users(100)
    fake.posts(100)
