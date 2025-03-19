import cv2 as cv
import numpy as np

def cartoonify_image(img_path, save_path):
    # 이미지 로드
    img = cv.imread(img_path)
    
    # 1. 노이즈 제거를 위한 블러 적용
    img_blur = cv.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    
    # 2. 엣지 감지
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_blur = cv.medianBlur(gray, 7)
    edges = cv.adaptiveThreshold(gray_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=9, C=2)
    
    # 3. 컬러 양자화 (k-means 클러스터링)
    data = np.float32(img_blur).reshape((-1, 3))
    K = 8  # 색상 군집 개수
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv.kmeans(data, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()].reshape(img.shape)
    
    # 4. 엣지와 결합하여 만화 효과 적용
    cartoon = cv.bitwise_and(quantized, quantized, mask=edges)
    
    # 이미지 저장
    cv.imwrite(save_path, cartoon)
    
    # 결과 출력
    cv.imshow('Original Image', img)
    cv.imshow('Cartoonized Image', cartoon)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 실행
cartoonify_image('img_path', 'save_path')