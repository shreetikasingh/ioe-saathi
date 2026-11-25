Exam: 2078 Bhadra

TRIBHUVAN UNIVERSITY
INSTITUTE OF ENGINEERING
Examination Control Division
2078 Bhadra

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

1. Determine whether the signal $x[n] = \cos\left[\frac{\pi n}{2}\right] \cdot \cos\left[\frac{\pi n}{4}\right]$ is periodic or non periodic and if it is periodic, find its fundamental period. $[4]$

2. Find the output of LTI system having impulse response $h[n] = u[n] - u[n-4]$ and input signal $x[n] = (1/2)^n u[n]$. $[5]$

3. Define ROC. Find inverse z-transform of $X(z) = \frac{(z^3 + z^2 + 1.5z + 0.5)}{(z^3 + 1.5z^2 + 0.5z)}$, $\text{ROC}: |z| < \frac{1}{2}$. $[1+5]$

4. Determine the zero-input response for a second order system given by: $[4]$
$$y[n] - 3y[n-1] - 4y[n-2] = x[n]$$

5. Plot the pole-zero in z-plane and draw magnitude response (not to the scale) of the system described by difference equation. $[2+4]$
$$y[n] - 0.4 \ y[n-1] +0.25 \ y[n-2] = x[n] - 0.4x[n-1]$$

6. The system function of a filter is $H(z) = 1 + \frac{13}{24}z^{-1} + \frac{5}{8}z^{-2} + \frac{1}{3}z^{-3}$. Draw the Direct Form and Lattice Structure implementation of the above filter. $[3+7]$

7. Design a linear phase FIR filter using KAISER window to meet the following specifications: $[8]$
$$\begin{cases}
|H(e^{jw})| \le 0.01; & 0 \le w \le 0.25\pi \\
0.95 \le |H(e^{jw})| \le 1.05; & 0.35\pi \le w \le 0.6\pi \\
|H(e^{jw})| \le 0.01; & 0.65\pi \le w \le \pi
\end{cases}$$

8. What is optimum filter? Show mathematical expression of Remez exchange algorithm for FIR filter design. $[1+6]$

9. Design a LPF Butterworth filter using Impulse Invariance Method (IIM) method with passband and stopband frequencies $200\text{Hz}$ and $500\text{Hz}$ respectively. The passband and stopband attenuations are $5\text{dB}$ and $12\text{dB}$ respectively. The sampling frequency is $5000\text{Hz}$. What is pre-warping and why it is necessary? Explain. $[12+3]$

10. Differentiate between DFT and DTFT. Find the circular convolution of $x_1[n] = \{2, 1, 2, 1\}$ and $x_2[n] = \{1, 2, 3, 4\}$ $[2+6]$

11. Find the $8-\text{point}$ DFT of $x[n] = u[n] - u[n-4]$ using FFT DIT algorithm. $[7]$