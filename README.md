# Numerical ODE Solver

This project uses Python to approximate and visualize the solution to an ordinary differential equation using Euler's method. The first version focuses on the logistic growth equation, a common model used to describe population growth with a carrying capacity.

## Project Goal

The goal of this project is to connect differential equations with computational mathematics by implementing a numerical method from scratch and comparing the approximation to the exact solution.

This project demonstrates:

- Python programming
- Basic numerical methods
- Differential equations
- Data visualization with Matplotlib
- Mathematical modeling
- GitHub project documentation

## Logistic Growth Equation

The logistic growth equation is:

`dy/dt = r y (1 - y/K)`

where:

- `y` is the population or quantity being modeled
- `t` is time
- `r` is the growth rate
- `K` is the carrying capacity

Unlike simple exponential growth, logistic growth slows down as the population approaches the carrying capacity.

## Euler's Method

Euler's method is a numerical technique for approximating the solution to a differential equation.

The method uses the current value and the current slope to estimate the next value:

next_y = current_y + step_size * derivative

In this project, Euler's method is used to approximate the logistic growth equation over time.

Parameters Used
Initial value: y0 = 10
Growth rate: r = 0.5
Carrying capacity: K = 100
Start time: t = 0
End time: t = 20
Step size: 0.5
Results

The graph below compares the Euler approximation to the exact solution of the logistic growth equation.

The Euler approximation follows the same general pattern as the exact solution. 
The population starts at 10, increases quickly, and gradually levels off near the carrying capacity of 100. 
Since Euler's method is an approximation, small differences appear between the numerical and exact solutions.

Files
logistic_growth_euler.py      Python script implementing Euler's method
logistic_growth_plot.png      Graph comparing Euler approximation and exact solution
README.md                     Project explanation and documentation

## How to Run

To run this project locally, install Matplotlib:

pip install matplotlib

Then run:

python logistic_growth_euler.py

or, on Windows:

py logistic_growth_euler.py
Future Improvements

Future versions of this project may include:

Smaller step-size comparisons
Error analysis
Fourth-order Runge-Kutta method
SciPy solver comparison
Additional differential equation models such as SIR, predator-prey, and damped harmonic motion
Interactive visualization using Streamlit

## What I Learned

This project helped me practice translating a differential equation into Python code, implementing a numerical approximation method, and comparing computational results to an exact mathematical solution.
