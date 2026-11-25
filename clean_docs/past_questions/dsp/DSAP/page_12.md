Exam: 2076 Chaitra

TRIBHUVAN UNIVERSITY
INSTITUTE OF ENGINEERING
Examination Control Division
2076 Chaitra

| Exam. | Regular |
| :--- | :--- |
| Level | BE |
| Programme | BCT |
| Year / Part | IV / I |

| Full Marks | 80 |
| :--- | :--- |
| Pass Marks | 32 |
| Time | 3 hrs. |

**Subject: - Digital Signal Analysis and Processing (CT 704)**

1. Define even and odd type discrete time signals with suitable example. Plot the signal $x[-2n+3]$ where $x[n] = \{1, 2, 0, -1, -3, -4\}$. $[2+3]$

2. Determine whether the following system are: $[5]$
   a) $y[n] = x[-n]$ is time-invariant or not.
   b) $y[n] = x[n^2]$ is linear or not.

3. Find the output of LTI system having input signal $x[n] = u[n+1] - u[n-4]$ and impulse response $h[n] = (1/2)^n u[n-1]$. $[6]$

4. Define ROC of z-transform. Find inverse z-transform using partial fraction expansion of $X(z) = \frac{z^4 + 5z^3 - 3z + 4}{z^2 - 1.5z - 1}$, ROC: $|z| < 0.5$. $[2+6]$

5. Draw the pole-zero in the z-plane for a system with poles at $0.45 \pm j1.06$ and zeroes at $0.58 \pm j2.06$. Also plot the magnitude response (not to the scale) of the system. $[2+6]$

6. Compute Lattice and Ladder coefficients and Draw lattice-ladder structure for given IIR system $H(z) = \frac{0.5 - 2z^{-1} + 3z^{-2}}{1 - 0.5z^{-1} - 0.7z^{-2} + 0.3z^{-3}}$. $[6+4]$

7. Realize the given system in Cascade form of $2^{\text{nd}}$ order section in signal flow graph representation. $[4]$
   $H(z) = \frac{\{(1 - 0.5z^{-1})(1 + 0.35z^{-1})(1 - 0.3e^{j2n\pi/5}z^{-1})(1 - 0.3e^{-j2n\pi/5}z^{-1})\}}{\{(1 - 0.6e^{j n\pi/3}z^{-1})(1 - 0.6e^{-j n\pi/3}z^{-1})(1 + 0.5e^{j2n\pi/7}z^{-1})(1 + 0.5e^{-j2n\pi/7}z^{-1})\}}$

8. Design the FIR filter using suitable window for the specifications: $[6]$
   $0.899 \le |H(e^{j\omega})| \le 1$, for $|\omega| \le 0.2\pi$
   $|H(e^{j\omega})| \le 0.01$, for $0.4\pi \le \omega \le \pi$

9. What is optimum filter? Show mathematical expression of Remez exchange algorithm for FIR filter design. $[1+5]$

10. Design a digital low pass Butterworth filter by applying bilinear transformation techniques for the given specifications: $[10]$
    Passband peak to peak ripple $\le 1\text{ dB}$
    Passband edge frequency $= 1.2\text{ KHz}$
    Stopband Attenuation $\ge 40\text{ dB}$
    Stopband edge frequency $= 2.5\text{ KHz}$
    Sample rate $= 8\text{ KHz}$

11. Find 8-point DFT of sequence $x[n] = \{1, 2, 3, 3, 5, 0, 4, 6\}$ using Decimation in frequency Fast Fourier Transform (DIFFFT) algorithm. $[7]$

12. Find $x_3[n]$ if DFT of $x_3[n]$ is given by $X_3(k) = X_1(k) * X_2(k)$ where $X_1(k)$ and $X_2(k)$ are 4-point DFT of $x_1[n]=\{1, 2, -2\}$ and $x_2[n]=\{1, 2, 3, -1\}$ respectively. $[5]$

***