clear all
close all
%% Importing the time frames from the Astyx Dataset
A = importdata('000011.txt')
B = importdata('000012.txt')
C = importdata('000013.txt')
D = importdata('000014.txt')
E = importdata('000015.txt')
F = importdata('000016.txt')
G = importdata('000017.txt')
H = importdata('000018.txt')
I = importdata('000019.txt')
J = importdata('000020.txt')
%% Referencing the X and Y direction from the dataset in this particular time frame
L = A.data(:,1);
M = A.data(:,2);
N = B.data(:,1);
O = B.data(:,2);
P = C.data(:,1);
Q = C.data(:,2);
R = D.data(:,1);
S = D.data(:,2);
T = E.data(:,1);
U = E.data(:,2);
V = F.data(:,1);
W = F.data(:,2);
X = G.data(:,1);
Y = G.data(:,2);
Z = H.data(:,1);
Z1= H.data(:,2);
Z2= I.data(:,1);
Z3= I.data(:,2);
Z4= J.data(:,1);
Z5= J.data(:,2);
%% Plotting the graph in 2D visualization form
figure()
scatter(L,M)
pause (0.1)
scatter (N,O)
pause (0.1)
scatter (P,Q)
pause (0.1)
scatter (R,S)
pause (0.1)
scatter (T,U)
pause (0.1)
scatter(V,W)
pause(0.1)
scatter(X,Y)
pause(0.1)
scatter(Z,Z1)
pause(0.1)
scatter(Z2,Z3)
pause(0.1)
scatter(Z4,Z5)
pause(0.1)
xlabel('X-direction')
ylabel('Y-direction')
title('Radar data')



