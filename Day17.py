import numpy as np
with open("input17.txt") as input:
    data = input.read().split("\n")[:-1]
    data = data[0].split(":")
    data = data[1].lstrip()
    data = data.split("=")
    data.extend(data[1].split(","))
    yRange = data[-3].split("..")
    yRange = [int(i) for i in yRange]
    xRange = data[-2].split("..")
    xRange = [int(i) for i in xRange]
    print(xRange, yRange)
    yTarget = abs(min(yRange[0], yRange[1])) - 1
    print(int(yTarget * (yTarget + 1) / 2))

    def point_collision(x, y, xRange=xRange, yRange=yRange):
        within_x = (x >= xRange[0]) and (x <= xRange[1])
        within_y = (y >= yRange[0]) and (y <= yRange[1])
        if within_x and within_y:
            return True
        else:
            return False

    def trajectory(x_speed, y_speed, x, y, xRange, yRange):
        x_coord = [x]
        y_coord = [y]
        while x <= xRange[1] and y >= yRange[0]:
            x += x_speed
            y += y_speed
            x_coord += [x]
            y_coord += [y]
            x_speed = max(0, x_speed-1)
            y_speed -= 1

        return (x_coord, y_coord)

    def check_trajectory(x_speed, y_speed, x=0, y=0, xRange=xRange, yRange=yRange):
        x_path, y_path = trajectory(x_speed, y_speed, x, y, xRange, yRange)
        hit_target = any(
            map(
                point_collision,
                x_path,
                y_path,
            )
        )
        if hit_target:
            return (x_speed, y_speed)
        else:
            return None

x_range = np.arange(0, 250)
y_range = np.arange(-250, 250)
x_mesh, y_mesh = np.meshgrid(x_range, y_range)
launch_tests = map(check_trajectory, x_mesh.ravel(), y_mesh.ravel())
successes = [hit for hit in launch_tests if hit]
print(len(successes))


