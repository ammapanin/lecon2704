# -*- coding: utf-8 -*-
# from __future__ import division
# from . import models
# from ._builtin import Page, WaitPage
# from otree.common import Currency as c#, currency_range
# from .models import Constants

from decimal import Decimal
import random
import time
from .models import *

def vars_for_all_templates(self):
  return {
    'round_num': self.subsession.round_number,
    'num_of_rounds': Constants.num_rounds,  # no of periods
    'num_participants': Constants.players_per_group,
  } 
  
class Introduction_first_page(Page):

  #form_model = models.Player
  #form_fields = [ 'time' ]

  
  def is_displayed(self):
#    self.player.prolific_PID = self.participant.label #self.request.GET.get('participant_label')
    return self.subsession.round_number == 1
    
class Introduction_second_page(Page):

  def before_next_page(self):
    self.player.time_video_page_start = time.time()
    
  def is_displayed(self):
    return self.subsession.round_number == 1


    
class ID0P(Page):
  def before_next_page(self):
    self.player.time_video_page_leave = time.time()
    
  def is_displayed(self):  
    rest = self.player.id_in_group % 3 #2
    res0 = (rest == 0)
    #pair = (rest == 0)
    return ((self.subsession.round_number == 1) and res0) #pair
     
class ID0N(Page):

  def before_next_page(self):
    self.player.time_video_page_leave = time.time()

  def is_displayed(self):  
    rest = self.player.id_in_group % 3#2
    res1 = (rest == 1)
    #impair = (rest == 1)
    return ((self.subsession.round_number == 1) and res1)  #impair


class ID0NN(Page):
    
  def is_displayed(self):  
    rest = self.player.id_in_group % 3
    res2 = (rest == 2)
    return ((self.subsession.round_number == 1) and res2)  
    

class ID(Page):
    
  form_model = 'player'
  form_fields = [ 'Q1',]
  def is_displayed(self):  
    rest = self.player.id_in_group % 2
    return ((self.subsession.round_number == 1))    
    
class ID1(Page):
    
  form_model = 'player'
  form_fields = ['Q2_r6_increase_L', 'Q3_r7_increase_L', 'Q4_r8_increase_L',]
  def is_displayed(self):  
    rest = self.player.id_in_group % 2
    return (self.player.Q1 == 1)
#    pair = (rest == 0)
#    return ((self.subsession.round_number == 1) and pair)
    
class ID2(Page):
    
  form_model = 'player'
  form_fields = ['Q2_envscore80_R', 'Q3_envscore65_R', 'Q4_envscore50_R', 'Q5_envscore35_R', 'Q6_envscore20_R', 'Q7_envscore5_R', ]
  def is_displayed(self):  
    rest = self.player.id_in_group % 2
    return (self.player.Q1 == 2)
#    impair = (rest == 1)
#    return ((self.subsession.round_number == 1) and impair)


class Questionnaire(Page):   
  form_model = 'player'
  form_fields = [ 'Env_question',
                  'Env_q_1',
                  'Env_q_2',
                  'Env_q_3',
                  'Env_q_4',
                  'Env_q_5',
                  'Env_q_6',
                  'Financial_literacya',
                  'Financial_literacyc',
                  'Financial_literacyd',
                  'Financial_literacye',
                  'Financial_literacyf'] 
  def is_displayed(self):   
    return (self.subsession.round_number == 1)
        
page_sequence = [
            Introduction_first_page,
            Introduction_second_page,
            #ID,
            #ID1,
            #ID2,            
            ID0P,
            ID0N,
            ID0NN,
            ID,
            ID1,
            ID2,
            Questionnaire
            ]



