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
    Q1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return(FR:Rendement)=8%"], [2, "Portfolio 2: Environmental Score=95%, Return(FR:Rendement)=5%"]]) 

    Q2_r6_increase_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return(FR:Rendement)=8%"], [2, "Portfolio 2: Environmental Score=95%, Return(FR:Rendement)=6%"]]) #Q2_500_6m
    Q3_r7_increase_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return(FR:Rendement)=8%"], [2, "Portfolio 2: Environmental Score=95%, Return(FR:Rendement)=7%"]]) #Q3_500_6m   
    Q4_r8_increase_L = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return(FR:Rendement)=8%"], [2, "Portfolio 2: Environmental Score=95%, Return(FR:Rendement)=8%"]]) #Q4_500_6m
 
    Q2_envscore80_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=80%, Return(FR:Rendement)=5%"], [2, "Portfolio 2: Environmental Score=5%, Return(FR:Rendement)=8%"]]) #Q1_20000_6m    
    Q3_envscore65_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=65%, Return(FR:Rendement)=5%%"], [2, "Portfolio 2: Environmental Score=5%, Return(FR:Rendement)=8%"]]) #Q2_20000_6m   
    Q4_envscore50_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=50%, Return(FR:Rendement)=5%"], [2, "Portfolio 2: Environmental Score=5%, Return(FR:Rendement)=8%"]]) #Q3_20000_6m 
    Q5_envscore35_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=35%, Return(FR:Rendement)=5%"], [2, "Portfolio 2: Environmental Score=5%, Return(FR:Rendement)=8%"]]) #Q4_20000_6m 
    Q6_envscore20_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=20%, Return(FR:Rendement)=5%"], [2, "Portfolio 2: Environmental Score=5%, Return(FR:Rendement)=8%"]]) #Q5_20000_6m                   
    Q7_envscore5_R = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1, "Portfolio 1: Environmental Score=5%, Return(FR:Rendement)=5%"], [2, "Portfolio 2: Environmental Score=5%, Return(FR:Rendement)=8%"]]) #Q1_500_1year
        
    Env_question = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Not worried at all // Pas inquiet du tout"], [2, "A little worried // Un peu inquiet"], [3, "I often think about it // J'y pense souvent"], [4, "I am very worried about it // Je suis très inquiet"], [5, "Prefer not to answer // Je préfère de ne pas répondre"]])
    
    Env_q_1 = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"]])
    
    Env_q_2 = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"]])
    
    Env_q_3 = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"]])
    
    Env_q_4 = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"]])
    
    Env_q_5 = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"]])
    
    Env_q_6 = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes"], [2, "No"]])

    Financial_literacya = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "More than $102 // Plus que 102$"], [2, "Exactly $102 // Exactement 102$"], [3, "Less than $102 // Moins que 102$"], [4, "Do not know // Je ne sais pas"], [5, "Prefer not to answer // Je préfère de ne pas répondre"]])
    
    Financial_literacyc = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "True // Vraie"], [2, "False // Fausse"], [3, "Do not know // Je ne sais pas"], [4, "Prefer not to answer  // Je préfère de ne pas répondre"]])
    
    Financial_literacyd = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Yes // Oui"], [2, "No // Non"], [3, "Prefer not to answer  // Je préfère de ne pas répondre"]])
    
    Financial_literacye = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Little or none // Peu de connaissances, ou pas du tout"], [2, "I have sufficient level of knowledge // J'ai assez de connaissances"], [3, "I have a good understanding of financial markets // J'ai des bonnes connaissances des marchés financiers"], [4, "I consider myself an expert // Je suis un expert de ces questions"]])
    
    Financial_literacyf = models.PositiveIntegerField(widget=widgets.RadioSelect, choices=[[1, "Little or none // Peu d'expérience, ou pas du tout"], [2, "I have a sufficient level experience in financial markets // J'ai assez d'expérience sur les marchés financiers "], [3, "I have a fair share of experience in financial markets // J'ai une bonne part d'expérience sur les marchés financiers"], [4, "I have a lot of experience in financial markets // J'ai beaucoup d'expérience sur les marchés financiers"]])

    time_video_page_start = models.FloatField()
    time_video_page_leave = models.FloatField()

    continue_return = models.BooleanField(default = True)
    continue_page = models.BooleanField(default = True)

    time = models.IntegerField( default=0 )

     
