from flask import Flask, render_template, request, jsonify  # เพิ่ม jsonify
from Radar import RadarCompare
app = Flask(__name__)

# Initialize the RadarCompare instance
radar_compare = RadarCompare()

@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    radar_image = None  # เพิ่มตัวแปรเก็บภาพ radar
    score_values = []  # Initialize an empty list to store scores
    if request.method == 'POST':
        university_name = request.form.get('university_name')
        data = university_name
        # Get the score values from the form
        score_values = [
            float(request.form.get('language_score')),
            float(request.form.get('thinking_score')),
            float(request.form.get('arts_score')),
            float(request.form.get('science_score')),
            float(request.form.get('math_score')),
            float(request.form.get('general_score'))
        ]
        # Call the PlotRadar function with universities and score_values
        radar_image = radar_compare.PlotRadar([university_name], [score_values])
        
    return render_template('index.html', data=data, radar_image=radar_image)


if __name__ == '__main__':
    app.run(debug=True)
