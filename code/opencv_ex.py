import cv2 as cv
import sys

img = cv.imread('your file path')

# 지정된 경로의 이미지를 잘 읽었는지 확인
if img is None:
    print("지정된 경로의 파일 없음")
print(type(img))
print(img.shape)

# 3. 영상을 읽고 표시하기
def Image_display(img):
    cv.imshow('Image Display', img)
    #pixcel의 rbg값 출력
    print(img[0,0,0], img[0,0,1], img[0,0,2])


# 4. 영상 형태 변환하고 크기 축소하기
def grayNresize(img):
    # BGR컬러 영상을 명암 영상으로 변환
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 명암 영상 사이즈 축소(1/2배 축소)
    gray_small = cv.resize(gray_scale, dsize=(0,0), fx=0.5, fy=0.5)
    #각각 저장
    cv.imwrite('your file path', gray_scale)
    cv.imwrite('your file path', gray_small)

    cv.imshow('Color image', img)
    cv.imshow('Gray image', gray_scale)
    cv.imshow('Gray small image', gray_small)


# 7. 영상에 도형을 그리고 글씨 쓰기
def draw(event, x, y, flags, param): #callback function
    if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭됐을 때
        # cursor 위치에 (200,200) 크기의 빨간색 선 두께 2px의 정사각형을 그림
        cv.rectangle(img, (x, y), (x+200, y+200), (0,0,255),2)
    elif event == cv.EVENT_RBUTTONDOWN: # 마우스 오른쪽 버튼 클릭됐을 때
        # cursor 위치에 (100,100) 크기의 파란색 선 두께 2px의 정사각형을 그림
        cv.rectangle(img, (x, y), (x+100, y+100), (255,0,0),2)
    cv.imshow('Drawing', img)
 
# 8. 마우스 드래그로 도형 크기 조절하기
def draw_size_control(event, x, y, flags, param): #callback function
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭됐을 때
        # cursor 위치에 (200,200) 크기의 빨간색 선 두께 2px의 정사각형을 그림
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP: # 마우스 오른쪽 버튼 클릭됐을 때
        # cursor 위치에 (100,100) 크기의 파란색 선 두께 2px의 정사각형을 그림
        cv.rectangle(img, (ix, iy), (x, y), (255,0,0),2)
    cv.imshow('Drawing', img)

# 9. 페인팅 기능 만들기
BrushSize = 5
LColor, RColor = (255,0,0), (0,0,255)
def painting(event, x, y, flags, param): #callback function
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, RColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSize, RColor, -1)
    cv.imshow('Painting', img)

if __name__ == '__main__':
    # Image_display(img)
    # grayNresize(img)

    # cv.waitKey()
    # cv.destroyAllWindows()

    # # 윈도우 이름 짓기
    # cv.namedWindow('Drawing')
    # cv.imshow('Drawing', img)
    # # #'Drawing' 윈도우에 draw 콜백 함수 지정해 줌
    # # cv.setMouseCallback('Drawing', draw)

    # #'Drawing' 윈도우에 draw 콜백 함수 지정해 줌
    # cv.setMouseCallback('Drawing', draw_size_control)


    # 윈도우 이름 짓기
    cv.namedWindow('Painting')
    cv.imshow('Painting', img)
    cv.setMouseCallback('Painting', painting)

    while True:
        if cv.waitKey(1)==ord('q'):
            cv.destroyAllWindows()
            break

