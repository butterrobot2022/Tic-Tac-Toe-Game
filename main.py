options = ['x', 'o']

layout = "1 | 2 | 3  \n" \
         "4 | 5 | 6  \n" \
         "7 | 8 | 9  \n"

game_is_on = True
print(layout)

while game_is_on:
    n = 0
    ints = [str(n) for n in range(1, 10)]
    choice = input("Input your choice: ").lower()

    if choice == "break":
        game_is_on = False
        print('Game Over!')

    if choice in options:

        num = input("Where? ")
        if num not in ints:
            print("Invalid input")
        layout = layout.replace(num, choice, 1)
        print(layout)

    if (layout[0] == 'x' and layout[12] == 'x' and layout[24] == 'x') or (layout[4] == 'x' and layout[16] == 'x' and
                                                                          layout[28] == 'x') or (
            layout[8] == 'x' and layout[20] == 'x' and layout[32] == 'x') or (
            layout[0] == 'x' and layout[4] == 'x' and layout[8] == 'x') or (
            layout[12] == 'x' and layout[16] and layout[20] == 'x') or (
            layout[24] == 'x' and layout[28] == 'x' and layout[32] == 'x') \
            or (layout[0] == 'x' and layout[16] == 'x' and layout[32] == 'x') or (
            layout[8] == 'x' and layout[16] == 'x' and layout[24] == 'x'):
        print("PlayerX wins!")
        print("Game Over...")
        game_is_on = False

    elif (layout[0] == 'o' and layout[12] == 'o' and layout[24] == 'o') or (layout[4] == 'o' and layout[16] == 'o' and
                                                                            layout[28] == 'o') or (
            layout[8] == 'o' and layout[20] == 'o' and layout[32] == 'o') or (
            layout[0] == 'o' and layout[4] == 'o' and layout[8] == 'o') or (
            layout[12] == 'o' and layout[16] and layout[20] == 'o') or (
            layout[24] == 'o' and layout[28] == 'o' and layout[32] == 'o') \
            or (layout[0] == 'o' and layout[16] == 'o' and layout[32] == 'o') or (
            layout[8] == 'o' and layout[16] == 'o' and layout[24] == 'o'):
        print("PlayerO wins!")
        print("Game Over...")
        game_is_on = False

    elif '1' not in layout and '2' not in layout and '3' not in layout and '4' not in layout and '5' not in layout and '6' not in layout and '7' not in layout and '8' not in layout and '9' not in layout:
        game_is_on = False
        print("Game Over!")
