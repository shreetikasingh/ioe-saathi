Exam: 2081 Baishakh

**TRIBHUVAN UNIVERSITY**  
**INSTITUTE OF ENGINEERING**  
**Examination Control Division**  
**2081 Baishakh**

| Exam. | Back | Full Marks | 80 |
| :--- | :--- | :--- | :--- |
| Level | BE | Pass Marks | 32 |
| Programme | BEI, BCT | Time | 3 hrs. |
| Year / Part | IV / I | | |

**Subject: - Digital Signal Analysis and Processing (CT 704)**

---

1. A discrete-time LTI system is given by difference equation $y(n) = x(n) + e^a y(n-1)$. Check this system for BIBO stability. $[5]$

2. Find the output $y(n)$ of LTI system having impulse response $h(n) = \left(\frac{1}{3}\right)^n u(n-3)$ and input $x(n) = \left(\frac{1}{6}\right)^{n-6} u(n)$. $[6]$

3. Determine the inverse z-transform of $X(z) = \frac{1}{1 - 0.8z^{-1} + 0.12z^{-2}}$. 
   (i) if $\text{ROC is } |z| > 0.6$ 
   (ii) if $\text{ROC is } |z| < 0.2$ 
   (iii) if $\text{ROC is } 0.2 < |z| < 0.6$ $[2+2+3]$

4. Plot the pole-zero in $z$ plane and draw the magnitude response (not to the scale) of the system described by difference equation $y(n) = 0.67 x(n) - 0.3 x(n-1) + 2.75 y(n-1)$ $[3+7]$

5. a) Draw the cascaded form structure of $H(z) = \frac{10(1 - 0.25z^{-1})(1 - 0.667z^{-1})(1 + 2z^{-1})}{(1 - 0.75z^{-1})(1 - 0.125z^{-1}) \{1 - (0.5+j0.5)z^{-1}\} \{1 - (0.5-j0.5)z^{-1}\}}$ $[5]$

   b) Draw the lattice structure for the given FIR filter and also check whether the system is stable. $H(z) = 1 + (13/24) z^{-1} + (5/8) z^{-2} + (1/3) z^{-3}$ $[5]$

6. Design a linear phase FIR filter using suitable window to meet following specifications:
   $$\begin{aligned}
   0.99 \le |H(e^{j\omega})| \le 1.01, &\quad \text{for } 0 \le |\omega| \le 0.3\pi \\
   |H(e^{j\omega})| \le 0.01, &\quad \text{for } 0.35\pi \le |\omega| \le \pi
   \end{aligned}$$ $[10]$

7. What is Gibbs phenomenon and how can it be minimized? Why Kaiser window is better than other fixed windows in FIR filter design? $[3+3]$

8. Differentiate between bilinear transformation and impulse invariance. Design a Butterworth digital IIR lowpass filter using bilinear transformation by taking $T = 0.1$ second, to satisfy the following specifications. $[2+10]$
   $$\begin{aligned}
   0.6 \le |H(e^{j\omega})| \le 1, &\quad 0 \le \omega \le 0.35\pi \\
   |H(e^{j\omega})| \le 0.1, &\quad 0.7\pi \le \omega \le \pi
   \end{aligned}$$

9. Why Decimation in Time Fast Fourier Transform (DITFFT) Algorithm is better than direct computation of DFT? Find 4 point DFT of the sequence $x(n) = \{2, 2, 4\}$ using DITFFT algorithm. $[2+6]$

10. Compute circular convolution of the following two sequences using DFT. $x(n) = \{1, 2, 4, 5\}$ and $h(n) = \{2, 1, 6, 8\}$ $[6]$

***