#-*- coding: utf-8 -*-
# <standard imports>
# from __future__ import division
# from otree.db import models
# from otree.constants import BaseConstants
# from otree.models import BaseSubsession, BaseGroup, BasePlayer
# # from django_countries.fields import CountryField
# # from django_languages.fields import LanguageField
# # from django.conf.global_settings import LANGUAGES
# # from likert_field.models import LikertField
# # from otree_tools.models import fields as tool_models


from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)

import random


#from otree import widgets
#from otree.common import Currency as c
#import random
# </standard imports>

doc = """
"""

keywords = ("Aiste")

class Constants(BaseConstants):
    name_in_url = 'groupA'
    players_per_group = None
    num_rounds = 1
 
class Group(BaseGroup):
    
    pass

class Subsession(BaseSubsession):

    def creating_session(self):
      for p in self.get_players():
          p.payoff = c(10)
          
          
class Player(BasePlayer):
            
    Q1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return=8%"], [2, "Portfolio 2: Environmental Score=95%, Return=5%"]]) #Q1_500_6m

#    Q1_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return=8%"], [2, "Portfolio 2: Environmental Score=95%, Return=5%"]]) #Q1_500_6m
    Q2_r6_increase_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return=8%"], [2, "Portfolio 2: Environmental Score=95%, Return=6%"]]) #Q2_500_6m
    Q3_r7_increase_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return=8%"], [2, "Portfolio 2: Environmental Score=95%, Return=7%"]]) #Q3_500_6m   
    Q4_r8_increase_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return=8%"], [2, "Portfolio 2: Environmental Score=95%, Return=8%"]]) #Q4_500_6m
    
#    Q1_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=95%, Return=5%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q1_500_6m    
    Q2_envscore80_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=80%, Return=5%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q1_20000_6m    
    Q3_envscore65_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=65%, Return=5%%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q2_20000_6m   
    Q4_envscore50_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=50%, Return=5%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q3_20000_6m 
    Q5_envscore35_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=35%, Return=5%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q4_20000_6m 
    Q6_envscore20_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=20%, Return=5%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q5_20000_6m                   
    Q7_envscore5_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return=5%"], [2, "Portfolio 2: Environmental Score=5%, Return=8%"]]) #Q1_500_1year
    
   # Env_q_individual=tool_models.MultipleChoiceModelField(label="How do you fight against the climate change in your private life? (maximum 3 choices)", min_choices=1, max_choices=3)
    
    Env_question = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Not worried at all"], [2, "A little worried"], [3, "I often think about it"], [4, "I am very worried about it"], [5, "Prefer not to answer"]])
    
    Financial_literacya = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "More than $102"], [2, "Exactly $102"], [3, "Less than $102"], [4, "Do not know"], [5, "Prefer not to answer"]])
    
    Financial_literacyc = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "True"], [2, "False"], [3, "Do not know"], [4, "Prefer not to answer"]])
    
    Financial_literacyd = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"], [3, "Prefer not to answer"]])
    
    Financial_literacye = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Little or none"], [2, "I have sufficient level of knowledge"], [3, "I have a good understanding of financial markets"], [4, "I consider myself an expert"]])
    
    Financial_literacyf = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Little or none"], [2, "I have a sufficient level experience in financial markets."], [3, "I have a fair share of experience in financial markets"], [4, "I have a lot of experience in financial markets"]])
    

    time_video_page_start = models.FloatField()
    time_video_page_leave = models.FloatField()

    print(time_video_page_start)
    
    time = models.IntegerField( default=0 )

    #prolific_PID =  models.CharField( default=str(" ") ) # to store the ID provided by Prolific to each participant
    
    
