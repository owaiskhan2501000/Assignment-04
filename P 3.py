class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def is_correct(self, selected_option):
        return selected_option == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        score = 0
        for question in self.questions:
            question.display_question()
            selected_option = int(input("Your answer (enter the option number): "))
            
            if 1 <= selected_option <= len(question.options):
                if question.is_correct(selected_option):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {question.correct_option}: {question.options[question.correct_option - 1]}\n")
            else:
                print("Invalid option. Please choose a valid option.\n")

        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")
        user.record_score(self.name, score)


class User:
    def __init__(self, username):
        self.username = username
        self.scores = {}

    def record_score(self, quiz_name, score):
        if quiz_name not in self.scores:
            self.scores[quiz_name] = []
        self.scores[quiz_name].append(score)

    def view_scores(self):
        print(f"Scores for {self.username}:")
        for quiz_name, scores in self.scores.items():
            average_score = sum(scores) / len(scores)
            print(f"{quiz_name}: {scores} (Average Score: {average_score})")



if __name__ == "__main__":
    q1 = Question("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1)
    q2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2)
    q3 = Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2)


    quiz1 = Quiz("General Knowledge Quiz", [q1, q2, q3])

    user1 = User("JohnDoe")

    quiz1.take_quiz(user1)
    
    user1.view_scores()
