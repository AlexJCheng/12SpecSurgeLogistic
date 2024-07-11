import matplotlib.pyplot as plt
import numpy as np

# Define the domain
global x
x = np.linspace(0, 90 , 900)

# Plot size
ymin = 0
ymax = 4
ystep = 1
xmin = 0
xmax = 90
xstep = 30

def calc_eq(a, k, l):
    y = l / (1 + a * np.e ** (-1 * k * (x)))
    return y

def plot_setup():
    plt.figure(figsize=(6,6))
    
    # Add thick lines at x=0 and y=0
    plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
    plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

    # Set labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Logistic Function')

    # Set the limits of x and y axes
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    # Show grid
    plt.grid(which = 'major', linewidth = 0.5)
    plt.xticks(np.arange(xmin,xmax+xstep,xstep))
    plt.yticks(np.arange(ymin,ymax+ystep,ystep))

def plot_inf(a, k, l):
    plt.plot(np.log(a)/k, l/(2), marker = 'o')
    plt.annotate(f'({round(np.log(a)/k, 2)}, {round(l/2, 2)})', (np.log(a)/k, l/2))
    print((np.log(a)/k, l/2))

def main():
    plot_setup()
    k = 0.1
    a = np.e ** (36* k)
    l = 3.4
    '''
    #Multiple array of A
    for i in a:
        y = calc_eq(i, k, l)
        plt.plot(x, y, label = f'{l} / (1 + {i}e^(-{k}x))')
        plot_inf(i, k, l)'''
    
    '''
    #Multiple array of K
    for i in k:
        y = calc_eq(a, i, l)
        plt.plot(x, y, label = f'{l} / (1 + {a}e^(-{i}x))')
        plot_inf(a, i, l)'''
    
    '''
    #Multiple array of L
    for i in l:
        y = calc_eq(a, k, i)
        plt.plot(x, y, label = f'{i} / (1 + {a}e^(-{k}x))')
        plot_inf(a, k, i)'''
    
    y = calc_eq(a, k, l)
    plt.plot(x, y, label = f'{l} / (1 + {a}e^(-{k}x))')
    plot_inf(a, k, l)

    plt.legend()
    plt.savefig(f'MDMLog{l}(1 + {a}e^(-{k}x)).png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()

