from datetime import datetime
from main import get_weather_data
import unittest


class TestWeatherApi(unittest.TestCase):

    def test_location_name(self):
        self.assertEqual(get_weather_data(
            "Barcelona", "ES").location_name, "Barcelona")
        self.assertEqual(get_weather_data(
            "Toronto", "CA").location_name, "Toronto")
        self.assertEqual(get_weather_data(
            "Cordoba", "AR").location_name, "Cordoba")

    def test_time(self):
        self.assertEqual(get_weather_data(
            "Buenos Aires", "AR").requested_time, datetime.now())
        self.assertTrue(":" in str(
            get_weather_data("Cordoba", "AR").requested_time))
        self.assertTrue(
            type(int(get_weather_data("Cordoba", "AR").sunrise)) == int)
        self.assertTrue(
            type(int(get_weather_data("Cordoba", "AR").sunset)) == int)

    def test_humidity(self):
        self.assertTrue(
            type(int(get_weather_data("Cordoba", "AR").humidity)) == int)

    def test_pressure(self):
        self.assertTrue(
            type(int(get_weather_data("Cordoba", "AR").pressure)) == int)
