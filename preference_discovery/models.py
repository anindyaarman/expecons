from random import sample
import random

import numpy as np
import pandas as pd
from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Putu Sanjiwacika Wibisana'

doc = """
Adaptation of Preference Discovery by Delaney, Jacobson and Moenig (2018) for risk preference discovery.
"""

class Constants(BaseConstants):
    name_in_url = 'preference_discovery_v2'
    players_per_group = None
    num_rounds = 33
    num_training_rounds = 3
    num_real_rounds_per_session = 10
    endowment = c(1000)
    multiplier = 2
    with open('preference_discovery/Lottery.csv', encoding="utf-8") as file:
        prospects = pd.read_csv(file)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    payoff_thisround = models.CurrencyField()
    player_payoff = models.CurrencyField()

    def set_payoff(self):
        players = self.get_players()
        payoff_thisround = [p.payoff_thisround for p in players]
        self.player_payoff = sum(payoff_thisround)

    def set_tot_payoffs(self):
        player_payoff = sum([p.payoff for p in self.player.in_previous_rounds()])
        return player_payoff


class Player(BasePlayer):

    def sequence_setup(self):
        set1 = Constants.prospects[Constants.prospects['Game_Type'] == "Block_1"]
        set2 = Constants.prospects[Constants.prospects['Game_Type'] == "Block_2"]
        set3 = Constants.prospects[Constants.prospects['Game_Type'] == "Block_3"]
        orgnl_sequence = [set1, set2, set3]
        player_sequence = random.sample(orgnl_sequence, len(orgnl_sequence))
        player_prospects = player_sequence[0].append(player_sequence[1], ignore_index=True).append(player_sequence[2],ignore_index=True)
        player_prospects['rounds'] = [self.session.config["rounds"]] * 63
        self.participant.vars["p_app_sequence"] = player_prospects  # Contains the dataframe for all parameters for all players
    
    def set_player_param(self):
        # round settings
        self.training_round = 1 if self.round_number <= self.session.config["training_rounds"] else 0
        if self.round_number == 1:
            self.participant.vars["prospect_table"] = Constants.prospects
            self.endowment = self.session.config["endowment"]
            self.participant.vars["payoff_vector"] = list()
        elif self.round_number == self.session.config["training_rounds"] + 1:
            self.participant.vars["prospect_table"] = Constants.prospects
        # randomizer
        rand = sample(list(range(0, 20)), 4)
        rand.append(20)
        self.participant.vars["random_indexes"] = rand
        self.participant.vars["displayed_lotteries"] = list(
            self.participant.vars["prospect_table"].loc[self.participant.vars["random_indexes"], "Index"])
        self.participant.vars["displayed_prospects"] = self.participant.vars["prospect_table"].loc[
                                                       self.participant.vars["random_indexes"], :]
        self.displayed_lotteries = str(list(self.participant.vars["displayed_lotteries"]))

    def payoff_realizer(self):
        df = self.participant.vars["displayed_prospects"]
        print("new")
        print(df)
        print("ori")
        print(self.participant.vars["displayed_prospects"])
        df["Allocation"] = [self.Lotere_A, self.Lotere_B, self.Lotere_C, self.Lotere_D,
                              self.Lotere_E]  ### df[["Allocation"]] = [0,0,2,1,2]
        df["payoff"] = [0, 0, 0, 0, 0]
        for i in self.participant.vars["random_indexes"]:
            df.loc[i,"A_or_B"] = np.random.choice(["A","B"], p=[df.loc[i,"p1"],df.loc[i,"p2"]])
            df.loc[i,"payoff"] = df.loc[i,"x1"] * df.loc[i,"Allocation"] if df.loc[i,"A_or_B"] == "A" else df.loc[i,"x2"] * df.loc[i,"Allocation"]
        self.payoff_thisround = int(df[["payoff"]].sum())
        self.payoff = self.payoff_thisround
        if not self.training_round:
            self.participant.vars["payoff_vector"].append(self.payoff_thisround)
        self.participant.vars["prospect_table"].update(df)
        for i in range(0, len(self.participant.vars["prospect_table"])):
            if self.participant.vars["prospect_table"].loc[i, "A_or_B"] != "X":
                if self.participant.vars["prospect_table"].loc[i, "A_or_B"] == "A":
                    self.participant.vars["prospect_table"].loc[i, "p1"] = 1
                    self.participant.vars["prospect_table"].loc[i, "p2"] = 0
                elif self.participant.vars["prospect_table"].loc[i, "A_or_B"] == "B":
                    self.participant.vars["prospect_table"].loc[i, "p1"] = 0
                    self.participant.vars["prospect_table"].loc[i, "p2"] = 1
            else:
                pass
        self.participant.vars["displayed_prospects"] = df

    def set_payoff(self):
        self.payiff = self.payoff_thisround
    
    endowment = models.IntegerField()
    player_payoff = models.IntegerField()
    payoff_thisround = models.IntegerField()
    displayed_lotteries = models.StringField()
    training_round = models.BooleanField()

    
    Lotere_A = models.IntegerField(min=0, max=10, initial=0)
    Lotere_B = models.IntegerField(min=0, max=10, initial=0)
    Lotere_C = models.IntegerField(min=0, max=10, initial=0)
    Lotere_D = models.IntegerField(min=0, max=10, initial=0)
    Lotere_E = models.IntegerField(min=0, max=10, initial=0)
    

    ## Vars for questionnaire

    Name = models.StringField(label="Nama Lengkap Anda:")
    Age = models.IntegerField(label="Usia:", min=14, max=35)
    Gender = models.StringField(label="Gender:", choices=["Pria", "Wanita"])
