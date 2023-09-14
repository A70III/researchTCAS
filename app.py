# Import ไลบรารีและโมดูลที่จำเป็น
from flask import Flask, request, render_template, redirect
from RadarGraph import RadarGraph
import pandas as pd

# สร้างแอพ Flask
app = Flask(__name__)

# กำหนดตัวแปรรับค่าคะแนนและชื่อมหาวิทยาลัย
ListU_Score = []
ListU_Name = []

# สร้างอ็อบเจ็กต์ RadarGraph
radar_obj = RadarGraph()

# สร้างเส้นทางหน้าแรก
@app.route('/')
def index():
    return render_template('index.html')

# เส้นทางสำหรับรับค่าและบันทึกคะแนน
@app.route('/', methods=['GET', 'POST'])
def foo():
    ScoreGroup = []
    if 'finish' in request.form:
        return redirect('/finish_page')
    UniversityName = request.form['UniversityName']

    # รับค่าคะแนนจากฟอร์มและเพิ่มลงในรายชื่อคะแนน
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
    print(ListU_Score)  # ใส่คะแนนในกลุ่มได้ละ

    # เพิ่มชื่อมหาวิทยาลัยลงในรายการ
    ListU_Name.append(UniversityName)
    universities = ListU_Name
    print(ListU_Name)

    # หากมีคะแนนมหาวิทยาลัยมากกว่าหรือเท่ากับ 10 คะแนน ก็จะพล็อตกราฟ Radar
    if len(ListU_Score) >= 10:
        radar_obj.PlotRadar(ListU_Name, ListU_Score)
        return render_template('radar_image.html', universities=universities, ListU_Score=ListU_Score)

    return render_template('index.html')

# เส้นทางสำหรับหน้าสรุปผล
@app.route('/finish_page')
def another_page():
    universities = ListU_Name
    radar_obj.PlotRadar(ListU_Name, ListU_Score)
    return render_template('radar_image.html', universities=universities, ListU_Score=ListU_Score)

# เส้นทางสำหรับรีเซ็ตค่า
@app.route('/reset', methods=['POST'])
def reset():
    global ListU_Score
    global ListU_Name
    ListU_Score = []
    ListU_Name = []
    return redirect('/')

# รันแอพ Flask
if __name__ == '__main__':
    app.run(debug=True)
