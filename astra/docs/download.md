# ⬇️ 다운로드

!!! warning "면책 조항"
    [면책 조항]

    이 프로그램은 사용자의 HTS 환경에서 작동하는 단순한 자동화 매크로 도구입니다.  
    특정 종목에 대한 매수/매도 시점 추천을 제공하지 않으며, 수익을 보장하지 않습니다.  
    **투자에 대한 모든 책임은 사용자 본인에게 있습니다.**

    본 프로그램은 투자 권유, 투자 자문 또는 투자 일임의 목적이 아니며,   
    순수한 개인 개발 프로젝트로 **비상업적으로 제공되는 도구**입니다.

    사용자는 본 프로그램을 사용함으로써, 그로 인해 발생할 수 있는 모든 결과에 대해  
    **개발자에게 어떠한 법적 책임도 묻지 않음을 동의한 것으로 간주됩니다.**

## 0.6.0 (2025-04-29) [⬇️]()
- 처음 실행할 때 면책조항 팝업이 뜨도록 함 (동의하지 않으면 사용 불가)
- 동적 그리드 매매법 추가 ([설명 및 사용 방법](dynamic_grid.md))

## 0.5.4 (2025-04-15) [⬇️](https://drive.google.com/file/d/1hBoBrifr6neVJzAn47R8OWPTEjqwyQ69/view?usp=sharing)
- HTS 실행 및 종료할 때 "파일 저장 창" 이 떠있는 경우에 창 닫기
- [시트매매] 시가, 고가, 저가를 시트에 저장

## 0.5.3 (2025-04-14) [⬇️](https://drive.google.com/file/d/1_2mbxg3Uoxw5RP8mh2RxoSiGt1ThJX1j/view?usp=sharing)
- [시트매매] 실시간 감시에서 가격입력창을 못찾는 오류 수정
- [시트매매] 실시간 감시에서 파일 저장 실패하는 경우에도 계속 진행할 수 있도록 처리

## 0.5.1 (2025-04-12) [⬇️](https://drive.google.com/file/d/1A6xmFRvo4MJCkANz1w8q6KRWH1h5xGCP/view?usp=sharing)
- 애프터장에서 현재가를 주문창이 아니라 실시간 체결추이 창에서 받아오도록 수정
- 텔레그램 메시지 전송 실패하면 슬롯이 종료안되는 오류 수정
- 텔레그램 토큰을 다른 사용자용으로 교체하면 반영이 안되는 오류 수정

## 0.5.0 (2025-04-10) [⬇️](https://drive.google.com/file/d/1xYo_VxGqGV3_iVn0CyQ4MZR0LhgWXJcI/view?usp=sharing)
- [시트매매] 실시간 감시 기능 추가
- 종가, 주문가능금액, 평균매수금 처리 속도 개선 (파일 이름 입력 부분)

## 0.4.12 (2025-04-08) [⬇️](https://drive.google.com/file/d/1eqEYqpHab2rjrckBvRYIZc3rYKnkG0Lc/view?usp=sharing)
- 시트 아이디에 URL 지원

## 0.4.11 (2025-04-07) [⬇️](https://drive.google.com/file/d/1lju0xchi2X_LZyMfMcV6901IGiFRglIQ/view?usp=sharing)
- 멀티 슬롯 사용 중에 오류 발생시 다음 슬롯의 텔레그램 봇으로 메시지가 보내지는 오류 수정

## 0.4.10 (2025-04-05) [⬇️](https://drive.google.com/file/d/1VASy5H0buRczBgjKF_CCMctmuUJV99tW/view?usp=sharing)
- 멀티 슬롯 사용할 때 오류 발생 시 종료하지 않고 다음 슬롯 진행
- [떨사오팔] 마지막 티어 주문시 발생하는 오류 수정

## 0.4.9 (2025-04-02) [⬇️](https://drive.google.com/file/d/1v7Zzj0Gzq_DfOCNo9QvzvL3x-EnMBDEN/view?usp=sharing)
- 매수/매도 주문 속도 개선
- 주문취소 속도 개선

## 0.4.8 (2025-03-29) [⬇️](https://drive.google.com/file/d/1q8ATOXZtmNQbcGHoMiuEQFQCfEU5xCMO/view?usp=sharing)
- 슬롯 폰트 크기 증가
- 특정 해상도에서 주문 취소 기능 안되는 오류 수정
- 오류 발생했을 때 텔레그램 메시지가 두 번 보내지는 오류 수정
- [떨사오팔] 매수율 기능 추가 (+,- 모두 지원)
- [떨사오팔] 마지막 티어는 정액매수 하지 않도록 수정
- [떨사오팔] 정액매수 주문마다 수량이 동일하게 수정

## 0.4.7 (2025-03-15) [⬇️](https://drive.google.com/file/d/1IfrOLL_Jvfr-q5a9sB3DD3avxi6soZUF/view?usp=sharing)
- 미체결 주문이 많은 경우 (대략 10개 이상) 주문 취소해도 일부 주문이 남아 있는 오류 수정
- [시트매매] 주문수량이 없을 때, 커스텀 텔레그램 메시지가 업데이트 이전 내용으로 보내지는 오류 수정

## 0.4.6 (2025-03-12) [⬇️](https://drive.google.com/file/d/1B48swTmka60TfZvLzhOTLjsYt3L36PBy/view?usp=sharing)
- 송송 시트 및 이전 버전 시트 오류 수정

## 0.4.5 (2025-03-11) [⬇️](https://drive.google.com/file/d/1gsfnhDW2hClPCUPxuGPOBzhWmIWvRSwu/view?usp=sharing)
- 멀티 슬롯 옵션 사용할 때, 다음 슬롯의 텔레그램봇에 메시지가 보내지는 오류 수정

## 0.4.4 (2025-03-10) [⬇️](https://drive.google.com/file/d/1R1SxsZTC43q-uC-UyM1MEac2APzrflFZ/view?usp=sharing)
- 명령줄 옵션에서 멀티 슬롯 지원 (예) `--auto 1,3,4`
- 지정한 종목 보유수량 없을 때 평균매수금액 오류 수정
- [시트매매] 문자열 앞뒤로 공백 제거

## 0.4.2 (2025-03-07) [⬇️](https://drive.google.com/file/d/1l3DcvcIXkdaBwLTiJWj5WngdiEulGx04/view?usp=drive_link)
- 통합증거금 신청되었을 때 주문가능금액 오류 수정
- 보유수량 없을 때 평균매수금액 오류 수정
- 매수/매도 주문확인창 처리 속도 개선

## 0.4.1 (2025-03-06) [⬇️](https://drive.google.com/file/d/19Qi9nhWDoybqfsXIGzLmrel646s8HsXa/view?usp=sharing)
- CSV 파일 이름 입력할 때 일부 문자가 무시되는 오류 수정
- HTS 창이 화면 밖으로 나가서 진행이 안될 때 에러 메시지 표시

## 0.4.0 (2025-03-05) [⬇️](https://drive.google.com/file/d/11COdmrtKBLdsjgo69wxpsH7IevyLyZPs/view?usp=sharing)
- 전일종가, 주문가능금액 확인 속도 개선 (파일로 저장해서 읽어오는 방식으로 변경)
- 설치 파일 용량 감소 (180MB -> 26MB)
- DB증권 지원 종료 (수요가 없는데 관리할 필요가 없음. 추후에 수요가 생기면 다시 지원 예정)
- HTS 경로 입력받기 (.env 파일에 MERITZ_HTS_PATH=D:\메리츠증권\iMERITZ XII\Main\imeritz.exe 추가)
- HTS 종료하지 않도록 설정 (.env 파일에 ASTRA_KEEP_HTS=TRUE 추가)
- [시트매매] 평균매수가 받아오기
- [시트매매] VWAP/TWAP/Limit VWAP/Limit TWAP 지원

## 0.3.9 (2025-02-20) [⬇️](https://drive.google.com/file/d/19QyzBvxsmZqQqTnJU9MxRZ2eJCs1cgFl/view?usp=sharing)
- 텔레그램 메시지에 Astra 버전 추가
- 텔레그램 토큰 처음 등록했을 때 메시지가 안오는 버그 수정
- "최선집행기준 안내" 창 닫기 (전체 창 닫기 기능으로 안닫아짐)
- [시트매매] 주문 취소 기능 추가

## 0.3.8 (2025-02-18) [⬇️](https://drive.google.com/file/d/1iYo4QCgnwbUKUP5ldpF74jWdZOZF2EvU/view?usp=sharing)
- 다중 공인인증서 지원


## 0.3.6 (2025-02-17) [⬇️](https://drive.google.com/file/d/1g1sT5wHA4LA9Owf-UFylVFVXOsuutATD/view?usp=sharing)
- 전일 종가를 읽어 올 때 간헐적으로 소수점(.)을  콤마(,)로 인식하는 문제 수정


## 0.3.5 (2025-02-16)
- 0.3.3 및 0.3.4 에서 발생한 버그 수정


## 0.3.4 (2025-02-15)
- 0.3.3 에서 발생했던 오류 수정 (비밀번호 입력 오류)


- 주문 입력할 때 속도 개선


- <span style="color: red">Windows 10에서 실행 불가</span>


## 0.3.3 (2025-02-13)
- 계좌번호 순서가 4 이상일 때 오동작하는버그 수정


- [시트매매] 주문 셀에 이상한 값이 들어있으면 무시


- [시트매매] 커스텀 텔레그램 메시지 기능 추가


- [시트매매] 대기 시간 기능 추가


- <span style="color: red">버그 발생으로 사용불가</span>


## 0.3.2 (2025-02-12)
- GUI 모드에서는 주문완료후 HTS 종료하지 않도록 수정


- [시트매매] 주문 넣는 셀을 50개로 증가


## 0.3.1 (2025-02-11)
- 슬롯 5개 추가


- 계좌번호 순서를 입력받도록 함


- 속도 개선 (계좌번호와 종목은 처음 한 번만 입력후 변경하지 않음)


- 명령줄에서 실행할 때 슬롯 번호 입력하도록 변경 (astra.exe --auto 2)


- [시트매매] 워크시트 이름을 입력받도록 함


- [시트매매] 상태확인 체크박스 추가 (시간이 오래걸리므로 필요없는 경우 스킵함)


## 0.2.18 (2025-02-06) [⬇️](https://drive.google.com/file/d/1XtLE9-N6QWzH7iHfuxZcrqGzZn-wvprc/view?usp=sharing)
- 주문입력확인창 옵션이 꺼있을 때 정상 동작하도록 처리


- [시트매매] 수량이 0인 주문 무시


## 0.2.17 (2025-01-27)
- 주문이 성공하면 HTS 종료


## 0.2.16 (2025-01-25)
- 0.2.15 에서 여전히 발생하는 dll 로딩 문제 수정 


## 0.2.15 (2025-01-25)
- 특정 환경에서 dll 로딩 오류 발생하는 문제 해결


    - VCRUNTIME140.dll


    - win32api 관련


- <span style="color: red">버그 발생으로 사용불가</span>


## 0.2.14 (2025-01-24)
- 공인인증서 암호에 특수문자 (^, +, %) 가 들어있을 때 로그인 실패하는 버그 수정


- [시트매매] LOC, MOC 를 소문자로 입력했을 때 실패하는 버그 수정


- [시트매매] 전일종가, 현재가, 보유수량, 주문가능금액을 시트에 업데이트 한 이후에 업데이트시간을 기록함


## 0.2.13 (2025-01-22)
- 메리츠 로그인 화면에서 "인증서 자동 팝업" 이 체크되어 있는 경우에 진행이 안되는 버그 수정


## 0.2.12 (2025-01-21)
- 자동 모드에서 간헐적으로 텔레그램 메시지가 보내지지 않는 버그 수정


## 0.2.10 (2025-01-14)
- 떨사오팔  정보초기화 기능 추가


## 0.2.8 (2025-01-11)
- 텔레그램 메시지가 안보내지는 버그 수정


## 0.2.7 (2025-01-11)
- OCR 성능 개선


## 0.2.6 (2025-01-07)
- 메리츠증권 HTS 에서 dll 로딩 오류 수정


## 0.2.4 (2025-01-03)
- 설정들을 반복해서 저장할 때, 처음 값으로 반영이 되는 버그 수정


- 공인인증서 창을 못찾는 버그 수정


## 0.2.1 (2024-12-24)
- 시트매매 탭에서 텔레그램 항목 추가


## 0.2.0 (2024-12-24)
- 메리츠증권 지원


- 시트매매 지원


## 0.1.23 (2024-12-17)
- 전일종가 잘못 인식하는 버그 수정


- 프로그램을 종료해도 프로세스가 죽지 않고 남아 있는 버그 수정


## 0.1.20 (2024-11-14)
- 잔고량이 4자리 수일 때 (1000 주 이상) 콤마(,) 때문에 오류나는 버그 수정


## 0.1.19 (2024-11-12)
- HTS 에서 공지사항 창 닫히지 않는 버그 수정


- 전날 종가 인식 버그 수정


- 설정 파일을 현재 경로가 아니라 계정 경로에 저장


## 0.1.16 (2024-10-25)
- 프로그램 종료할 때 에러 팝업(Can't remove ...) 발생하지 않도록 처리


- MTS 시작할 때 예상하지 않은 팝업이 뜨는 경우 처리


## 0.1.14 (2024-10-04)
- 손절과 일반 매도가 동시에 일어났을 때 제대로 처리하지 못하는 버그 수정


## 0.1.13 (2024-10-02)
- pre-market 에서 시장가 주문이 불가능하므로, 손절은 현재가로 지정가 주문을 하도록 수정


## 0.1.11 (2024-09-27)
- 추가 주문을 할 때 속도 개선 (수량, 가격만 수정해서 주문함)


## 0.1.10 (2024-09-25)
- HTS 제어하는 속도 개선


## 0.1.9 (2024-09-24)
- 종가가 소수점 4자리로 표시되는 경우에, 이 가격으로 주문을 넣으면 오류가 발생되므로 소수점 2자리로 반올림한 후 주문함


## 0.1.8 (2024-09-20)
- 작업스케줄러에서 실행한 경우 .env 파일을 못찾는 버그 수정


## 0.1.7 (2024-09-20)
- 종가가 많이 하락한 경우를 커버하기 위해 추가 매수 주문 (-20% 까지 커버, 10개로 나눠서 주문)


## 0.1.6 (2024-09-19)
- 주문 완료 후 현재 상태 표시 안되는 버그 수정


## 0.1.5 (2024-09-19)
- 매수, 매도 LOC 주문가격이 동일하면 자전거래 의심으로 거절되므로 매도 가격에 $0.01 를 올려서 주문


## 0.1.4 (2024-09-18)
- 실행 위치가 astra 저장 위치와 다른 경우 처리


## 0.1.2 (2024-09-17)
- 명령줄 옵션으로 자동으로 주문 실행하는 기능 추가


## 0.1.1 (2024-09-16)
- 버그 수정


## 0.1.0 (2024-09-16)
- 초기 버전 릴리즈
