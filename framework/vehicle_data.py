"""
vehicle_data.py

This module contains the VehicleData class for handling vehicle trajectory data.

"""
import numpy as np
import matplotlib.pyplot as plt


class VehicleData:
    """
    VehicleData class

    This class represents a collection of vehicle trajectory data and
    provides various methods for data analysis and visualization.

    Methods:
        __init__(self, data_file)
        pitfall_check(self)
        by_id(self, id)
        split_segments(self)
        filter(self, func=None)
        plot(self, segments, auto_close=True)

    Attributes:
        data: numpy.ndarray
            Array containing the vehicle trajectory data

    Usage:
        # Create an instance of VehicleData
        obj = VehicleData(data_file)

        # Check for pitfall condition
        has_pitfall = obj.pitfall_check()

        # Select data by id
        data_subset = obj.by_id(id)

        # Split the data into segments
        segments = obj.split_segments()

        # Apply filter on segments
        filtered_segments = obj.filter(func)

        # Plot the segments
        obj.plot(segments)
    """

    def __init__(self, data_file):
        self.data = np.load(data_file)

    def pitfall_check(self):
        """
        checks for pitfall condition of single occurance of an data id
        """
        unique_ids, counts = np.unique(self.data[:, 1], return_counts=True)
        single_occurrences = unique_ids[counts == 1]
        if len(single_occurrences) > 0:
            return True

        return False

    def by_id(self, data_id):
        """
        selects a certain id and making subset of data
        """
        return self.data[self.data[:, 1] == data_id]

    def split_segments(self):
        """
        splits data into segements
        """
        unique_ids = np.unique(self.data[:, 1])
        segments = []
        for data_id in unique_ids:
            segment = self.by_id(data_id)
            segments.append(segment)
        return segments

    def filter(self, func=None):
        """
        filtering the segments with or without an funtion
        """
        segments = self.split_segments()
        filtered_segments = []
        for segment in segments:
            if func is None or func(segment):
                filtered_segments.append(segment)
        return filtered_segments

    def plot(self, segments):
        """
        plots the data segments
        """
        for segment in segments:
            x_values = segment[:, 2]
            y_values = segment[:, 3]
            plt.plot(x_values, y_values)
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        plt.title("Trajectories")
        # Set x-axis limits based on data
        plt.xlim(np.min(self.data[:, 2]), np.max(self.data[:, 2]))
        # Set y-axis limits based on data
        plt.ylim(np.min(self.data[:, 3]), np.max(self.data[:, 3]))
        plt.show()
