from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_total(a, b, c):
    return a + b + c

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        total = calculate_total(a, b, c)
        return render_template('result.html', total=total)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)