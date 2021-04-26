
from .models import *

class Heterogeneity(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'child', 'residency']
    
class Information(Page):
    form_model = 'group'
    def vars_for_template(self):
        group = self.group
        player = self.player
        player_even = player.id_in_group % 2 == 0
        return dict(
            player_even = player_even 
        )
class Idealmaternity(Page):
    form_model = 'player'
    form_fields = ['mandatorypaternity',
                   'idealmaternity',
                   'mandatorymaternity',
                   'idealpaternity']

class Peercomparaison(Page):
    form_model = 'player'
    form_fields = ['peermaternity', 'peerpaternity']

class Publicgood(Page):
    form_model = 'player'
    form_fields = ['Publicgoodgame']

class End(Page):
    form_model = 'player'
    
page_sequence = [#Heterogeneity,
                 Information,
                 Idealmaternity,
                 Peercomparaison,
                 Publicgood]
