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
    print('(x-x/6)**2:',q_2_each)
    q_2_all += q_2_each
#print(q_2_all)
q_2_ss = q_2_all/q_2_len
print('Q261_分散=',q_2_ss)
print('Q261_標準偏差=',math.sqrt(q_2_ss))



