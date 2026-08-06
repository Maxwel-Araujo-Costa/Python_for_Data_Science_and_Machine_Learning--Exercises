import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2

def plot_basic_figure():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.plot(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    plt.show()

def plot_two_axes_figure():
    fig = plt.figure()
    ax1 = fig.add_axes([0,0,1,1])
    ax2 = fig.add_axes([0.2,0.5,.2,.2])
    ax1.plot(x,y)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax2.plot(x,y)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    plt.show()

def plot_inset_plot_with_custom_limits():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax2 = fig.add_axes([0.2,0.5,.4,.4])
    ax.plot(x,z)
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax2.plot(x,y)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('zoom')
    ax2.set_xlim(20,22)
    ax2.set_ylim(30,50)
    plt.show()

def create_side_by_side_subplots():
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].plot(x,y,color="blue", lw=3, ls='--')
    axes[1].plot(x,z,color="red", lw=3, ls='-')
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,2))
    axes[0].plot(x,y,color="blue", lw=5)
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[1].plot(x,z,color="red", lw=3, ls='--')
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("z")
    plt.show()

def main ():
    print("Exercise 1: Basic Figure")
    plot_basic_figure()

    print("Exercise 2: Figure with Two Axes")
    plot_two_axes_figure()

    print("Exercise 3: Inset Plot with Custom Limits")
    plot_inset_plot_with_custom_limits()

    print("Exercise 4: Creating Side-by-Side Subplots")
    create_side_by_side_subplots()

if __name__ == "__main__":
    main()