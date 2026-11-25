Exam: 2080 Bhadra

1. A discrete time system has input $x(n)$ and output $y(n)$. The input output relation of the system is given by
   $$y(n) = \sum_{k=0}^{n} x(k)$$
   Check whether the system is memory less, time invariant and stable or not? $[2+2+2]$

2. Determine whether the given signal is periodic or not. If the signal is periodic, determine the fundamental period $x[n] = e^{\frac{j\pi n}{16}} \cos\left\{\frac{n\pi}{17}\right\}$. $[5]$

3. Define the Region of Convergence (ROC) $[1+6]$
   Find the inverse of $H(z) = \frac{(1 + 2z^{-1} + z^{-2})}{(1 - 0.75z^{-1} + 0.125z^{-2})}$; ROC $0.25 < |z| < 0.5$

4. Plot the pole-zero on the z-plane and draw Magnitude response (not to the scale) of an LTI system described by the equation, $y(n) = x(n) + 0.8x(n - 1) + 0.8x(n - 2) + 0.49y(n - 2)$. $[3+7]$

5. Draw the Lattice structure from the following system function.
   $$H(z) = \frac{1}{1 - 0.2z^{-1} + 0.4z^{-2} + 0.6z^{-3}}$$ $[10]$

6. Design the symmetric FIR Low Pass Filter (LPF) for which the desired frequency response is expressed as
   $H_d(W) = e^{-jW\tau}, |W| \le W_c$ and $0$ elsewhere. The length of the filter should be $7$ and $W_c = 1 \text{ rad/sample}$. Make use of the Hanning window. $[10]$

7. Kaiser window is to be used to design a linear phase FIR filter that meets following specification $[2+2+2]$
   $|H(e^{j\omega})| \le 0.01, \quad 0.21\pi \le |\omega| \le \pi$
   $0.95 \le |H(e^{j\omega})| \le 1.05, \quad 0 \le |\omega| \le 0.19\pi$.
   Calculate the optimum value of ripple, attenuation and window length.

8. Using Bilinear transformation, design a Butterworth low pass filter which satisfies following conditions:
   $0.9 \le |H(e^{jw})| \le 1, \quad \text{for } 0 \le w \le \frac{\pi}{2}$
   $|H(e^{jw})| 0.2, \quad \text{for } \frac{3\pi}{4} \le w \le \pi$ $[12]$
   Consider sampling frequency of $1 \text{ Hz}$.

9. Compute 8-point DIF-FFT of sequence $x(n) = \{2, 1, 2, 1, 1, 2, 1, 2\}$. $[8]$

10. Obtain the circular convolution of the following sequences:
    $x_1(n) = \{1, 2, 3, 1\}$ and $x_2(n) = \{4, 3, 2, 2\}$ $[6]$