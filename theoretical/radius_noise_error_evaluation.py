# ---   IMPORTS   --- #
# ------------------- #
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# ---   RESULTS   --- #
# ------------------- #
# Directory for the error-radius experiments with noise on the one-sheet hyperb.
HYPERBOLOID_RESULTS='/ext4/lidar_data/math/geomfeats2nd/noise/hyperboloid/'
# Directory for the error-radius experiments with noise on the hyperb. parabol.
PARABOLOID_RESULTS='/ext4/lidar_data/math/geomfeats2nd/noise/paraboloid/'
# Directory for the error-radius experiments with noise on the ellipsoid
ELLIPSOID_RESULTS='/ext4/lidar_data/math/geomfeats2nd/noise/ellipsoid/'
# Directory for the error-radius experiments with noise on the cylinder
CYLINDER_RESULTS='/ext4/lidar_data/math/geomfeats2nd/noise/cylinder/'
# Directory for the error-radius experiments with noise on the catenoid
CATENOID_RESULTS='/ext4/lidar_data/math/geomfeats2nd/noise/catenoid/'
# Directory for the error-radius experiments with noise on the toroid
TOROID_RESULTS='/ext4/lidar_data/math/geomfeats2nd/noise/toroid/'


# ---  METHODS  --- #
# ----------------- #
def digest_results(results_dir, case_idx, variety, geom_feat):
    # Iterate over results
    pass  # TODO Rethink : Implement


# ---   MAIN   --- #
# ---------------- #
if __name__ == '__main__':
    # Prepare figure
    fig = plt.figure(figsize=(12, 5))
    # Digest results
    digest_results(
        HYPERBOLOID_RESULTS, 0, 'One-sheet hyperboloid', 'twGaussC'
    )
    digest_results(
        PARABOLOID_RESULTS, 1, 'Hyperbolic paraboloid', 'twMeanC'
    )
    digest_results(
        ELLIPSOID_RESULTS, 2, 'Ellipsoid', 'twGaussC'
    )
    digest_results(
        CYLINDER_RESULTS, 3, 'Cylinder', 'twMeanC'
    )
    digest_results(
        CATENOID_RESULTS, 4, 'Catenoid', 'twGaussC'
    )
    digest_results(
        TOROID_RESULTS, 5, 'Toroid', 'twMeanC'
    )
    # Format figure
    fig.tight_layout()
    # Save and show figure
    plt.savefig('/tmp/radius_noise_error.jpg', dpi=300)
    plt.show()
