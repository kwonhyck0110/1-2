import json
import os
import random   # 난수 생성용 모듈 추가
from datetime import datetime  # 날짜/시간 기록용 모듈 추가

STATE_FILE = "state.json"

# ======================================================
# Quiz 클래스: 개별 퀴즈 하나를 표현
# ======================================================

class Quiz:
    """개별 퀴즈를 표현하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, index=None):
        """문제와 선택지를 출력"""
        prefix = f"[{index}] " if index is not None else ""
        print(f"\n{prefix}{self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}) {choice}")

    def is_correct(self, user_answer):
        """정답 여부 판별"""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 변환용 dict"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @staticmethod
    def from_dict(data):
        """dict를 Quiz 객체로 복원"""
        return Quiz(data["question"], data["choices"], data["answer"])

# ======================================================
# 기본 퀴즈 데이터 (5개 이상)
# 주제: 전기 및 반도체 기초
# ======================================================

    @staticmethod
    def get_default_quizzes():
        """기본 퀴즈 목록 반환 (최소 5개 이상)"""
        return [
            Quiz("전기에서 저항을 나타내는 단위는?", ["볼트", "옴", "암페어", "와트"], 2),
            Quiz("앤비디아의 창업자는?", ["리사 수", "이재용", "젠슨 황", "스티브 잡스"], 3),
            Quiz("전류의 크기와 방향이 일정한 주기를 가지고 주기적으로 바뀌는 전기가 무엇인가?", ["직류", "정류", "변류", "교류"], 4),
            Quiz("전기와 자기의 개념 통합, 전자기력 정립을 한 과학자는?", ["맥스웰", "아인슈타인", "테슬라", "페러데이"], 1),
            Quiz("상황에 따라 전기가 흐를수도 안 흐를수도 있는 물질은?", ["도체", "절연체", "반도체", "초전도체"], 3),
            Quiz("전선에 주로 사용되는 원소는?", ["금", "은", "알루미늄", "구리"], 4),
        ]

# ======================================================
# QuizGame 클래스: 게임 전체 관리
# ======================================================

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.history = []  # 점수 히스토리 리스트 추가
        self.load()

# ---------- 파일 입출력 ----------

    def load(self):
        """state.json에서 데이터를 불러온다."""
        if not os.path.exists(STATE_FILE):
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = Quiz.get_default_quizzes()
            self.best_score = 0
            self.history = []
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = int(data.get("best_score", 0))
            self.history = data.get("history", [])  # 히스토리 데이터 복원
            if not self.quizzes:
                self.quizzes = Quiz.get_default_quizzes()
        except (json.JSONDecodeError, KeyError, ValueError, TypeError) as e:
            print(f"[경고] 데이터 파일 손상 ({e}). 기본 데이터로 복구합니다.")
            self.quizzes = Quiz.get_default_quizzes()
            self.best_score = 0
            self.history = []

    def save(self):
        """state.json 파일 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": self.history,  # 히스토리 데이터 추가 저장
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"[오류] 저장 실패: {e}")

# ---------- 공통 입력 유틸 ----------

    def read_int(self, prompt, min_v, max_v):
        """정수 범위를 검증하는 입력 함수"""
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("빈 입력입니다. 다시 입력해주세요.")
                continue
            try:
                val = int(raw)
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue
            if val < min_v or val > max_v:
                print(f"{min_v}~{max_v} 사이의 숫자를 입력해주세요.")
                continue
            return val

    def read_text(self, prompt):
        """공백 없는 텍스트를 받는 입력 함수"""
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("빈 입력입니다. 다시 입력해주세요.")
                continue
            return raw

    def list_quizzes(self):
        """퀴즈 목록 출력"""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")
        for i, quiz in enumerate(self.quizzes, start=1):
            quiz.show(index=i)
            print(f"  → 정답: {quiz.answer}번")

    def show_best_score(self):
        """최고 점수 확인"""
        if self.best_score == 0:
            print("\n아직 퀴즈 기록이 없습니다.")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점")

    def add_quiz(self):
        """사용자 정의 퀴즈 추가"""
        print("\n[퀴즈 추가]")
        question = self.read_text("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choices.append(self.read_text(f"선택지 {i}: "))
        answer = self.read_int("정답 번호 (1~4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.save()
        print("퀴즈가 성공적으로 추가되었습니다!")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        play_quizzes = self.quizzes[:]
        random.shuffle(play_quizzes)

        print("\n🎲 문제를 무작위 순서로 출제합니다!")
        score = 0
        total = len(play_quizzes)
        
        for i, quiz in enumerate(play_quizzes, start=1):
            quiz.show(index=i)
            user_ans = self.read_int("정답 번호 입력 (1~4): ", 1, 4)
            if quiz.is_correct(user_ans):
                print("정답입니다! 🎉")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번 이었어요.")

        print(f"\n결과: {total}문제 중 {score}개 정답")
        
        # 1. 히스토리 기록 추가 (날짜/시간, 푼 문제 수, 맞힌 개수)
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "date": now_str,
            "total": total,
            "score": score
        }
        self.history.append(record)

        # 2. 최고 점수 갱신 판별
        if score > self.best_score:
            print(f"🏆 최고 점수 갱신! ({self.best_score} → {score})")
            self.best_score = score
            
        self.save()
    def delete_quiz(self):
        """등록된 퀴즈 중 하나를 삭제하고 state.json에 저장한다."""
        if not self.quizzes:
            print("\n삭제할 퀴즈가 없습니다.")
            return

        print("\n[퀴즈 삭제]")
        self.list_quizzes()
        
        target_idx = self.read_int(
            f"삭제할 퀴즈 번호를 입력하세요 (1~{len(self.quizzes)}): ", 
            1, 
            len(self.quizzes)
        )
        
        # 리스트 인덱스는 0부터 시작하므로 target_idx - 1
        deleted_quiz = self.quizzes.pop(target_idx - 1)
        self.save()
        print(f"'{deleted_quiz.question}' 퀴즈가 성공적으로 삭제되었습니다. 🗑️")

# ---------- 메뉴 ----------

    def show_menu(self):
        print("\n==== 파이썬 기초 퀴즈 게임 ====")
        print("1) 퀴즈 풀기")
        print("2) 퀴즈 추가")
        print("3) 퀴즈 목록 보기")
        print("4) 최고 점수 확인")
        print("5) 점수 기록 히스토리 보기")  # 메뉴 추가
        print("6) 퀴즈 삭제")
        print("7) 종료")

    def run(self):
        while True:
            try:
                self.show_menu()
                choice = self.read_int("메뉴 선택 (1~7): ", 1, 7)
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
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
                self.save()
                break

def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    main()

# ---------- 퀴즈 삭제 ----------
    def delete_quiz(self):
        """등록된 퀴즈 중 하나를 삭제하고 state.json에 저장한다."""
        if not self.quizzes:
            print("\n삭제할 퀴즈가 없습니다.")
            return

        print("\n[퀴즈 삭제]")
        self.list_quizzes()
        
        target_idx = self.read_int(
            f"삭제할 퀴즈 번호를 입력하세요 (1~{len(self.quizzes)}): ", 
            1, 
            len(self.quizzes)
        )
        
        # 리스트 인덱스는 0부터 시작하므로 target_idx - 1
        deleted_quiz = self.quizzes.pop(target_idx - 1)
        self.save()
        print(f"'{deleted_quiz.question}' 퀴즈가 성공적으로 삭제되었습니다. 🗑️")

#--------- 히스토리 출력 기능 ----------

    def show_history(self):
            """전체 게임 기록 출력"""
            if not self.history:
                print("\n아직 진행된 게임 기록이 없습니다.")
                return

            print("\n==== 📜 점수 기록 히스토리 ====")
            for i, rec in enumerate(self.history, start=1):
                print(f"{i}. [{rec['date']}] Total: {rec['total']}문제 | 정답: {rec['score']}개")