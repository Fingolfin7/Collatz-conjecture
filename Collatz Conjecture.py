from matplotlib import pyplot as plt


def findMax(list_vals):
    maxVal = 0
    for val in list_vals:
        if val > maxVal:
            maxVal = val

    return maxVal


def run_sequence(seed=int):
    val_list = []

    def iterate(val, count):
        if val == 0:
            return
        if val == 1 and count > 0:  # base case
            # val_list.append(val)
            return

        elif val % 2 == 1:
            val_list.append((val * 3) + 1)  # if val is odd multiply by three and add 1 (3n + 1)

        elif val % 2 == 0:
            val_list.append(val / 2)  # if val is even divide by two

        index = count
        count += 1

        iterate(val_list[index], count)

    iterate(seed, 0)
    print(f"Steps for seed {seed}: {val_list}")
    print(f"Max value {findMax(val_list)}\n")
    plt.plot(list(range(0, len(val_list))), val_list)


def parse_input(in_str):
    startIndex = 0
    commaIndex = 0
    parsed_vals = []

    while True:
        commaIndex = in_str.find(",", commaIndex)

        if commaIndex == -1:
            parsed_vals.append(int(in_str[startIndex:]))
            break
        else:
            parsed_vals.append(int(in_str[startIndex: commaIndex]))
            startIndex = commaIndex + 1
            commaIndex += 1

    return parsed_vals


def main():
    print("Enter a seed list (of finite positive integers!).\nFor example: '1,2,3' or '7' or '27, 123, 12'")
    seed_list = parse_input(input(">"))
    print(f"Seeds: {seed_list}")

    for seed in seed_list:
        run_sequence(seed)

    plt.title("Collatz Conjecture")
    plt.xlabel("Counts (Stopping Times)")
    plt.ylabel("Values")

    plt.show()


main()
