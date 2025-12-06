#!/usr/bin/env python3
# compute_drt.py
# Computes DRT via Tikhonov + L-curve selection and reconstructs Z, saves outputs.

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy.signal import find_peaks
import csv, math, os

# ------------------ USER DATA ENTRY ------------------
# Paste your Re,Im data here (exactly as provided).
data_str = """
2929.1162109375,2603.81958007812
232.252655029297,3189.68310546875
357.157745361328,2454.66479492188
-342.455902099609,2763.5439453125
-5534.751953125,7651.46923828125
7527.26171875,6543.2568359375
5525.3759765625,3055.6943359375
3197.48974609375,3209.40380859375
2073.33081054688,4139.38623046875
1466.94372558594,5645.974609375
2027.89099121094,6674.14794921875
2061.05346679688,8297.0478515625
3274.62744140625,9313.7275390625
3313.66772460938,10406.0517578125
4325.34375,12075.04296875
4818.4345703125,13960.0400390625
6453.4970703125,15494.642578125
7272.61767578125,17415.029296875
9309.158203125,19075.400390625
10881.0419921875,21070.41015625
13003.7880859375,23190.244140625
15467.087890625,25584.548828125
19124.01171875,26785.1328125
20937.626953125,29889.61328125
25223.611328125,30499.669921875
28574.923828125,32696.537109375
33613.96875,33739.7890625
36503.03125,35348.203125
41482.05859375,42859.81640625
48109.578125,43333.98828125
53622.3828125,42673.5
57333.34375,43950.30859375
63814.7109375,44610.4609375
89024.046875,48878.09375
81478.9453125,38890.44140625
83607.1328125,37862.546875
87640.53125,33193.76953125
90570.71875,31034.794921875
93269.234375,27560.802734375
95409.6796875,25657.9921875
97911.4921875,22706.94921875
99092.1875,19578.171875
100860.1953125,16866.533203125
101488.953125,15039.169921875
103264.203125,14752.8251953125
101677.84375,10978.0771484375
101467.7734375,10529.1611328125
101315.8125,9693.1083984375
101615.59375,10040.6953125
102271.546875,9903.197265625
102067.8125,10186.83203125
102344.515625,10579.466796875
102682.59375,11660.3896484375
104005.109375,12343.583984375
105096.2734375,13278.9375
105982.7734375,14060.298828125
106851.34375,15187.6845703125
109195.890625,15657.1103515625
111368.328125,16976.58984375
112969.421875,18074.009765625
115326.421875,18529.28515625
116987.765625,18670.3125
118515.5625,19128.24609375
121268.140625,19456.923828125
123202.7578125,19231.158203125
124705.4375,18889.109375
126729.0078125,19646.6171875
128551.2890625,18748.240234375
130089.0390625,18578.12890625
132217.3125,19028.25390625
133574.578125,19340.9140625
134722.828125,18978.330078125
135871.890625,20013.888671875
137792.265625,21462.001953125
139518.375,22026.046875
141156.8125,23684.646484375
138595.015625,23366.177734375
142516.34375,27916.3203125
144925.21875,29212.671875
147394.1875,31162.107421875
146813.875,32543.962890625
152242.65625,36593.4609375
153466.90625,39297.80078125
156997.578125,44207.6875
159277.65625,49210.90625
162617.046875,52651.046875
165994.65625,58277.62890625
170206.921875,65877.0859375
174569.03125,70801.8515625
180370.28125,77377.453125
185134.953125,85279.4453125
191035.84375,92931.390625
198408.9375,102519.0625
205963.8125,112130.3671875
214233.890625,122395.34375
223555.5625,134257.09375
233472.546875,146403.9375
244651.203125,160083.015625
256952.59375,174057.515625
270527.0625,189631.984375
285200.25,206215.828125
300702.6875,224098.234375
318443.71875,243455.9375
335826.53125,264461.46875
"""
# Paste your frequency list here (Hz), one per line (use . as decimal sep)
freq_str = """
7000018,5
6006764
5154459
4423090,5
3795501,75
3256959
2794824,5
2398261,25
2057972,125
1765968,25
1515393
1300373
1115860,625
957532,3125
821667,1875
705082,75
605032,6875
519187,9375
445516,625
382302,1875
328060,0625
281509,78125
241565,84375
207291,04688
177878,1875
152640,65625
130984,63281
112399,79688
96450,04688
82764,25
71017,66406
60941,21094
52293,64453
44870,84766
38505,79297
33040,75391
28355,10742
24328,24023
20876,63086
17916,79102
15374,48145
13194,03223
11319,77148
9714,5957
8340,37402
7151,01514
6138,81641
5268,17871
4521,44434
3878,75732
3328,93433
2855,91187
2450,78662
2102,97852
1804,41882
1548,51379
1328,72168
1140,36353
978,43262
839,7326
720,69464
618,21936
530,50964
455,43686
390,625
335,32156
287,69821
246,81688
211,83044
181,80385
155,9481
133,84372
114,88944
98,58012
84,59389
72,56195
62,29237
53,44368
45,86592
39,35769
33,77855
28,97099
24,86475
21,33109
18,3177
15,7088
13,48533
11,56554
9,92693
8,51966
7,3082
6,2751
5,38051
4,61732
3,96574
3,40044
2,91947
2,50521
2,14865
1,84475
1,5818
1,35811
1,16517
1,00006
"""
# If your Im column is given as -Im(Z) in your file, set this to True to invert sign:
IM_IS_NEGATIVE = False

# Output filenames
OUT_GAMMA_CSV = 'drt_gamma_tau.csv'
OUT_RECON_CSV = 'drt_reconstructed.csv'
OUT_GAMMA_PNG = 'drt_gamma_tau.png'
OUT_NYQUIST_PNG = 'drt_nyquist_fit.png'
# ----------------------------------------------------

# parse data
lines = [ln.strip() for ln in data_str.strip().splitlines() if ln.strip()]
data = np.array([list(map(float, ln.split(','))) for ln in lines])
Re = data[:,0]
Im = data[:,1]
if IM_IS_NEGATIVE:
    Im = -Im
Z = Re + 1j*Im

# parse freqs (allow comma decimal separators by converting to dots)
freq_lines = [ln.strip().replace(',', '.') for ln in freq_str.strip().splitlines() if ln.strip()]
freqs = np.array([float(f) for f in freq_lines])

if freqs.size != Z.size:
    raise ValueError(f"Frequency length ({freqs.size}) != data length ({Z.size}). Fix your inputs.")

# typical ordering: sort by descending freq (HF->LF)
order = np.argsort(-freqs)
freqs = freqs[order]
Z = Z[order]
Re = Re[order]
Im = Im[order]
omega = 2.0*np.pi*freqs

# build tau grid: from ~1/(2π f_max) * 1e-3 to 1/(2π f_min) * 1e3 (extend range a bit)
tau_min = 1.0/(2*np.pi*freqs.max()) * 1e-3
tau_max = 1.0/(2*np.pi*freqs.min()) * 1e3
Ntau = 250
taus = np.logspace(np.log10(tau_min), np.log10(tau_max), Ntau)
dln = np.log(taus[1]/taus[0])

# build kernel matrices
K_re = np.zeros((len(omega), Ntau)) 
K_im = np.zeros((len(omega), Ntau))
for i, w in enumerate(omega):
    x = w*taus
    K_re[i,:] = 1.0/(1.0 + x**2) * dln
    K_im[i,:] = - (x/(1.0 + x**2)) * dln

# estimate R_inf (HF real intercept) as minimum Re at top 2-5 points
Rinf = np.min(Re[:5])
y_re = Re - Rinf
y_im = Im
K_stack = np.vstack([K_re, K_im])
y_stack = np.concatenate([y_re, y_im])

# Tikhonov regularizer: second derivative (discrete)
L = np.zeros((Ntau-2, Ntau))
for i in range(1, Ntau-1):
    L[i-1, i-1] = 1.0
    L[i-1, i]   = -2.0
    L[i-1, i+1] = 1.0

# function to solve for gamma for given lambda (Tikhonov)
def solve_tikhonov(lambda_reg):
    A = K_stack.T.dot(K_stack) + lambda_reg * (L.T.dot(L))
    b = K_stack.T.dot(y_stack)
    # solve
    gamma = linalg.solve(A, b, assume_a='pos')
    # clip negative values to zero
    gamma[gamma < 0] = 0.0
    return gamma

# scan lambda values and choose via L-curve curvature
lambdas = np.logspace(-8, 3, 60)
resid_norm = []
reg_norm = []
solutions = []
for lam in lambdas:
    sol = solve_tikhonov(lam)
    solutions.append(sol)
    r = K_stack.dot(sol) - y_stack
    resid_norm.append(np.linalg.norm(r))
    reg_norm.append(np.linalg.norm(L.dot(sol)))
resid_norm = np.array(resid_norm)
reg_norm = np.array(reg_norm)

# compute curvature of L-curve (log-log)
log_r = np.log(resid_norm + 1e-20)
log_s = np.log(reg_norm + 1e-20)
t = np.log(lambdas)
from numpy import gradient
dx = gradient(log_r, t)
dy = gradient(log_s, t)
ddx = gradient(dx, t)
ddy = gradient(dy, t)
curv = np.abs(ddx * dy - dx * ddy) / (dx*dx + dy*dy)**1.5
best_idx = np.nanargmax(curv)
best_lambda = lambdas[best_idx]
gamma = solutions[best_idx]

# reconstruct Z from gamma
Z_recon = np.zeros(len(omega), dtype=complex)
for i,w in enumerate(omega):
    Z_recon[i] = Rinf + np.sum(gamma * (1.0/(1.0 + (w*taus)**2)) * dln) + 1j * np.sum(gamma * ( - (w*taus)/(1.0 + (w*taus)**2) ) * dln)

# save gamma
with open(OUT_GAMMA_CSV, 'w', newline='') as f:
    wcsv = csv.writer(f)
    wcsv.writerow(['tau_s', 'gamma'])
    for t0, g in zip(taus, gamma):
        wcsv.writerow([t0, g])
print("Saved", OUT_GAMMA_CSV)

# save reconstructed Z
with open(OUT_RECON_CSV, 'w', newline='') as f:
    wcsv = csv.writer(f)
    wcsv.writerow(['freq_Hz', 'Re_data', 'Im_data', 'Re_fit', 'Im_fit'])
    for ff, zd, zf in zip(freqs, Z, Z_recon):
        wcsv.writerow([ff, zd.real, zd.imag, zf.real, zf.imag])
print("Saved", OUT_RECON_CSV)

# plot gamma
plt.figure(figsize=(6,4))
plt.loglog(taus, gamma, '-k')
plt.xlabel('tau (s)')
plt.ylabel('gamma(τ) (Ω per ln τ)')
plt.title(f'DRT γ(τ)  (best λ = {best_lambda:.2e})')
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig(OUT_GAMMA_PNG, dpi=300)
plt.show()
print("Saved", OUT_GAMMA_PNG)

# plot Nyquist data and reconstruction
plt.figure(figsize=(6,6))
plt.plot(Re, Im, 'o', label='data', markersize=4)
plt.plot(Z_recon.real, -Z_recon.imag, '-', label='DRT reconstruction')
plt.xlabel('Re(Z) / Ω')
plt.ylabel('Im(Z) / Ω')
plt.legend()
plt.grid(True)
plt.title('Nyquist: data vs DRT reconstruction')
plt.savefig(OUT_NYQUIST_PNG, dpi=300)
plt.show()
print("Saved", OUT_NYQUIST_PNG)

# find peaks (height threshold relative)
peaks, props = find_peaks(gamma, height=np.max(gamma)*0.02, distance=3)
peak_summary = []
for p in peaks:
    # integrate area (R contribution) with a small window around peak; better to integrate until valley boundaries
    # we use ±5 points as a first approximation
    left = max(0, p-5)
    right = min(Ntau-1, p+5)
    area = np.sum(gamma[left:right+1]) * dln
    peak_summary.append((p, taus[p], gamma[p], area))
print("Detected peaks (index, tau_s, gamma_height, area ~ R (Ω) ):")
for s in peak_summary:
    print(s)


