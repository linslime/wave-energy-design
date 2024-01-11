function [u1,u2,w1,w2] = longge2(u1,u2,w1,w2,h,a,b)

x = a:h:b;

for i = 1:length(x)-1

k11 = f1(x(i) , u1(i) , u2(i) , w1(i) , w2(i));
k21 = f2(x(i) , u1(i) , u2(i) , w1(i) , w2(i));
L11 = f3(x(i) , u1(i) , u2(i) , w1(i) , w2(i));
L21 = f4(x(i) , u1(i) , u2(i) , w1(i) , w2(i));

k12 = f1(x(i)+h/2 , u1(i)+h*k11/2 , u2(i)+h*k21/2 , w1(i)+h*L11/2, w2(i)+h*L21/2);
k22 = f2(x(i)+h/2 , u1(i)+h*k11/2 , u2(i)+h*k21/2 , w1(i)+h*L11/2, w2(i)+h*L21/2);
L12 = f3(x(i)+h/2 , u1(i)+h*k11/2 , u2(i)+h*k21/2 , w1(i)+h*L11/2, w2(i)+h*L21/2);
L22 = f4(x(i)+h/2 , u1(i)+h*k11/2 , u2(i)+h*k21/2 , w1(i)+h*L11/2, w2(i)+h*L21/2);

k13 = f1(x(i)+h/2 , u1(i)+h*k12/2 , u2(i)+h*k22/2 , w1(i)+h*L12/2 , w2(i)+h*L22/2);
k23 = f2(x(i)+h/2 , u1(i)+h*k12/2 , u2(i)+h*k22/2 , w1(i)+h*L12/2 , w2(i)+h*L22/2);
L13 = f3(x(i)+h/2 , u1(i)+h*k12/2 , u2(i)+h*k22/2 , w1(i)+h*L12/2 , w2(i)+h*L22/2);
L23 = f4(x(i)+h/2 , u1(i)+h*k12/2 , u2(i)+h*k22/2 , w1(i)+h*L12/2 , w2(i)+h*L22/2);

k14 = f1(x(i)+h , u1(i)+h*k13 , u2(i)+h*k23 , w1(i)+h*L13 , w2(i)+h*L23);
k24 = f2(x(i)+h , u1(i)+h*k13 , u2(i)+h*k23 , w1(i)+h*L13 , w2(i)+h*L23);
L14 = f3(x(i)+h , u1(i)+h*k13 , u2(i)+h*k23 , w1(i)+h*L13 , w2(i)+h*L23);
L24 = f4(x(i)+h , u1(i)+h*k13 , u2(i)+h*k23 , w1(i)+h*L13 , w2(i)+h*L23);

u1(i+1) = u1(i) + h/6 * (k11 + 2*k12 + 2*k13 + k14);
u2(i+1) = u2(i) + h/6 * (k21 + 2*k22 + 2*k23 + k24);
w1(i+1) = w1(i) + h/6 * (L11 + 2*L12 + 2*L13 + L14);
w2(i+1) = w2(i) + h/6 * (L21 + 2*L22 + 2*L23 + L24);

end
end
