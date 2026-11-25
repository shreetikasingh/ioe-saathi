Exam: 2066 Magh

1. Plot the sequence $x(n) = u(n) - u(n-5) + 5\delta(n-6) + nu(n-7) - nu(n-9)$ where $u(n)$ is the unit step sequence and $\delta(n)$ is unit sample sequence. [2]

2. Write whether or not the following sequences are periodic and write the period. [4]

   a) $x(h) = \cos\left(\frac{3\pi}{8}n + \frac{\pi}{4}\right)$

   b) $x(n) = \sin(0.8n)$

3. Find the expression for discrete Fourier series of the sequence [4]
   $$x(n) = \sum_{m=-\infty}^{\infty} \delta(n-4m).$$

4. Show whether or not the following systems are (a) linear; (b) time invariant, (c) causal, (d) memoryless, (e) BIBO stable. [10]

   a) $y(n) = 2^{\log_2(x(n))} + 2^{\log_2(x(n))}$

   b) $y(n) = \sin\{x(n) - x(n-1)\}$

5. Perform circular convolution of the sequences $x_1(n) = [1, 2]$, $0 \leq n \leq 1$ and $x_2(n) = [1, 2, 4, 5]$, $0 \leq n \leq 3$. [4]

6. Show the computation of DFT of sequence $x(n) = [1, 3, 4, 5]$ using decimation in time FFT algorithm and find the values of $X(k)$. [6]

7. Let a system be characterized by difference equation. [10]
   $y(n) - 0.5y(n-1) - 0.25y(n-2) - x(n) = 0$, where input $x(n) = 0.2^n u(n)$, initial conditions $y(-1) = 2$, $y(-2) = 4$.

   Find (a) zero input response of the system, (b) zero state response of the system, (c) total response of the system, (d) system function $H(z)$ (e) poles of $H(z)$.

8. Find the lattice-ladder filter structure for the LTI system with system function. [6]
   $$H(z) = \frac{\frac{1}{2} + \frac{1}{3}z^{-1} + \frac{1}{4}z^{-2} + \frac{1}{5}z^{-3}}{1 + \frac{1}{5}z^{-1} + \frac{2}{5}z^{-2} + \frac{3}{5}z^{-3}}$$