from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

selected_rows = []  # เก็บรายการแถวที่ถูกเลือก
ListU_Name = []  # เก็บรายการข้อมูลที่ถูกเลือกในรูปแบบของสตริง
ListU_Score = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global selected_rows, ListU_Name, ListU_Score

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
        LangScr = selected_data['Language']
        ThinkScr = selected_data['Thinking']
        ArtScr = selected_data['Arts and Society']
        SciScr = selected_data['Science']
        MathScr = selected_data['Mathematics']
        GenScr = selected_data['General']

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
        return render_template('radar_image.html', universities=ListU_Name, ListU_Score=ListU_Score)

    # อ่านข้อมูลจากไฟล์ Excel เพื่อสร้างเมนู dropdown
    df = pd.read_excel('Processed_Data.xlsx')  # แทนชื่อไฟล์ตามที่คุณต้องการ
    data = df.to_dict(orient='records')  # แปลงข้อมูลเป็นรายการของพจนานุกรม

    # ตรวจสอบว่าเลือกได้หรือไม่
    allow_selection = len(ListU_Name) < 10  # อนุญาตให้เลือกเมื่อไม่เกิน 10 รายการ

    # ส่งข้อมูลไปยัง HTML พร้อมกับรายการที่ถูกเลือกและสถานะการเลือก
    return render_template('index.html', data=data, selected_row=ListU_Name, allow_selection=allow_selection)



if __name__ == '__main__':
    app.run(debug=True)
