# 33기 1차 프로젝트 6팀 ToWe

![KakaoTalk_Photo_2022-05-28-22-53-59 001](https://user-images.githubusercontent.com/93895746/172115466-3caf6857-746e-4436-9184-a49d6006a035.png)

## 프로젝트 선정이유

- 깔끔하고 아기자기한 UI로 보기 좋게 레이아웃을 잡고, 기능 구현에 중점을 두어 개발할 수 있다.
- 커머스 사이트로써 기본적인 페이지 구성이 잘 되어 있다.

<br><br>

## 프로젝트 소개

한정된 기간동안 기획과 디자인보다는 개발에 집중하기 위해서 일부를 (무직타이거)을 참조하여 학습목적으로 제작하였습니다. <br>
코드 및 이미지를 남용 및 악용할 경우 법적으로 문제될 수 있습니다. <br>
이 프로젝트에서 사용되고 있는 로고 및 배너는 해당 프로젝트 팀 소유이므로 외부인이 허가없이 사용할 수 없습니다.

<br><br>

## 1. 프로젝트 기간 및 인원

**프로젝트 기간**
22.05.23 ~ 22.06.03 (약2주)

<br><br>

## 2. 개발 인원

#### Front-end : 김형석, 김슬비, 김정준, 노해리, 유지후

#### Back-end : 정치영, 정병휘

<br><br>

## 3. 구현 항목

### 필수구현

#### 회원가입 / 로그인, 메인페이지, 상품 리스트, 상품 상세, 장바구니, Nav / Footer, 마이페이지

### 추가 구현

#### 베스트10, 주문하기(포인트결제), 리뷰 / 게시판

<br><br>

## 4. 기술 스택

### Front-end

: HTML/CSS, JavaScript, React.js, React-Router, Sass

### Back-end

: Python, Django

<br><br>

## 5. 협업도구

### (1) git & github
<br>

(Front-end) https://github.com/wecode-bootcamp-korea/33-1st-ToWe-frontend <br>

(Back-end) https://github.com/wecode-bootcamp-korea/33-1st-ToWe-backend

<br>

### (2) Trello

![](https://velog.velcdn.com/images/seul06/post/278a77fb-8985-45c4-b809-763545d0b289/image.png)

- 팀원간 프로젝트 협업도구로는 Trello를 활용했다.

<br>

### (3)Slack

![스크린샷 2022-06-06 오후 4 44 42](https://user-images.githubusercontent.com/93895746/172118267-98978164-f17e-44ae-b36d-ef1fed4518f4.png)

<br>
<br>

# 33-1st-ToWe-backend
정병휘, 정치영

## Back-end 기능 구현

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

#### 검색 / 조건별필터 / 정렬 / 페이지네이션 기능 구현

```
• Q객체를 이용한 필터기능 구현
• contains를 이용한 검색기능 구현
• 정렬기능 구현
• LIMIT OFFSET로 슬라이시를 이용한 페이지네이션 구현
```

### 5. 제품 상세 API

#### 제품아이디 요청시 제품 정보 반환

### 6. 좋아요 기능 API

#### 좋아요 ON/OFF기능 / 제품리스트 페이지에 좋아요 여부 추가

```
• 좋아요API[POST]를 getorcreate를 이용해서 CREATE / DELETE 동시 구현 
• 상품리스트API를 Private/Public 2가지로 나눈 후 Private에는 로그인데코레이터와 좋아요 여부 
```

### 7. 리뷰 기능 API

#### RESTful 방식으로 제품 ID를 식별, 해당 제품에 대한 리뷰 작성 및 확인 기능
```
• 제품ID 및 유저ID(Token)을 통해 제품과 유저를 식별
• POST, GET 메서드를 활용하여 리뷰작성 및 리뷰확인 기능 구현
```
    
### 8. 장바구니 기능 API

```
• 장바구니 담기(post), 확인(get), 삭제(delete) 기능 구현
• transaction 활용 입력데이터 무결성 확보 구현
```

### 9. 주문관리 기능 API

```
• 결제시스템을 모방하여 포인트를 사용하여 주문하기 기능 구현
  (토큰, Proudct_Option_id, Quantity 값을 입력받아 '주문' 테이블에 삽입)
• 데이터 삽입시 transaction 활용, 데이터 무결성 확보
• 유저의 '주문확인' 기능 구현
```

## 시연영상

[![Video Label](http://img.youtube.com/vi/wX-WB_yCXtg/0.jpg)](https://youtu.be/wX-WB_yCXtg)

https://www.youtube.com/watch?v=wX-WB_yCXtg
