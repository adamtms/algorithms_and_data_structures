import matplotlib.pyplot as plt

def compare_sorting_times(labels, times, index):
    labels = [label.__name__ if callable(label) else label for label in labels]
    n =len(labels)
    graph_number = 0
    _, axs = plt.subplots(n//2 + n%2, 2, layout='constrained', figsize=(10,5))

    for label in labels:
        widths = []
        for algorithms_name, measurement in times.items():
            widths.append(measurement[index][label])
        ax = axs[graph_number//2][graph_number%2]
        bar_container = ax.bar([s.replace("_sort", "") for s in times.keys()], widths)
        ax.bar_label(bar_container, [f"{i:.1E}" if i < 0.1 else round(i,3) for i in widths], label_type="center", padding=7)
        ax.set_ylabel('Time (s)')
        ax.set_title(label)
        graph_number += 1
    plt.show()
