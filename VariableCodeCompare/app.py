from flask import Flask, request, render_template
from University import University
from RadarGraph import RadarGraph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ListUniver = []
    if request.method == 'POST':
        university = University()
        

        university.NameUni = request.form['NameUni']

        for score in university.MajorScore:
            if score is None:
                score = 0

    return render_template('index.html', ListUniver=ListUniver)


if __name__ == '__main__':
    app.run(debug=True)
