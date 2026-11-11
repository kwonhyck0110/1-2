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