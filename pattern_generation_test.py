#stock cutting problem, "pivot" method

#idea is to use the smallest target value as a "pivot" since that number will be the least "flexible"
#use factors of target numbers (may not be the most optimal but is easy to program and the logic is "direct")
#if target is prime or factors exceed possible cuts, subtract 1 until it is not

import numpy as np

#modified factor function, returns list of factors less than or equal to y
def factor_mod(x, y):
    f = [n for n in range(1, x + 1) if x % n == 0]
    f[:] = [i for i in f if i <=y]
    return f

#stock length
L = 59

#cut lengths
l_1 = 5
l_2 = 7
l_3 = 9

l = [l_1, l_2, l_3]
l_len = len(l)

#target
t_1 = 103
t_2 = 33
t_3 = 10

t = [t_1, t_2, t_3]
#####################################################
#minimum target
t_mint = min(t)
ind_mint = t.index(t_mint)
l_mint = l[ind_mint]

a_min = L//l_mint #maximum of solely l_min that can be cut

#extra cuts for cases where we don't have enough factors
t_ex = 0

while len(factor_mod(t_mint, a_min)) < 2:
    t_mint -= 1
    t_ex += 1

def pattern(n, l):
    p = []
    l_red = [i for i in l if i != l_mint]
    for i in n:
        L_red = L - i*l_mint
        l_min = min(l_red)  # smallest cut value
        ind_min = l_red.index(l_min)
        ind = 0
        for j in l_red:
            n_i = L_red // j
            r_i = L_red % j
            pat = np.zeros(l_len)
            pat[ind_mint] = i
            if j != l_min:
                if r_i > l_min:
                    n_min = r_i // l_min
                else:
                    n_min = 0
                pat[ind_min] = n_min
            pat[ind] = n_i
            p.append(pat)
            ind += 1
    return(p)
