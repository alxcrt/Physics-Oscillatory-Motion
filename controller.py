from model import InputForm
from flask import Flask, render_template, request
from compute import compute
from fractions import Fraction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data,form.w.data, form.fi0.data)
    else:
        result = None

    return render_template('view_plain.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
