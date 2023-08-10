import numpy as np
import matplotlib.pyplot as plt


data = [
    [0.0, 0.0, 0.0, 80.0, 0.0, 20.0],   # Example 1 (Chulalongkorn University)
    [35.0, 0.0, 0.0, 35.0, 0.0, 30.0],   # Example 2 (Kasetsart University)
    [25.0, 20.0, 0.0, 10.0, 45.0, 0.0],  # Example 3 (Khon Kaen University)
    [20.0, 40.0, 0.0, 0.0, 0.0, 40.0]    # Example 4 (King Mongkut's Thonburi)
]


labels = ['Language', 'Thinking', 'Arts and Society', 'Science', 'Mathematics', 'General']


colors = ['pink', 'green', 'red', 'orange']


universities = [
    "Chulalongkorn University",
    "Kasetsart University",
    "Khon Kaen University",
    "King Mongkut's Thonburi"
]


for i, sample_data in enumerate(data):
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)


    sample_data = np.append(sample_data, sample_data[0])
    angles = np.append(angles, angles[0])

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})


    ax.plot(angles, sample_data, color=colors[i], linewidth=2)

    ax.fill(angles, sample_data, color=colors[i], alpha=0.25)


    ax.scatter(angles, sample_data, color=colors[i], s=100, label=universities[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.yaxis.grid(True)
    ax.set_title(universities[i], size=15, weight='bold')


    ax.set_ylim(0, max(sample_data) + 10)


    ax.legend(loc='lower center',bbox_to_anchor=(0.5,-0.1))

plt.show()
