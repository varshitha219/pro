import matplotlib.pyplot as ploot
import numpy as me
Fs = 100
f = 5
sample = 100
x = me.arange(sample)
y = me.sin(2 * np.pi * f * x / Fs)
ploot.plot(x, y)
ploot.xlabel('sample(n)')
ploot.ylabel('voltage(V)')
ploot.show()