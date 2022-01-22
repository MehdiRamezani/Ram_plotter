import matplotlib.colors as clr
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline, BSpline , UnivariateSpline

class MidpointNormalize(clr.Normalize):
    def __init__(self, vmin=None, vmax=None, vcenter=None, clip=False):
        self.vcenter = vcenter
        clr.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.vcenter, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))
