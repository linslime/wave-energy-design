% function RK4()
clc;clear;
Ts = 0.01;
h = Ts;
time = 1.5;
N = time/Ts;
t = linspace(Ts,time,N);

y = zeros(1,N+1);
for m=2:N
    k1 = exp(m*Ts);
    k2 = exp(m*Ts+h/2*k1);
    k3 = exp(m*Ts+h/2*k2);
    k4 = exp(m*Ts+h*k3);
    y(1,m+1) = y(1,m) +(k1+2*k2+2*k3+k4)*h/6;
end

figure
plot(t,exp(t))
hold on
y = y(1,2:N+1);
y = y+1;
plot(t,y)
legend('真实','数值解');
