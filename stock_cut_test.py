import numpy as np

#############################################################
#values here are manually calculated
#stock length
L = 15

#cut length
l_1 = 4
l_2 = 6
l_3 = 7

l = np.array([l_1,l_2,l_3])

#basis patterns
a_1 = L//l_1
a_2 = L//l_2
a_3 = L//l_3

#alternate cut patterns (currently hard coded)
a_4 = np.array([2,1,0])
a_5 = np.array([2,0,1])
a_6 = np.array([0,1,1])

new_patterns = [a_4,a_5,a_6]
#############################################################

#target (changeable)
t_1 = 190
t_2 = 300
t_3 = 500

t = np.array([t_1, t_2, t_3])

#initial matrix
b = np.diag([a_1, a_2, a_3])
b_inv = np.linalg.inv(b)
s = np.dot(b_inv,t) #initial solution
y = np.sum(b_inv, axis=0) #cost metric

#introduce "lowest cost" new pattern if "cost" < 0
for i in (new_patterns):
    c_new = 1-np.dot(y,i)
    if c_new < 0:
        c = c_new
        a_new = i #set pattern to be introduced
        new_patterns.remove(i)

        #calculate new matrix
        ba = np.dot(b_inv,a_new)
        p = np.divide(s,ba, out=np.zeros_like(s), where=ba!=0) #set division by 0 to = 0
        min = np.min(p[np.nonzero(p)])

        p = p.tolist()
        i = p.index(min)

        #new matrix
        b[:,i] = a_new
        b_inv = np.linalg.inv(b)
        s = np.dot(b_inv,t)
        y = np.sum(b_inv, axis=0) #cost metric

    else:
        print("Optimal Solution Reached")
        s = np.ceil(s) #round up to nearest integer
        print("Total stock used: {}".format(sum(s)))
        b_t = np.transpose(b)
        w = np.dot(s,(L - np.dot(b_t,l)))
        print("Total waste: {}".format(w))
        #solution matrix corresponds to each row in pattern matrix
        #each row represents a pattern from the length matrix
        print(s) #solution matrix
        print(b_t) #pattern matrix
        print(l)
