from flask import Flask, request, render_template, redirect
from RadarGraph import RadarGraph

app = Flask(__name__)

ListU_Score = []
ListU_Name = []
radar_obj = RadarGraph()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def foo():
    ScoreGroup = []
    if 'finish' in request.form:
        return redirect('/finish_page')
    UniversityName = request.form['UniversityName']

    LangScr = float(request.form['Language'])
    ThinkScr = float(request.form['Thinking'])
    ArtScr = float(request.form['ArtNSoci'])
    SciScr = float(request.form['Science'])
    MathScr = float(request.form['Math'])
    GenScr = float(request.form['General'])

    ScoreGroup.append(LangScr)
    ScoreGroup.append(ThinkScr)
    ScoreGroup.append(ArtScr)
    ScoreGroup.append(SciScr)
    ScoreGroup.append(MathScr)
    ScoreGroup.append(GenScr)
    ListU_Score.append(ScoreGroup)
    print(ListU_Score)##ใส่คะแนนใน group สิบครั้งได้ละ
    
    ListU_Name.append(UniversityName)
    universities = ListU_Name
    print(ListU_Name)
    
    
    if len(ListU_Score)>=10:
        radar_obj.PlotRadar(ListU_Name,ListU_Score)
        
        return render_template('radar_image.html',universities=universities,ListU_Score=ListU_Score)
    
    
    
    return render_template('index.html')

@app.route('/finish_page')
def another_page():
    universities = ListU_Name
    radar_obj.PlotRadar(ListU_Name,ListU_Score)
    return render_template('radar_image.html',universities=universities,ListU_Score=ListU_Score)


if __name__ == '__main__':
    app.run(debug=True)