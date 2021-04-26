
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)

cu = c

doc = ''
class Constants(BaseConstants):
    name_in_url = 'groupD'
    players_per_group = None
    num_rounds = 1
    solutions = ('A', 'A', 'B', 'D', 'C', 'A', 'D', 'B', 'D', 'A')
def creating_session(subsession):
    session = subsession.session
    import random
    num_players = len(subsession.get_players())
    treatment_list = []
    for i in range(num_players):
        if i % 3 == 1:
            treatment_list.append(1)
        elif i % 3 == 2:
            treatment_list.append(2)
        else:
            treatment_list.append(3)
    for player in subsession.get_players():
        index = random.randint(0,len(treatment_list)-1)
        player.group_no = treatment_list.pop(index)
    
class Subsession(BaseSubsession):
    creating_session = creating_session
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    group_no = models.IntegerField()
    E1 = models.StringField(choices=[['A', 'In broad terms'], ['B', 'For example, '], ['C', 'In contrast,'], ['D', 'Nevertheless']], label='1. Choose the best answer:')
    E2 = models.StringField(choices=[['A', 'more pragmatically'], ['B', 'speaking in a more pragmatic way, '], ['C', 'speaking in a way more pragmatically, '], ['D', 'in a more pragmatic-speaking way,']], label='2. Choose the best answer:')
    E3 = models.StringField(choices=[['A', 'teaching'], ['B', 'teaches '], ['C', 'to teach '], ['D', 'and teaching']], label='3. Choose the best answer:')
    E4 = models.StringField(choices=[['A', 'Consequently, philosophy students have been receiving an increasing number of job offers. '], ['B', 'Therefore, because of the evidence, colleges increased their offerings in philosophy. '], ['C', 'Notwithstanding the attractiveness of this course of study, students have resisted majoring in philosophy. '], ['D', 'However, despite its many utilitarian benefits, colleges have not always supported the study of philosophy.']], label='4. Which choice most effectively sets up the information that follows?')
    E5 = models.StringField(choices=[['A', 'Therefore'], ['B', 'Thus, '], ['C', 'Moreover, '], ['D', 'However, ']], label='5. Choose the best answer:')
    Q1 = models.StringField(choices=[['A', '3'], ['B', '5.7'], ['C', '9.5'], ['D', '14.3']], label='6. A pediatrician uses the model h = 3a + 28.6 to estimate the height h of a boy, in inches, in terms of the boy’s age a, in years, between the ages of 2 and 5. Based on the model, what is the estimated increase, in inches, of a boy’s height each year? ')
    Q2 = models.StringField(choices=[['A', '(0, 7) '], ['B', '(1, 7) '], ['C', '(7, 7)'], ['D', '(14, 2)']], label='7. A line in the xy-plane passes through the origin and has a slope of 1/7 . Which of the following points lies on the line? ')
    Q3 = models.StringField(choices=[['A', '115'], ['B', '120'], ['C', '124'], ['D', '173']], label='8. Katarina is a botanist studying the production of pears by two types of pear trees. She noticed that Type A trees produced 20 percent more pears than Type B trees did. Based on Katarina’s observation, if the Type A trees produced 144 pears, how many pears did the Type B trees produce?')
    Q4 = models.StringField(choices=[['A', 'x − 5 is a factor of p(x). '], ['B', 'x − 2 is a factor of p(x). '], ['C', 'x + 2 is a factor of p(x). '], ['D', 'The remainder when p(x) is divided by x − 3 is −2.']], label='9. For a polynomial p(x), the value of p(3) is −2. Which of the following must be true about p(x)? ')
    Q5 = models.StringField(choices=[['A', 'a > b '], ['B', 'b > a '], ['C', '|a| > |b|'], ['D', 'a = -b']], label='10. y < -x+a and y > x+b. In the xy-plane, if (0,0) is a solution to the system of inequalities above, which of the following relationships between a and b must be true? ')
    actual_scores = models.IntegerField(initial=0)
    self_evaluation1 = models.IntegerField(label='How many questions do you think you answered correctly? (1-10)', max=10, min=0)
    self_evaluation2 = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have you ever heard of Imposter Syndrome Before?')
    self_evaluation3 = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have you ever heard of overconfidence before?')
    gender = models.StringField(choices=[['A', 'Male'], ['B', 'Female'], ['C', 'Prefer Not to Say'], ['D', 'Other']], label='Gender')
    age = models.IntegerField(label='How old are you', max=100, min=0)
    education = models.StringField(choices=[['A', 'BA'], ['B', 'MA'], ['C', 'PhD'], ['D', 'Other']], label='What is your level of education, if you are currently pursuing a degree select that one.')
    studyfield = models.StringField(blank=True, label='What did you study/are you studying?')
    ExperEcon = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have you ever taken an Experimental Economics course?')
