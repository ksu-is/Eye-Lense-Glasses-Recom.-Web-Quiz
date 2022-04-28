from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError
from random import randrange

class CorrectAnswer(object):
    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        message = 'Incorrect answer.'

        if field.data != self.answer:
            raise ValidationError(message)

class PopQuiz(Form):
    class Meta:
        csrf = False
    q1 = RadioField(
        "What does our company, EyeRis, do to help our customers?",
        choices=[('True', 'We offer affordable prices for everyone.'), ('False', 'We offer high unaffordable prices.')],
        validators=[CorrectAnswer('True')]
        )
    q2 = RadioField(
        "What shape of lenses do most of our customers prefer?",
        choices=[('True', 'Round'), ('False', 'Square')],
        validators=[CorrectAnswer('True')]
    )
    q3 = RadioField(
        "What year did our company develop itself ?",
        choices=[('False', '2018'), ('False', '2019'), ('True', '2020'), ('False', '2021')],
        validators=[CorrectAnswer('True')]
        )
    q4 = RadioField(
        "Do we offer eye exams on our page and where ?",
        choices=[('False', 'Yes, we offer eye exams. It is found on the "Products" page.'), ('True', 'Yes, we offer eye exams. It can be found on the "Contact Us" page.'), ('False', 'Yes, it can be found on the "Products" page'), ('False', 'No, we do not offer eye exams.')],
        validators=[CorrectAnswer('True')]
        )
    q5 = RadioField(
        "What page can you use to learn more about our company's mission and vision?",
        choices=[('False', 'The "Contact Us" Page'), ('False', 'The "Products" Page'), ('False', 'The "Home" page'), ('True', 'The "About Us" page')],
        validators=[CorrectAnswer('True')]
        )
    q6 = RadioField(
        "Where is our company located?",
        choices=[('False', 'Newark, NJ'), ('True', 'Atlanta, GA'), ('False', 'Philadelphia, PA'), ('False', 'Miami, FL')],
        validators=[CorrectAnswer('True')]
        )
    q7 = RadioField(
        "Did you learn a lot about our company?",
        choices=[('True', 'Yes'), ('False', 'No')],
        validators=[CorrectAnswer('True')]
        )
