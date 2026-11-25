Exam: 2079 Bhadra

TRIBHUVAN UNIVERSITY
INSTITUTE OF ENGINEERING
Examination Control Division
2079 Bhadra

| Exam. | Regular |
|---|---|
| Level | BE | Full Marks | 80 |
| Programme | BEI, BCT | Pass Marks | 32 |
| Year / Part | IV / I | Time | 3 hrs. |

**Subject: - Digital Signal Analysis And Processing (CT 704)**

1. Define energy and power signal. Determine whether the signal $x[n] = \cos\left[\frac{2\pi n}{5}\right] + \sin\left[\frac{\pi n}{3}\right]$ is periodic or non-periodic and if it is periodic, find its fundamental period. $[2+2]$

2. Find the output of LTI system having input signal $x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3]$ and $h[n] = 2\delta[n+1] + 2\delta[n-1]$. $[5]$

3. Find inverses Z-transform of $X(z) = \frac{(2z^4 + 2z^3 - 3z + 2)}{(z^2 - 1.5z - 1)}$, $\text{ROC}: |z| < 0.5$, using partial fraction expansion method. $[6]$

4. Plot the pole-zero in z-plane and draw the magnitude response (not to the scale) of the equation of the system describe by difference equation:
$y[n] - 0.35y[n-1] + 0.25y[n-2] = x[n] - 0.75x[n-1]$. $[3+7]$

5. Draw direct form I and Direct form II realization of the following system.
$y[n] - 0.25y[n-2] + x[n] + 0.4x[n-1] + 0.5x[n-2]$ $[2+2]$

6. Given a 3-stage lattice filter for all zero polynomial with coefficients $K_1 = 1/4$, $K_2 = 1/2$ and $K_3 = 1/3$. Obtain the system function and FIR filter coefficients of this filter. $[6]$

7. Define Gibb's phenomenon. Design the FIR filter using Kaiser window technique for the specifications:
$$0.899 \le |H(e^{jw})| \le 1 \quad \text{for } |w| \le 0.2\pi$$
$$|H(e^{jw})| \le 0.01 \quad \text{for } 0.4\pi \le w \le \pi$$
$[2+8]$

8. Discuss the Remez exchange algorithm for FIR filter design. $[5]$

9. Design a low pass discrete time Butterworth filter using bilinear transformation having following specifications: $[11+4]$
Passband frequency ($W_p$) = $0.25\pi$ radians
Stopband frequency ($W_s$) = $0.55\pi$ radians
Passband ripple ($\delta_p$) = $0.11$
Stopband ripple ($\delta_s$) = $0.21$. Consider sampling frequency of $0.5$ Hz.

Also, covert the obtained digital low pass filter to high pass filter with new pass band frequency, $W'_p = 0.45\pi$ using digital domain transformation.

10. Why we need FFT? Find the 8-point DFT of the following sequence using radix-2 DITFFT algorithm. $[2+6]$

11. If $X_1(k)$ and $X_2(k)$ are DFT of sequence $x_1[n] = \{1, 0, 0, 1\}$ and $x_2[n] = \{2, 0, 2\}$ respectively then find the sequence $X_3[n]$; if DFT of $x_3[n]$ is given by $X_3(k) = X_1(k) \cdot X_2(k)$. $[7]$