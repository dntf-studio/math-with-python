import statistics
import math

i = [10,1,3,7,1]
mean = statistics.mean(i)
# 平均値 = 4.4
median = statistics.median(i)
# 中央値 = 3
mode = statistics.mode(i)
# 最頻値 = 1

q_1 = [6,4,8,5,2]
q_1_len1 = len(q_1)
q_1_sum1 = sum(q_1)
q_1_mean = q_1_sum1/q_1_len1
#print('mean',q_1_mean)

q_1_alled = 0
for q_1_each in q_1:
    q_1_each=(q_1_each-q_1_mean)**2
    #print(q_1_each)
    q_1_alled += q_1_each
#print(q_1_alled)
q_1_ss = q_1_alled/q_1_len1
#print('Q1_分散=',q_1_ss)
#print('Q1_標準偏差=',math.sqrt(q_1_ss))
#----------------------------------------------------------
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

