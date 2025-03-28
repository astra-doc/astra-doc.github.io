# 📌 자주 묻는 질문

??? note "슬롯 개수를 늘릴 수 있을까요?"
    아직 공식 기능은 아니지만 아래와 같이 따라하면 슬롯을 늘릴 수 있습니다.

    1. 파일 탐색기 주소에 다음을 입력
        ```bash
        %userprofile%\.astra
        ```
    2. .env 파일을 메모장에서 열기
    3. 다음을 추가하고 저장 (숫자는 원하는 개수로 설정)
        ```bash
        ASTRA_SLOT_COUNT=10
        ```
    4. Astra 재실행
    
??? note "새 버전을 설치하면 설정을 다시 해야할까요?"
    설정은 사용자 계정 경로(%userprofile%\\.astra)에 저장하고 있으므로, 설정을 다시할 필요는 없습니다.
    하지만 버전 업데이트가 되면서 새로운 설정이 추가된 경우에는 저장이 필요합니다.

??? note "메리츠 HTS를 D 드라이브에 설치한 경우 실행이 안됩니다"
    아래와 같이 따라하면 HTS 경로를 수정할 수 있습니다.

    1. 파일 탐색기 주소에 다음을 입력
        ```bash
        %userprofile%\.astra
        ```
    2. .env 파일을 메모장에서 열기
    3. 아래처럼 HTS 경로를 입력
        ```bash
        MERITZ_HTS_PATH=D:\메리츠증권\iMERITZ XII\Main\imeritz.exe
        ```
    4. Astra 재실행

??? note "자동 스케줄러로 실행할 때 주문 완료 후에 HTS 창을 남겨 두고 싶어요"
    아래와 같이 따라하면 HTS 경로를 수정할 수 있습니다.

    1. 파일 탐색기 주소에 다음을 입력
        ```bash
        %userprofile%\.astra
        ```
    2. .env 파일을 메모장에서 열기
    3. 다음을 추가하고 저장
        ```bash
        ASTRA_KEEP_HTS=TRUE
        ```
    4. Astra 재실행
