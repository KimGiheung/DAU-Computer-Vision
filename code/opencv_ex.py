import cv2 as cv
import sys
import numpy as np
img = cv.imread('')

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

# 5. 웹캠에서 비디오 읽기
def webcam_read():
    # cv.VideoCapture: 웹 캠과 연결 시도
    # cv.CAP_DSHOW: 비디오가 화면에 바로 뜨게 함
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)

    if not cap.isOpened():
        sys.exit('카메라 연결 실패')
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print('프레임 획득 실패')
            break  
        cv.imshow('video display', frame) 

        key=cv.waitKey(1)
        if key==ord('q'):
            break
    # 카메라 연결 끊기
    cap.release()
    # 윈도우 닫기
    cv.destroyAllWindows()

# 6. 비디오에서 수집한 영상 이어 붙이기
def combinate_video(): 
    #카메라 연결
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    if not cap.isOpened():
        sys.exit("카메라 연결 실패")

    # video를 구성할 frame들을 저장할 배열 생성
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            print('프레임 획득에 실패하여 루프를 나갑니다.')
            break
        # 1밀리초 동안 키보드 입력을 기다림
        cv.imshow('video display', frame) 

        key = cv.waitKey(1) 
        # 'c'키가 들어오면 프레임을 리스트에 추가
        if key == ord('c'):
            frames.append(frame)
        # 'q'키가 들어오면 루프 나옴.
        elif key == ord('q'):
            break
    

    cap.release()
    cv.destroyAllWindows()

    # 수집된 영상이 있다면
    if len(frames)>0:
        imgs=frames[0]
        # 최대 3개가지 이어 붙임
        for i in range(1, min(3, len(frames))):
            # 입력 배열들을 가로로 배열
            imgs = np.hstack((imgs, frames[i]))
        cv.imshow('collcted imges', imgs)
        
        cv.waitKey()
        cv.destroyAllWindows()
    print(len(frames))
    print(frames[0].shape)
    print(type(imgs))
    print(imgs.shape)
# 7. 영상에 도형을 그리고 글씨 쓰기
def drawn_image():
    cx = int(img.shape[0]/2)
    cy = int(img.shape[1]/2)
    # 그림 중앙에 정사각형 그리기
    cv.rectangle(img,(cy-100, cx-100), (cy+100, cx+100), (0,255,0),3)
    cv.putText(img, 'center box',(cy-150,cx-100), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,100), 2)
    resized_img = cv.resize(img, dsize=(0,0), fx=0.5, fy=0.5)
    cv.imwrite('', resized_img)
    cv.imshow('Draw', resized_img)

    cv.waitKey()
    cv.destroyAllWindows()

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
    # draw_size_control()
    # cv.setMouseCallback('Drawing', draw_size_control)


    # # 윈도우 이름 짓기
    # cv.namedWindow('Painting')
    # cv.imshow('Painting', img)
    # cv.setMouseCallback('Painting', painting)
    # webcam_read()
    combinate_video()
    # drawn_image()
    while True:
        # 키보드 입력에 'q'가 들어오면 모든 윈도우를 끄고 종료함
        if cv.waitKey(1)==ord('q'):
            cv.destroyAllWindows()
            break

