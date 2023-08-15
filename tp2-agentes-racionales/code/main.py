from reflexiveAgent import ReflexiveAgent
from environment import Environment
import random
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Constants
    env_sizes = [2**k for k in range(1, 8)]
    dirt_rates = [0.1, 0.2, 0.4, 0.8]
    iters = 100
    # Array to store performance
    performance = [
        [None for _ in range(len(env_sizes))] for _ in range(len(dirt_rates))
    ]

    for i in range(len(dirt_rates)):
        for j in range(len(env_sizes)):
            size = env_sizes[j]

            # Store avg performance
            points = 0
            moves = 0
            clean_rate = 0

            for k in range(iters):
                env = Environment(size, size, dirt_rates[i])
                agent = ReflexiveAgent(
                    random.randint(
                        0, size - 1), random.randint(0, size - 1), env
                )
                points += agent.points
                moves += 1000 - agent.remaining_moves
                clean_rate += 1 - (env.dirty_squares /
                                   env.initial_dirty_squares)

            performance[i][j] = [
                points / iters,
                moves / iters,
                clean_rate / iters,
                moves / points,
            ]

    # Plot performance
    for line in performance:
        print(*line)

    # Constants for plotting
    colors = [
        "r",
        "g",
        "b",
        "y",
    ]

    x = env_sizes
    X_axis = np.arange(len(x))
    width = 0.2

    # Plot 1
    fig1 = plt.figure(figsize=(10, 10))
    ax1 = fig1.add_subplot()

    for i in range(len(dirt_rates)):
        y = [line[2] for line in performance[i]]
        ax1.bar(
            X_axis - 1.5 * width + width * i,
            y,
            color=colors[i],
            width=width,
            label=f"dirt_rate={dirt_rates[i]}",
        )

    ax1.set_xlabel("Environment size")
    ax1.set_xticks(X_axis, x)
    ax1.set_ylabel("Clean rate")
    ax1.set_title(
        "Clean rate vs environment size\n(100 iterations with a max of 1000 moves)"
    )
    ax1.legend()

    # Save figure to file
    fig1.savefig("clean_rate.png")

    # Plot 2
    fig2 = plt.figure(figsize=(10, 10))
    ax2 = fig2.add_subplot()

    for i in range(len(dirt_rates)):
        y = [line[3] for line in performance[i]]
        ax2.bar(
            X_axis - 1.5 * width + width * i,
            y,
            color=colors[i],
            width=width,
            label=f"dirt_rate={dirt_rates[i]}",
        )

    ax2.set_xlabel("Environment size")
    ax2.set_xticks(X_axis, x)
    ax2.set_ylabel("Moves per point")
    ax2.set_title(
        "Moves per point vs environment size\n(100 iterations with a max of 1000 moves)"
    )
    ax2.legend()

    # Save figure to file
    fig2.savefig("moves_per_point.png")

    # # Plot 3
    # # Requiere cambiar el eje y a escala logaritmica y desactivar el limite de movimientos
    # fig3 = plt.figure(figsize=(10, 10))
    # ax3 = fig3.add_subplot()

    # for i in range(len(dirt_rates)):
    #     y = [line[1] for line in performance[i]]
    #     ax3.bar(
    #         X_axis - 1.5 * width + width * i,
    #         y,
    #         color=colors[i],
    #         width=width,
    #         label=f"dirt_rate={dirt_rates[i]}",
    #     )

    # ax3.set_xlabel("Environment size")
    # ax3.set_xticks(X_axis, x)
    # ax3.set_ylabel("Moves")
    # ax3.set_yscale("log")
    # ax3.set_title(
    #     "Moves to clear 100% vs environment size\n(logarithmic scale for y-axis)"
    # )
    # ax3.legend()

    # fig3.savefig("moves.png")

    # Plot 4 - avg points
    fig4 = plt.figure(figsize=(10, 10))
    ax4 = fig4.add_subplot()

    for i in range(len(dirt_rates)):
        y = [line[0] for line in performance[i]]
        ax4.bar(
            X_axis - 1.5 * width + width * i,
            y,
            color=colors[i],
            width=width,
            label=f"dirt_rate={dirt_rates[i]}",
        )

    ax4.set_xlabel("Environment size")
    ax4.set_xticks(X_axis, x)
    ax4.set_ylabel("Points")
    ax4.set_yscale("log")
    ax4.set_title(
        "Points vs environment size\n(100 iterations with a max of 1000 moves, logarithmic scale)"
    )
    ax4.legend()

    # Save figure to file
    fig4.savefig("points.png")
    plt.show()
