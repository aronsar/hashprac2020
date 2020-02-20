import math


def print2D(maze):
    print("<---------START--------->")
    for row in maze:
        print(row)
    print("<----------END---------->")


def knapsackProblem(pizzas, maxSlices):
    dp = [[0 for _ in range(maxSlices)] for _ in range(len(pizzas) + 1)]

    for numOfPizza in range(len(pizzas) + 1):
        for slice in range(maxSlices):
            if numOfPizza == 0:
                dp[numOfPizza][slice] = 0
            else:
                dp[numOfPizza][slice] = max((dp[numOfPizza - 1][slice - pizzas[numOfPizza - 1]] + pizzas[numOfPizza - 1]) if slice >= pizzas[numOfPizza - 1] else -math.inf, dp[numOfPizza - 1][slice])
        print2D(dp)

    return dp[-1][-1]


def main():

    with open("a_example.in", "r") as inputFile:
        input = inputFile.read().splitlines()

    maxSlices, types = map(int, input[0].split(" "))
    pizzas = list(map(int, input[1].split(" ")))
    print(knapsackProblem(pizzas, maxSlices))

    return


if __name__ == "__main__":
    main()
