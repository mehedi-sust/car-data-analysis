import unittest
from framework.VehicleData import VehicleData
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.testing as mptesting


class TestVehicleData(unittest.TestCase):
    def setUp(self):
        # setup test data and test data file
        data = np.array(
            [
                [1, 0, 23.7822085, 90.8496086],
                [2, 0, 23.8437297, 90.5741694],
                [3, 0, 23.860403, 90.400025],
                [4, 1, 23.886050, 90.429461],
                [5, 1, 23.829811, 90.445120],
            ]
        )
        self.test_data_file = "test_data.npy"
        np.save(self.test_data_file, data)

    def tearDown(self):
        # remove test data file
        os.remove(self.test_data_file)

    def test_split_segments(self):
        # test the split segments method
        obj = VehicleData(self.test_data_file)
        segments = obj.split_segments()

        self.assertEqual(len(segments), 2)

        # test segments id

        ids = [segment[0, 1] for segment in segments]
        self.assertEqual(set(ids), {0, 1})

    def test_by_id(self):
        # test getting data by id
        obj = VehicleData(self.test_data_file)

        first_id = obj.by_id(0)
        second_data = obj.by_id(1)

        # check if data contains correct IDs
        self.assertTrue(np.all(first_id[:, 1] == 0))
        self.assertTrue(np.all(second_data[:, 1] == 1))

    def test_pitfall_check(self):
        # test pitfall check
        obj = VehicleData("test_data.npy")
        has_pitfall = obj.pitfall_check()

        # here is no pitfall contidion
        self.assertFalse(has_pitfall)

    def test_plot(self):
        # test the plot image
        obj = VehicleData("test_data.npy")

        segments = obj.split_segments()

        # plot segments

        fig, ax = plt.subplots()
        obj.plot(segments)

        fig.savefig("./tests/actual_plot.png")

        # compare images
        expected_image = plt.imread("./tests/expected_plot.png")
        actual_image = plt.imread("./tests/actual_plot.png")
        np.testing.assert_array_equal(expected_image, actual_image)

        # cleanup the generated plot image
        plt.close(fig)
        os.remove("./tests/actual_plot.png")


if __name__ == "__main__":
    unittest.main()
