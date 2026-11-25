Exam: 2075 Ashwin

31 TRIBHUVAN UNIVERSITY
INSTITUTE OF ENGINEERING
Examination Control Division
2075 Ashwin

| Exam. | Back |
| :--- | :--- |
| Level | BE | Full Marks | 80 |
| Programme | BCT | Pass Marks | 32 |
| Year / Part | IV / I | Time | 3 hrs. |

**Subject: - Digital Signal Analysis and Processing (CT704)**

1. Determine whether the following sequences are linear or not: $[3+3]$
   a) $y[n] = x^2[n]$
   b) $y[n] = \cos\left(\frac{5\pi}{8}n + \frac{\pi}{4}\right)$

2. Find the output of LTI system having impulse response $h[n] = 2^n * \{u[n] - u[n-3]\}$ and input signal $x[n] = \delta[n] + \delta[n-1] + \delta[n-2]$. $[5]$

3. List out the properties of Region of convergence and locate the ROC of the following signal. $[3+6]$
   $x[n] = (0.6)^n u[n] + (0.25)^n u[n]$

4. Draw the poles and zeros in the z-plane for a system with poles at $0.45 \pm j1.06$ and zeros at $0.58 \pm j2.06$. Also plot the magnitude response of the system. $[2+8]$

5. Draw the Lattice structure from the following system function: $[7+3]$
   $$\frac{1}{3 + \frac{39}{24}Z^{-1} + \frac{15}{8}Z^{-2} + \frac{3}{9}Z^{-3}}$$
   And represent $\frac{5}{8}$ and $-\frac{5}{8}$ in sign magnitude, 1's complement and 2's complement format.

6. Design a digital low-pass filter with the following specification: $[12]$
   i) Pass-band magnitude constant to $0.7\text{ dB}$ below the frequency of $0.15\ \pi$
   ii) Stop-band attenuation at least $14\text{ dB}$ for the frequencies between $0.6\pi$ to $\pi$
   
   Use Butterworth approximation as a prototype and use bilinear transformation method to obtain the digital filter.

7. Design a linear phase FIR filter using Kaiser Window to meet the following specifications: $[8+4]$
   $$\begin{aligned}
   0.99 \le |H(e^{jw})| \le 1.01, &\quad \text{for } 0 \le w \le 0.19\pi \\
   |H(e^{jw})| \le 0.01, &\quad \text{for } 0.21\pi \le w \le \pi
   \end{aligned}$$
   Draw the flow chart for Optimum filter design.

8. How fast is FFT compare to DFT? Draw the butterfly diagram of 8-point DFT of a sequence as $x[n] = n+1$ using Decimation in Time FFT algorithm. $[3+7]$

9. State the circular convolution property of DFT. Find the circular convolution of: $[1+5]$