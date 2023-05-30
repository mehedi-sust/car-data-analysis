"""
the script to execute main method to utilize VehicleData module and
analyze and visualize data
"""

from framework.vehicle_data import VehicleData

def main(data_file):
    """
    main function to analyze and visualize vehicle data.

    Args:
        data_file (str): Path to the data file.

    Returns:
        None
    """
    # creating an instance of VehicleData with data_file
    obj = VehicleData(data_file)

    '''
    # currently not is use
    has_pitfall = obj.pitfall_check()

    if has_pitfall:
        print("stopping execution. pitfall condition found.")
        exit(0)
    '''

    # selecting all segments
    #segments = obj.split_segments()

    # the filter function to filter segments by length
    def length(trajectory):
        return len(trajectory)

    filtered_segments = obj.filter(length)
    obj.plot(filtered_segments)

    '''
    # selecting only single id and plot it
    segment = obj.by_id(0)
    segments = [segment]
    obj.plot(segments)
    '''


if __name__ == "__main__":
    """
    defining the data file path and calling main method
    """
    DATA_FILE = "./data/data.npy"
    # DATA_FILE_GEN = "./data/data_generated.npy"
    # DATA_FILE_TEST = "./data/data_test.npy"
    main(DATA_FILE)
    # main(DATA_FILE_GEN)
    # main(DATA_FILE_TEST)
