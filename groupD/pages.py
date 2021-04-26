
from .models import *

class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'education', 'studyfield', 'ExperEcon']
class Question1(Page):
    form_model = 'player'
    form_fields = ['E1', 'E2', 'E3', 'E4', 'E5']
class Question2(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
class ImposterSyndrome(Page):
    form_model = 'player'
    form_fields = ['self_evaluation2']
    def is_displayed(self):
        group = self.group
        player = self.player
        return player.group_no == 2
    
class Overconfidence(Page):
    form_model = 'player'
    form_fields = ['self_evaluation3']
    def is_displayed(self):
        group = self.group
        player = self.player
        return player.group_no == 3

class Selfevaluation(Page):
    form_model = 'player'
    form_fields = ['self_evaluation1']

class Results(Page):
    form_model = 'player'
    def vars_for_template(self):
        player = self.player
        ans = []
        ans.append(player.E1)
        ans.append(player.E2)
        ans.append(player.E3)
        ans.append(player.E4)
        ans.append(player.E5)
        ans.append(player.Q1)
        ans.append(player.Q2)
        ans.append(player.Q3)
        ans.append(player.Q4)
        ans.append(player.Q5)
        
        for i in range(0,10):
            if ans[i] == Constants.solutions[i]:
                player.actual_scores += 1
            else:
                player.actual_scores = player.actual_scores
        return dict()
    
page_sequence = [#Demographics,
                 Question1,
                 Question2,
                 ImposterSyndrome,
                 Overconfidence,
                 Selfevaluation]

