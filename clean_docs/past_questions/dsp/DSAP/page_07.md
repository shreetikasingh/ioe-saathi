Exam: 2080 Baishakh

TRIBHUVAN UNIVERSITY
INSTITUTE OF ENGINEERING
Examination Control Division
2080 Baishakh

| Exam. | Back |
| :--- | :--- |
| Level | BE |
| Programme | BEI, BCT |
| Year / Part | IV / I |

| Full Marks | 80 |
| :--- | :--- |
| Pass Marks | 32 |
| Time | 3 hrs. |

**Subject: - Digital Signal Analysis and Processing (CT 704)**

1. Check whether following signals are periodic or not. If yes, state their periodic time. $[2+2]$
   a) $x[n] = \sin(n\pi) + \cos(n\pi)$
   b) $x[n] = \sin(3n\pi/5) + \cos(4n\pi/7)$

2. Find the output of LTI system having impulse response $h[n] = (1/2)^n u[n]$ and input $x[n] = 5e^{j\pi n/3}$ for $-\infty < n < \infty$. $[5]$

3. Define ROC. Find inverse z-transform of $X(z) = \frac{(1+2z^{-1}+z^{-2})}{(1-1.5z^{-1}+0.5z^2)}$, ROC: $|z|>1$. $[1+5]$

4. Differentiate between FIR system and IIR System. The poles of a system are located at $0.45 \pm j1.6$ and zeros at $0.58 \pm j2.06$. Map the poles and zeros in the z-plane and plot the magnitude response (not in scale) of the system. $[4+6]$

5. Compute Lattice-ladder coefficients and draw lattice structure for given system
   $H(z) = \frac{(2 - 0.7z^{-1} + 0.5z^{-2})}{(1 - 0.3z^{-1} + 0.25z^{-2})}$. $[6]$

6. Realize the given system in Cascade Form of $2^\text{nd}$ order section flow graph representation.
   $H(z) = \frac{\{(1-0.4\text{ }z^{-1})\text{ }(1+0.2\text{ }z^{-1})\text{ }(1-0.3e^{j\pi/6}\text{ }z^{-1})\text{ }(1-0.3e^{-j\pi/6}\text{ }z^{-1})\}}{\{(1-0.5e^{j\pi/3}\text{ }z^{-1})\text{ }(1-0.5e^{-j\pi/3}\text{ }z^{-1})\text{ }(1+0.7e^{j\pi/4}\text{ }z^{-1})\text{ }(1+0.7e^{-j\pi/4}\text{ }z^{-1})\}}\text{}$. $[4]$

7. In which case do we choose FIR filter and IIR filter? Design a linear phase FIR filter using Kaiser Window to meet the following specifications: $[2+8]$
   $0.99 \le |H(e^{jw})| \le 1.01 \quad \text{for } 0 \le w \le 0.016\pi$
   $|H(e^{jw})| \le 0.01 \quad \text{for } 0.08\pi \le w \le 2\pi$

8. Explain in detail about how Gibb's oscillation arise while using the rectangular window in FIR filter design. $[5]$

9. Design a low pass digital IIR filter by Bilinear Transformation method to an approximate Butterworth low pass filter, if passband edge frequency is $0.26\pi\text{ radians}$ and maximum deviation of $0.99\text{ dB}$ below $0\text{ dB}$ gain in the passband. The maximum gain of $-14.99\text{ dB}$ and frequency is $0.58\pi\text{ radians}$ in stopband, Consider sampling frequency $0.5\text{ Hz}$. $[11]$

10. Describe digital domain Spectral Transformation features and parameters for low pass to high pass in IIR Filter design. $[4]$

11. How fast is FFT? Find 8-point DFT of sequence $x[n] = \{1, 1, 0, 0, 1, 1, 2\}$ using Decimation in Time Fast Fourier Transform(DITFFT) algorithm. $[2+6]$

12. Write the complexity of DFT and FFT? Obtain the circular convolution of the following sequences: $[2+5]$
    $X_1[n] = \{1, 2, 3, 1\}$ and
    $X_2[n] = \{4, 3, 2, 2\}$

***