import math
import utils


def print2D(maze):
    print("<---------START--------->")
    for row in maze:
        print(row)
    print("<----------END---------->")


def knapsackProblem(pizzas, maxSlices):
    dp = [[0 for _ in range(maxSlices + 1)] for _ in range(len(pizzas) + 1)]
    orderDP = [[set() for _ in range(maxSlices + 1)] for _ in range(len(pizzas) + 1)]

    for numOfPizza in range(len(pizzas) + 1):
        for slice in range(maxSlices + 1):
            if numOfPizza == 0:
                dp[numOfPizza][slice] = 0
            else:
                if (dp[numOfPizza - 1][slice - pizzas[numOfPizza - 1]] + pizzas[numOfPizza - 1]) if slice >= pizzas[numOfPizza - 1] else -math.inf > dp[numOfPizza - 1][slice]:
                    dp[numOfPizza][slice] = (dp[numOfPizza - 1][slice - pizzas[numOfPizza - 1]] + pizzas[numOfPizza - 1])
                    orderDP[numOfPizza][slice] = orderDP[numOfPizza][slice].union(orderDP[numOfPizza - 1][slice - pizzas[numOfPizza - 1]])
                    orderDP[numOfPizza][slice].add(numOfPizza - 1)
                else:
                    dp[numOfPizza][slice] = dp[numOfPizza - 1][slice]
                    orderDP[numOfPizza][slice] = orderDP[numOfPizza][slice].union(orderDP[numOfPizza - 1][slice])

    return len(orderDP[-1][-1]), orderDP[-1][-1]


def main():
    maxSlices, types, pizzas = utils.load_input_file("c_medium.in")
    print(knapsackProblem(pizzas, maxSlices))

    return


if __name__ == "__main__":
    main()
