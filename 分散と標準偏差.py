import statistics
import math

#---------------分散 & 標準偏差-----------------------------------------------
q_2 = [5,6,8,6,5,3,9,6]
q_2_len = len(q_2)
q_2_sum = sum(q_2)
q_2_mean = q_2_sum/q_2_len  
print('mean:',q_2_mean)

q_2_all = 0
for q_2_each in q_2:
    q_2_each = (q_2_each-q_2_mean)**2
    print('(x-x/',q_2_len,')**2:',q_2_each)
    q_2_all += q_2_each
#print(q_2_all)
q_2_ss = q_2_all/q_2_len
print('分散=',q_2_ss)
q_2_aa = math.sqrt(q_2_ss)
print('標準偏差=',round(q_2_aa,1))



