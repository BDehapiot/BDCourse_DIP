#%% Imports

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'

#%% 

# Define the time range
t_analog = np.arange(0, 2*np.pi, 0.1)
t_digital = np.arange(0, 2*np.pi, 0.25)

# Define the analog and digital sinusoid functions
analog_signal = np.sin(t_analog)
digital_signal = np.sin(t_digital)

# Create a new figure
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-1.1, 1.1)
ax.set_yticks(np.linspace(-1, 1, 5))
# plt.grid()

# Plot the analog signal
ax.plot(t_analog, analog_signal, 'k-', label='Analog')

# Plot the digital signal
ax.step(t_digital, digital_signal, 'r-', label='Digital', where='mid')

# Add a title and legend to the plot
ax.set_title('Analog vs Digital Signal')
ax.legend()

# save as svg
plt.savefig('analog2digital.svg')