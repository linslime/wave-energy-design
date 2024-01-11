function output = V(u1)
if u1<=2
    output = pi*u1;
else
    output=2*pi+(1-((2.8-u1)/0.8)^3)*(0.8*pi)/3;
end