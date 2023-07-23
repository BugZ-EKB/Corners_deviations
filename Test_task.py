import matplotlib.pyplot as plt
import pandas as pd
import os
from IPython.display import Image


class MyPlot:
    def __init__(self, plots_dir):
        self.plots_dir = plots_dir
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)

    def draw_plots(self, file_name):
        df = pd.read_json(file_name)

        return_path = []

        # accuracy of corner prediction
        true_prediction = sum(df['gt_corners'] == df['rb_corners']) / len(df) * 100
        false_prediction = 100 - true_prediction
        plt.bar(['True prediction', 'False prediction'],
                [true_prediction, false_prediction])
        plt.title(f'Accuracy of corner prediction: {true_prediction}%')
        plt.ylabel('Rooms')
        path_1 = os.path.join(self.plots_dir, 'corner_accuracy.png')
        return_path.append(path_1)
        plt.savefig(path_1)
        plt.close()

        # mean deviations
        mean_dev_sum = df['mean']
        mean_dev_floor = df['floor_mean']
        mean_dev_ceiling = df['ceiling_mean']
        fig, axs = plt.subplots(1, 3, figsize=(12,6))
        plt.title('mean deviations')
        axs[0].hist(mean_dev_sum)
        axs[0].set_title('Mean')
        axs[0].set_ylabel('Rooms')

        axs[1].hist(mean_dev_floor)
        axs[1].set_title('Floor mean')

        axs[2].hist(mean_dev_ceiling)
        axs[2].set_title('Ceiling mean')

        path_2 = os.path.join(self.plots_dir, 'mean_deviation.png')
        return_path.append(path_2)
        plt.savefig(path_2)
        plt.close()

        # min deviations
        min_dev_sum = df['min']
        min_dev_floor = df['floor_min']
        min_dev_ceiling = df['ceiling_min']
        fig, axs = plt.subplots(1, 3, figsize=(12, 6))
        axs[0].hist(min_dev_sum)
        axs[0].set_title('min')
        axs[0].set_ylabel('Rooms')

        axs[1].hist(min_dev_floor)
        axs[1].set_title('Floor min')

        axs[2].hist(min_dev_ceiling)
        axs[2].set_title('Ceiling min')

        path_3 = os.path.join(self.plots_dir, 'min_deviation.png')
        return_path.append(path_3)
        plt.savefig(path_3)
        plt.close()

        # max deviations
        max_dev_sum = df['max']
        max_dev_floor = df['floor_max']
        max_dev_ceiling = df['ceiling_max']
        fig, axs = plt.subplots(1, 3, figsize=(12, 6))
        axs[0].hist(max_dev_sum)
        axs[0].set_title('max')
        axs[0].set_ylabel('Rooms')

        axs[1].hist(max_dev_floor)
        axs[1].set_title('Floor max')

        axs[2].hist(max_dev_ceiling)
        axs[2].set_title('Ceiling max')

        path_4 = os.path.join(self.plots_dir, 'max_deviation.png')
        return_path.append(path_4)
        plt.savefig(path_4)
        plt.close()

        # total deviations - mean, min, max
        mean_dev = df['mean']
        min_dev = df['min']
        max_dev = df['max']
        fig, axs = plt.subplots(1, 3, figsize=(12, 6))
        axs[0].hist(mean_dev)
        axs[0].set_title('mean')
        axs[0].set_ylabel('Rooms')

        axs[1].hist(min_dev)
        axs[1].set_title('min')

        axs[2].hist(max_dev)
        axs[2].set_title('max')

        path_4 = os.path.join(self.plots_dir, 'mean_min_max.png')
        return_path.append(path_4)
        plt.savefig(path_4)
        plt.close()

        return return_path
