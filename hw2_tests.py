import data
import hw2
import unittest


# Test cases for classes and functions defined in the data and hw2 modules.
class TestCases(unittest.TestCase):
    # Part 1 - Testing Point class from data module

    def test_point_initialization(self):
        point = data.Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_point_equality(self):
        point1 = data.Point(1, 2)
        point2 = data.Point(1, 2)
        point3 = data.Point(2, 1)
        self.assertEqual(point1, point2)
        self.assertNotEqual(point1, point3)

    # Part 2 - Testing Duration class from data module

    def test_duration_initialization(self):
        duration = data.Duration(2, 30)
        self.assertEqual(duration.minutes, 2)
        self.assertEqual(duration.seconds, 30)

    def test_duration_repr(self):
        duration = data.Duration(2, 30)
        self.assertEqual(repr(duration), 'Duration(2, 30)')

    # Part 3 - Testing Song class from data module

    def test_song_initialization(self):
        duration = data.Duration(3, 21)
        song = data.Song("Artist", "Title", duration)
        self.assertEqual(song.artist, "Artist")
        self.assertEqual(song.title, "Title")
        self.assertEqual(song.duration, duration)

    def test_song_equality(self):
        song1 = data.Song("Artist", "Title", data.Duration(3, 21))
        song2 = data.Song("Artist", "Title", data.Duration(3, 21))
        self.assertEqual(song1, song2)

    # Part 4 - Testing Rectangle class from data module

    def test_rectangle_initialization(self):
        rect = data.Rectangle(data.Point(1, 1), data.Point(3, 3))
        self.assertEqual(rect.top_left, data.Point(1, 1))
        self.assertEqual(rect.bottom_right, data.Point(3, 3))

    def test_rectangle_equality(self):
        rect1 = data.Rectangle(data.Point(1, 1), data.Point(3, 3))
        rect2 = data.Rectangle(data.Point(1, 1), data.Point(3, 3))
        self.assertEqual(rect1, rect2)

    # Part 5 - Additional functionality in hw2 module

    def test_create_rectangle(self):
        rect = hw2.create_rectangle(data.Point(2, 2), data.Point(10, 10))
        self.assertEqual(rect.top_left, data.Point(2, 10))
        self.assertEqual(rect.bottom_right, data.Point(10, 2))

    def test_shorter_duration_than(self):
        d1 = data.Duration(3, 30)
        d2 = data.Duration(4, 0)
        self.assertTrue(hw2.shorter_duration_than(d1, d2))
        self.assertFalse(hw2.shorter_duration_than(d2, d1))

    # Part 6 - Testing edge cases and complex scenarios in hw2

    def test_running_time(self):
        song1 = data.Song("Artist A", "Song A", data.Duration(3, 30))  # Corrected order
        song2 = data.Song("Artist B", "Song B", data.Duration(4, 0))   # Corrected order
        duration = hw2.running_time([song1, song2], [0, 1, 0])
        self.assertEqual(duration.minutes, 11)
        self.assertEqual(duration.seconds, 0)

    def test_validate_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        self.assertTrue(hw2.validate_route(city_links, ['san luis obispo', 'santa margarita', 'atascadero']))
        self.assertFalse(hw2.validate_route(city_links, ['san luis obispo', 'atascadero']))

    def test_longest_repetition(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3]), 4)
        self.assertEqual(hw2.longest_repetition([]), None)


# Runs the test cases when the file is executed directly.
if __name__ == '__main__':
    unittest.main()
