import matplotlib.pyplot as plt
import random as rd

x_s = [i for i in range(10)]
y_s = [rd.randint(40, 80) for i in range(10)]


def my_plot(x_list, y_list, title_txt):
    plt.plot(x_list, y_list)
    plt.title(title_txt)
    plt.show()


if __name__ == '__main__':
    print(type(my_plot(x_s, y_s)))