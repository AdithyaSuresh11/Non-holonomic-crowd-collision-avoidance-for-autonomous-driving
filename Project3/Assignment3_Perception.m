%%% AuE8930 - Machine Perception and Intelligence%%%
%%% Assignment 3 %%%
%%% Instructor- Dr. Bing Li %%%
%%% Teaching Assistant- Ziyue Feng %%%
%%% Submitted by Adithya Suresh, C18590622 %%%
warning off
%% Question 1
% 3D Point LIDAR cloud data visualization colored by the reflectivity value 
A = fopen('002_00000000.bin');
C = fread(A,'single');
x = [];
y = [];
z = [];
intensity = [];
%%% Parsing the LIDAR data with respect to the X,Y,Z from X1,Y1,Z1,I1...
for i=1:4:length(C)
    x =[x,C(i)];
end
for j=2:4:length(C)
    y =[y,C(j)];
end
for k=3:4:length(C)
    z =[z,C(k)];
end
for m=4:4:length(C)
    intensity =[intensity,C(m)];
end
figure(1)
ptCloud = pointCloud([x(:),y(:),z(:)],'Intensity',intensity(:)); %%% Visualizing with respect to intensity
pcshow(ptCloud)
title('3D visualization of raw point cloud LIDAR data');
%% Question 2
% 3D resolution granularity is selected with voxel/ box grid filter to down-sample all the 3D point cloud points to 3D voxel space points
figure(2)
gridStep = 1.0;
ptCloudA = pcdownsample(ptCloud,'gridAverage',gridStep); %%% Box grid filter for downsampling
pcshow(ptCloudA)
title('3D downsampled LIDAR data');
%% Question 3a and b
%RANSAC algorithm's variant M-estimator SAmple and Consensus algorithm was selected to apply to the 3D voxel space.
tic %%% Computational time complexity verification
maxDistance = 0.02;
referenceVector = [0,0,1];
maxAngularDistance = 0.1;
[model,inlierIndices,outlierIndices] = pcfitplane(ptCloudA,maxDistance,referenceVector,maxAngularDistance);
plane1 = select(ptCloudA,inlierIndices); %%% 3D point cloud data is selected with respect to planes of choice
remainPtCloud = select(ptCloudA,outlierIndices);
roi = [-inf,inf;0.4,inf;-inf,inf];
sampleIndices = findPointsInROI(remainPtCloud,roi);
[model2,inlierIndices,outlierIndices] = pcfitplane(remainPtCloud,...
            maxDistance,'SampleIndices',sampleIndices);
plane2 = select(remainPtCloud,inlierIndices); %%% 3D point cloud data is selected with respect to planes of choice
remainPtCloud = select(remainPtCloud,outlierIndices);
figure(3)
pcshow(plane1)
hold on;
plot(model)
title('Point cloud data on the Plane')
toc %%% The elapsed time gives the time complexity of the RANSAC algorithm to compute
%% Question 3c
% All the ground points are removed in the 3D voxel space points
maxDist = 0.6;
refVec = [0,0,10];
maxAng = 5;
[model3,inlierIndices,outlierIndices] = pcfitplane(ptCloudA,maxDist,refVec,maxAng);
ptCloudWithoutGround = select(ptCloudA,outlierIndices,'OutputSize','full'); %%% Filtering the ground points only
figure(4)
pcshow(ptCloudWithoutGround)
title('Point cloud visualization without Ground points')
%% Question 4
% X-Y projection is performed to the off-ground points and 2D matrix is visualized as an image
[ptCloudnew,indices] = removeInvalidPoints(ptCloudWithoutGround); %%% Invalid points like NaN are removed
new_x = ptCloudnew.Location(:,1);
new_y = ptCloudnew.Location(:,2);
matrix = [new_x,new_y]; %%%2D matrix from the 3D point cloud data
figure(5)
scatter(matrix(:,1),matrix(:,2),1,'w');
set(gca,'color',[0,0,0])
title('3D point cloud to 2D image')
xlabel('X-coordinate')
ylabel('Y-coordinate')
axis equal
%% Question 5a
% Visualization of the raw point cloud data in polar coordinate
x1 = ptCloud.Location(:,1);
y1 = ptCloud.Location(:,2);
z1 = ptCloud.Location(:,3);
a1 = ptCloud.Intensity(:);
thrd_matrix =[x1,y1,z1];
figure(6);
[x1, y1, z1] = sphere;
mesh(70*x1,70*y1,70*z1, 'Marker', '.', 'EdgeColor', 'flat', 'FaceColor', 'none', 'LineStyle', ':')
hold on;
plot3(0,0, 0, '+r', 'MarkerSize', 20)
axis equal
axis off
hold on
pcshow(ptCloud)
title('Polar Coordinate visualization in 3D Spherical form')
%%  Question 5b
% Visualization of 2D depth image from the polar coordinates
x2 = ptCloud.Location(:,1);
y2 = ptCloud.Location(:,2);
z2 = ptCloud.Location(:,3);
a2 = ptCloud.Intensity(:);
thrd_matrix =[x2,y2,z2];
[theta1,rho1,z3]= cart2sph(x2,y2,z2); %%%Polar form visualization
[azimuth, bin_elevation, a] = sph2cart(theta1,rho1,z3);
figure(7)
polarplot= polarscatter(theta1,z3,0.1,a1);
set(gca,'color',[0,0,0])
title('3D Polar Coordinate to 2D Depth image visualization')