## 📌 프로젝트 개요

**파일명**: `design_dome.py`

- 천장의 돔(반구체) 길이를 측정한 결과 10m가 나왔다.
- 돔은 타원이 아니라 완전한 반구체 형태이다.
- 돔의 전체 면적과 무게를 계산하기 위한 Python 프로그램을 제작한다.

---

## 🎯 개발 목표

- 완전한 반구체 돔의 **겉면적**을 구한다.
- **sphere_area()** 함수를 작성한다.
- 함수는 다음의 파라미터를 입력받는다:
  - `diameter` : 돔의 지름 (단위: m)
  - `material` : 재질 (유리/알루미늄/탄소강), 기본값은 “유리”
  - `thickness` : 돔 두께 (단위: cm), 기본값은 1cm
- 지름과 재질은 **input()**으로 사용자에게 입력받도록 한다.

---

## 🧮 계산 공식

### 1. 반구체의 면적 (겉면적)

\[

A=2×π×r 

\]

- \( A \) = 돔의 겉면적 (㎡)
- \( r \) = 돔의 반지름 (m)

---

### 2. 돔의 체적 (두께 고려)

돔은 단순히 겉면적만 있는 것이 아니라 두께를 가진 “껍데기” 형태이므로, 다음과 같이 부피를 계산한다:



![image](https://github.com/user-attachments/assets/745d4af0-bf04-40d1-bbb3-2b970df77da6)


- \( R_{\text{outer}} \) = 바깥쪽 반지름 (cm)
- \( R_{\text{inner}} \) = 안쪽 반지름 (cm)

---

### 3. 무게 계산


![image](https://github.com/user-attachments/assets/58af2234-545f-4f02-959a-b0e256f4c4d4)


단, 화성의 중력을 반영하기 위해:


![image](https://github.com/user-attachments/assets/1f9e1504-e95f-4a38-baae-9aff8c267743)


---

## ⚙️ 재질별 밀도

| 재질      | 밀도 (g/cm³) |
|-----------|-------------:|
| 유리      |         2.4 |
| 알루미늄  |         2.7 |
| 탄소강    |        7.85 |

---

## 🔧 프로그램 동작

- `sphere_area()` 함수 실행 시:
  - 지름과 재질은 **input()**으로 받는다.
  - 두께 입력이 없으면 기본값 1cm로 처리한다.
- 면적과 무게 계산 후, **전역 변수**에 결과를 저장한다.

전역 변수 이름:
- material
- diameter
- thickness
- area
- weight

---

## 💻 출력 형식
재질 =⇒ 유리, 지름 =⇒ 10.0, 두께 =⇒ 1, 면적 =⇒ 314.159, 무게 =⇒ 1118.547 kg


- 모든 수치는 소수점 이하 셋째 자리까지만 출력한다.
- 무게는 화성 중력 기준으로 환산된 값이다.

---

## 💾 파일

- **design_dome.py**


