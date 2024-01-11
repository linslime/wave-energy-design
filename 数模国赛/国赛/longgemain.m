% main func
clear;clc;
u1(1) = 0;
u2(1) = 0;
w1(1) = 0;
w2(1) = 0;
h=0.01;
a = 0;b=500;
[u1,u2,w1,w2] = longge2(u1,u2,w1,w2,h,a,b);
figure 
plot(a:h:b,w1,'r-');
hold on
plot(a:h:b,u1,'b-.');
xlabel('time');
ylabel('x');
legend('w1','u1');
