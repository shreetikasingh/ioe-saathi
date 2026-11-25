Exam: 

9. For the first order filter, $y(n) = Q\{a \ y(n - 1)\} + x(n)$, the product term "$a \ y(n - 1)$" has been quantized by rounding to $3\text{ bits}$. $y(-1) = 0$, $x(n) = 0.875\delta(n)$, $a = -0.5$. Show whether the filter goes into limit cycle. What is the period of limit cycle? $[4]$

10. Design a digital low-pass Butterworth filter using Bilinear transformation. Filter specifications are as follows: Pass band frequency ($\omega_p) = 0.3\pi$, Stop band frequency ($\omega_s) = 0.4\pi$, Pass band ripple ($\delta_p) = 0.11$, Stop band ripple ($\delta_s) = 0.21$. $[15]$
    
    a) Find the order of filter ($N$)
    
    b) Find the cutoff frequency ($\omega_c$)
    
    c) Find the poles ($s_k$) of the squared magnitude response of analog Butterworth filter
    
    d) Find $H(s)$
    
    e) Find the digital Butterworth filter $H(z)$

11. Design a digital low-pass FIR filter with the following specifications using Kaiser Window. Pass band frequency ($\omega_p) = 0.25\pi$, stop band frequency ($\omega_s) = 0.65\pi$, Pass band ripple ($\delta_p) = 0.035$, Stop band ripple ($\delta_s) = 0.035$.
    
    a) Find the order of filter ($N$)
    
    b) Find the cutoff frequency ($\omega_c$)
    
    c) Find the value of shape parameter ($\beta$)
    
    d) Find Kaiser window ($w(n)$)
    
    e) Find the filter impulse response ($h(n)$)

    Some modified Bessel function values are as given below.

    | $x$ | $0$ | $1.3165$ | $1.7237$ | $1.8455$ | $1.9271$ | $1.93$ | $1.9903$ | $2$ |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | $J_0(x)$ | $1$ | $1.4826$ | $1.8926$ | $2.0508$ | $2.1675$ | $2.1718$ | $2.2642$ | $2.2796$ |

    ***