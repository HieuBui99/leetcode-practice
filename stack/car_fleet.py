from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    - Calculate the time each car will take to reach the target.
    - Sort the cars based on their position in descending order because we know the definite time of the last car.
    - Loop through the cars and check if the current car will take more time than the last car (fleet).
    """
    cars = sorted(zip(position, speed), reverse=True)
    time = [(target - pos)/spd for pos, spd in cars]
    n_fleet = 1

    t = time[0]
    for i in range(1, len(cars)):
        cur_time = time[i]
        if cur_time > t:
            t = cur_time
            n_fleet += 1
    
    return n_fleet