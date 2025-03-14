import math


def main():
    # Configuration
    gravity = 9.81
    target_data = [100, 20]

    # Variables
    current_player = 1
    is_match_running = True
    in_round = True
    did_the_banana_hit_the_target = False

    while is_match_running:
        if current_player == 1:
            player_input = get_player_input("[Player 1]")
            i = 0
            while in_round:
                position_data = get_position_based_on_time(gravity, i, player_input[0], player_input[1], player_input[2])
                did_the_banana_hit_the_target = check_if_banana_hit_target(position_data, target_data)
                i = i + 1

                if did_the_banana_hit_the_target == 1:
                    print(f"[Player 1] did hit the target!")
                    break
                if did_the_banana_hit_the_target == -1:
                    print(f"[Player 1] did miss the target!\nSwitching to next player!")
                    break

            if did_the_banana_hit_the_target == 1:
                break
            else:
                current_player = 2

        if current_player == 2:
            player_input = get_player_input("[Player 2]")
            i = 0
            while in_round:
                position_data = get_position_based_on_time(gravity, i, player_input[0], player_input[1], player_input[2])
                did_the_banana_hit_the_target = check_if_banana_hit_target(position_data, target_data)
                i = i + 1

                if did_the_banana_hit_the_target == 1:
                    print(f"[Player 2] did hit the target!")
                    break
                if did_the_banana_hit_the_target == -1:
                    print(f"[Player 2] did miss the target!\nSwitching to next player!")
                    break

            if did_the_banana_hit_the_target == 1:
                break
            else:
                current_player = 1


def get_player_input(player):
    throw_height = int(input(player + " Please enter the height you are throwing: "))
    throw_angle = math.radians(int(input(player + " Please enter your throw angle: ")))
    velocity = int(input(player + " Please enter your speed (m/s): "))

    return throw_height, throw_angle, velocity


def get_position_based_on_time(g, t, height, angle, speed):
    x = (speed * math.cos(angle) * t)
    y = height + (speed * math.sin(angle) * t - g / 2 * t * t)

    return int(x), int(y), t


def print_position(data):  # data should be a tuple from getPositionBasedOnTime()
    x_position = data[0]
    y_position = data[1]
    current_time = data[2]

    if y_position >= 0:
        print(f"Time {round(current_time, 2)}s || X:Y {round(x_position, 3)}:{round(y_position, 3)}")


def check_if_grounded(position_data):
    return position_data[1] > 0.0


def check_if_banana_hit_target(position_data, target_data):
    if position_data[1] < -1:
        return -1
    if position_data[0] > target_data[0] & position_data[1] > target_data[1]:
        return 1
    else:
        return 0




if __name__ == "__main__":
    main()
