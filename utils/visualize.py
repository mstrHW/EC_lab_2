import matplotlib.pyplot as plt
import os


def plot_path(path, coords, epoch, images_dir=None, show_plots=0):
    for i in range(len(path) - 1):
        x = [coords[path[i]][0], coords[path[i + 1]][0]]
        y = [coords[path[i]][1], coords[path[i + 1]][1]]
        plt.plot(x, y, marker='o', markersize=2)

    plt.plot(
        [coords[path[len(path)-1]][0], coords[path[0]][0]],
        [coords[path[len(path)-1]][1], coords[path[0]][1]],
        marker='o',
        markersize=2,
    )

    title = 'Best path with {} iterations'.format(epoch)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')

    if images_dir is not None:
        plt.savefig(os.path.join(images_dir, title))
    plt.clf()

    if show_plots:
        plt.show()


def plot_convergence(x_list, y_list, images_dir=None, show_plots=0):
    title = 'Convergence'

    plt.plot(x_list, y_list)
    plt.xlabel('Iteration')
    plt.ylabel('Minimal distance')
    plt.title(title)

    if images_dir is not None:
        plt.savefig(os.path.join(images_dir, title))
    plt.clf()

    if show_plots:
        plt.show()
