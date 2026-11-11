# 📘 Python 기초 학습 퀴즈 프로그램

## 1. 프로젝트 개요
이 프로젝트는 Python 기초, 클래스/객체, 파일 입출력, Git 기초 학습 내용을
복습할 수 있도록 만든 **콘솔 기반 퀴즈 프로그램**입니다.
사용자가 문제를 풀면 정답 여부를 판별하고, 점수와 진행 상태를
`state.json` 파일에 저장하여 다음 실행 시 이어서 풀 수 있도록 구성했습니다.

---

## 2. 퀴즈 주제와 선정 이유
- **주제**: [예: Python 기초 문법 퀴즈 / Git 명령어 퀴즈 등 본인 주제 작성]
- **선정 이유**:
  - 학습한 내용을 스스로 점검하기에 가장 효과적인 방법이 퀴즈라고 생각했습니다.
  - 변수, 조건문, 반복문, 클래스, 파일 입출력 등 수업에서 배운 개념을
    실제 프로그램으로 구현해보며 복습 효과를 얻을 수 있습니다.
  - JSON 파일로 상태를 저장하는 구조를 통해 파일 입출력도 함께 연습할 수 있습니다.

---

## 3. 실행 방법

### (1) 저장소 클론
```bash
git clone [https://github.com/kwonhyck0110/1-2.git]
cd [C:\1-2]
```

### (2) Python 실행 (Python 3.8 이상 권장)
```bash
python main.py
```

### (3) 진행 상태 초기화 (선택)
이전 기록을 지우고 처음부터 풀고 싶다면 `state.json` 파일을 삭제하세요.
```bash
rm state.json
```

---

## 4. 기능 목록
- ✅ 퀴즈 문제 출제 (객관식 / 단답형)
- ✅ 정답 여부 즉시 판별 및 피드백 제공
- ✅ 점수 집계 및 결과 출력
- ✅ 진행 상태 저장 (`state.json`) — 중단한 지점부터 이어 풀기 가능
- ✅ 잘못된 입력에 대한 예외 처리 (`try/except`)
- ✅ 퀴즈 데이터와 로직 분리 (클래스 기반 구조)

---

## 5. 파일 구조
```
project/
├── sc              # 실행 스크린샷
├── .gitignore      # Git이 추적하지 않았으면 하는 파일/폴더 목록"을 적어두는 설정 파일
├── 1-2_Quiz        # Quiz실행파일
├── README.md       # 프로젝트 설명 문서
└── state.json      # 사용자 진행 상태 (자동 생성)
```

---

## 6. 데이터 파일 설명

### 📁 `questions.json`
- **경로**: 프로젝트 루트 디렉터리 (`./questions.json`)
- **역할**: 퀴즈 문제 목록과 사용자의 최고 점수·플레이 기록을 저장합니다.
- **인코딩**: UTF-8

#### 전체 구조
```json
{
  "quizzes": [ ... ],
  "best_score": 0,
  "history": []
}
```

#### 최상위 필드
| 필드명 | 타입 | 설명 |
|--------|------|------|
| `quizzes` | list | 퀴즈 문제 객체들의 배열 |
| `best_score` | int | 사용자의 최고 점수 |
| `history` | list | 이전 플레이 기록 (점수/날짜 등) |

#### `quizzes` 배열 내부 객체 스키마
```json
{
  "question": "전기에서 저항을 나타내는 단위는?",
  "choices": ["볼트", "옴", "암페어", "와트"],
  "answer": 2
}
```

| 필드명 | 타입 | 설명 |
|--------|------|------|
| `question` | str | 출제할 문제 내용 |
| `choices` | list[str] | 4개의 보기 (객관식 선택지) |
| `answer` | int | 정답 번호 (**1부터 시작**, 1~4 사이의 값) |

> ⚠️ `answer`는 **0부터가 아닌 1부터** 시작하는 번호예요.
> 예: `choices`가 `["볼트", "옴", "암페어", "와트"]`이고 `answer`가 `2`이면 정답은 **"옴"** 입니다.

#### 퀴즈 주제
전기/반도체 분야의 기초 상식 문제 **총 6문항**으로 구성되어 있습니다.
(저항 단위, 전류 종류, 전기 소재, 관련 인물 등)

---

### 📁 `state.json`
- **경로**: 프로젝트 루트 디렉터리 (`./state.json`)
- **역할**: 현재 진행 중인 퀴즈의 상태(현재 문제 번호, 점수 등)를 저장합니다.
- **특징**: 개인 데이터이므로 `.gitignore`에 등록되어 Git에 올라가지 않습니다.

#### 스키마 예시
```json
{
  "current_index": 2,
  "score": 1
}
```

| 필드명 | 타입 | 설명 |
|--------|------|------|
| `current_index` | int | 현재 풀고 있는 문제의 인덱스 (0부터 시작) |
| `score` | int | 현재까지 맞힌 문제 수 |

---

##  학습 포인트 정리
이 프로젝트를 통해 아래 개념을 실제로 적용했습니다.

---


## 7. 학습 개념 정리 — Python 기초

이 프로젝트를 만들며 사용한 Python 기초 개념을 정리합니다.
각 개념이 실제 코드의 어떤 부분에서 쓰였는지 함께 설명합니다.

---

### 7-1. 변수 (Variable)

**변수**는 값을 저장해두고 이름으로 불러 쓰는 "상자"입니다.
같은 값을 여러 번 사용하거나, 값이 바뀔 때마다 코드 전체를 수정하지 않아도
되도록 하기 위해 사용합니다.

```python
score = 0           # 점수를 저장하는 변수
user_name = "지민"   # 사용자 이름을 저장하는 변수
```

> 💡 이 프로젝트에서는 사용자의 **점수**, **현재 문제 번호**, **정답 여부** 등을
> 변수에 저장해 관리합니다.

---

### 7-2. 자료형 (Data Type)

Python에서 자주 쓰는 5가지 자료형입니다.

| 자료형 | 설명 | 예시 | 프로젝트에서의 활용 |
|--------|------|------|---------------------|
| `int` | 정수 | `0`, `100`, `-5` | 점수, 문제 번호, 정답 인덱스 |
| `str` | 문자열 | `"안녕"`, `"옴"` | 문제 내용, 보기 텍스트 |
| `bool` | 참/거짓 | `True`, `False` | 정답 여부 판별 결과 |
| `list` | 순서 있는 목록 | `["볼트", "옴", "암페어"]` | 보기(`choices`), 기록(`history`) |
| `dict` | key-value 쌍 | `{"question": "...", "answer": 2}` | 하나의 퀴즈 문제 전체 |

#### 실제 적용 예시
```python
quiz = {
    "question": "전기에서 저항을 나타내는 단위는?",   # str
    "choices": ["볼트", "옴", "암페어", "와트"],      # list
    "answer": 2                                     # int
}
is_correct = True                                   # bool
```

> 💡 `questions.json` 전체 구조가 바로 **dict + list + str + int**의 조합이에요!

---

### 7-3. 조건문 (if / elif / else)

**조건에 따라 다른 동작**을 하도록 분기시키는 문법입니다.
"만약 ~라면 A를, 아니면 B를 해라" 같은 상황에서 사용합니다.

```python
user_answer = int(input("정답 번호를 입력하세요: "))

if user_answer == quiz["answer"]:
    print("✅ 정답입니다!")
    score += 1
elif user_answer < 1 or user_answer > 4:
    print("⚠️ 1~4 사이의 숫자를 입력하세요.")
else:
    print("❌ 틀렸습니다.")
```

- `if`: 첫 번째 조건을 확인
- `elif`: 위 조건이 거짓일 때 추가 조건 확인 (여러 개 가능)
- `else`: 위 모든 조건이 거짓일 때 실행

> 💡 이 프로젝트에서는 **정답/오답 판별**, **잘못된 입력 처리**, **최고 점수 갱신 여부** 등에
> 조건문을 사용합니다.

---

### 7-4. 반복문 (for / while)

같은 작업을 **여러 번 반복**할 때 사용합니다.

#### `for` 문 — 횟수나 목록이 정해져 있을 때
```python
for quiz in quizzes:          # quizzes 리스트의 각 문제를 하나씩 꺼냄
    print(quiz["question"])
    for i, choice in enumerate(quiz["choices"], start=1):
        print(f"{i}. {choice}")
```

#### `while` 문 — 조건이 참인 동안 계속 반복
```python
while True:
    user_input = input("정답 번호 (1~4): ")
    if user_input.isdigit() and 1 <= int(user_input) <= 4:
        break   # 올바른 입력이면 반복 종료
    print("다시 입력해주세요.")
```

| 구분 | 언제 사용? |
|------|------------|
| `for` | 반복 횟수나 대상(리스트 등)이 **명확히 정해진 경우** |
| `while` | 반복 횟수를 모르고, **특정 조건이 만족될 때까지** 반복해야 하는 경우 |

> 💡 이 프로젝트에서는 **문제를 하나씩 출제할 때 `for`**,
> **올바른 입력이 들어올 때까지 다시 묻는 상황에 `while`**을 사용할 수 있습니다.

---

### 7-5. 함수 (Function)

**함수**는 반복되는 코드를 묶어 이름을 붙여둔 "기능 블록"입니다.
한 번 정의하면 필요할 때마다 호출해서 재사용할 수 있어
코드가 짧아지고 읽기 쉬워집니다.

```python
def check_answer(user_input, correct_answer):
    """사용자 답과 정답을 비교해 True/False 반환"""
    return user_input == correct_answer

# 함수 호출
result = check_answer(2, quiz["answer"])
if result:
    print("정답!")
```

#### 함수의 핵심 요소
| 요소 | 설명 |
|------|------|
| `def` | 함수를 정의하는 키워드 |
| **매개변수(parameter)** | 함수에 전달하는 입력값 (`user_input`, `correct_answer`) |
| **반환값(return)** | 함수가 실행 후 돌려주는 결과값 |

> 💡 이 프로젝트에서는 **문제 출제**, **정답 확인**, **점수 저장**, **파일 불러오기** 등
> 각 역할을 함수로 나눠 구현하면 코드가 훨씬 깔끔해집니다.

---

### 📌 전체 흐름 요약

```
[변수]에 저장된 [자료형] 데이터를,
[반복문]으로 하나씩 꺼내 [조건문]으로 판별하고,
그 과정을 [함수]로 묶어 재사용한다.
```

이 5가지 개념이 서로 맞물려 하나의 퀴즈 프로그램이 완성됩니다! 🎯

---

## 📄 README에 추가할 "클래스와 객체" 섹션

## 8. 학습 개념 정리 — 클래스와 객체 (OOP 입문)

이 프로젝트의 퀴즈 기능을 **클래스**로 구조화하면서 배운 객체지향(OOP) 개념을 정리합니다.

---

### 8-1. 클래스(Class)란 무엇이고, 왜 사용하는가?

**클래스**는 **관련된 데이터(속성)와 기능(메서드)을 하나로 묶어둔 설계도**입니다.
그리고 이 설계도로 찍어낸 실제 결과물을 **객체(object) / 인스턴스(instance)** 라고 부릅니다.

> 🏭 비유: 클래스는 **붕어빵 틀**, 객체는 **그 틀로 구운 붕어빵** 🐟

#### 왜 사용하나요?
아래와 같이 변수가 흩어져 있다고 생각해보세요.

```python
# 😵 클래스 없이 — 데이터와 기능이 흩어짐
question = "전기에서 저항을 나타내는 단위는?"
choices = ["볼트", "옴", "암페어", "와트"]
answer = 2

def check(user_input, correct):
    return user_input == correct
```

문제가 늘어날수록 변수가 많아지고, 어떤 함수가 어떤 데이터와 짝인지 헷갈립니다.

```python
# 😎 클래스로 묶으면 — 데이터 + 기능이 한 덩어리
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check(self, user_input):
        return user_input == self.answer
```

#### 클래스의 장점
| 장점 | 설명 |
|------|------|
| **묶음 관리** | 관련 데이터와 기능이 한 곳에 모여 코드가 깔끔해짐 |
| **재사용성** | 같은 구조의 객체를 여러 개 쉽게 만들 수 있음 |
| **유지보수** | 수정할 때 클래스 한 곳만 고치면 전체가 반영됨 |
| **확장성** | 상속·다형성 등으로 기능을 확장하기 쉬움 |

> 💡 이 프로젝트에서는 **Quiz 클래스**로 문제 하나하나를 객체로 만들어 관리합니다.

---

### 8-2. `__init__` 메서드와 `self`의 역할

#### 🔹 `__init__` — 객체가 태어날 때 자동 호출되는 "생성자"

객체를 만들 때 **처음에 어떤 값으로 초기화할지** 정해주는 특별한 메서드입니다.
이름 앞뒤에 언더스코어가 2개(`__`)씩 붙어 있어 **"던더(dunder) 메서드"** 라고도 불러요.

```python
class Quiz:
    def __init__(self, question, choices, answer):
        # 객체가 생성될 때 자동으로 실행됨
        self.question = question
        self.choices = choices
        self.answer = answer

# 객체 생성 시 __init__이 호출됨
q1 = Quiz("저항 단위는?", ["볼트", "옴", "암페어", "와트"], 2)
```

#### 🔹 `self` — "이 객체 자신"을 가리키는 이름

메서드의 첫 번째 매개변수는 항상 `self`입니다.
이는 **"지금 이 메서드를 호출한 바로 그 객체"** 를 가리킵니다.

```python
q1 = Quiz("저항 단위는?", ["볼트", "옴", "암페어", "와트"], 2)
q2 = Quiz("앤비디아 창업자는?", ["리사 수", "이재용", "젠슨 황", "스티브 잡스"], 3)

q1.check(2)   # 이때 self = q1  → q1.answer(2)와 비교
q2.check(1)   # 이때 self = q2  → q2.answer(3)와 비교
```

> 💡 `self` 덕분에 **같은 클래스에서 만들어진 여러 객체가 각자의 데이터를 따로** 가질 수 있어요.
> `q1`과 `q2`는 같은 Quiz 클래스지만, 서로 다른 문제/정답을 가지고 있죠!

#### 자주 하는 실수 ⚠️
```python
class Quiz:
    def __init__(question, choices, answer):   # ❌ self 빠짐!
        ...
    def check(user_input):                     # ❌ self 빠짐!
        ...
```
→ 메서드의 **첫 매개변수는 반드시 `self`** 를 써야 합니다.

---

### 8-3. 속성(Attribute)과 메서드(Method)

클래스 안의 두 가지 구성 요소를 구분해봅시다.

| 구분 | 역할 | 예시 |
|------|------|------|
| **속성(Attribute)** | 객체가 가진 **데이터** (명사) | `self.question`, `self.answer` |
| **메서드(Method)** | 객체가 할 수 있는 **동작** (동사) | `check()`, `display()` |

#### 전체 예시 — Quiz 클래스 완성본

```python
class Quiz:
    def __init__(self, question, choices, answer):
        # 🔹 속성(Attribute): 이 문제가 가진 데이터
        self.question = question   # 문제 내용
        self.choices = choices     # 보기 목록
        self.answer = answer       # 정답 번호

    # 🔹 메서드(Method): 이 문제가 할 수 있는 동작
    def display(self):
        """문제와 보기를 화면에 출력"""
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def check(self, user_input):
        """사용자 답이 맞는지 확인"""
        return user_input == self.answer
```

#### 사용 예시

```python
# 1️⃣ 객체 생성 (붕어빵 굽기)
q1 = Quiz(
    question="전기에서 저항을 나타내는 단위는?",
    choices=["볼트", "옴", "암페어", "와트"],
    answer=2
)

# 2️⃣ 속성 접근 — 점(.)으로 데이터 꺼내기
print(q1.question)   # "전기에서 저항을 나타내는 단위는?"
print(q1.choices)    # ["볼트", "옴", "암페어", "와트"]

# 3️⃣ 메서드 호출 — 점(.)으로 기능 실행
q1.display()
result = q1.check(2)   # True
print("정답!" if result else "오답!")
```

> 💡 **속성은 `.변수명`으로 꺼내 쓰고, 메서드는 `.함수명()`으로 실행합니다.**

---

### 8-4. 프로젝트에서의 활용 흐름

`questions.json`의 데이터를 **Quiz 객체 리스트**로 만들어 관리하면 아주 깔끔해져요.

```python
import json

# JSON에서 데이터 읽기
with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# dict → Quiz 객체로 변환
quizzes = [Quiz(q["question"], q["choices"], q["answer"]) for q in data["quizzes"]]

# 모든 문제를 반복문으로 출제
score = 0
for quiz in quizzes:
    quiz.display()                          # 메서드로 문제 출력
    user_input = int(input("답: "))
    if quiz.check(user_input):              # 메서드로 정답 확인
        score += 1

print(f"최종 점수: {score} / {len(quizzes)}")
```

---

### 📌 핵심 요약

```
[클래스] = 데이터(속성) + 기능(메서드)를 묶은 설계도
[객체]   = 클래스로 찍어낸 실제 인스턴스
[__init__] = 객체가 태어날 때 속성을 초기화하는 생성자
[self]     = "이 객체 자신"을 가리키는 특별한 이름
```

| 개념 | 한 줄 설명 |
|------|------------|
| 클래스 | 붕어빵 **틀** |
| 객체 | 틀로 구운 **붕어빵** |
| `__init__` | 붕어빵을 처음 구울 때의 **반죽 레시피** |
| `self` | **지금 이 붕어빵** 자신 |
| 속성 | 붕어빵의 **팥 / 슈크림** (데이터) |
| 메서드 | 붕어빵이 할 수 있는 **"먹히기", "데워지기"** (동작) |

클래스는 처음엔 낯설지만, 한 번 익숙해지면 코드 구조가 훨씬 깔끔해지는 걸 느끼게 될 거예요! 🎯




## 9. 학습 개념 정리 — 파일 입출력과 JSON

프로그램을 종료하면 변수에 저장된 값은 모두 사라집니다. 😢
**다음에 실행해도 데이터를 남겨두려면 "파일"에 저장**해야 하는데,
이때 사용하는 Python 기초 개념들을 정리합니다.

---

### 9-1. 파일 열기 / 읽기 / 쓰기

Python은 `open()` 함수로 파일을 열고, 작업이 끝나면 **반드시 닫아야** 합니다.
가장 안전하고 권장되는 방법은 `with` 문을 사용하는 것입니다.

#### 🔹 기본 문법
```python
with open("파일경로", "모드", encoding="utf-8") as 변수:
    # 파일 작업 수행
    ...
# with 블록이 끝나면 파일이 자동으로 닫힘 ✅
```

#### 🔹 주요 모드(mode)
| 모드 | 의미 | 특징 |
|------|------|------|
| `"r"` | **읽기(read)** | 파일이 없으면 오류 발생 |
| `"w"` | **쓰기(write)** | 파일을 **새로 만들거나 기존 내용 덮어씀** ⚠️ |
| `"a"` | **추가(append)** | 기존 내용 뒤에 **이어서** 작성 |

> 💡 `encoding="utf-8"`은 **한글이 깨지지 않게** 하기 위해 꼭 넣어주세요!

#### 🔹 파일 읽기 예시
```python
# questions.json 파일 전체 내용을 문자열로 읽기
with open("questions.json", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

#### 🔹 파일 쓰기 예시
```python
# 점수를 파일에 저장 (기존 내용은 사라짐)
with open("state.txt", "w", encoding="utf-8") as f:
    f.write("최고 점수: 5\n")
```

#### 🔹 `with`를 쓰는 이유
```python
# ❌ 옛날 방식 — 닫는 걸 깜빡하면 파일이 손상될 수 있음
f = open("questions.json", "r", encoding="utf-8")
content = f.read()
f.close()   # 이걸 빼먹기 쉬움!

# ✅ with 방식 — 자동으로 닫아주니 안전
with open("questions.json", "r", encoding="utf-8") as f:
    content = f.read()
```

---

### 9-2. JSON 형식이란?

**JSON(JavaScript Object Notation)** 은 **데이터를 사람과 컴퓨터가
모두 읽기 쉬운 형태로 저장하는 텍스트 형식**입니다.

#### 🔹 생긴 모습 (우리 프로젝트 예시)
```json
{
  "quizzes": [
    {
      "question": "전기에서 저항을 나타내는 단위는?",
      "choices": ["볼트", "옴", "암페어", "와트"],
      "answer": 2
    }
  ],
  "best_score": 0,
  "history": []
}
```

#### 🔹 왜 JSON을 사용할까요?

| 이유 | 설명 |
|------|------|
| **가독성** | 중괄호·대괄호 구조가 명확해 사람이 바로 읽을 수 있음 |
| **Python 호환성** | `dict`·`list`·`str`·`int`·`bool` 자료형과 **구조가 거의 똑같음** |
| **범용성** | 거의 모든 프로그래밍 언어가 JSON을 지원함 |
| **가벼움** | 텍스트 기반이라 파일 크기가 작고 전송이 빠름 |

#### 🔹 JSON ↔ Python 자료형 매칭
| JSON | Python |
|------|--------|
| `object` `{}` | `dict` |
| `array` `[]` | `list` |
| `string` `"..."` | `str` |
| `number` | `int`, `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

> 💡 JSON의 중괄호·대괄호를 보면 Python의 dict·list와 거의 1:1로 대응돼요!

#### 🔹 Python에서 JSON 다루기 — `json` 모듈

```python
import json

# 📥 JSON 파일 → Python dict/list로 읽기 (load)
with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["quizzes"][0]["question"])   # 첫 번째 문제 출력
print(data["best_score"])               # 0

# 📤 Python dict/list → JSON 파일로 저장 (dump)
data["best_score"] = 5
data["history"].append({"score": 5, "date": "2025-01-15"})

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

| 함수 | 역할 |
|------|------|
| `json.load(f)` | 파일에서 읽어 **Python 객체로 변환** |
| `json.dump(data, f)` | Python 객체를 **JSON 문자열로 변환해 파일에 저장** |

> ⚠️ 옵션 꿀팁
> - `ensure_ascii=False` → **한글이 `\uXXXX`로 깨지지 않게** 그대로 저장
> - `indent=2` → **들여쓰기 2칸**으로 보기 좋게 저장

---

### 9-3. try / except — 오류 처리

프로그램 실행 중 **예상치 못한 오류(예외, Exception)** 가 발생하면
프로그램이 즉시 멈춰버립니다. 이를 미리 대비하는 문법이 `try/except`예요.

#### 🔹 기본 문법
```python
try:
    # 오류가 발생할 수 있는 코드
    ...
except 오류종류:
    # 오류 발생 시 대신 실행할 코드
    ...
```

#### 🔹 왜 필요할까요? (오류 없는 코드 vs 있는 코드)

```python
# ❌ 오류 처리 없음 — 파일이 없으면 프로그램이 즉시 종료됨
with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)
# FileNotFoundError: [Errno 2] No such file or directory: 'questions.json'
```

```python
# ✅ 오류 처리 — 파일이 없어도 프로그램이 계속 실행됨
try:
    with open("questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("⚠️ 문제 파일이 없습니다. 기본값으로 시작합니다.")
    data = {"quizzes": [], "best_score": 0, "history": []}
```

#### 🔹 자주 만나는 예외 종류
| 예외 이름 | 언제 발생? |
|-----------|-----------|
| `FileNotFoundError` | 파일이 존재하지 않을 때 |
| `json.JSONDecodeError` | JSON 형식이 잘못됐을 때 |
| `KeyError` | dict에 없는 key로 접근할 때 |
| `ValueError` | 문자열을 숫자로 변환 실패 등 |
| `ZeroDivisionError` | 0으로 나누기를 시도할 때 |

#### 🔹 여러 예외를 한꺼번에 처리

```python
try:
    with open("questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("⚠️ 파일이 없어요.")
except json.JSONDecodeError:
    print("⚠️ JSON 형식이 잘못됐어요.")
except Exception as e:
    print(f"⚠️ 알 수 없는 오류: {e}")
```

> 💡 `except Exception as e`는 **"그 외 모든 오류"** 를 잡는 안전장치예요.
> 변수 `e`에 오류 메시지가 담겨, 디버깅할 때 유용합니다.

#### 🔹 사용자 입력 처리 예시

```python
try:
    user_input = int(input("정답 번호 (1~4): "))
    if user_input < 1 or user_input > 4:
        print("⚠️ 1~4 사이 숫자만 입력하세요.")
except ValueError:
    print("⚠️ 숫자만 입력할 수 있어요.")
```

---

### 9-4. 프로젝트에서의 전체 활용 흐름

```python
import json

# 1️⃣ 파일 읽기 (오류 처리 포함)
try:
    with open("questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("문제 파일이 없습니다. 프로그램을 종료합니다.")
    exit()

# 2️⃣ 퀴즈 진행
score = 0
for quiz in data["quizzes"]:
    print(quiz["question"])
    for i, c in enumerate(quiz["choices"], start=1):
        print(f"  {i}. {c}")
    
    try:
        user_input = int(input("답: "))
        if user_input == quiz["answer"]:
            score += 1
    except ValueError:
        print("숫자만 입력하세요. 이 문제는 틀린 것으로 처리됩니다.")

# 3️⃣ 최고 점수 갱신 후 파일에 쓰기
if score > data["best_score"]:
    data["best_score"] = score
    print(f"🎉 신기록 달성! {score}점")

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"최종 점수: {score}점 (최고: {data['best_score']}점)")
```

---

### 📌 핵심 요약

```
[파일 I/O]  → 프로그램이 꺼져도 데이터를 남기는 방법
[JSON]     → 사람·컴퓨터 모두 읽기 쉬운 데이터 저장 형식
[try/except] → 예상치 못한 오류에도 프로그램이 멈추지 않게 하는 안전장치
```

| 개념 | 한 줄 요약 |
|------|-----------|
| `open() / with` | 파일을 **안전하게 열고 자동으로 닫기** |
| 모드 `r/w/a` | **읽기 / 덮어쓰기 / 이어쓰기** |
| `json.load` | 파일 → **Python 객체**로 변환 |
| `json.dump` | Python 객체 → **파일에 저장** |
| `try/except` | 오류가 나도 **프로그램을 멈추지 않음** |

이제 우리 프로그램은 **데이터를 저장하고, 안전하게 오류를 처리하는** 진짜 프로그램이 됐어요! 🎯


## 10. 학습 개념 정리 — Git 기초

이 프로젝트를 GitHub에 올리고 버전을 관리하면서 배운 Git 개념을 정리합니다.

---

### 10-1. Git이란 무엇이고, 왜 필요한가?

**Git**은 **코드의 변경 이력을 기록하고 관리하는 버전 관리 시스템(VCS)** 입니다.
간단히 말해 **"코드 전용 타임머신 + 협업 도구"** 예요. ⏰

#### 🔹 Git이 없다면?
```
📁 project/
  ├── quiz_v1.py
  ├── quiz_v2.py
  ├── quiz_v2_수정.py
  ├── quiz_최종.py
  ├── quiz_최종_진짜최종.py
  └── quiz_최종_진짜진짜마지막.py   😵
```

#### 🔹 Git이 있다면?
```
📁 project/
  └── quiz.py   ← 파일은 하나!
      (내부에 모든 변경 이력이 기록됨)
```

#### 🔹 Git의 핵심 이점

| 이점 | 설명 |
|------|------|
| **이력 관리** | 언제, 누가, 무엇을 바꿨는지 모두 기록 |
| **복구 가능** | 실수해도 **과거 시점으로 되돌릴 수 있음** |
| **협업** | 여러 명이 **동시에 작업**하고 합칠 수 있음 |
| **백업** | GitHub 같은 원격 저장소에 올려두면 **데이터 손실 걱정 없음** |
| **실험** | 브랜치로 **메인 코드에 영향 없이 새 기능 테스트** 가능 |

> 💡 **Git**은 버전 관리 **도구**, **GitHub**은 Git 저장소를 올려두는 **온라인 서비스**예요. (헷갈리기 쉬움!)

---

### 10-2. Git의 3가지 영역 이해하기

명령어를 배우기 전에, Git이 파일을 어떻게 관리하는지 먼저 알아야 해요.

```
[작업 디렉토리] ──add──▶ [스테이징 영역] ──commit──▶ [로컬 저장소] ──push──▶ [원격 저장소]
  (코드 수정)              (커밋 대기)              (버전 저장)             (GitHub)
```

| 영역 | 설명 |
|------|------|
| **작업 디렉토리(Working Directory)** | 지금 코드를 수정하고 있는 폴더 |
| **스테이징 영역(Staging Area)** | 커밋할 파일을 **골라 담는 바구니** |
| **로컬 저장소(Local Repository)** | 내 컴퓨터에 **버전 이력이 저장되는 곳** |
| **원격 저장소(Remote Repository)** | GitHub 같은 **인터넷상의 저장소** |

---

### 10-3. 핵심 명령어 7가지

#### 🔹 `git init` — 저장소 만들기
현재 폴더를 **Git으로 관리하기 시작**합니다. (`.git` 숨김 폴더가 생성됨)
```bash
cd my-project
git init
```
> 💡 프로젝트 시작 시 **딱 한 번만** 실행합니다.

---

#### 🔹 `git add` — 스테이징 영역에 올리기
수정한 파일 중 **커밋할 파일을 골라 바구니에 담습니다**.
```bash
git add quiz.py           # 특정 파일만
git add .                 # 수정된 모든 파일
```

---

#### 🔹 `git commit` — 버전 저장(스냅샷 찍기)
스테이징 영역의 파일들을 **하나의 버전으로 기록**합니다.
```bash
git commit -m "퀴즈 정답 확인 기능 추가"
```
> 💡 **커밋 메시지**는 "무엇을/왜 바꿨는지" 미래의 내가 알 수 있도록 명확히 작성!

---

#### 🔹 `git push` — 원격 저장소로 올리기
로컬 커밋을 **GitHub에 업로드**합니다.
```bash
git push origin main
```
- `origin`: 원격 저장소의 기본 별칭
- `main`: 올릴 브랜치 이름

---

#### 🔹 `git pull` — 원격 저장소에서 가져오기
GitHub의 최신 변경사항을 **내 컴퓨터로 내려받고 병합**합니다.
```bash
git pull origin main
```
> 💡 **협업 시 작업 시작 전에 항상 `pull`** 부터 하는 습관을 들이세요!

---

#### 🔹 `git checkout` — 브랜치/시점 이동
다른 **브랜치로 이동**하거나 **과거 커밋으로 돌아갈 때** 사용합니다.
```bash
git checkout main              # main 브랜치로 이동
git checkout feature/login     # feature/login 브랜치로 이동
git checkout -b new-feature    # 새 브랜치를 만들며 이동 (-b = branch)
```
> 💡 최신 Git에서는 `git switch`(브랜치 이동), `git restore`(파일 복원)로 역할을 나누기도 해요.

---

#### 🔹 `git clone` — 원격 저장소 복제
GitHub의 저장소를 **내 컴퓨터에 통째로 내려받습니다**.
```bash
git clone https://github.com/사용자명/저장소명.git
```
> 💡 `init`은 새 프로젝트 시작용, `clone`은 기존 프로젝트를 가져올 때 사용!

---

#### 📋 명령어 한눈에 보기

| 명령어 | 역할 | 언제 사용? |
|--------|------|-----------|
| `git init` | 저장소 생성 | 새 프로젝트 시작 시 |
| `git add` | 스테이징에 올림 | 파일 수정 후 |
| `git commit` | 버전 저장 | 작업 단위 완료 시 |
| `git push` | 원격에 업로드 | 커밋 후 공유할 때 |
| `git pull` | 원격에서 다운로드 | 작업 시작 전 |
| `git checkout` | 브랜치/시점 이동 | 다른 작업으로 전환 시 |
| `git clone` | 저장소 복제 | 기존 프로젝트 받을 때 |

---

### 10-4. 브랜치(Branch) — 평행우주 만들기

**브랜치**는 **메인 코드에 영향을 주지 않고 따로 작업할 수 있는 독립된 공간**입니다.

```
main       ●────●────●─────────●────▶
                 \              /
feature           ●────●────●──
                 (새 기능 개발)
```

#### 🔹 왜 브랜치를 쓸까요?

| 상황 | 브랜치의 장점 |
|------|---------------|
| 새 기능 개발 | main은 **안정 상태 유지**, 실험은 브랜치에서 |
| 버그 수정 | 수정용 브랜치를 만들어 **안전하게 해결** |
| 협업 | 각자 **자기 브랜치**에서 작업 후 합치기 |

#### 🔹 브랜치 기본 사용법

```bash
# 1️⃣ 현재 브랜치 확인
git branch

# 2️⃣ 새 브랜치 생성
git branch feature/score-save

# 3️⃣ 브랜치로 이동
git checkout feature/score-save

# 💡 2+3을 한 번에 — 자주 쓰는 방법
git checkout -b feature/score-save
```

#### 🔹 브랜치에서 작업 후 병합(merge)

```bash
# 1️⃣ feature 브랜치에서 작업 + 커밋
git add .
git commit -m "점수 저장 기능 추가"

# 2️⃣ 합칠 대상인 main 브랜치로 이동
git checkout main

# 3️⃣ feature 브랜치를 main으로 병합
git merge feature/score-save

# 4️⃣ 더 이상 필요 없으면 브랜치 삭제
git branch -d feature/score-save
```

> 💡 **병합 충돌(Merge Conflict)** 이 일어나면, 충돌 부분을 직접 수정 후
> `git add` → `git commit`으로 마무리하면 됩니다.

---

### 10-5. 원격 저장소와 함께 쓰기 (clone + pull)

협업 시 가장 많이 쓰는 흐름이에요!

#### 🔹 처음 프로젝트를 받을 때 — `clone`

```bash
# GitHub 저장소를 내 컴퓨터로 복제
git clone https://github.com/사용자명/quiz-project.git

# 복제된 폴더로 이동
cd quiz-project
```
> 💡 `clone`은 **한 번만** 하면 돼요. 이후엔 `pull`로 업데이트합니다.

#### 🔹 작업 시작 전 — `pull`로 최신 상태 유지

```bash
# 작업 시작 전에 항상!
git pull origin main
```

#### 🔹 전체 협업 흐름 요약

```
1. git clone      → 처음 한 번만, 저장소 복제
2. git pull       → 작업 시작 전, 최신 코드 받기
3. 코드 수정
4. git add .      → 변경 파일 스테이징
5. git commit -m "..." → 버전 저장
6. git push       → 원격 저장소에 공유
```

---

### 10-6. 이 프로젝트의 실제 Git 사용 예시

```bash
# 🏁 1. 프로젝트 시작
git init
git add .
git commit -m "초기 커밋: 퀴즈 프로그램 기본 구조"

# 🌐 2. GitHub 원격 저장소 연결
git remote add origin https://github.com/myname/quiz-project.git
git push -u origin main

# 🌿 3. 새 기능은 브랜치에서 작업
git checkout -b feature/best-score
# ... 최고 점수 기능 개발 ...
git add .
git commit -m "최고 점수 저장 기능 추가"

# 🔀 4. main에 병합 후 원격에 올리기
git checkout main
git merge feature/best-score
git push origin main

# 🤝 5. 다른 사람과 협업 중이라면
git pull origin main   # 작업 전 최신화
```

---

### 📌 핵심 요약

```
[Git]     = 코드의 타임머신 + 협업 도구
[브랜치]   = 메인에 영향 없이 실험할 수 있는 평행우주
[원격저장소] = GitHub 같은 온라인 공유 공간
```

| 상황 | 명령어 |
|------|--------|
| 새 프로젝트 시작 | `git init` |
| 기존 프로젝트 받기 | `git clone` |
| 변경사항 저장하기 | `add` → `commit` → `push` |
| 최신 상태로 맞추기 | `git pull` |
| 새 기능 개발 | `checkout -b` → 작업 → `merge` |

Git을 익히면 **혼자서도 안전하게**, **여럿이서도 효율적**
---

## end. 작성자
- 이름: [권혁]
- 작성일: [2026-11-11]