Exam: 2081 Bhadra

1. Determine if the signal $x[n] = \cos\left(\frac{2\pi n}{5}\right) + \sin\left(\frac{\pi n}{3}\right)$ is periodic or not. If the signal is periodic, find its fundamental period. $[4]$

2. Find the output of an LTI System with impulse response $h[n] = 2\delta[n+1] + 2\delta[n-1]$ when an input of $x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3]$ is applied to it. $[5]$

3. Define ROC of z-transform. Find the inverse z-transform using partial fraction expansion of
$$X(z) = \frac{2z^3 - 5z^2 + z + 3}{(z-1)(z-2)} \quad \text{for ROC } |z| < 1$$ $[1+5]$

4. Plot the pole - zero in z plane and draw magnitude response (not to the scale) of the system described by difference equation
$$y[n] - 0.4\,y[n-1] + 0.25\,y[n-2] = x[n] - 0.4\,x[n-1]$$ $[3+7]$

5. Compute the lattice and ladder coefficients and draw lattice-ladder structure for the given IIR system
$$H(z) = \frac{1 + z^{-1} + z^{-2}}{(1 + 0.5z^{-1})(1 + 0.3z^{-1})(1 + 0.4z^{-1})}$$ $[6+4]$

6. Design a low pass FIR filter using suitable window to meet following specifications: $[8]$
$$0.99 \leq |H(e^{jw})| \leq 1.01 \quad \text{for } 0 \leq |w| \leq 0.3\pi$$
$$|H(e^{jw})| \leq 0.01 \quad \text{for } 0.35\pi \leq |w| \leq \pi$$

7. What do you mean by optimum filter? Describe the Remez exchange algorithm for FIR filter design along with the flowchart. $[1+6]$

8. Design a digital low pass IIR filter using Bilinear transformation to meet following specifications: $[12+3]$
$$0.9 \leq |H(e^{jw})| \leq 1 \quad \text{for } 0 \leq |w| \leq \frac{\pi}{2}$$
$$|H(e^{jw})| \leq 0.2 \quad \text{for } \frac{3\pi}{4} \leq |w| \leq \pi$$
Use Butterworth approximation for design with sampling frequency of $1\text{Hz}$. Compare Impulse Invariance Method and Bilinear Transformation method.

9. How does FFT reduce computational complexity compared to direct calculation of DFT?
Compute $8$-point DFT of $x[n] = \{1, -2, -4, 3, 0, 1\}$ using DIT-FFT algorithm. $[2+7]$

10. If $X_1(k)$ and $X_2(k)$ are the $5$-point DFT of $x_1(n) = 3^n \;\; 0 \leq n \leq 3$ and $x_2(n) = 2^n \;\; 0 \leq n \leq 4$. Find $x_3(n)$ if $X_3(k) = X_1(k)X_2(k)$ $[6]$