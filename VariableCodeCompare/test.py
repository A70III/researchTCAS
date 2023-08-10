class RadarCompare:
    
    def __init__(self) -> None:
        self.dataMajorPoint = []
        self.universities = []
        self.fig = None
        
    def PlotRadar(self, universities, dataMajorPoint, max_value=None):
        import numpy as np
        import matplotlib.pyplot as plt

        # Data for the radar charts
        self.dataMajorPoint = dataMajorPoint
    
        # Labels for the radar chart axes
        Majors = ['Language', 'Thinking', 'Arts and Society', 'Science', 'Mathematics', 'General']

        # Colors for each sample
        colors = ['magenta', 'blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'brown', 'black']  # limit to compare = 10

        # Names of the universities
        self.universities = universities

        # Create a figure and subplot
        self.fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'polar': True})

        # Determine the maximum value for scaling if not provided
        if max_value is None:
            max_value = max(max(data) for data in dataMajorPoint)

        # Plot the radar charts
        for i, sample_data in enumerate(self.dataMajorPoint):
            scaled_data = np.array(sample_data) * (100 / max_value)
            angles = np.linspace(0, 2 * np.pi, len(Majors), endpoint=False).tolist()
            scaled_data = np.append(scaled_data, scaled_data[0])
            angles += angles[:1]  # Close the plot

            ax.plot(angles, scaled_data, marker='o', linestyle='-', color=colors[i], linewidth=2, label=universities[i])
            ax.fill(angles, scaled_data, color=colors[i], alpha=0.25)

        # Set the ticks and labels for the radar chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(Majors)
        ax.yaxis.grid(True)
        plt.subplots_adjust(top=1.05)

        # Add a legend
        ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.39))

        # Set the title
        title_offset = 1.1  # You can adjust the value as needed
        ax.set_title("Comparison of Universities", size=20, weight='bold', y=title_offset)

        # Show the plot
        plt.show()

# Example usage
radar = RadarCompare()
universities = ["University A", "University B"]
dataMajorPoint = [[4, 5, 3, 2, 4, 5], [3, 4, 5, 2, 3, 4]]
radar.PlotRadar(universities, dataMajorPoint, max_value=100)  # Specify the maximum value for scaling
