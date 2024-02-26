import cv2
a=cv2.imread(r"D:\CV PRACTICAL PROGRAMS\opencv.jpg");
Lap=[0, 1, 0, 1, -4, 1, 0, 1, 0];
a1=cv2.cvt(a,Lap,r"D:\CV PRACTICAL PROGRAMS\opencv.jpg");
a2=uint8(a1);
imtool(abs(a-a2),[])
lap=[-1 ,-1, -1, -1, 8, -1, -1, -1 ,-1];
a3=cv2.cvt(a,lap,r"D:\CV PRACTICAL PROGRAMS\opencv.jpg");
a4=uint8(a3);
imtool(abs(a+a4),[])
