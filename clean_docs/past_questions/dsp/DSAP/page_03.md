Exam: 2082 Baishakh

**TRIBHUVAN UNIVERSITY**  
**INSTITUTE OF ENGINEERING**  
**Examination Control Division**  
**2082 Baishakh**

| Exam. | Back |
| :--- | :--- |
| Level | BE |
| Programme | BCT, BEI |
| Year / Part | IV / I |

**Full Marks:** 80  
**Pass Marks:** 32  
**Time:** 3 hrs.

**Subject: - Digital Signal Analysis and Processing (CT 704)**

---

1. A discrete time system has input $x[n]$ and output $y[n]$ and its input - output relation is  
   $$y[n] = x[n] + x[-n]$$  
   Is the system causal, time invariant or not? $[2+2]$

2. Find the output of an LTI system having impulse response $h[n] = \left(\frac{1}{2}\right)^n u[n]$ excited by an input $x[n] = 5e^{j\frac{\pi n}{3}}$. $[5]$

3. Define ROC of a Z-transform. Determine $x[n]$ for $X(z) = \frac{1}{1 - 1.5z^{-1} + 0.5z^{-2}}$ if: $[1+5]$  
   a) $|z| > 1$  
   b) $|z| < 0.5$  
   c) $0.5 < |z| < 1$ using partial fraction method.

4. The poles of a system are located at $0.45 \pm j1.6$ and the zeros at $0.58 \pm j2.06$. Map the poles and zeros in the z-plane and plot the magnitude and phase response (not to scale) of the system. $[3+7]$

5. A third order low pass filter has a system function  
   $$H(z) = \frac{0.2759 + 0.5121z^{-1} + 0.5121z^{-2} + 0.2759z^{-3}}{1 - 0.0010z^{-1} + 0.6546z^{-2} - 0.0775z^{-3}}.$$  
   Implement the filter using lattice-ladder structure. $[10]$

6. Differentiate between analog and digital filter. Design an FIR lowpass digital filter that will have a $-3\text{ dB}$ cut-off at $30\pi\text{ rad/s}$ and an attenuation of $50\text{ dB}$ at $45\pi\text{ rad/s}$. The filter is required to have a linear phase and the system uses a sampling rate of $100\text{ Hz}$. $[2+6]$

7. Explain Gibbs phenomenon in FIR filter design. Describe Remez exchange algorithm for FIR filter design along with flowchart. $[2+5]$

8. Using bilinear transformation technique, design a Butterworth filter which satisfies the following conditions: $[12+3]$  
   $$
   \begin{aligned}
   0.8 \le |H(e^{j\omega})| \le 1 & \quad 0 \le \omega \le 0.2\pi \\
   |H(e^{j\omega})| \le 0.2 & \quad 0.6\pi \le \omega \le \pi
   \end{aligned}
   $$  
   Consider sampling frequency $1\text{ Hz}$.  
   Compare Impulse Invariance Method and Bilinear Transformation technique for analog filter to digital filter conversion.

9. What is Fast Fourier Transform algorithm? How Decimation in Frequency Fast Fourier Transform algorithm reduces the calculation complexity of DFT? Find $4$ point DFT of the sequence $x[n] = \{1, 4, -1\}$ using Decimation in Frequency Fast Fourier Transform algorithm. $[1+2+6]$

10. Find the circular convolution of the sequences $x_1[n] = \{1, 1, -1, -1, 2\}$ and $x_2[n] = \{1, -1, -2\}$. $[6]$

***