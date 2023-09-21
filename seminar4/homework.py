import statistics as st
import math

mas1 = [1,2,3,4,5]
mas2 = [8,7,6,9,0]

m_x = st.mean(mas1)
m_y = st.mean(mas2)

# sum1 = 0
# sum2 = 0
# for i in range(len(mas1)):
#     sum1 = sum1 + (mas1[i]-m_x) * (mas2[i]-m_y)
#     sum2 = sum2 + (mas1[i]-m_x) * (mas1[i]-m_x) * (mas2[i]-m_y) * (mas2[i]-m_y)
# print(sum1 / math.sqrt(sum2))

r_xy = sum(map(lambda mas1, mas2: (mas1 - m_x) * (mas2 - m_y), mas1, mas2)) / math.sqrt(sum(map(lambda mas1, mas2: (mas1 - m_x) * (mas1 - m_x) * (mas2 - m_y) * (mas2 - m_y), mas1, mas2)))
print(r_xy)
