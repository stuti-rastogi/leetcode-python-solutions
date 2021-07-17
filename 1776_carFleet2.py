class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # check cars to the right, store index in stack
        # always monotonically increasing in speed
        stack = []
        num_cars = len(cars)
        collision_times = [-1] * num_cars

        for i in range(num_cars-1, -1, -1):
            p, s = cars[i]
            while stack:
                ahead_car_p, ahead_car_s = cars[stack[-1]]
                # possible collision
                if s > ahead_car_s:
                    time = (ahead_car_p - p) / (s - ahead_car_s)
                    # if the car in front is going to collide with a car before our current car
                    # reaches the car in front, no point in considering the car in front
                    # its speed will get slowed down to the car it collides with
                    if collision_times[stack[-1]] > 0 and time >= collision_times[stack[-1]]:
                        stack.pop()
                    else:
                        break
                # no need to consider this car on stack again
                # because current car is slower so that blocks any cars to left
                else:
                    stack.pop()
            # if something is left on stack, that is the car our current car collides with
            if stack:
                collision_times[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)

        return collision_times
