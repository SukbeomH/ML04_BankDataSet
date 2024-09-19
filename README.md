## ML04_BankDataSet

ML04_BankDataSet Machine Learning

## How to fork the repository

0. 현재 레포지토리를 포크한다
1. 로컬에 작업할 폴더를 생성
2. 터미널에서 작업폴더를 열고 (혹은 VS Code로 열고)
3. 위 링크로 들어가서 레포지토리를 포크한다
4. 각자 작업할 폴더에서 포크한 자신의 레포지토리 주소를 클론
5. `git clone <your-repo.git> .` 명령어로 클론한다
6. `git remote -v` 로 현재 리모트 저장소를 확인한다
7. `git remote add upstream <original-repo.git>` 으로 원본 레포지토리를 추가한다
8. `git remote -v` 로 현재 리모트 저장소를 확인한다
9. `git pull upstream main` 으로 원본 레포지토리의 내용을 가져온다
10. ??? 작업 한?다???

# 은행 데이터셋을 활용한 머신러닝

## Members

@euneun9
@Coke-Eating-Polarbear
@gaeun19
@SukbeomH

## 데이터셋

**Example**

```csv
age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,deposit
59,admin.,married,secondary,no,2343,yes,no,unknown,5,may,1042,1,-1,0,unknown,yes
56,admin.,married,secondary,no,45,no,no,unknown,5,may,1467,1,-1,0,unknown,yes
41,technician,married,secondary,no,1270,yes,no,unknown,5,may,1389,1,-1,0,unknown,yes
55,services,married,secondary,no,2476,yes,no,unknown,5,may,579,1,-1,0,unknown,yes
54,admin.,married,tertiary,no,184,no,no,unknown,5,may,673,2,-1,0,unknown,yes
```

## 데이터셋 정보

- age: 나이
- job: 직업
- marital: 결혼 여부
- education: 교육 수준
- default: 신용 한도 초과 여부
- balance: 연간 평균 잔고
- housing: 주택 대출 여부
- loan: 개인 대출 여부
- contact: 연락 수단
- day: 마지막 연락일
- month: 마지막 연락 월
- duration: 마지막 통화 시간
- campaign: 이번 캠페인 연락 횟수
- pdays: 이전 캠페인 마지막 연락 후 경과 기간
- previous: 이번 캠페인 이전 연락 횟수
- poutcome: 이전 캠페인 성공 여부
- deposit: 예금 장려 여부

## 데이터셋 출처

- [Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

## Overview
