from wtforms import Form, IntegerField, validators
from math import pi
from fractions import Fraction

class InputForm(Form):
    #default
    A = IntegerField(
        label='amplitude (m)',
        validators=[validators.InputRequired()])
    # b = FloatField(
    #     label='damping factor (kg/s)', default=0,
    #     validators=[validators.InputRequired()])
    w = IntegerField(
        label='frecventa(1/s)',
        validators=[validators.InputRequired()])
    fi0 = IntegerField(
        label='faza initiala rad/s',
        validators=[validators.InputRequired()])
