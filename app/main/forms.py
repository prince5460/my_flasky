# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-2-27 下午4:47
@Desc :
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
