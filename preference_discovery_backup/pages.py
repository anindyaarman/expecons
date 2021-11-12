from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import ast
import random
import numpy as np


class No1Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        return {self.player.set_prospect(),
                self.subsession.set_session_param()}


class No2Instructions1(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        p = self.participant.vars['all_prospects']
        return {
            'endowment': self.session.config['endowment'],
            'round': self.subsession.round_number,
            'playable_rounds': self.session.config['rounds'],
            'prob_A_g1': p[0][1] * 100, 'gain_A_g1': p[0][2], 'prob_B_g1': round(1 - p[0][1], 2) * 100,
            'gain_B_g1': p[0][3],
            'show_g1': p[0][5], 'exp_g1': p[0][4], 'noise_g1': p[0][6],
            'prob_A_g2': p[1][1] * 100, 'gain_A_g2': p[1][2], 'prob_B_g2': round(1 - p[1][1], 2) * 100,
            'gain_B_g2': p[1][3],
            'show_g2': p[1][5], 'exp_g2': p[1][4], 'noise_g2': p[1][6],
            'prob_A_g3': p[2][1] * 100, 'gain_A_g3': p[2][2], 'prob_B_g3': round(1 - p[2][1], 2) * 100,
            'gain_B_g3': p[2][3],
            'show_g3': p[2][5], 'exp_g3': p[2][4], 'noise_g3': p[2][6],
            'prob_A_g4': p[3][1] * 100, 'gain_A_g4': p[3][2], 'prob_B_g4': round(1 - p[3][1], 2) * 100,
            'gain_B_g4': p[3][3],
            'show_g4': p[3][5], 'exp_g4': p[3][4], 'noise_g4': p[3][6],
            'prob_A_g5': p[4][1] * 100, 'gain_A_g5': p[4][2], 'prob_B_g5': round(1 - p[4][1], 2) * 100,
            'gain_B_g5': p[4][3],
            'show_g5': p[4][5], 'exp_g5': p[4][4], 'noise_g5': p[4][6],
            'prob_A_g6': p[5][1] * 100, 'gain_A_g6': p[5][2], 'prob_B_g6': round(1 - p[5][1], 2) * 100,
            'gain_B_g6': p[5][3],
            'show_g6': p[5][5], 'exp_g6': p[5][4], 'noise_g6': p[5][6],
            'prob_A_g7': p[6][1] * 100, 'gain_A_g7': p[6][2], 'prob_B_g7': round(1 - p[6][1], 2) * 100,
            'gain_B_g7': p[6][3],
            'show_g7': p[6][5], 'exp_g7': p[6][4], 'noise_g7': p[6][6],
            'prob_A_g8': p[7][1] * 100, 'gain_A_g8': p[7][2], 'prob_B_g8': round(1 - p[7][1], 2) * 100,
            'gain_B_g8': p[7][3],
            'show_g8': p[7][5], 'exp_g8': p[7][4], 'noise_g8': p[7][6],
            'prob_A_g9': p[8][1] * 100, 'gain_A_g9': p[8][2], 'prob_B_g9': round(1 - p[8][1], 2) * 100,
            'gain_B_g9': p[8][3],
            'show_g9': p[8][5], 'exp_g9': p[8][4], 'noise_g9': p[8][6],
            'prob_A_g10': p[9][1] * 100, 'gain_A_g10': p[9][2], 'prob_B_g10': round(1 - p[9][1], 2) * 100,
            'gain_B_g10': p[9][3],
            'show_g10': p[9][5], 'exp_g10': p[9][4], 'noise_g10': p[9][6],
            'prob_A_g11': p[10][1] * 100, 'gain_A_g11': p[10][2], 'prob_B_g11': round(1 - p[10][1], 2) * 100,
            'gain_B_g11': p[10][3],
            'show_g11': p[10][5], 'exp_g11': p[10][4], 'noise_g11': p[10][6],
        }


class No2Instructions2(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        p = self.participant.vars['all_prospects']
        return {
            'endowment': self.session.config['endowment'],
            'round': self.subsession.round_number,
            'playable_rounds': self.session.config['rounds'],
            'prob_A_g1': p[0][1] * 100, 'gain_A_g1': p[0][2], 'prob_B_g1': round(1 - p[0][1], 2) * 100,
            'gain_B_g1': p[0][3],
            'show_g1': p[0][5], 'exp_g1': p[0][4], 'noise_g1': p[0][6],
            'prob_A_g2': p[1][1] * 100, 'gain_A_g2': p[1][2], 'prob_B_g2': round(1 - p[1][1], 2) * 100,
            'gain_B_g2': p[1][3],
            'show_g2': p[1][5], 'exp_g2': p[1][4], 'noise_g2': p[1][6],
            'prob_A_g3': p[2][1] * 100, 'gain_A_g3': p[2][2], 'prob_B_g3': round(1 - p[2][1], 2) * 100,
            'gain_B_g3': p[2][3],
            'show_g3': p[2][5], 'exp_g3': p[2][4], 'noise_g3': p[2][6],
            'prob_A_g4': p[3][1] * 100, 'gain_A_g4': p[3][2], 'prob_B_g4': round(1 - p[3][1], 2) * 100,
            'gain_B_g4': p[3][3],
            'show_g4': p[3][5], 'exp_g4': p[3][4], 'noise_g4': p[3][6],
            'prob_A_g5': p[4][1] * 100, 'gain_A_g5': p[4][2], 'prob_B_g5': round(1 - p[4][1], 2) * 100,
            'gain_B_g5': p[4][3],
            'show_g5': p[4][5], 'exp_g5': p[4][4], 'noise_g5': p[4][6],
            'prob_A_g6': p[5][1] * 100, 'gain_A_g6': p[5][2], 'prob_B_g6': round(1 - p[5][1], 2) * 100,
            'gain_B_g6': p[5][3],
            'show_g6': p[5][5], 'exp_g6': p[5][4], 'noise_g6': p[5][6],
            'prob_A_g7': p[6][1] * 100, 'gain_A_g7': p[6][2], 'prob_B_g7': round(1 - p[6][1], 2) * 100,
            'gain_B_g7': p[6][3],
            'show_g7': p[6][5], 'exp_g7': p[6][4], 'noise_g7': p[6][6],
            'prob_A_g8': p[7][1] * 100, 'gain_A_g8': p[7][2], 'prob_B_g8': round(1 - p[7][1], 2) * 100,
            'gain_B_g8': p[7][3],
            'show_g8': p[7][5], 'exp_g8': p[7][4], 'noise_g8': p[7][6],
            'prob_A_g9': p[8][1] * 100, 'gain_A_g9': p[8][2], 'prob_B_g9': round(1 - p[8][1], 2) * 100,
            'gain_B_g9': p[8][3],
            'show_g9': p[8][5], 'exp_g9': p[8][4], 'noise_g9': p[8][6],
            'prob_A_g10': p[9][1] * 100, 'gain_A_g10': p[9][2], 'prob_B_g10': round(1 - p[9][1], 2) * 100,
            'gain_B_g10': p[9][3],
            'show_g10': p[9][5], 'exp_g10': p[9][4], 'noise_g10': p[9][6],
            'prob_A_g11': p[10][1] * 100, 'gain_A_g11': p[10][2], 'prob_B_g11': round(1 - p[10][1], 2) * 100,
            'gain_B_g11': p[10][3],
            'show_g11': p[10][5], 'exp_g11': p[10][4], 'noise_g11': p[10][6],
        }


class No3Start(Page):

    def is_displayed(self):
        return self.round_number <= self.session.config['rounds']

    def vars_for_template(self):
        p = self.participant.vars['all_prospects']
        return {
            'round': self.subsession.round_number,
            'playable_rounds': self.session.config['rounds'],
            'list': self.participant.vars['all_prospects'],
            'prob_A_g1': p[0][1] * 100, 'gain_A_g1': p[0][2], 'prob_B_g1': round(1 - p[0][1], 2) * 100,
            'gain_B_g1': p[0][3],
            'show_g1': p[0][5], 'exp_g1': p[0][4], 'noise_g1': p[0][6],
            'prob_A_g2': p[1][1] * 100, 'gain_A_g2': p[1][2], 'prob_B_g2': round(1 - p[1][1], 2) * 100,
            'gain_B_g2': p[1][3],
            'show_g2': p[1][5], 'exp_g2': p[1][4], 'noise_g2': p[1][6],
            'prob_A_g3': p[2][1] * 100, 'gain_A_g3': p[2][2], 'prob_B_g3': round(1 - p[2][1], 2) * 100,
            'gain_B_g3': p[2][3],
            'show_g3': p[2][5], 'exp_g3': p[2][4], 'noise_g3': p[2][6],
            'prob_A_g4': p[3][1] * 100, 'gain_A_g4': p[3][2], 'prob_B_g4': round(1 - p[3][1], 2) * 100,
            'gain_B_g4': p[3][3],
            'show_g4': p[3][5], 'exp_g4': p[3][4], 'noise_g4': p[3][6],
            'prob_A_g5': p[4][1] * 100, 'gain_A_g5': p[4][2], 'prob_B_g5': round(1 - p[4][1], 2) * 100,
            'gain_B_g5': p[4][3],
            'show_g5': p[4][5], 'exp_g5': p[4][4], 'noise_g5': p[4][6],
            'prob_A_g6': p[5][1] * 100, 'gain_A_g6': p[5][2], 'prob_B_g6': round(1 - p[5][1], 2) * 100,
            'gain_B_g6': p[5][3],
            'show_g6': p[5][5], 'exp_g6': p[5][4], 'noise_g6': p[5][6],
            'prob_A_g7': p[6][1] * 100, 'gain_A_g7': p[6][2], 'prob_B_g7': round(1 - p[6][1], 2) * 100,
            'gain_B_g7': p[6][3],
            'show_g7': p[6][5], 'exp_g7': p[6][4], 'noise_g7': p[6][6],
            'prob_A_g8': p[7][1] * 100, 'gain_A_g8': p[7][2], 'prob_B_g8': round(1 - p[7][1], 2) * 100,
            'gain_B_g8': p[7][3],
            'show_g8': p[7][5], 'exp_g8': p[7][4], 'noise_g8': p[7][6],
            'prob_A_g9': p[8][1] * 100, 'gain_A_g9': p[8][2], 'prob_B_g9': round(1 - p[8][1], 2) * 100,
            'gain_B_g9': p[8][3],
            'show_g9': p[8][5], 'exp_g9': p[8][4], 'noise_g9': p[8][6],
            'prob_A_g10': p[9][1] * 100, 'gain_A_g10': p[9][2], 'prob_B_g10': round(1 - p[9][1], 2) * 100,
            'gain_B_g10': p[9][3],
            'show_g10': p[9][5], 'exp_g10': p[9][4], 'noise_g10': p[9][6],
            'prob_A_g11': p[10][1] * 100, 'gain_A_g11': p[10][2], 'prob_B_g11': round(1 - p[10][1], 2) * 100,
            'gain_B_g11': p[10][3],
            'show_g11': p[10][5], 'exp_g11': p[10][4], 'noise_g11': p[10][6],
        }

    def before_next_page(self):
        return {self.player.goods_rand(),
                self.player.set_player_param()}


class No4Purchase(Page):

    def is_displayed(self):
        return self.round_number <= self.session.config['rounds']

    def vars_for_template(self):
        p = self.participant.vars['all_prospects']
        return {
            'endowment': self.session.config['endowment'],
            'shown': eval(self.player.available),
            'round': self.subsession.round_number,
            'playable_rounds': self.session.config['rounds'],
            'list': self.participant.vars['all_prospects'],
            'prob_A_g1': p[0][1] * 100, 'gain_A_g1': p[0][2], 'prob_B_g1': round(1 - p[0][1], 2) * 100,
            'gain_B_g1': p[0][3],
            'show_g1': p[0][5], 'exp_g1': p[0][4], 'noise_g1': p[0][6],
            'prob_A_g2': p[1][1] * 100, 'gain_A_g2': p[1][2], 'prob_B_g2': round(1 - p[1][1], 2) * 100,
            'gain_B_g2': p[1][3],
            'show_g2': p[1][5], 'exp_g2': p[1][4], 'noise_g2': p[1][6],
            'prob_A_g3': p[2][1] * 100, 'gain_A_g3': p[2][2], 'prob_B_g3': round(1 - p[2][1], 2) * 100,
            'gain_B_g3': p[2][3],
            'show_g3': p[2][5], 'exp_g3': p[2][4], 'noise_g3': p[2][6],
            'prob_A_g4': p[3][1] * 100, 'gain_A_g4': p[3][2], 'prob_B_g4': round(1 - p[3][1], 2) * 100,
            'gain_B_g4': p[3][3],
            'show_g4': p[3][5], 'exp_g4': p[3][4], 'noise_g4': p[3][6],
            'prob_A_g5': p[4][1] * 100, 'gain_A_g5': p[4][2], 'prob_B_g5': round(1 - p[4][1], 2) * 100,
            'gain_B_g5': p[4][3],
            'show_g5': p[4][5], 'exp_g5': p[4][4], 'noise_g5': p[4][6],
            'prob_A_g6': p[5][1] * 100, 'gain_A_g6': p[5][2], 'prob_B_g6': round(1 - p[5][1], 2) * 100,
            'gain_B_g6': p[5][3],
            'show_g6': p[5][5], 'exp_g6': p[5][4], 'noise_g6': p[5][6],
            'prob_A_g7': p[6][1] * 100, 'gain_A_g7': p[6][2], 'prob_B_g7': round(1 - p[6][1], 2) * 100,
            'gain_B_g7': p[6][3],
            'show_g7': p[6][5], 'exp_g7': p[6][4], 'noise_g7': p[6][6],
            'prob_A_g8': p[7][1] * 100, 'gain_A_g8': p[7][2], 'prob_B_g8': round(1 - p[7][1], 2) * 100,
            'gain_B_g8': p[7][3],
            'show_g8': p[7][5], 'exp_g8': p[7][4], 'noise_g8': p[7][6],
            'prob_A_g9': p[8][1] * 100, 'gain_A_g9': p[8][2], 'prob_B_g9': round(1 - p[8][1], 2) * 100,
            'gain_B_g9': p[8][3],
            'show_g9': p[8][5], 'exp_g9': p[8][4], 'noise_g9': p[8][6],
            'prob_A_g10': p[9][1] * 100, 'gain_A_g10': p[9][2], 'prob_B_g10': round(1 - p[9][1], 2) * 100,
            'gain_B_g10': p[9][3],
            'show_g10': p[9][5], 'exp_g10': p[9][4], 'noise_g10': p[9][6],
            'prob_A_g11': p[10][1] * 100, 'gain_A_g11': p[10][2], 'prob_B_g11': round(1 - p[10][1], 2) * 100,
            'gain_B_g11': p[10][3],
            'show_g11': p[10][5], 'exp_g11': p[10][4], 'noise_g11': p[10][6],
        }

    form_model = 'player'

    def get_form_fields(self):
        fields = ['Lotere_1'] + eval(self.player.available)
        return fields

    def error_message(self, values):
        print('values is', values)
        fields = ['Lotere_1'] + eval(self.player.available)
        if values[fields[0]] + values[fields[1]] + values[fields[2]] + \
                values[fields[3]] + values[fields[4]] > int(self.player.endowment):
            return 'Total pilihan Anda melebihi koin yang tersedia!'

    def before_next_page(self):
        return {self.player.set_util(),
                self.player.purchase_counter(),
                self.player.update_prospect()}


class No5Result(Page):

    def is_displayed(self):
        return self.round_number <= self.session.config['rounds']

    def vars_for_template(self):
        return {
            'lists': eval(self.player.sel_prospect_payoff),
            'round': self.subsession.round_number,
            'playable_rounds': self.session.config['rounds'],
            'util': self.player.util
        }

    def before_next_page(self):
        return {self.player.set_util(),
                self.player.purchase_counter(),
                self.player.update_prospect()}


class No6EndQuestionnaire(Page):

    def is_displayed(self):
        return self.round_number == self.session.config['rounds']

    form_model = "player"
    form_fields = ["Name", "Age", "Gender"]

    def before_next_page(self):
        if self.round_number == self.session.config['rounds']:
            return {
                self.player.set_payoff()
            }


class No6EndResult(Page):

    def is_displayed(self):
        return self.round_number == self.session.config['rounds']

    def vars_for_template(self):
        return {
            'payoff': self.player.payoff
        }




page_sequence = [No1Introduction,
                 No2Instructions1,
                 No2Instructions2,
                 No3Start,
                 No4Purchase,
                 No5Result,
                 No6EndQuestionnaire,
                 No6EndResult]
