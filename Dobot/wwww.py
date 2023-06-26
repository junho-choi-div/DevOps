import cv2
import sys


src = cv2.imread('./test_img.bmp')
src = cv2.resize(src,dsize=(src.shape[1]//2,src.shape[0]//2))
if src is None:
    print('Image open failed!')
    sys.exit()
    
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 블러를 통해 노이즈 제거
blr = cv2.GaussianBlur(gray, (3, 3), 1.0)

# 트랙바 함수 정의
def on_trackbar(pos):
    # 트랙바 초기값 정보 받아오기
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    # 받아온 정보를 cv2.HoughCircles에 입력
    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=70, minRadius=10, maxRadius=80)
    
    dst = src.copy() # 복사한 입력영상 위에 원 그리기
    if circles is not None:
        for i in range(circles.shape[1]) :# 검출된 원 갯수만큼 반복
            cx, cy, radius = circles[0][i] # i번째 원에 데이터 저장
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA) # 저장된 데이터를 이용해 원 그리기
    
    cv2.imshow('img', dst)
    
# 트랙바 생성
cv2.imshow('img', src)

# 트랙바 범위
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)

# 트랙바 초깃값
cv2.setTrackbarPos('minRadius', 'img', 10) # 초기값 10
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)

cv2.waitKey()

cv2.destroyAllWindows()