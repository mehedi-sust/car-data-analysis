import numpy as np
import matplotlib.pyplot as plt


class VehicleData:
    def __init__(self, data_file):
        self.data = np.load(data_file)

    # checking for pitfall condition
    def pitfall_check(self):
        unique_ids, counts = np.unique(self.data[:, 1], return_counts=True)
        single_occurrences = unique_ids[counts == 1]
        if len(single_occurrences) > 0:
            return True
        else:
            return False

    # selecting a certain id and making subset of data
    def by_id(self, id):
        return self.data[self.data[:, 1] == id]

    # splitting into segements
    def split_segments(self):
        unique_ids = np.unique(self.data[:, 1])
        segments = []
        for id in unique_ids:
            segment = self.by_id(id)
            segments.append(segment)
        return segments

    # filtering the segments with or without an funtion
    def filter(self, func=None):
        segments = self.split_segments()
        filtered_segments = []
        for segment in segments:
            if func is None or func(segment):
                filtered_segments.append(segment)
        return filtered_segments

    # plotting the data segments
    def plot(self, segments, ax=None):
        for segment in segments:
            x_values = segment[:, 2]
            y_values = segment[:, 3]
            plt.plot(x_values, y_values)
        plt.xlabel('Latitude')
        plt.ylabel('Longitude')
        plt.title('Trajectories')
        plt.xlim(np.min(self.data[:, 2]), np.max(self.data[:, 2]))  # Set x-axis limits based on data
        plt.ylim(np.min(self.data[:, 3]), np.max(self.data[:, 3]))  # Set y-axis limits based on data
        plt.show()