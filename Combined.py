import matplotlib.pyplot as plt
import numpy as np

# Define the domain
global x1, x2
x1 = np.linspace(0, 200, 2000)
x2 = np.linspace(200, 2000, 18000)

# Plot size
ymin = 0
ymax = 4
ystep = 1
xmin = 0
xmax = 2000
xstep = 500

def calc_s_eq(a, k):
    return a * x2 * np.e ** (-1 * k * x2)

def calc_eq(a, k, l):
    return l / (1 + a * np.e ** (-1 * k * (x1)))
    
def plot_setup():
    plt.figure(figsize=(6,6))
    
    # Add thick lines at x=0 and y=0
    plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
    plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

    # Set labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Surge Function')

    # Set the limits of x and y axes
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    # Show grid
    plt.grid(which = 'major', linewidth = 0.5)
    plt.xticks(np.arange(xmin,xmax+xstep,xstep))
    plt.yticks(np.arange(ymin,ymax+ystep,ystep))

def plot_s_inf(a, k):
    plt.plot(2/k, (2*a)/(k * np.e ** 2), marker = 'o')
    plt.annotate(f'({2/k}, {round((2*a)/(k * np.e ** 2),2)})', (2/k + 0.3, (2*a)/(k * np.e ** 2)))

def plot_s_max(k, y):
    plt.plot(1/k, max(y), marker = 'o')
    plt.annotate(f'({1/k}, {round(max(y),2)})', (1/k + 0.3, max(y)))

def plot_inf(a, k, l):
    plt.plot(np.log(a)/k, l/(2), marker = 'o')
    plt.annotate(f'({round(np.log(a)/k, 2)}, {round(l/2, 2)})', (np.log(a)/k, l/2))
    print((np.log(a)/k, l/2))

def main():
    plot_setup()
    a = 0.048
    k = 0.0052
    lk = 0.1
    la = np.e ** (36* lk)
    ll = 3.4

    y1 = calc_s_eq(a, k)
    plt.plot(x2, y1, label = f'{a}xe^(-{k}x)')
    y2 = calc_eq(la, lk, ll)
    plt.plot(x1, y2, label = f'{ll} / (1 + {la}e^(-{lk}x))')
    plot_s_max(k, y1)
    plot_s_inf(a, k)
    plot_inf(la, lk, ll)

    plt.legend()
    plt.savefig(f'MDMfinal.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()


    


