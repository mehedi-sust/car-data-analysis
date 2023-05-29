from framework.VehicleData import VehicleData
import numpy as np


def main(data_file):
    # creating an instance of VehicleData with data_file
    obj = VehicleData(data_file)
    has_pitfall = obj.pitfall_check()

    """
    if has_pitfall:
        print("stopping execution. pitfall condition found.")
        exit(0)
    """

    # selecting all segments
    segments = obj.split_segments()
    
    # the filter function to filter segments by length
    def length(trajectory):
        return len(trajectory)

    filtered_segments = obj.filter(length)
    obj.plot(filtered_segments)

    """
    # selecting only single id and plot it
    segment = obj.by_id(0)
    segments = [segment]
    obj.plot(segments)
    """


if __name__ == "__main__":
    data_file = "./data/data.npy"
    data_file_gen = "./data/data_generated.npy"
    data_file_test = "./data/data_test.npy"
    main(data_file)
    # main(data_file_generated)
    # main(data_file_test)
