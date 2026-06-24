import matplotlib.pyplot as plt
import math


def logistic_derivative(y, r, K):
    """
    Computes the derivative dy/dt for the logistic growth equation.

    dy/dt = r * y * (1 - y / K)

    Parameters:
        y: current population/value
        r: growth rate
        K: carrying capacity

    Returns:
        The rate of change at the current value of y.
    """
    return r * y * (1 - y / K)


def euler_method(y0, r, K, t_start, t_end, step_size):
    """
    Approximates the solution to the logistic growth equation using Euler's method.

    Euler's method formula:
        next_y = current_y + step_size * derivative

    Parameters:
        y0: initial population/value
        r: growth rate
        K: carrying capacity
        t_start: starting time
        t_end: ending time
        step_size: size of each time step

    Returns:
        Two lists:
            times: the time values
            values: the approximate y values
    """
    times = []
    values = []

    t = t_start
    y = y0

    while t <= t_end:
        times.append(t)
        values.append(y)

        derivative = logistic_derivative(y, r, K)
        y = y + step_size * derivative
        t = t + step_size

    return times, values


def exact_solution(t, y0, r, K):
    """
    Computes the exact solution of the logistic growth equation.

    Formula:
        y(t) = K / (1 + ((K - y0) / y0) * e^(-r t))
    """
    return K / (1 + ((K - y0) / y0) * math.exp(-r * t))


def main():
    # Model parameters
    y0 = 10       # initial population/value
    r = 0.5       # growth rate
    K = 100       # carrying capacity
    t_start = 0
    t_end = 20
    step_size = 0.5

    # Euler approximation
    times, euler_values = euler_method(y0, r, K, t_start, t_end, step_size)

    # Exact solution values at the same time points
    exact_values = [exact_solution(t, y0, r, K) for t in times]

    # Plot both solutions
    plt.plot(times, euler_values, label="Euler Approximation")
    plt.plot(times, exact_values, label="Exact Solution")

    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Logistic Growth: Euler's Method vs Exact Solution")
    plt.legend()
    plt.grid(True)

    plt.savefig("logistic_growth_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
