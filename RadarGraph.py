class RadarGraph:
    
    def __init__(self) -> None:
        pass
        
    def PlotRadar(self, UniversityList, ScoreList):
        import numpy as np
        import matplotlib.pyplot as plt
        import os
        
        self.UniversityList = UniversityList
        self.ScoreList = ScoreList

        # Labels for the radar chart axes (หกด้าน)
        Majors = ['Language', 'Thinking', 'Arts and Society', 'Science', 'Mathematics', 'General']

        # Colors for each sample
        colors = ['magenta', 'blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'brown', 'black']  # จำกัดไว้ให้เท่านั้น

        # Create a figure and subplot
        self.fig, ax = plt.subplots(figsize=(6, 7.5), subplot_kw={'polar': True})


        for i, sample_data in enumerate(ScoreList):
            angles = np.linspace(0, 2 * np.pi, len(Majors), endpoint=False).tolist()
            sample_data += sample_data[:1]  # Close the plot
            angles += angles[:1]  # Close the plot
            countUniver = "University {}".format(i+1)

            ax.plot(angles, sample_data, marker='o', linestyle='-', color=colors[i], linewidth=2, label=countUniver)
            ax.fill(angles, sample_data, color=colors[i], alpha=0.25)

        # Set the ticks and labels for the radar chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(Majors)

        ax.yaxis.grid(True)
        plt.subplots_adjust(top=1.05)


        # Add a legend
        ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.39), ncol=3)

        # Set the title
        title_offset = 1.1  # You can adjust the value as needed
        ax.set_title("Comparison of Universities", size=15, weight='bold', y=title_offset)

        # Show the plot
        static_folder = os.path.join(os.getcwd(), 'static')
        plot_path = os.path.join(static_folder, 'radar_chart.png')
        plt.savefig(plot_path)
