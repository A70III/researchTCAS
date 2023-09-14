import numpy as np
import matplotlib.pyplot as plt
import os

class RadarGraph:
    
    def __init__(self) -> None:
        pass
        
    def PlotRadar(self, UniversityList, ScoreList):
        self.UniversityList = UniversityList
        self.ScoreList = ScoreList

        # ประกาศ Label ของแต่ละแกนของ Radar Chart
        Majors = ['Language', 'Thinking', 'Arts and Society', 'Science', 'Mathematics', 'General']

        # กำหนดสีสำหรับแต่ละตัวอย่าง
        colors = ['magenta', 'blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'brown', 'black']  # จำกัดไว้ให้เท่านั้น

        # สร้างกราฟและ subplot
        self.fig, ax = plt.subplots(figsize=(6, 7.5), subplot_kw={'polar': True})

        for i, sample_data in enumerate(ScoreList):
            angles = np.linspace(0, 2 * np.pi, len(Majors), endpoint=False).tolist()
            sample_data += sample_data[:1]  # ปิดรูปกราฟ
            angles += angles[:1]  # ปิดรูปกราฟ
            countUniver = "university {}".format(i+1)

            ax.plot(angles, sample_data, marker='o', linestyle='-', color=colors[i], linewidth=2, label=countUniver)
            ax.fill(angles, sample_data, color=colors[i], alpha=0.25)

        # กำหนดเส้นและป้ายชื่อของแกนใน Radar Chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(Majors)

        ax.yaxis.grid(True)
        plt.subplots_adjust(top=1.05)

        # เพิ่มสัญลักษณ์
        ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.39), ncol=3)

        # กำหนดหัวเรื่อง
        title_offset = 1.1  # คุณสามารถปรับค่าได้ตามที่ต้องการ
        ax.set_title("Comparison of Universities", size=15, weight='bold', y=title_offset)

        # แสดงกราฟ
        static_folder = os.path.join(os.getcwd(), 'static')
        plot_path = os.path.join(static_folder, 'radar_chart.png')
        plt.savefig(plot_path)
