fs = 44100;
twopi = 2 * pi;
f1 = 600;

x = linspace(0,1,fs);
sn1 = sin(x * twopi * 600);

sound(sn1, fs);