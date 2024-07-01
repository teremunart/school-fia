import math


def main():
    # Configuration
    gravity = 9.81
    steps = .01  # increase for smaller steps, decrease for more steps

    # Input
    throw_height = float(input("Please enter the height you are throwing: "))
    throw_angle = math.radians(float(input("Please enter your throw angle: ")))
    velocity = float(input("Please enter your speed (m/s): "))

    # Variables
    is_in_air = True
    time_spent = .0
    position_data = []
    highestHeight = 0.0

    while is_in_air:
        position_data = getPositionBasedOnTime(gravity, time_spent, throw_height, throw_angle, velocity)
        printPosition(position_data)
        is_in_air = checkIfGrounded(position_data)

        time_spent = time_spent + steps

        if highestHeight < position_data[1]:
            highestHeight = position_data[1]

    print(f"Your max height: {round(highestHeight, 2)}m \nYour max distance {round(position_data[0], 2)}m")


def getPositionBasedOnTime(g, t, height, angle, speed):
    x = (speed * math.cos(angle) * t)
    y = height + (speed * math.sin(angle) * t - g / 2 * t * t)

    return x, y, t


def printPosition(data):  # data should be a tuple from getPositionBasedOnTime()
    x_position = data[0]
    y_position = data[1]
    current_time = data[2]

    if y_position >= 0:
        print(f"Time {round(current_time, 2)}s || X:Y {round(x_position, 3)}:{round(y_position, 3)}")


def checkIfGrounded(position_data):
    return position_data[1] > 0.0


if __name__ == "__main__":
    main()
