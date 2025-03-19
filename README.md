# my_cartoon_rendering
My cartoon rendering using OpenCV

**설명**
이미지 파일을 카툰 형식으로 반환해주는 프로그램입니다.

이 코드는 OpenCV를 이용해 이미지를 만화 스타일로 변환합니다.
-노이즈 제거: bilateralFilter()로 부드러운 필터링 적용
-엣지 감지: adaptiveThreshold()로 경계를 강조
-색상 단순화: k-means clustering으로 색상을 제한
-엣지와 색상 결합: bitwise_and()로 만화 효과 생성
-마지막으로 변환된 이미지를 저장하고 출력

**예시1**
![원본 이미지](/imgs/img-k2.jpg)
원본 이미지

![변형된 이미지](/imgs/cartoon-k2.jpg)
변형된 이미지

**예시2**
![원본 이미지](/imgs/img-night-city.jpg)
원본 이미지

![변형된 이미지](/imgs/cartoon-night-city.jpg)
변형된 이미지지

**추가 설명**
1. 예시1에서 전차의 모습은 만화의 느낌으로 잘 재표현된 것을 볼 수 있습니다.
2. 하지만 예시 2에서는 원본 색감과는 조금 달리 표현된 부분이 있고 또한 비가 내리는 부분이 잘 표현되지 않는 등 부정확한 표현을 볼 수 있습니다.

**한계점**
1. 이 코드에서는 k-means clustering을 사용하기 때문에 작은 색상 변화가 있는 부분에서는 표현이 부정확할 수 있습니다.
2. adaptiveThreshold()는 배경이 복잡하거나 명암 차이가 적은 부분에서 엣지를 제대로 감지하지 못할 수 있습니다.