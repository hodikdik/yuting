from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/emotionanalysis.html')
def emotionanalysis():  # put application's code here
    return render_template('emotionanalysis.html')

@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    return render_template('wordcloud.html')

@app.route('/type.html')
def type():  # put application's code here
    return render_template('type.html')

@app.route('/direction.html')
def direction():  # put application's code here
    return render_template('direction.html')

if __name__ == '__main__':
    app.run()
