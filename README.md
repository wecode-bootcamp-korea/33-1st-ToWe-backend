# 33-1st-ToWe-backend
정병휘, 정치영

# 메모장

## 7. Back-end 기능 구현

### 1. ERD

![ERD_3](https://user-images.githubusercontent.com/101810494/173720423-84cabf61-5c94-4de1-a835-ab61df9c0bd3.jpg)

### 2. 회원가입 및 로그인 API

#### ID, Password 암호화 및 유효성 검사
```
• bcrypt 활용한 Password 암호화 적용
• JWT 활용한 로그인 기능 구현
• 정규표현식 활용한 유효성 검사
• 유효성 검사 모듈화(validator)
• 로그인 데코레이터 기능 구현
```

### 3. 유저정보 확인 API

#### 사용자 관점에서 해당 유저정보 요청시 개인정보 확인 기능 구현
```
• 로그인 데코레이터를 통한 유저정보 식별
• 해당유저의 개인정보 / 리뷰정보 / 구매정보 확인 기능 구현
```

### 4. 제품 리스트 API

- dfd

### 5. 제품 상세 API

- dfd

### 6. 좋아요 기능 API

- ㅇㄹㅇ

### 7. 리뷰 기능 API

#### RESTful 방식으로 제품 ID를 식별, 해당 제품에 대한 리뷰 작성 및 확인 기능
```
• 제품ID 및 유저ID(Token)을 통해 제품과 유저를 식별
• POST, GET 메서드를 활용하여 리뷰작성 및 리뷰확인 기능 구현
```
    
### 8. 장바구니 기능 API

```
• RESTful 방식으로 제품 ID를 식별, 해당 제품에 대한 리뷰 작성 및 확인 기능
```

### 9. 주문관리 기능 API

```
• GET 호출을 통해서 백엔드로부터 데이터를 받아온 뒤 여러개의 데이터를 setState 함수를 통해 렌더링 작업
• POST 호출을 통해 로그인시 발급받은 토큰을 localStorage에서 가져와 headers에 담아서 보낸뒤 페이지 이동
```

## 시연영상
https://www.youtube.com/watch?v=wX-WB_yCXtg

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/wX-WB_yCXtg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
