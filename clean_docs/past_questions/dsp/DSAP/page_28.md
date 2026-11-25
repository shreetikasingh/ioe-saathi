Exam: 2067 Mangsir

1. Compute and plot even and odd component of the sequence $x(n) = 2u[n] - 2u[n-4]$ where $u[n]$ is unit step sequence. [2]

2. Write whether or not the following sequences are periodic and write the period. [4]
   
   a) $x[n] = \cos\left(\frac{5\pi}{3}n\right)$
   
   b) $x[n] = \sin\left(\frac{\pi n}{\sqrt{2}} + \frac{\pi}{8}\right)$

3. Find the discrete Fourier coefficients of the periodic sequence with period $N = 11$ defined over a period as $x[n] = \begin{cases} 1, & |n| \le 2 \\ 0, & 2 < |n| \le 5 \end{cases}$. [4]

4. Show whether or not the system $y(n) = nx[2(n-2)]$, $n > 0$ is (a) linear, (b) time invariant, (c) memoryless. [5]

5. Find the system function $H(z)$ of the system characterised by difference equation $y[n] - \frac{5}{6}y[n-1] - \frac{1}{6}y[n-2] - x[n] = 0$. Find the poles and zeros of the system. Use the pole-zero diagram to plot the approximate frequency response magnitude of the system. [10]

6. Realize the system function $H(z) = \frac{\left(1 - \frac{1}{3}z^{-1}\right)\left(1 - \frac{1}{4}z^{-1}\right)\left(1 - \frac{1}{8}z^{-1}\right)}{\left(1 - \frac{5}{6}z^{-1}\right)\left(1 - \frac{1}{6}z^{-1}\right)\left(1 - \frac{3}{4}e^{-j\frac{\pi}{4}}z^{-1}\right)\left(1 - \frac{3}{4}e^{j\frac{\pi}{4}}z^{-1}\right)}$ in terms of cascade of second order sections. Draw the block diagram of the cascade realization. [8]

7. Show by giving examples that the quantization error by truncation for sign magnitude number, $e_{tsm}$, lies in the range $-(2^{-b} - 2^{-bu}) \le e_{tsm} \le (2^{-b} - 2^{-bu})$ and that for the $2$'s complement number, $e_{t2c}$, lies in the range $-(2^{-b} - 2^{-bu}) \le e_{t2c} \le 0$. $b_u$ is the number of bits before quantization and $b$ is the number of bits after quantization. [6]

8. How does an IIR filter differ from an FIR filter? [4]