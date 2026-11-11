import json
import os
import random

STATE_FILE = "state.json"


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


class QuizGame:
    """퀴즈 게임 전체 흐름 관리 클래스"""
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()

    def load(self):
        """state.json 파일 읽기 (UTF-8)"""
        if not os.path.exists(STATE_FILE):
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = Quiz.get_default_quizzes()
            self.best_score = 0
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = int(data.get("best_score", 0))
            if not self.quizzes:
                self.quizzes = Quiz.get_default_quizzes()
        except (json.JSONDecodeError, KeyError, ValueError, TypeError) as e:
            print(f"[경고] 데이터 파일 손상 ({e}). 기본 데이터로 복구합니다.")
            self.quizzes = Quiz.get_default_quizzes()
            self.best_score = 0

    def save(self):
        """현재 상태(퀴즈 목록, 최고 점수, 히스토리)를 state.json에 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": getattr(self, "history", []),
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"[오류] 저장에 실패했습니다: {e}")

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
        """퀴즈 게임 진행"""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        quizzes = self.quizzes[:]
        random.shuffle(quizzes)

        score = 0
        for i, quiz in enumerate(quizzes, start=1):
            quiz.show(index=i)
            user_ans = self.read_int("정답 번호 입력 (1~4): ", 1, 4)
            if quiz.is_correct(user_ans):
                print("정답입니다! 🎉")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n결과: {len(quizzes)}문제 중 {score}개 정답")
        if score > self.best_score:
            print(f"🏆 최고 점수 갱신! ({self.best_score} → {score})")
            self.best_score = score
        self.save()

    def show_menu(self):
        print("\n==== 파이썬 기초 퀴즈 게임 ====")
        print("1) 퀴즈 풀기")
        print("2) 퀴즈 추가")
        print("3) 퀴즈 목록 보기")
        print("4) 최고 점수 확인")
        print("5) 종료")

    def run(self):
        """메인 실행 루프"""
        while True:
            try:
                self.show_menu()
                choice = self.read_int("메뉴 선택 (1~5): ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    print("프로그램을 종료합니다.")
                    self.save()
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n안전하게 프로그램을 종료합니다.")
                self.save()
                break

def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    main()