import statistics
import math
#---------------分散 & 標準偏差-----------------------------------------------
q_2 = [5,6,8,6,5,3,9,6] # < - plz put in
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

#-----------------平均値で求める分散と標準偏差--------------------
print('-----------------------------------------------')
q_nrs = [50,70,90,80,50] # < - plz put in
q_nrs_len = len(q_nrs)
q_nrs_sum = sum(q_nrs)
q_nrs_mean = q_nrs_sum/q_nrs_len
print('mean:',q_nrs_mean)

q_nrs_al = 0
for q_nrs_each in q_nrs:
    q_nrs_each = q_nrs_each**2
    q_nrs_al +=  q_nrs_each

print('all:',q_nrs_al)
q_nrs_1x2_mean = q_nrs_al/q_nrs_len
print('x2の平均値:',q_nrs_1x2_mean)
q_nrs_ss = q_nrs_1x2_mean-q_nrs_mean**2
print('分散=',q_nrs_ss)
q_nrs_aa = math.sqrt(q_nrs_ss)
print('標準偏差=',round(q_nrs_aa,1))