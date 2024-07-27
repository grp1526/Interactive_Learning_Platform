document.addEventListener('DOMContentLoaded', () => {
    const quizForm = document.getElementById('quiz-form');

    if (quizForm) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault();
            let score = 0;
            const questions = document.querySelectorAll('.question');
            questions.forEach((question, index) => {
                const selectedOption = question.querySelector('input[type="radio"]:checked');
                if (selectedOption && selectedOption.value === quiz.questions[index].answer) {
                    score++;
                }
            });
            alert(`Your score is: ${score} / ${questions.length}`);
        });
    }
});
