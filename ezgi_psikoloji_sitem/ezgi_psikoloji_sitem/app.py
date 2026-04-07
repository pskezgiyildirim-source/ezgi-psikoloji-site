from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/hakkimda')
def hakkimda():
    return render_template('hakkimda.html')

@app.route('/hizmetler')
def hizmetler():
    return render_template('hizmetler.html')

# Seminerler Sayfası Bağlantısı Eklendi!
@app.route('/seminerler')
def seminerler():
    return render_template('seminerler.html')

# Blog Sayfası Bağlantısı
@app.route('/blog')
def blog():
    return render_template('blog.html')
if __name__ == '__main__':
 app.run(debug=True, port=5001)