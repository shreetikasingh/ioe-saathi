Exam: 2069 Chaitra

1. Define Energy and Power type signal with suitable example. Check the signal $x[n] = \cos(2n\pi/5) + \sin(\pi n/3)$ is periodic or not. $[2+2]$

2. Define LTI system. Find the output of LTI system having impulse response $h[n] = 2u[n] - 2u[n-4]$ and input signal $x[n] = (1/3)^n u[n]$. $[1+4]$

3. State the properties of region of convergence (ROC)? Derive the time shifting property of Z-transform. $[3+3]$

4. Why do we need Difference Equation? Draw Pole-zero in Z-Plane and plot magnitude response (not to the scale) of the system described by difference equation $y[n] - 0.4y[n-1] + 0.2y[n-2] = x[n] + 0.1x[n-1] - 0.06x[n-2]$. $[2+2+6]$

5. Determine the Direct Form II realization of the following system $y(n) = -0.1y(n-1) + 0.72y(n-2) + 0.7x(n) - 0.252x(n-2)$. $[4]$

6. Compute the lattice coefficients and draw the lattice structure of following FIR system $H(z) = 1 + 2z^{-1} - 3z^{-2} + 4z^{-3}$. $[6]$

7. Design a digital FIR filter for the design of the low pass filter having $\omega_p = 0.3\pi$, $\omega_s = 0.5\pi$, $\alpha_s = 40\text{ dB}$ using suitable window function. $[8]$

8. What is optimum filter? Describe Remez exchange algorithm for FIR filter design with flow chart. $[1+6]$

9. What is the advantage of bilinear transformation? Design a low pass discrete time Butterworth filter applying bilinear transformation having specifications as follows: $[2+9+4]$
   * Pass band frequency ($\omega_p$) = $0.25\pi\text{ radians}$
   * Stop band frequency ($\omega_s$) = $0.55\pi\text{ radians}$
   * Pass band ripple ($\delta_p$) = $0.11$
   * And stop band ripple ($\delta_s$) = $0.21$
   * Consider sampling frequency $0.5\text{ Hz}$

   Also, convert the obtained digital low-pass filter to high-pass filter with new pass band frequency ($w'_p$) = $0.45\pi$ using digital domain transformation.

10. Why do we need FFT? Find 8-point DFT of sequence $x[n] = \{1, 1, 2, 2, 1, 1, 2, 1\}$ using Decimation in frequency FFT (DIFFT) algorithm. $[2+7]$

11. Find $x_3[n]$ if DFT of $x_3[n]$ is given by $X_3(k) = X_1(k) X_2(k)$ where $X_1(k)$ and $X_2(k)$ are 4-point DFT of $x_1[n] = \{1, 2, -2\}$ and $x_2[n] = \{1, 2, 3, -1\}$ respectively. $[6]$