%% Question 3.1
% grays=rgb2gray(img1);
% figure();
% imshow(img1)
% ALready a grayscale image
figure(1000)
histeq(img1) ;
%hist eq. gives a well distributed intensity image
title('Hist. equalization gray scale image')
% figure()
% for i=0.1:0.01:1;
% BW = im2bw(img1,i)
% print(i)
% imshow(BW)
% end
% Select the threshold of the image using the loop

figure()
BW=im2bw(img1,0.93);
BW=imfill(BW,'holes')
imshow(BW)
title('Binary image')

% Question 3.2
BW = edge(BW,'canny');
% figure();
% imshow(BW);
%%
figure()
% [H,T,R] = hough(BW,'RhoResolution',0.5,'Theta',-90:0.5:89);
[H,T,R] = hough(BW,'RhoResolution',0.1,'Theta',-90:0.5:89);
subplot(2,1,1);
imshow(img1);
title('ParkingLot');
subplot(2,1,2);
imshow(imadjust(rescale(H)),'XData',T,'YData',R,...
'InitialMagnification','fit');
title('Hough transform of Parking Lot');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;
colormap(gca,hot);
[H,theta,rho] = hough(BW);
P = houghpeaks(H,10,'threshold',ceil(0.3*max(H(:))));
x = theta(P(:,2));
y = rho(P(:,1));
plot(x,y,'s','color','red');
lines = houghlines(BW,theta,rho,P,'FillGap',400,'MinLength',50);

figure, imshow(img1), hold on
max_len = 0;
for k = 1:length(lines)
xy = [lines(k).point1; lines(k).point2];
plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');
% Plot beginnings and ends of lines
plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
% Determine the endpoints of the longest line segment
len = norm(lines(k).point1 - lines(k).point2);
if ( len > max_len)
max_len = len;
xy_long = xy;
end
end
% highlight the longest line segment
plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','black');
