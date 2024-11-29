from scipy import stats
import matplotlib.pyplot as plt
"""
Define functions for linear regression
"""

def get_line_of_best_fit(x, y, x_axis):
    slope, y_intercept, r, p, err = stats.linregress(x, y)
    r_squared = r ** 2
    
    line_of_best_fit_y = [slope * input + y_intercept for input in x]
    
    plt.scatter(x, y, color='b', label='Points')
    plt.plot(x, line_of_best_fit_y, color='r', label=f'Line of Best Fit w/ $R^2 = {r_squared:.3f}$')
    
    # Set plot labels and title
    plt.xlabel(x_axis)
    plt.ylabel("Score Differential")
    plt.title(f"Score Differential vs {x_axis}")
    
    # Show legend
    plt.legend()
    
    plt.savefig(f"linear-regression-pngs/{x_axis}.png")
    
    plt.clf()
    
    return slope, y_intercept, r_squared
    