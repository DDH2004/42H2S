#!/usr/bin/env python
#arrays/lists

import scipy.stats
# import numpy as np
hi1 = input("")
a = min(hi1)
b = max(hi1)
mean1 = np.mean(hi1)
mid1 = np.median(hi1)
mode1 = scipy.stats.mode(hi1)
print('Min: ' + str(a))
print('Max: ' + str(b))
print('Mean: ' + str(mean1))
print('Median: ' + str(mid1))
print('Mode: ' + str(mode1[0][0]))
print('Range: ' + str(b - a))