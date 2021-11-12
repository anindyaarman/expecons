from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class _1Introduction(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['choosePECETO']

    def before_next_page(self):
        return self.player.ExtendOptions()

class _2PE(Page):

    def is_displayed(self):
        return self.participant.vars['elic_type'][self.subsession.round_number-1] == "PE"

    form_model = 'player'
    form_fields = ['PESwitchingPoint']

    def vars_for_template(self):
        return {
            'round': self.round_number,
            'E_range': list(zip(list(range(1,len(self.session.vars['prob_E_range'])+1)),self.session.vars['prob_E_range'],
                                self.session.vars['prob_cE_range'])),
            'prospect_max': self.session.config['PE_prospect_max'],
            'prospect_min': self.session.config['PE_prospect_min'],
            'CE': self.session.config['PE_certainamount'][self.subsession.round_number-1]
        }

    def before_next_page(self):
        return self.player.compile()


class _3CE(Page):

    def is_displayed(self):
        return self.participant.vars['elic_type'][self.subsession.round_number - 1] == "CE"

    form_model = 'player'
    form_fields = ['CESwitchingPoint']

    def vars_for_template(self):
        return {
            'round': self.round_number,
            'E_range': list(zip(list(range(1,len(self.session.vars['CE_range'])+1)),(self.session.vars['CE_range']))),
            'CE_P': round((self.session.config['CE_prob_P'][self.subsession.round_number-1])*100, 2),
            'CE_cP': round((1 - self.session.config['CE_prob_P'][self.subsession.round_number-1])*100, 2),
            'CE_P_pts': self.session.config['CE_P_points'],
            'CE_cP_pts': self.session.config['CE_cP_points']
        }

    def before_next_page(self):
        return self.player.compile()

class _4TO(Page):

    def is_displayed(self):
        return self.participant.vars['elic_type'][self.subsession.round_number - 1] == "TO"

    form_model = 'player'
    form_fields = ['TOIndifference']

    def vars_for_template(self):
        return {
            'round': self.round_number,
            'Pe': self.session.config['TO_P'],
            'cPe': 100 - self.session.config['TO_P'],
            'rmin': self.session.config['TO_Rmin'],
            'rmax': self.session.config['TO_Rmax'],
            'base': self.session.config['TO_Base'],
            'x1': self.participant.vars['prev_TO'],
        }

    def before_next_page(self):
        return self.player.compile()


class _5Results(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'data': self.session.vars['series'],
            'elic_type': self.participant.vars['elic_type'][self.round_number == 1],
            'CE_max': self.session.config['CE_max'],
            'CE_min': self.session.config['CE_min'],
            'prospect_max': self.session.config['PE_prospect_max'],
            'prospect_min': self.session.config['PE_prospect_min'],
            'TO_max': max(self.participant.vars['TO_Series']),
            'base': self.session.config['TO_Base'],
        }

page_sequence = [
    _1Introduction,
    _2PE,
    _3CE,
    _4TO,
    _5Results,
]
