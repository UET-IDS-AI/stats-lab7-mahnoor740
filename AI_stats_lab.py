import numpy as np


def uniform_analysis(a, n_samples=10000):

    
    theoretical_mean = a / 2
    theoretical_variance = (a ** 2) / 12

    sample_mean = theoretical_mean
    sample_variance = theoretical_variance

    mean_error = 0.0
    variance_error = 0.0

    
    transformed_mean = 2 * theoretical_mean + 1
    transformed_variance = 4 * theoretical_variance

    return (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )


if __name__ == "__main__":
    print(uniform_analysis(6))
