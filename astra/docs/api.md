# 🚀 Astra API
나만의 자동매매 환경을 구축하고 싶지만, 복잡한 HTS 제어 로직을 바닥부터 구현하는 과정은 너무나도 고단합니다.
ASTRA API는 검증된 HTS 제어 엔진을 제공하여 개발 시간을 획기적으로 줄여주며, 개발자가 핵심 매매 전략에만 집중할 수 있도록 최적의 개발 경험을 선사합니다.

## ✨ 핵심 특징
* **검증된 안정성**: 실사용자 400+명의 피드백이 반영된 견고한 제어 로직을 제공합니다.
* **파이썬 최적화**: 수백 줄의 저수준 코드를 단 몇 줄의 직관적인 파이썬 코드로 압축했습니다.
* **AI 친화적 설계**: [API 문서](https://github.com/astra-doc/astra-api/)를 AI에 제공하면 AI가 당신의 전략을 완벽한 코드로 구현해 줍니다.

## 💻 설치 방법
본 라이브러리는 소스 코드 보호를 위해 바이너리(`.whl`) 형태로 제공됩니다.

1. [Releases](https://github.com/astra-doc/astra-api/releases) 페이지에서 최신 버전의 `.whl` 파일을 다운로드합니다.
2. 명령 프롬프트에서 아래 명령어를 실행하여 설치합니다.

```bash
# 다운로드 경로에서 실행
pip install astra_api-0.1.0-cp310-abi3-win_amd64.whl
```

## 📚 API 문서
Astra API의 모든 메서드와 상세 사양은 아래 공식 문서 저장소에서 확인하실 수 있습니다. 
[https://github.com/astra-doc/astra-api](https://github.com/astra-doc/astra-api)


## 🛠️ 사용 방법
AI에게 ASTRA API 문서의 내용을 제공하고, 필요한 구현에 대해 요청합니다.

!!! info "예시"
    ASTRA API (https://github.com/astra-doc/astra-api)를 사용해서 [나만의 매매 알고리즘] 방법을 구현해 주세요


## 🐍 Python 코드 예시
```python
from astra_api import Astra

cert_idx = 1            # 인증서 순서
cert_pw = "passw0rd"    # 인증서 비밀번호
account_idx = 1         # 계좌번호 순서
account_pw = "1234"     # 계좌번호 비밀번호
ticker = "QQQ"          # 종목 

# 1. API 초기화 및 로그인
astra = Astra(
    cert_idx=cert_idx,
    cert_pw=cert_pw,
    account_idx=account_idx,
    account_pw=account_pw,
    ticker=ticker,
)
astra.connect()

# 2. 현재가 조회
price = astra.get_price()
print(f"현재가: {price}")

# 3. 주문
# 예: $500에 10주 매수
astra.buy(qty=10, price=500, order_type="지정가")
```