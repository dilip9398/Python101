class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        self.current_qno = self.question_list[self.question_no]
        self.question_no += 1
        self.user_answer = input(f"Q.{self.question_no}: {self.current_qno.text} (True/False) : ")
        self.check_answer(self.user_answer, self.current_qno.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You Got it right!")
            self.score += 1
        else:
            print("Your wrong!")

        print(f"The correct answer:  {current_answer}")
        print(f"The current score: {self.score}/{self.question_no}")
        print("\n")



