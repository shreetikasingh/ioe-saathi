Exam: 2083 Bhadra

Subject: - Digital Signal Analysis and Processing (CT 704)

1. Define Energy and Power signal with examples. Determine whether the signal $x[n] = \cos\left[\frac{2\pi n}{5}\right] + \sin\left[\frac{\pi n}{3}\right]$ is periodic or non-periodic and if it is periodic, find its fundamental period. $[2+3]$

2. Find the output of a LTI system having input $x[n] = (\frac{1}{6})^n u[n]$ and impulse response $h[n] = (\frac{1}{3})^n u[n - 3]$. $[5]$

3. Determine the inverse z-transform of $X(z) = \frac{1}{1 - 4.5z^{-1} + 3.5^{-2}}$: $[3+3]$
   
   a) if ROC: $|z| > 3.5$ and (b) if ROC: $|z| < 1.0$

4. Differentiate between FIR system and IIR System. The poles of a system are located at $0.45 \pm j1.6$ and zeros at $0.58 \pm j2.06$. Map the poles and zeros in the z-plane and plot the magnitude response (not to the scale) of the system. $[2+2+6]$

5. The IIR filter is described by $y(n) - \frac{2}{5}y(n - 1) + \frac{1}{5}y(n - 2) = x(n) + \frac{1}{4}x(n - 1)$. Realize it using lattice structure and cascade structure. $[6+4]$

6. Design a Low Pass FIR filter using a suitable window to meet the following specifications. $[8]$
   Passband edge frequency $= 2\text{ kHz}$
   Stopband edge frequency $= 5\text{ kHz}$
   Stopband attenuation $= 42\text{ dB}$
   Sampling frequency $= 20\text{ kHz}$

7. Design a FIR filter using Kaiser window that meets the following specification: $[7]$
   $$\begin{array}{ll}
   0.9 < |H(e^{j\omega})| < 1.01 & \text{for } |\omega| < 0.3\pi \\
   |H(e^{j\omega})| < 0.01 & \text{for } 0.5\pi < |\omega| < \pi
   \end{array}$$

8. What are the demerits of Impulse Invariance method in comparison to Bilinear transformation? Design a digital low pass IIR filter using bilinear transformation to meet following specification. $[3+12]$
   
   a) Passband extends from $0$ to $0.25\pi$ with maximum attenuation of $0.5\text{ dB}$ in passband.
   
   b) Stopband extends from $0.55\pi$ with minimum attenuation of $15\text{ dB}$ in stopband.
   
   Use Butterworth approximation for design with sampling frequency of $1\text{Hz}$.

9. What is a Twiddle factor? Compute the length-4 sequence from its DFT which is given by $X(k) = 4, 1 - j, -2, 1 + j$. $[1+6]$

10. Find the 8-point DFT using DIF-FFT of the given sequence $x[n] = \{1, 2, 3, 4, 5\}$. $[7]$

***