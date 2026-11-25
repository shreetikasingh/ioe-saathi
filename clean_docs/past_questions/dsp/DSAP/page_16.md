Exam: 2074 Chaitra

1. Plot the sequence $x[n] = u[n] - u[n-3] + 5\delta[n-4] = nu[n-6]$. List out the properties of LTI system. $[3+2]$

2. Determine whether the following system are: $[3+3]$
   a) $y[n] = y[n-4] + x[n-4]$ is Time-invariant or not
   b) $y[n] = x^2[n]$ is Linear or Non-linear

3. Define a ROC. What are the properties of ROC of z-transform? Find the inverse Z-transform of $X(z) = (2z^2 + 2z^2 + 3z + 5) / (z^2 - 0.1z - 0.2)$, $\text{ROC}: |z| < 0.4$. $[1+3+5]$

4. The poles of a system are located at: $0.45-0.77i$ and $-2 \pm 0.3i$. Map the poles and zero in the z-plane and plot the magnitude response of the system. $[2+8]$

5. Obtain the Direct Form I and Direct Form II realization of the following system. $[5]$
   $3y[n] + y[n-1] + 2y[n-4] = 2x[n] + x[n-3]$

6. Determine the lattice coefficients corresponding to the FIR filter with the system function: $[5]$
   $H(z) = A_3(z) = 1 + \frac{52}{96}z^{-1} + \frac{25}{40}z^{-2} + \frac{1}{3}z^{-3}$

7. Design a digital low-pass filter with the following specification: $[12]$
   i) Pass-band magnitude constant to $0.7\text{ dB}$ below the frequency of $0.15\pi$
   ii) Stop-band attenuation at least $14\text{ dB}$ for the frequencies between $0.6\pi$ to $\pi$
      Use Butterworth approximation as a prototype and use impulse invariance method to obtain the digital filter.

8. Design a FIR linear phase filter using Kaiser window that meets the following specifications: $[9+3]$
   $|H(e^{j\omega})| \le 0.01, 0 \le |\omega| \le 0.25\pi$
   $0.95 \le |H(e^{j\omega})| \le 1.05, 0.35\pi \le |\omega| \le 0.6\pi$
   $|H(e^{j\omega})| \le 0.01, 0.65\pi \le |\omega| \le \pi$
   Also determine the minimum length $(M+1)$ of the impulse response and Kaiser window parameter $\beta$.

9. Why do we need DFT? Draw the butterfly structure to compute the DFT of the following signal using Radix-2 DIFFFT algorithm, and compute $X(2)$ and $X(1)$ only $x[n] = \{1.5, -1, 1.8, 0.6, 3, 1, 7\}$ $[3+7]$

10. Define zero padding. Find the linear convolution through circular convolution with padding of zeros for the following sequences: $x[n] = \{1, 1, 1, 1\}$ and $h[n]\{2, 3\}$. $[1+5]$