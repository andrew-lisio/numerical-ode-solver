import matplotlib.pyplot as plt
import math


def logistic_derivative(y, r, K):
    """
    Compute dy/dt for the logistic growth equation.

    dy/dt = r * y * (1 - y / K)

    Parameters:
        y (float): Current population or quantity.
        r (float): Growth rate.
        K (float): Carrying capacity.

    Returns:
        float: Rate of change at the current value of y.
    """
    return r * y * (1 - y / K)


def euler_method(y0, r, K, t_start, t_end, step_size):
    """
    Approximate the logistic growth equation using Euler's method.

    Euler's method estimates the next value using:

        next_y = current_y + step_size * derivative

    Parameters:
        y0 (float): Initial population or quantity.
        r (float): Growth rate.
        K (float): Carrying capacity.
        t_start (float): Starting time.
        t_end (float): Ending time.
        step_size (float): Size of each step forward in time.

    Returns:
        tuple: A list of time values and a list of approximate y values.
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
    Compute the exact solution of the logistic growth equation.

    The exact solution is used to compare against Euler's numerical approximation.

    Parameters:
        t (float): Time value.
        y0 (float): Initial population or quantity.
        r (float): Growth rate.
        K (float): Carrying capacity.

    Returns:
        float: Exact solution value at time t.
    """
    return K / (1 + ((K - y0) / y0) * math.exp(-r * t))


def main():
    """
    Run the logistic growth simulation and generate a comparison plot.
    """

    # Model parameters
    y0 = 10
    r = 0.5
    K = 100
    t_start = 0
    t_end = 20
    step_size = 0.5

    # Approximate the solution using Euler's method
    times, euler_values = euler_method(y0, r, K, t_start, t_end, step_size)

    # Compute the exact solution at the same time points
    exact_values = [exact_solution(t, y0, r, K) for t in times]

    # Create and save the plot
    plt.figure(figsize=(9, 6))
    plt.plot(times, euler_values, marker="o", label="Euler Approximation")
    plt.plot(times, exact_values, label="Exact Solution")

    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Logistic Growth: Euler's Method vs Exact Solution")
    plt.legend()
    plt.grid(True)

    plt.savefig("logistic_growth_plot.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
