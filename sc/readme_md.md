# 📘 전기·반도체 기초 상식 퀴즈 프로그램

## 1. 프로젝트 개요

이 프로젝트는 Python 기초 문법(변수, 자료형, 제어문, 함수), 객체지향 설계(클래스와 객체), 파일 입출력(JSON), 그리고 Git 버전 관리 개념을 학습하고 복습하기 위해 개발한 **콘솔 기반 대화형 퀴즈 프로그램**입니다.

사용자는 등록된 문제를 무작위 순서로 풀며 실시간으로 정답 여부를 확인하고, 새로운 퀴즈를 추가하거나 불필요한 문제를 삭제할 수 있습니다. 또한 모든 문제 데이터와 최고 점수, 플레이 히스토리는 프로젝트 루트의 `state.json` 파일에 안전하게 저장되어 프로그램을 종료한 뒤 재실행해도 데이터가 그대로 유지됩니다.

---

## 2. 퀴즈 주제와 선정 이유

* **주제**: 전기 및 반도체 공학 기초 상식 퀴즈
* **선정 이유**:
  * **전공 지식 활용**: 전기 및 반도체 공학의 핵심 기초 개념(단위, 전류 종류, 소재)과 주요 과학자·인물의 업적을 퀴즈 형태로 구성하여 전공 기초를 자연스럽게 복습하고자 했습니다.
  * **실전 프로그래밍 구조 체득**: 퀴즈 문제를 `Quiz` 객체로 모델링하고, 게임 전체 흐름과 JSON 파일 입출력을 `QuizGame` 클래스로 분리하여 유지보수가 용이한 객체지향 구조를 직접 구현해 보았습니다.

---

## 3. 실행 방법

### (1) 저장소 복제 (Clone)
```bash
git clone https://github.com/kwonhyck0110/1-2.git
cd 1-2
```

### (2) 프로그램 실행 (Python 3.8 이상 권장)
프로젝트 루트 경로에서 아래 명령어를 입력해 실행합니다.
```bash
python 1-2_Quiz.py
```

### (3) 데이터 초기화 (선택 사항)
저장된 퀴즈 목록과 점수 기록을 초기화하고 기본 6문항으로 다시 시작하려면 `state.json` 파일을 삭제한 뒤 실행하세요.
```bash
rm state.json
```

---

## 4. 주요 기능 목록

1. **🎲 퀴즈 풀기 (무작위 출제)**: `random.shuffle()`을 사용해 등록된 문제를 매번 다른 순서로 출제하고, 즉시 정답 판별 및 점수를 계산합니다.
2. **➕ 퀴즈 추가**: 사용자가 직접 문제, 4개의 선택지, 정답 번호(1~4)를 입력하여 새로운 퀴즈를 등록합니다.
3. **📋 퀴즈 목록 보기**: 현재 저장되어 있는 전체 퀴즈의 문제, 보기, 정답 번호를 한눈에 조회합니다.
4. **🏆 최고 점수 확인**: 역대 플레이에서 달성한 최고 점수를 확인합니다.
5. **📜 점수 기록 히스토리 보기**: `datetime` 모듈을 활용해 게임을 완료한 날짜·시간, 총 문제 수, 맞힌 개수를 누적 기록하고 조회합니다.
6. **🗑️ 퀴즈 삭제**: 목록에서 번호를 선택해 기존 퀴즈를 삭제하고 파일에 즉시 반영합니다.
7. **💾 안전한 파일 입출력 및 예외 복구**: UTF-8 인코딩으로 한글 깨짐 없이 데이터를 저장하며, 파일 권한 오류(`PermissionError`) 및 파일 손상(`JSONDecodeError`) 시 자동 백업(`state.json.bak`) 후 기본 데이터로 복구합니다.

---

## 5. 파일 구조

```text
1-2/
├── sc/               # 실행 결과 및 Git 워크플로우 증빙 스크린샷 폴더
├── .gitignore        # Git 버전 관리에서 제외할 파일(state.json 등) 설정 파일
├── 1-2_Quiz.py       # 퀴즈 게임 메인 실행 파일 (Quiz, QuizGame 클래스 포함)
├── README.md         # 프로젝트 설명 및 핵심 개념 정리 문서
├── state.json        # 퀴즈 목록, 최고 점수, 플레이 히스토리 저장 파일 (자동 생성)
└── state.json.bak    # state.json 손상 감지 시 자동 생성되는 백업 파일
```

---

## 6. 데이터 파일 설명 (`state.json`)

* **경로**: 프로젝트 루트 디렉터리 (`./state.json`)
* **인코딩**: UTF-8 (`ensure_ascii=False` 적용으로 한글 원문 유지)
* **역할**: 최초 실행 시 기본 제공되는 6문항(저항 단위, 엔비디아 창업자, 교류 개념, 맥스웰, 반도체, 구리)과 사용자가 추가·삭제한 퀴즈 목록, 최고 점수, 날짜별 히스토리를 영구 저장합니다.

### 전체 JSON 구조
```json
{
  "quizzes": [
    {
      "question": "전기에서 저항을 나타내는 단위는?",
      "choices": ["볼트", "옴", "암페어", "와트"],
      "answer": 2
    }
  ],
  "best_score": 6,
  "history": [
    {
      "date": "2026-11-11 12:00:00",
      "total": 6,
      "score": 6
    }
  ]
}
```

### 최상위 필드 명세
| 필드명 | 자료형 | 설명 |
| :--- | :--- | :--- |
| `quizzes` | `list[dict]` | 등록된 개별 퀴즈 데이터 객체들의 목록 |
| `best_score` | `int` | 사용자가 기록한 역대 최고 점수 |
| `history` | `list[dict]` | 플레이 일시(`date`), 총 문항 수(`total`), 득점(`score`) 기록 목록 |

### `quizzes` 내부 객체 명세
| 필드명 | 자료형 | 설명 |
| :--- | :--- | :--- |
| `question` | `str` | 출제할 문제 내용 |
| `choices` | `list[str]` | 4개의 객관식 선택지 목록 |
| `answer` | `int` | 정답 번호 (**1부터 시작**, 1~4 사이의 정수) |

> 💡 **참고**: 배열 인덱스(0~3)와 달리 사용자 직관성을 위해 `answer`는 **1번부터 4번** 기준으로 저장됩니다. 예를 들어 `choices`가 `["볼트", "옴", "암페어", "와트"]`이고 `answer`가 `2`라면 정답은 "옴"입니다.

---

## 7. 핵심 개념 정리 및 실제 코드 적용 설명

이 프로젝트를 개발하면서 배운 Python, 객체지향, 파일 입출력, Git의 핵심 개념들이 **실제 작성한 코드에서 어떻게 동작하는지** 직접 인용하여 설명합니다.

### 7-1. Python 기초 문법

#### 🔹 변수 (Variable)
변수는 프로그램 실행 중 필요한 데이터를 메모리에 담아두고 이름으로 재사용하거나 상태 변화를 추적하기 위해 사용합니다.
* **내 코드에서의 활용 (`play_quiz` 및 상수 선언)**:
```python
STATE_FILE = "state.json"
BACKUP_FILE = "state.json.bak"

score = 0
total = len(play_quizzes)
```
> 파일 경로를 상수 변수(`STATE_FILE`)로 관리해 오타를 줄이고, 게임 중 맞힌 개수(`score`)와 전체 문항 수(`total`)를 변수에 담아 실시간으로 점수를 집계했습니다.

#### 🔹 주요 자료형 (`int`, `str`, `bool`, `list`, `dict`)
| 자료형 | 설명 | 내 코드에서의 실제 사용 예시 |
| :--- | :--- | :--- |
| **`int`** | 정수 데이터 | `self.best_score = 0`, 정답 번호 `2` |
| **`str`** | 문자열 데이터 | `now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")`, 문제 지문 |
| **`bool`** | 참(`True`)/거짓(`False`) 논리값 | `return user_answer == self.answer` (`is_correct`의 반환값) |
| **`list`** | 순서가 있고 수정 가능한 목록 | `self.quizzes = []`, `choices = ["볼트", "옴", "암페어", "와트"]` |
| **`dict`** | `Key: Value` 쌍으로 구조화된 데이터 | `record = {"date": now_str, "total": total, "score": score}` |

#### 🔹 조건문 (`if` / `elif` / `else`)
조건식의 참·거짓 여부에 따라 프로그램의 실행 흐름을 분기합니다.
* **내 코드에서의 활용 (`run` 메뉴 분기 및 `play_quiz` 채점)**:
```python
# 1) 메뉴 선택에 따른 다중 분기 (run)
if choice == 1:
    self.play_quiz()
elif choice == 2:
    self.add_quiz()
elif choice == 3:
    self.list_quizzes()
elif choice == 4:
    self.show_best_score()
elif choice == 5:
    self.show_history()
elif choice == 6:
    self.delete_quiz()
elif choice == 7:
    print("프로그램을 종료합니다. 안녕히 가세요!")
    self.save()
    break

# 2) 정답 판별 및 최고 점수 갱신 (play_quiz)
if quiz.is_correct(user_ans):
    print("정답입니다! 🎉")
    score += 1
else:
    print(f"오답입니다. 정답은 {quiz.answer}번 이었어요.")
```

#### 🔹 반복문 (`for` vs `while`)
* **`for` 문**: 리스트나 범위처럼 **반복할 대상이 정해져 있을 때** 사용합니다.
```python
# 등록된 문제 수만큼 순회하며 문제 출력 (play_quiz)
for i, quiz in enumerate(play_quizzes, start=1):
    quiz.show(index=i)
    user_ans = self.read_int("정답 번호 입력 (1~4): ", 1, 4)
```
* **`while` 문**: 종료 조건이 만족될 때까지 **횟수 제한 없이 계속 반복해야 할 때** 사용합니다.
```python
# 올바른 범위의 정수가 입력될 때까지 무한 반복 검증 (read_int)
while True:
    raw = input(prompt).strip()
    if not raw:
        print("빈 입력입니다. 다시 입력해주세요.")
        continue
    ...
    return val
```

#### 🔹 함수 (Function) — 매개변수와 반환값 활용
반복되는 로직을 `def`로 묶어 매개변수(Parameter)로 입력을 받고 `return`으로 결과를 돌려주어 코드 중복을 없앴습니다.
* **내 코드에서의 활용 (`read_int`, `is_correct`)**:
```python
# 매개변수(prompt, min_v, max_v)를 받아 검증 후 정수(val)를 반환(return)
def read_int(self, prompt, min_v, max_v):
    """정수 범위를 검증하는 입력 함수"""
    while True:
        ...
        if val < min_v or val > max_v:
            print(f"{min_v}~{max_v} 사이의 숫자를 입력해주세요.")
            continue
        return val
```
> 이 함수 하나를 만들어 둔 덕분에 메뉴 선택(`1~7`), 정답 입력(`1~4`), 퀴즈 삭제 번호(`1~len(self.quizzes)`) 등 모든 숫자 입력에서 재사용할 수 있었습니다.

---

### 7-2. 클래스와 객체 (객체지향 설계)

#### 🔹 클래스 분리 설계 (`Quiz` vs `QuizGame`)
데이터와 기능을 하나의 설계도로 묶기 위해 책임을 두 클래스로 명확히 분리했습니다.

1. **`Quiz` 클래스**: 개별 퀴즈 1개의 데이터(속성)와 문제 출력·정답 판별·딕셔너리 변환(메서드)을 담당합니다.
```python
class Quiz:
    """개별 퀴즈를 표현하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question  # 속성(Attribute)
        self.choices = choices
        self.answer = answer

    def is_correct(self, user_answer):  # 메서드(Method)
        """정답 여부 판별"""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 변환용 dict"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }
```

2. **`QuizGame` 클래스**: 게임 전체의 상태 관리, 파일 입출력(`load`, `save`), 메뉴 흐름(`run`), 히스토리 및 퀴즈 추가/삭제를 총괄합니다.
```python
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.history = []  # 점수 히스토리 리스트 추가
        self.load()        # 객체 생성 시 자동으로 기존 데이터 로드
```

#### 🔹 `__init__` 메서드와 `self`의 역할
* **`__init__`**: 객체가 생성될 때 자동 실행되는 생성자로, `Quiz`에서는 문제·보기·정답을 초기화하고 `QuizGame`에서는 게임 상태 리스트를 초기화한 뒤 `self.load()`를 호출합니다.
* **`self`**: 메서드를 호출한 **객체 자기 자신**을 가리킵니다. 예를 들어 `quiz.is_correct(user_ans)`가 호출될 때 `self.answer`는 현재 출제 중인 바로 그 `quiz` 객체의 정답 번호를 참조합니다.

---

### 7-3. 파일 입출력과 예외 처리

#### 🔹 안전한 파일 읽기·쓰기 (`with open` & JSON)
`with open(..., encoding="utf-8")` 구문을 사용해 작업이 끝나면 파일이 자동으로 닫히도록 하고, `ensure_ascii=False` 옵션으로 한글이 깨지지 않고 그대로 `state.json`에 기록되도록 구현했습니다.

```python
# 저장 로직 (save)
data = {
    "quizzes": [q.to_dict() for q in self.quizzes],
    "best_score": self.best_score,
    "history": getattr(self, "history", []),
}
with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

#### 🔹 실제 코드로 구현한 예외 처리 및 복구 절차 (`try` / `except`)
프로그램 실행 중 예상치 못한 오류가 발생해도 비정상 종료되지 않도록 단계별 예외 처리를 작성했습니다.

1. **파일이 없는 경우 (`os.path.exists`)**: 에러를 내는 대신 기본 6문항을 불러와 바로 게임을 시작합니다.
```python
if not os.path.exists(STATE_FILE):
    print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
    self.quizzes = Quiz.get_default_quizzes()
    self.best_score = 0
    self.history = []
    return
```

2. **파일 읽기/쓰기 권한 오류 (`PermissionError`)**: 권한 부족 시 사용자에게 원인을 안내하고 기본 데이터로 안전하게 동작을 유지합니다.
```python
except PermissionError:
    # 1. 권한 오류 처리 (PermissionError)
    print("[오류] state.json 파일 읽기 권한이 없습니다. 권한을 확인해주세요.")
    self.quizzes = Quiz.get_default_quizzes()
    self.best_score = 0
    self.history = []
```

3. **JSON 파일 손상 시 백업 생성 및 복구 (`JSONDecodeError` 등)**: 손상된 파일을 `shutil.copy`로 `state.json.bak`에 백업해 둔 뒤 기본 퀴즈 데이터로 복구합니다.
```python
except (json.JSONDecodeError, KeyError, ValueError, TypeError) as e:
    # 2. 데이터 손상 시 백업 생성 및 복구 절차
    print(f"[경고] 데이터 파일이 손상되었습니다 ({e}).")
    try:
        shutil.copy(STATE_FILE, BACKUP_FILE)
        print(f"[알림] 손상된 이전 파일은 '{BACKUP_FILE}'로 백업되었습니다.")
    except Exception as backup_err:
        print(f"[오류] 백업 생성 실패: {backup_err}")

    print("기본 퀴즈 데이터로 복구하여 시작합니다.")
    self.quizzes = Quiz.get_default_quizzes()
    self.best_score = 0
    self.history = []
```

4. **사용자 입력 오류 및 강제 종료(`Ctrl+C`) 대응**: 문자를 잘못 입력했을 때(`ValueError`) 재입력을 유도하고, `Ctrl+C`(`KeyboardInterrupt`)로 종료할 때도 현재 상태를 자동 저장합니다.
```python
# 숫자 변환 실패 처리 (read_int)
try:
    val = int(raw)
except ValueError:
    print("숫자만 입력해 주세요.")
    continue

# 강제 종료 시 안전 저장 (run)
except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
    self.save()
    break
```

---

### 7-4. 대규모 데이터(퀴즈 1,000개 이상) 처리 시 성능 평가 및 설계 검토

* **현재 구조의 한계 분석**:
  * `load()` 실행 시 `state.json` 전체를 한 번에 메모리(`self.quizzes` 리스트)로 적재하므로 데이터가 수천~수만 건으로 늘어나면 RAM 점유율이 높아집니다.
  * 퀴즈 1건만 추가·수정해도 파일 전체를 덮어쓰는(`json.dump`) 구조이므로 파일 I/O 병목과 선형 탐색(`O(N)`) 지연이 발생할 수 있습니다.
* **확장 대응 설계 방안**:
  1. **지연 로딩 (Lazy Loading / Pagination)**: 전체 문제를 한 번에 읽지 않고 출제 또는 목록 조회 시 필요한 개수(예: 10~20문항 단위)만 부분 로드합니다.
  2. **해시 인덱싱 (Indexing)**: 문제 ID나 키워드 검색 시 Python `dict` 기반 인덱스(`O(1)`)를 구축하여 탐색 속도를 개선합니다.
  3. **경량 데이터베이스 전환 (`SQLite`)**: 데이터가 1,000건 이상으로 확장될 경우 별도 서버 설치가 필요 없는 내장 RDB인 `SQLite`로 전환하여, `LIMIT/OFFSET` 페이징 쿼리와 트랜잭션(ACID) 기반 부분 업데이트를 적용하는 것이 적합합니다.

---

## 8. Git 버전 관리 및 협업 워크플로우

### 8-1. Git의 필요성과 3가지 작업 영역
**Git**은 소스 코드의 변경 이력을 스냅샷 단위로 기록하는 분산 버전 관리 시스템입니다. 파일명을 `최종_진짜최종.py`처럼 늘리지 않고도 과거 시점으로 안전하게 복구할 수 있으며, 원격 저장소(GitHub)를 통해 백업과 협업을 수행합니다.

```text
[작업 디렉터리] ──(git add)──▶ [스테이징 영역] ──(git commit)──▶ [로컬 저장소] ──(git push)──▶ [원격 저장소(GitHub)]
```

### 8-2. 핵심 명령어 7종 정리
| 명령어 | 역할 및 설명 |
| :--- | :--- |
| **`git init`** | 현재 프로젝트 폴더를 Git 로컬 저장소로 초기화합니다. |
| **`git add`** | 수정하거나 새로 만든 파일을 커밋 대기 공간(Staging Area)에 등록합니다. |
| **`git commit`** | 스테이징된 변경 사항에 설명 메시지를 붙여 하나의 버전으로 영구 기록합니다. |
| **`git push`** | 로컬 저장소의 커밋 이력을 원격 저장소(GitHub)로 업로드합니다. |
| **`git pull`** | 원격 저장소의 최신 변경 사항을 내려받아 로컬 브랜치에 즉시 병합합니다. |
| **`git checkout`** | 작업할 브랜치를 전환하거나 새 브랜치를 생성(`-b`)합니다. |
| **`git clone`** | GitHub 원격 저장소의 전체 코드와 이력을 내 컴퓨터로 처음 복제해 옵니다. |

### 8-3. 작업 단위 규정 및 커밋 메시지 컨벤션
* **작업 단위 규정**: 하나의 기능 구현, 하나의 버그 수정, 하나의 문서 보완당 **1개의 독립된 커밋**을 생성하여 변경 이력을 명확히 추적할 수 있도록 관리합니다.
* **커밋 메시지 템플릿**: `<Type>: <작업 내용 요약>` 형식을 사용합니다.
  * `Feat`: 새로운 기능 추가 (예: `Feat: 퀴즈 삭제 기능 추가 및 state.json 동기화 처리`)
  * `Fix`: 오류 및 예외 처리 수정 (예: `Fix: PermissionError 예외 처리 및 백업 복구 추가`)
  * `Docs`: 문서 작성 및 수정 (예: `Docs: README 프로젝트 설명 및 개념 정리 보완`)
  * `Refactor`: 기능 변경 없는 코드 구조 개선 (예: `Refactor: 입력 검증 로직 read_int 함수로 분리`)
  * `Chore`: `.gitignore` 등 환경 설정

![git commit 로그](<sc/git log.png>)

### 8-4. 브랜치(Branch) 분기 및 병합(Merge)
메인 코드(`main`)의 안정성을 유지하면서 새로운 기능을 안전하게 개발하기 위해 기능 브랜치(`feature/...`)를 생성해 작업한 뒤, 검증이 완료되면 `main` 브랜치로 병합합니다.

```bash
git checkout -b feature/quiz-game   # 1. 기능 개발용 브랜치 생성 및 이동
# ... 기능 구현 및 커밋 ...
git checkout main                   # 2. 메인 브랜치로 복귀
git merge feature/quiz-game         # 3. 개발 완료된 기능 병합
```

![git commit graph 로그](<sc/git log --graph --oneline -all.png>)

### 8-5. 원격 저장소 동기화 (`clone` & `pull`)
| 1. Clone 전 | 2. 명령어 실행 | 3. Clone 후 |
| :---: | :---: | :---: |
| ![clone전](sc/clone_전.png) | ![clone pull 사용 증거](sc/git_clone.png) | ![clone후](sc/clone_후.png) |

---

## 9. 요구사항 변경 시 수정 대상 체크리스트 (유지보수 가이드)

향후 새로운 기능이 추가되거나 기존 규칙이 변경될 때 수정해야 할 클래스, 메서드 및 저장소(`state.json`) 필드 체크리스트입니다.

### 1) 점수 계산 방식 변경 시 (예: 문제별 차등 배점, 오답 감점제)
* [ ] **퀴즈 모델 (`Quiz` 클래스)**
  * `__init__`: 배점 속성(`self.points = 10` 등) 추가
  * `to_dict()` / `from_dict()`: 직렬화 및 복원 로직에 `"points"` 필드 반영
* [ ] **게임 컨트롤러 (`QuizGame` 클래스)**
  * `play_quiz()`: 정답 시 고정 `+1` 대신 `score += quiz.points` 또는 오답 감점 로직 수정
  * `add_quiz()`: 새 퀴즈 등록 시 문제 배점을 입력받는 절차 추가
* [ ] **저장 포맷 (`state.json`)**
  * `quizzes` 배열 내부 객체에 `"points"` 필드 추가

### 2) 퀴즈 데이터 모델 확장 시 (예: 정답 해설, 힌트, 난이도 추가)
* [ ] **퀴즈 모델 (`Quiz` 클래스)**
  * `__init__`: 신규 속성(`self.explanation`, `self.difficulty`) 추가
  * `show()`: 문제 출력 시 난이도 또는 힌트 표시 로직 반영
  * `to_dict()` / `from_dict()`: 기존 데이터 호환을 위해 `.get("explanation", "")` 기본값 처리 추가
* [ ] **게임 컨트롤러 (`QuizGame` 클래스)**
  * `play_quiz()`: 정답/오답 판별 직후 해설(`quiz.explanation`) 출력 구문 추가
  * `add_quiz()`: 퀴즈 생성 시 신규 항목을 입력받는 `read_text()` 로직 추가
* [ ] **저장 포맷 (`state.json`)**
  * `quizzes` 각 요소에 `"explanation"`, `"difficulty"` 필드 확장

### 3) 저장 포맷 및 기록 구조 변경 시 (예: 플레이어 이름, 풀이 소요 시간 기록)
* [ ] **게임 컨트롤러 (`QuizGame` 클래스)**
  * `load()` / `save()`: 최상위 딕셔너리 구조에 신규 상태 변수 매핑 및 기본값 처리
  * `play_quiz()`: 시작~종료 시간(`time` 모듈) 측정 후 `history` 기록 딕셔너리에 추가
  * `show_history()`: 기록 출력 포맷에 추가된 항목(소요 시간, 플레이어명 등) 반영
* [ ] **저장 포맷 (`state.json`)**
  * `history` 배열 내부 객체 스키마에 `"duration"`, `"player"` 등의 신규 필드 추가

---

## 10. 작성자 정보

* **작성자**: 권혁 (`kwonhyck0110`)
* **GitHub 저장소**: <https://github.com/kwonhyck0110/1-2.git>
* **최종 수정일**: 2026-11-11