import pandas as pd

excel_file_path = '\ExcelProcess\Raw_Data.csv'
columns_to_process = ['สถาบัน', 'วิทยาเขต', 'คณะ/สำนักวิชา', 'ชื่อหลักสูตร','รายละเอียด', 'เกรดเฉลี่ย'
                      , 'TGAT', 'TGAT1', 'TGAT2', 'TGAT3','TPAT3','A-Level คณิตศาสตร์ประยุกต์ 1'
                      ,'A-Level วิทยาเขาสตร์ประยุกต์','A-Level ฟิสิกส์','A-Level เคมี','A-Level ชีววิทยา'
                      ,'A-Level สังคมศาสตร์','A-Level ภาษาไทย','A-Level ภาษาอังกฤษ']

df = pd.read_csv(excel_file_path)

num_rows = df.shape[0]
df.iloc[:num_rows] = df.iloc[:num_rows].fillna(0)

totalMajorLanguage = ['TGAT1','A-Level ภาษาไทย','A-Level ภาษาอังกฤษ']
totalMajorThinking = ['TGAT2', 'TGAT3']
totalMajorArtsandSociety=['A-Level สังคมศาสตร์']
totalMajorScience = ['A-Level วิทยาศาสตร์ประยุกต์','A-Level ฟิสิกส์','A-Level เคมี','A-Level ชีววิทยา','TPAT3']
totalMajorMathematics = ['A-Level คณิตศาสตร์ประยุกต์ 1']
totalMajorGeneral = ['TGAT', 'เกรดเฉลี่ย']

# เลือกคอลัมน์ที่คุณต้องการเก็บ
columns_to_keep = ['สถาบัน', 'วิทยาเขต', 'คณะ/สำนักวิชา', 'ชื่อหลักสูตร','รายละเอียด']

# สร้าง DataFrame ใหม่โดยเลือกคอลัมน์ที่คุณต้องการเก็บ
result_df = df[columns_to_keep].copy()

# เพิ่มคอลัมน์ผลรวมที่คุณต้องการ
result_df['Language'] = df[totalMajorLanguage].sum(axis=1)
result_df['Thinking'] = df[totalMajorThinking].sum(axis=1)
result_df['Arts and Society'] = df[totalMajorArtsandSociety].sum(axis=1)
result_df['Science'] = df[totalMajorScience].sum(axis=1)
result_df['Mathematics'] = df[totalMajorMathematics].sum(axis=1)
result_df['General'] = df[totalMajorGeneral].sum(axis=1)

# บันทึกข้อมูลลงใน Excel
output_excel_file_path = '\ExcelProcess\Processed_Data.xlsx'  # ระบุเส้นทางไฟล์ Excel ที่ต้องการเขียน
result_df.to_excel(output_excel_file_path, index=False)

print(f'ข้อมูลถูกเขียนลงใน {output_excel_file_path}')
