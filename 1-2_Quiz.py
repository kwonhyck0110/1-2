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
            Quiz("전선에 주로 사용되는 원자는?", ["금", "은", "알루미늄", "구리"], 4),
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
            if not raw:
                print("빈 입력입니다. 다시 입력해주세요.")
                continue
            return raw