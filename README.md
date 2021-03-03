# OpenCv_conversion
---
개요
---
키보드를 누른 위치를 알수 있는 프로그램.

---
1. 가장 먼저 Python을 설치를 해야 합니다. 
[Python 설치 링크](https://www.python.org/)

2. 콘솔창에 아래와 같은 Python 모듈을 설치해야 합니다.
```
> pip install opencv-contrib-python
> pip install opencv-python
> pip install cv 또는 cv2
```
---

  #이미지 읽기
```
import cv2
im_gray = cv2.imread('on.png', cv2.IMREAD_GRAYSCALE)
```
 #회색조 이미지를 바이너리로 변환
```
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
```
# 저장
```
cv2.imwrite('bw_image.png', im_bw)
```
참고 자료
---

    https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html?highlight=imread#cv2.imread
    https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html

