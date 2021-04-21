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
    rest = self.player.id_in_group % 3 
    res0 = (rest == 0)
    return ((self.subsession.round_number == 1) and res0)
     
class ID0N(Page):
  def before_next_page(self):
    self.player.time_video_page_leave = time.time()

  def is_displayed(self):  
    rest = self.player.id_in_group % 3
    res1 = (rest == 1)
    return ((self.subsession.round_number == 1) and res1)  

class ID0NN(Page):
  def before_next_page(self):
    self.player.time_video_page_leave = time.time()
  def is_displayed(self):  
    rest = self.player.id_in_group % 3
    res2 = (rest == 2)
    return ((self.subsession.round_number == 1) and res2)  
    
class ID(Page):    
  form_model = 'player'
  form_fields = [ 'Q1',]
  def is_displayed(self):  
    return (self.subsession.round_number == 1)

  def before_next_page(self):
    # either continue with returns or continue with
    #  environment
    print("choice")
    print(self.player.Q1)
    
    if self.player.Q1 == 1:
      self.player.continue_return = True
    if self.player.Q1 == 2:
      self.player.continue_return = False
      
class r6(Page):
  form_model = 'player'
  form_fields = ['Q2_r6_increase_L']                

  def is_displayed(self):
    show_page = (self.player.continue_return == True &
                 self.player.continue_page == True)
    return show_page
  
  def before_next_page(self):
    print("choice")
    print(self.player.Q2_r6_increase_L)
    
    if self.player.Q2_r6_increase_L == 2:
      self.player.continue_page = False
      
class r7(Page):
  form_model = 'player'
  form_fields = ['Q3_r7_increase_L']
 
  def is_displayed(self):
    show_page = (self.player.continue_return == True &
                 self.player.continue_page == True)
    return show_page
  
  def before_next_page(self):
    if self.player.Q3_r7_increase_L == 2:
      self.player.continue_page = False
        
class r8(Page):
  form_fields = ['Q4_r8_increase_L']
  def is_displayed(self):
    show_page = (self.player.continue_return == True &
                 self.player.continue_page == True)
    return show_page
  
  def before_next_page(self):
    self.player.continue_page = False

class env80(Page):
  form_fields = ['Q2_envscore80_R']
  def is_displayed(self):
    show_page = (self.player.continue_return == False &
                 self.player.continue_page == True)
    return show_page

  def before_next_page(self):
    if self.player.Q2_envscore80_R == 2:
      self.player.continue_page = False

class env65(Page):
  form_fields = ['Q3_envscore65_R']
  def is_displayed(self):
    show_page = (self.player.continue_return == False &
                 self.player.continue_page == True)
    return show_page
  def before_next_page(self):
    if self.player.Q3_envscore65_R == 2:
      self.player.continue_page = False
      
class env50(Page):
  form_fields = ['Q4_envscore50_R']
  def is_displayed(self):
    show_page = (self.player.continue_return == False &
                 self.player.continue_page == True)
    return show_page

  def before_next_page(self):
    self.player.continue_page = False

class env35(Page):
  form_fields = ['Q5_envscore35_R']
  def is_displayed(self):
    show_page = (self.player.continue_return == False &
                 self.player.continue_page == True)
    return show_page

  def before_next_page(self):
    if self.player.Q5_envscore35_R == 2:
      self.player.continue_page = False

class env20(Page):
  form_fields = ['Q6_envscore20_R']
  def is_displayed(self):
    show_page = (self.player.continue_return == False &
                 self.player.continue_page == True)
    return show_page

  def before_next_page(self):
    if self.player.Q6_envscore20_R == 2:
      self.player.continue_page = False

class env5(Page):
  form_fields = ['Q7_envscore5_R']
  def is_displayed(self):
    show_page = (self.player.continue_return == False &
                 self.player.continue_page == True)
    return show_page

  def before_next_page(self):
    self.player.continue_page = False

class ID1(Page):  
  form_model = 'player'
  form_fields = ['Q2_r6_increase_L',
                 'Q3_r7_increase_L',
                 'Q4_r8_increase_L',]
  def is_displayed(self):  
    return (self.player.Q1 == 1)
  
class ID2(Page):
  form_model = 'player'
  form_fields = ['Q2_envscore80_R',
                 'Q3_envscore65_R',
                 'Q4_envscore50_R',
                 'Q5_envscore35_R',
                 'Q6_envscore20_R',
                 'Q7_envscore5_R', ]
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
  #Introduction_first_page,
  #Introduction_second_page,         
  #ID0P,
  #ID0N,
  #ID0NN,
  ID,
  r6,
  r7,
  r8,
  env80,
  env65,
  env50,
  env35,
  env20,
  env5,
  ID1,
  ID2,
  Questionnaire
]



