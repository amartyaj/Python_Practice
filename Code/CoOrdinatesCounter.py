#!/usr/bin/env python

coordinates = [ {"x": 5, "y": 4},
                {"x": 3, "y": 6},
                {"x": 5, "y": 4},
                {"x": 3, "y": 6},
                {"x": 2, "y": 4} ]

counter = {}

for coordinate in coordinates:
    try:
        counter[tuple(coordinate.items())]
    except KeyError:
        counter[tuple(coordinate.items())] = 1
    else:
        counter[tuple(coordinate.items())] += 1

print(counter)

