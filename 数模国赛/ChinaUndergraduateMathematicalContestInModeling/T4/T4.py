#第四题，变步长搜索法
import math
import matplotlib.pyplot as plt
import csv

#步长，初始值，及终止值
step = 0.01
start = 0
end = 400


J1 = 14137.79

def V(u1):
    if u1 <= 2:
        return math.pi * u1
    else:
        return 2 * math.pi +(1-math.pow((2.8-u1)/0.8,3)) * (0.8 * math.pi/3)

def J2(x2,x1):
    return 2433 * (0.25 + 0.2019575 + x2 - x1) * (0.25 + 0.2019575 + x2 - x1) + 354.8125

def f1(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return u2

def f2(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return (1760 * math.cos(1.9806 * x) - 528.5018 * u2 -V(u1) * 1025 * 9.8 + 80000 * (w1 - u1) + c1 * (w2 - u2)-(1-math.cos(p1+q1)) * 9.8 * 2433)*(1/(4866+1091.099))

def f3(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return w2

def f4(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return  (1-math.cos(p1+q1)) * 9.8 - 1 * (1/2433) * (80000 * (w1 - u1) + c1 * (w2 - u2))

def f5(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return p2

def f6(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return (2140 * math.cos(1.9806 * x) - 1655.909 * p2 - 8890.7 * p1 + 250000 * (q1 - p1) + d1 * (q2 - p2) - 1.2 * 4866 * 9.8 * math.sin(p1)) / (J1 + 7142.493)

def f7(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return q2

def f8(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return  ((0.25 + 0.2019575 + w1 - u1) * math.sin(p1 + q1) * 9.8 * 2433- 250000 * (q1 - p1) - d1 * (q2 - p2))/J2(w1,u1)

#龙格库塔
def RK4(u1,u2,w1,w2,p1,p2,q1,q2,x):
    for i in range(len(x) - 1):
        #第一个点
        k11 = f1(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        k21 = f2(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        L11 = f3(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        L21 = f4(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        r11 = f5(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        r21 = f6(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        t11 = f7(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        t21 = f8(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])

        #第二个点
        k12 = f1(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        k22 = f2(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        L12 = f3(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        L22 = f4(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        r12 = f5(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        r22 = f6(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        t12 = f7(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        t22 = f8(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)

        #第三个点
        k13 = f1(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        k23 = f2(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        L13 = f3(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        L23 = f4(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        r13 = f5(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        r23 = f6(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        t13 = f7(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        t23 = f8(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)

        k14 = f1(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        k24 = f2(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        L14 = f3(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        L24 = f4(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        r14 = f5(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        r24 = f6(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        t14 = f7(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        t24 = f8(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)

        u1[i + 1] = u1[i] + step / 6 * (k11 + 2 * k12 + 2 * k13 + k14)
        u2[i + 1] = u2[i] + step / 6 * (k21 + 2 * k22 + 2 * k23 + k24)
        w1[i + 1] = w1[i] + step / 6 * (L11 + 2 * L12 + 2 * L13 + L14)
        w2[i + 1] = w2[i] + step / 6 * (L21 + 2 * L22 + 2 * L23 + L24)
        p1[i + 1] = p1[i] + step / 6 * (r11 + 2 * r12 + 2 * r13 + r14)
        p2[i + 1] = p2[i] + step / 6 * (r21 + 2 * r22 + 2 * r23 + r24)
        q1[i + 1] = q1[i] + step / 6 * (t11 + 2 * t12 + 2 * t13 + t14)
        q2[i + 1] = q2[i] + step / 6 * (t21 + 2 * t22 + 2 * t23 + t24)
        # print(p2[i])

#主函数
if __name__ == "__main__":

    x = []
    temp = start
    while temp <= end:
        x.append(temp)
        temp += step
    u1 = [0 for i in range(len(x))]
    u2 = [0 for i in range(len(x))]
    w1 = [0 for i in range(len(x))]
    w2 = [0 for i in range(len(x))]
    p1 = [0 for i in range(len(x))]
    p2 = [0 for i in range(len(x))]
    q1 = [0 for i in range(len(x))]
    q2 = [0 for i in range(len(x))]


    list1 = range(59000,60001,1)
    list2 = range(100000,100001,5000)

    aver = []

    # c1 = 0
    # d1 = 70000
    # RK4(u1, u2, w1, w2, p1, p2, q1, q2, x)
    # p = [c1 * (u2[i] - w2[i]) * (u2[i] - w2[i]) + d1 * (p2[i] - q2[i]) * (p2[i] - q2[i]) for i in range(1500, 2500)]
    # aver.append([c1, d1, sum(p) / len(p)])

    for c in list1:
        for d in list2:
            print(c,d)
            c1 = c
            d1 = d

            u1[0] = 0
            u2[0] = 0
            w1[0] = 0
            w2[0] = 0
            p1[0] = 0
            p2[0] = 0
            q1[0] = 0
            q2[0] = 0

            RK4(u1,u2,w1,w2,p1,p2,q1,q2,x)
            p = [c * (u2[i] - w2[i]) * (u2[i] - w2[i]) + d * (p2[i] - q2[i]) * (p2[i] - q2[i])for i in range(30000,40000)]
            aver.append([c,d,sum(p) / len(p)])

    with open("D:\Desktop\\T4.1.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list(map(list, zip(*aver))))

    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.plot(x, u1, color="red" ,linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.plot(x, w1, color="blue", linewidth=1.0, linestyle="-")
    # plt.xlabel('时间/s')
    # plt.ylabel('位移/m')
    # plt.show()
    #
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.plot(x, p1, color="red", linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.plot(x, q1, color="blue", linewidth=1.0, linestyle="-")
    # plt.xlabel('时间/s')
    # plt.ylabel('位移/m')
    # plt.show()
    #
    # cha = [(w1[i] - u1[i]) for i in range(len(w1))]
    # plt.plot(x, cha, color="red", linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.xlabel('时间/s')
    # plt.ylabel('cha/m')
    # plt.show()
    #
    # cha = [(p1[i] - q1[i]) for i in range(len(w1))]
    # plt.plot(x, cha, color="red", linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.xlabel('时间/s')
    # plt.ylabel('cha/m')
    # plt.show()












