import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

# 1 inch = 2.54 cm
cm = 1/2.54

xmin = 0
xmax = 1
resolution = 100

# 좌표 생성
x = np.linspace(xmin,xmax,resolution)

y = x**2
y2 = np.sin(2*np.pi*x)
y3 = np.cos(2*np.pi*x)
y4 = x*np.log(x) + (1-x)*np.log(1-x)
y5 = np.exp(-x**2)
y6 = 1/2 + np.tanh((x-0.5)/0.01)/2

y7 = sci.erf(x)

# dpi 설정, 그래프크기(figsize) 결정
# https://www.elsevier.com/authors/policies-and-guidelines/artwork-and-media-instructions/artwork-sizing
fig = plt.figure(dpi=1000)
fig,ax=plt.subplots(figsize=(19*cm,19*cm))

# 각 그래프 곡선 별 설정(색상, 마커, 선 종류, 선 굵기, 마커 크기, 마커 주기)
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
ax.plot(x,y, color='#FF3333', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)
ax.plot(x,y2, color='#FF9900', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)
ax.plot(x,y3, color='#81c147', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)
ax.plot(x,y4, color='#008d62', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)
ax.plot(x,y5, color='#4aa8d8', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)
ax.plot(x,y6, color='#00498c', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)
ax.plot(x,y7, color='#8b00FF', marker='.', linestyle='solid', linewidth=2, markersize=9, markevery=2)

plt.xlabel("x")
plt.ylabel("y")
plt.yticks(np.arange(-2,1.1,0.25))
plt.ylim([-2,1.1])

# 범례에 수식 넣기
# https://matplotlib.org/stable/tutorials/text/mathtext.html
plt.legend([r'$y=x^2$',
            r'$y_2=\mathrm{sin}(2 \pi x)$',
            r'$y_3=\mathrm{cos}(2 \pi x)$',
            r'$y_4=x \mathrm{log}x+(1-x)\mathrm{log}(1-x)$',
            r'$y_5=e^{-x^2}$',
            r'$y_6=\frac{1}{2} + \frac{1}{2} \mathrm{tanh}(\frac{x-0.5}{0.01})$',
            r'$y_7=erf(x)$'], loc='lower left', ncol=2)

# 그래프를 이미지 파일로 저장(위의 dpi와 맞춰주자)
# eps 또는 tiff 사용 권장
plt.savefig('function.png', format='png', bbox_inches='tight', dpi=1000)