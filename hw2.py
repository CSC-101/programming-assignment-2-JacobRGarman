import data
from typing import Optional, List


# Part 1 - Define `create_rectangle`
def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    top_left = data.Point(min(point1.x, point2.x), max(point1.y, point2.y))
    bottom_right = data.Point(max(point1.x, point2.x), min(point1.y, point2.y))
    return data.Rectangle(top_left, bottom_right)


# Part 2 - Define `shorter_duration_than`
def shorter_duration_than(duration1: data.Duration, duration2: data.Duration) -> bool:
    return (duration1.minutes * 60 + duration1.seconds) < (duration2.minutes * 60 + duration2.seconds)


# Part 3 - Define `songs_shorter_than`
def songs_shorter_than(songs: List[data.Song], duration: data.Duration) -> List[data.Song]:
    return [song for song in songs if shorter_duration_than(song.duration, duration)]


# Part 4 - Define `running_time`
def running_time(songs: List[data.Song], playlist: List[int]) -> data.Duration:
    total_seconds = sum(
        (songs[i].duration.minutes * 60 + songs[i].duration.seconds)
        for i in playlist if 0 <= i < len(songs)
    )
    return data.Duration(total_seconds // 60, total_seconds % 60)


# Part 5 - Define `validate_route`
def validate_route(city_links: List[List[str]], route: List[str]) -> bool:
    if len(route) <= 1:
        return True

    city_pairs = {frozenset(link) for link in city_links}
    return all(frozenset(route[i:i + 2]) in city_pairs for i in range(len(route) - 1))


# Part 6 - Define `longest_repetition`
def longest_repetition(numbers: List[int]) -> Optional[int]:
    if not numbers:
        return None

    max_length = current_length = 1
    max_start = current_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
            current_length = 1
            current_start = i
    if current_length > max_length:
        max_start = current_start

    return max_start
