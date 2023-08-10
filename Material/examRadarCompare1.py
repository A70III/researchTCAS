import numpy as np
import matplotlib.pyplot as plt

# Data for the radar charts
data = [
    [0.0, 0.0, 0.0, 80.0, 0.0, 20.0],   # Example 1 (Chulalongkorn University)
    [35.0, 0.0, 0.0, 35.0, 0.0, 30.0],   # Example 2 (Kasetsart University)
    [25.0, 20.0, 0.0, 10.0, 45.0, 0.0],  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 0.0, 0.0, 0.0, 40.0],  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 20.0, 0.0, 0.0, 40.0] ,  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 0.0, 20.0, 0.0, 20.0] ,  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 0.0, 0.0, 0.0, 40.0] ,  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 20.0, 0.0, 0.0, 40.0] ,  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 0.0, 20.0, 0.0, 40.0] ,  # Example 3 (Khon Kaen University)     # Example 4 (King Mongkut's Thonburi)
]

# Labels for the radar chart axes
Majors = ['Language', 'Thinking', 'Arts and Society', 'Science', 'Mathematics', 'General']

# Colors for each sample

colors = ['magenta','blue', 'green', 'red', 'orange','purple','yellow','cyan','brown','black'] #limit to compare?

# Names of the universities
universities = [
    "Chulalongkorn University",
    "Kasetsart University",
    "Khon Kaen University",
    "King Mongkut's University of Technology Thonburi",
    "5",
    "6",
    "7",
    "8",
    "9",
]

# Create a figure and subplot
fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={'polar': True})

# Plot the radar charts
for i, sample_data in enumerate(data):
    angles = np.linspace(0, 2 * np.pi, len(Majors), endpoint=False).tolist()
    sample_data += sample_data[:1]  # Close the plot
    angles += angles[:1]  # Close the plot

    ax.plot(angles, sample_data, marker='o', linestyle='-', color=colors[i], linewidth=2, label=universities[i])
    ax.fill(angles, sample_data, color=colors[i], alpha=0.25)

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
