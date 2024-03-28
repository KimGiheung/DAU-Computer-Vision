import cv2 as cv
import sys

img = cv.imread('C:\\Users\\win\\Documents\\GitHub\\DAU-Computer-Vision\\data\\soccer.jpg')

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
    cv.waitKey()
    cv.destroyAllWindows()

# 4. 영상 형태 변환하고 크기 축소하기
def grayNresize(img):
    # BGR컬러 영상을 명암 영상으로 변환
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 명암 영상 사이즈 축소(1/2배 축소)
    gray_small = cv.resize(gray_scale, dsize=(0,0), fx=0.5, fy=0.5)
    #각각 저장
    cv.imwrite('C:\\Users\\win\\Documents\\GitHub\\DAU-Computer-Vision\\data\\soccer_gray.jpg', gray_scale)
    cv.imwrite('C:\\Users\\win\\Documents\\GitHub\\DAU-Computer-Vision\\data\\soccer_gray_small.jpg', gray_small)

    cv.imshow('Color image', img)
    cv.imshow('Gray image', gray_scale)
    cv.imshow('Gray small image', gray_small)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    Image_display(img)
    grayNresize(img)
