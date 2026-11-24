map = ["##########",
       "#........#",
       "#........#",
       "#........#",
       "##########"]

player_x = 1
player_y = 1

def map_draw(map, player_x, player_y):

    for y in range(len(map)):
        for x in range(len(map[y])):
            if x == player_x and y == player_y:
                print("@", end="")
            else:
                print(map[y][x], end="")
        print()

while True:
    map_draw(map, player_x, player_y)
    cmd = input("go -> (w,a,s,d)  quit -> q : ").strip().lower()

    if cmd == "q":
        break

    next_x = player_x
    next_y = player_y

    if cmd == "w":
        next_y -= 1
    elif cmd == "s":
        next_y += 1
    elif cmd == "a":
        next_x -= 1
    elif cmd == "d":
        next_x += 1
    else:
        print("Not exist command")
        continue

    if map[next_y][next_x] != "#":
        player_y = next_y
        player_x = next_x
    else:
        print("There is a wall")
