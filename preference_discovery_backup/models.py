from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np
from collections import Counter

author = 'Putu Sanjiwacika Wibisana'

doc = """
Adaptation of Preference Discovery by Delaney, Jacobson and Moenig (2018) for risk preference discovery.
"""


class Constants(BaseConstants):
    name_in_url = 'preference_discovery_v2'
    players_per_group = None
    num_rounds = 20
    table = 'preference_discovery/Float-Table.html'


class Subsession(BaseSubsession):

    def set_session_param(self):
        self.playable_rounds = self.session.config['rounds']

    playable_rounds = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_player_param(self):
        self.endowment = self.session.config['endowment']

    def set_prospect(self):  # Resulted in Nested Lists
        list_prospect = ['Lotere 1', 'Lotere 2', 'Lotere 3', 'Lotere 4', 'Lotere 5', 'Lotere 6',
                         'Lotere 7', 'Lotere 8', 'Lotere 9', 'Lotere 10', 'Lotere 11']  # index 0
        self.participant.vars['list_purchase'] = list_prospect
        list_probs = [1, 0.3, 0.45, 0.7, 0.8, 0.6, 0.5, 0.9, 0.1, 0.2, 0.05]  # index 1
        list_outcome = [60, 140, 130, 150, 115, 120, 130, 140, 120, 155, 175]  # index 2
        list_negate = [60, 70, 80, 40, 100, 95, 75, 40, 95, 80, 70]  # index 3
        exp_value = []  # index 4
        for i in range(0, 11):
            x1 = round((list_probs[i] * list_outcome[i]) + ((1 - list_probs[i]) * list_negate[i]), 0)
            exp_value = exp_value + [x1]
        list_show = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # index 5
        list_win = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # index 6
        utility = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # index 7
        lists = [list_prospect, list_probs, list_outcome, list_negate, exp_value, list_show, list_win, utility]
        all_prospects = []
        for i in range(0, 11):
            all_prospects.append([item[i] for item in lists])
        self.participant.vars['all_prospects'] = all_prospects

    def goods_rand(self):  # Resulting on lists
        lists = ['Lotere_2', 'Lotere_3', 'Lotere_4', 'Lotere_5', 'Lotere_6',
                 'Lotere_7', 'Lotere_8', 'Lotere_9', 'Lotere_10', 'Lotere_11']
        shown = list(np.random.choice(lists, size=4, replace=False))
        self.available = str(shown)
        if self.round_number == 1:
            self.participant.vars['available_hist'] = shown
        else:
            self.participant.vars['available_hist'] = self.participant.vars['available_hist'] + shown
        self.available_hist = str(self.participant.vars['available_hist'])

    def set_util(self):

        p = self.participant.vars['all_prospects']
        list_prospect = [self.Lotere_1, self.Lotere_2, self.Lotere_3, self.Lotere_4, self.Lotere_5,
                         self.Lotere_6, self.Lotere_7, self.Lotere_8, self.Lotere_9, self.Lotere_10,
                         self.Lotere_11]

        available = ['Lotere 1'] + eval(self.available)
        available = [w.replace('_', ' ') for w in available]
        sel_prospect_payoff = []
        for i in range(0, 11):
            p[i][7] = np.random.choice(["Win", "Lose"], p=[p[i][1], 1 - p[i][1]])  # Win or not win condition
            if p[i][0] in available:
                if p[i][7] == "Win" and list_prospect[i] > 0:
                    sel_prospect_payoff.append([p[i][0], p[i][7], list_prospect[i], p[i][2], list_prospect[i] * p[i][2]])
                elif p[i][7] == "Lose" and list_prospect[i] > 0:
                    sel_prospect_payoff.append([p[i][0], p[i][7], list_prospect[i], p[i][3], list_prospect[i] * p[i][3]])
                elif list_prospect[i] == 0:
                    pass
        self.sel_prospect_payoff = str(sel_prospect_payoff)
        self.util = 0
        for i in range(0, len(sel_prospect_payoff)):
            self.util += sel_prospect_payoff[i][2] * sel_prospect_payoff[i][3]

        if self.round_number == 1:
            self.participant.vars['payoff_vector'] = [self.util]
        elif self.round_number != 1:
            self.participant.vars['payoff_vector'].append(self.util)

    def purchase_counter(self):  # Resulting in dictionary
        list_full = ['Lotere 1', 'Lotere 2', 'Lotere 3', 'Lotere 4', 'Lotere 5', 'Lotere 6',
                     'Lotere 7', 'Lotere 8', 'Lotere 9', 'Lotere 10', 'Lotere 11']
        list_num = [self.Lotere_1, self.Lotere_2, self.Lotere_3, self.Lotere_4, self.Lotere_5,
                    self.Lotere_6, self.Lotere_7, self.Lotere_8, self.Lotere_9, self.Lotere_10,
                    self.Lotere_11]
        dictionary = dict(zip(list_full, list_num))
        if self.round_number == 1:
            self.participant.vars['purchase_hist'] = dictionary
        else:
            self.participant.vars['purchase_hist'] = Counter(self.participant.vars['purchase_hist']) + \
                                                     Counter(dictionary)
        self.purchase_hist = str(self.participant.vars['purchase_hist'])

    def update_prospect(self):
        list_purchase = self.participant.vars['list_purchase']  # List of prospects purchasable
        hist = self.participant.vars['purchase_hist']  # Dictionary
        p = self.participant.vars['all_prospects']  # Nested List
        for i in p:
            if hist[i[0]] > 0:
                i[5] = 1
            elif (hist[i[0]] == 0) & (i[0] != 'Lotere 1'):
                i[5] = 0
        self.participant.vars['all_prospects'] = p
        self.all_prospects = str(p)

    def set_payoff(self):
        self.payoff = sum(self.participant.vars['payoff_vector'])

    all_prospects = models.StringField()
    available_hist = models.StringField()
    purchase_hist = models.StringField()
    available = models.StringField()
    util = models.FloatField(initial=0)
    endowment = models.IntegerField()
    sel_prospect_payoff = models.StringField()

    ## Lotere is the Indonesian word for 'prospect'

    Lotere_1 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 1")
    Lotere_2 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 2")
    Lotere_3 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 3")
    Lotere_4 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 4")
    Lotere_5 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 5")
    Lotere_6 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 6")
    Lotere_7 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 7")
    Lotere_8 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 8")
    Lotere_9 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 9")
    Lotere_10 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 10")
    Lotere_11 = models.IntegerField(min=0, max=10, initial=0, label="Lotere 11")

    ## Vars for questionnaire

    Name = models.StringField(label="Nama Lengkap Anda:")
    Age = models.IntegerField(label="Usia:", min=14, max=35)
    Gender = models.StringField(label="Gender:", choices=["Pria", "Wanita"])
