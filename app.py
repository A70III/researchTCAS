from flask import Flask, render_template, request,redirect
from RadarGraph import RadarGraph
import pandas as pd

app = Flask(__name__)

selected_rows = []  # เก็บรายการแถวที่ถูกเลือก
ListU_Name = []  # เก็บรายการข้อมูลที่ถูกเลือกในรูปแบบของสตริง
ListU_Score = []

# สร้างอ็อบเจ็กต์ RadarGraph
radar_obj = RadarGraph()

@app.route('/', methods=['GET', 'POST'])
def index():
    global selected_rows, ListU_Name, ListU_Score
    if 'finish' in request.form: #กรณีตัดสินใจพอที่จะเลือก
        return redirect('/finish_page')

    if request.method == 'POST':
        selected_row = int(request.form['selected_row'])  # เลือกแถวที่ผู้ใช้เลือก

        # อ่านข้อมูลจากไฟล์ Excel
        df = pd.read_excel('Processed_Data.xlsx')  # แทนชื่อไฟล์ตามที่คุณต้องการ

        # ดึงข้อมูลจากแถวที่ถูกเลือก
        selected_data = df.iloc[selected_row]

        # สร้างสตริงเพื่อรวมข้อมูลในคอลัมน์ที่ต้องการ
        selected_info = (
            f"ลำดับ: {len(ListU_Name) + 1}\n"
            f"สถาบัน: {selected_data['สถาบัน']}\n"
            f"วิทยาเขต: {selected_data['วิทยาเขต']}\n"
            f"คณะ/สำนักวิชา: {selected_data['คณะ/สำนักวิชา']}\n"
            f"ชื่อหลักสูตร: {selected_data['ชื่อหลักสูตร']}\n"
            f"รายละเอียด: {selected_data['รายละเอียด']}"
        )

        # เพิ่มข้อมูลในรายการ ListU_Name
        ListU_Name.append(selected_info)

        # อ่านคะแนนจากคอลัมน์และเพิ่มใน ScoreGroup
        LangScr = int(selected_data['Language'])
        ThinkScr = int(selected_data['Thinking'])
        ArtScr = int(selected_data['Arts and Society'])
        SciScr = int(selected_data['Science'])
        MathScr = int(selected_data['Mathematics'])
        GenScr = int(selected_data['General'])

        ScoreGroup = []
        ScoreGroup.append(LangScr)
        ScoreGroup.append(ThinkScr)
        ScoreGroup.append(ArtScr)
        ScoreGroup.append(SciScr)
        ScoreGroup.append(MathScr)
        ScoreGroup.append(GenScr)

        # เพิ่ม ScoreGroup ใน ListU_Score
        ListU_Score.append(ScoreGroup)

        # จำกัดจำนวนแถวที่เก็บใน ListU_Name เพื่อไม่ให้เกิน 10 รายการ
        if len(ListU_Name) > 10:
            ListU_Name = ListU_Name[-10:]  # เก็บเฉพาะ 10 รายการล่าสุด
        print(ListU_Name)
        print(ListU_Score)

    # ตรวจสอบว่า ListU_Score มี 10 รายการขึ้นไปหรือไม่
    if len(ListU_Score) >= 10:
        radar_obj.PlotRadar(ListU_Name, ListU_Score)
        return render_template('radar_image.html', universities=ListU_Name, ListU_Score=ListU_Score)

    # อ่านข้อมูลจากไฟล์ Excel เพื่อสร้างเมนู dropdown
    df = pd.read_excel('Processed_Data.xlsx')  # แทนชื่อไฟล์ตามที่คุณต้องการ
    data = df.to_dict(orient='records')  # แปลงข้อมูลเป็นรายการของพจนานุกรม

    # ส่งข้อมูลไปยัง HTML พร้อมกับรายการที่ถูกเลือกและสถานะการเลือก
    return render_template('index.html', data=data, selected_row=ListU_Name)

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
