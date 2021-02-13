import statistics
import math
#-----------------平均値で求める分散と標準偏差--------------------
q_nrs = [50,70,90,80,50]
q_nrs_len = len(q_nrs)
q_nrs_sum = sum(q_nrs)
q_nrs_mean = q_nrs_sum/q_nrs_len
print('mean:',q_nrs_mean)

q_nrs_al = 0
for q_nrs_each in q_nrs:
    q_nrs_each = q_nrs_each**2
    q_nrs_al +=  q_nrs_each

q_nrs_1x2_mean = q_nrs_al/q_nrs_len
print('x2の平均値:',q_nrs_1x2_mean)
q_nrs_ss = q_nrs_1x2_mean-q_nrs_mean**2
print('分散=',q_nrs_ss)
q_nrs_aa = math.sqrt(q_nrs_ss)
print('標準偏差=',round(q_nrs_aa,1))