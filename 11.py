import numpy as np
import matplotlib.pyplot as plt

# csv 파일 읽기
filename = './single_crystal_test_out.csv'
data = np.genfromtxt(filename, dtype=float, delimiter=',', names=True)

# 원하는 값을 열의 제목으로 추출
x = data['e_zz']
y = data['stress_zz']
y2 = data['pk2']

# fontname 또한 설정 가능(검색 ㄱㄱ)

plt.plot(x,y, marker='o', linestyle='-', color='g')
plt.plot(x,y2, marker='x', color='r')

plt.title('Stress-Strain', fontsize=20)

# xlabel : x축 제목
# xticks : 최소,최대,주기
# xlim : 축에 나타내는 값의 범위
plt.xlabel('e_zz', fontsize=15)
plt.xticks(np.arange(min(x),max(x),0.0005), fontsize=9)
plt.xlim([0,0.005])

plt.ylabel('stress_zz', fontsize=15)
plt.yticks(np.arange(min(y),161,40), fontsize=11)
plt.ylim([0,170])

plt.legend(["stress_zz","pk2"])

plt.show