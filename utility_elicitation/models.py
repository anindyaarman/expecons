from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import ast


author = 'Putu Sanjiwacika Wibisana'

doc = """
Demonstration of several utility measurement method.
"""


class Constants(BaseConstants):
    name_in_url = 'utility_elicitation'
    players_per_group = None
    num_rounds = 9


class Subsession(BaseSubsession):

    def creating_session(self):
        # For Probability Equivalent
        self.session.vars['prob_E_range'] = [100-(5*i) for i in range(0,21)]
        self.session.vars['prob_cE_range'] = [(5*i) for i in range(0, 21)]
        # For Certainty Equivalent
        self.session.vars['CE_range'] = [round(self.session.config['CE_max']-((self.session.config['CE_max']/
                                                                               len(range(0,21)))*i),2) for i in range(0,21)]

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    choosePECETO = models.StringField()

    def ExtendOptions(self):
        if self.round_number == 1:
            self.participant.vars['prev_TO'] = []
        else: pass
        self.participant.vars['elic_type'] = [self.choosePECETO for _ in range(Constants.num_rounds)]
        self.choosePECETO = self.participant.vars['elic_type'][self.round_number]

    def compile(self):
        if self.participant.vars['elic_type'][0] == "PE":
            self.participant.vars['TO_Series'] = [99]
            if self.round_number == 1:
                self.participant.vars['switching_points'] = [int(self.PESwitchingPoint[:-1])]
            else: self.participant.vars['switching_points'].append(int(self.PESwitchingPoint[:-1]))
        elif self.participant.vars['elic_type'][0] == "CE":
            self.participant.vars['TO_Series'] = [99]
            if self.round_number == 1:
                self.participant.vars['switching_points'] = [int(self.CESwitchingPoint[:-1])]
            else: self.participant.vars['switching_points'].append(int(self.CESwitchingPoint[:-1]))
        elif self.participant.vars['elic_type'][0] == "TO":
            if self.round_number == 1:
                self.participant.vars['TO_Series'] = [int(self.TOIndifference)]
            else: self.participant.vars['TO_Series'].append(int(self.TOIndifference))
        #self.dump = str(self.participant.vars['switching_points'])
        if self.participant.vars['elic_type'][0] != "TO":
            self.participant.vars['PE_chosen'] = [self.session.vars['prob_E_range'][i-1] for i in self.participant.vars['switching_points']]
            self.participant.vars['CE_chosen'] = [self.session.vars['CE_range'][i-1] for i in self.participant.vars['switching_points']]
            if self.participant.vars['elic_type'][0] == "PE":
                self.dump = str(self.participant.vars['PE_chosen'])
            else: self.dump = str(self.participant.vars['CE_chosen'])
            #should go separate function?
            self.participant.vars['matrix'] = []
            if self.round_number == Constants.num_rounds:
                if self.participant.vars['elic_type'][0] == "PE":
                    self.participant.vars['matrix'] = list(zip(self.participant.vars['switching_points'],[i/100 for i in self.participant.vars['PE_chosen']],
                                      self.session.config['PE_certainamount']))
                elif self.participant.vars['elic_type'][0] == "CE":
                    self.participant.vars['matrix'] = list(zip(self.participant.vars['switching_points'],self.session.config['CE_prob_P'],
                                      self.participant.vars['CE_chosen']))
            else: pass
            data = [list(x) for x in zip([i[2] for i in self.participant.vars['matrix']],
                                         [i[1] for i in self.participant.vars['matrix']])]
            if self.participant.vars['elic_type'][0] == "PE":
                self.session.vars['series'] = [['X', 'U'], [self.session.config['PE_prospect_min'], 0], [self.session.config['PE_prospect_max'], 1]] + data
            else: self.session.vars['series'] = [['X', 'U'], [self.session.config['CE_min'], 0], [self.session.config['CE_max'], 1]] + data
        elif self.participant.vars['elic_type'][0] == "TO":
            if self.round_number == 1:
                self.participant.vars['TOs'] = [self.TOIndifference]
                self.participant.vars['prev_TO'] = [self.TOIndifference][0]
            else:
                self.participant.vars['TOs'].append(self.TOIndifference)
                self.participant.vars['prev_TO'] = self.participant.vars['TOs'][-1]
            if self.round_number == Constants.num_rounds:
                self.participant.vars['matrix'] = list(zip(self.participant.vars['TO_Series'],[round(0+i*(1/Constants.num_rounds),2)
                                                                                           for i in range(1,Constants.num_rounds+1)]))
                data = [list(x) for x in zip([i[0] for i in self.participant.vars['matrix']],
                                             [i[1] for i in self.participant.vars['matrix']])]
                self.session.vars['series'] = [['X', 'U'], [self.session.config['TO_Base'], 0], [max(self.participant.vars['TO_Series']), 1]] + data
            else: pass

    PESwitchingPoint = models.StringField()
    CESwitchingPoint = models.StringField()
    TOIndifference = models.FloatField()

    dump = models.StringField()
    dump2 = models.StringField()
