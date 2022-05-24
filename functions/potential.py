import matplotlib.pyplot as plt
import functions.getAverage as average
import streamlit as st
import functions.common as common
import uuid

import pandas as pd

def getPotentialsHistogram(difference_crystal, difference_compared, crystal_plc, compared_team):
    fifa_15_players = pd.read_csv('players_15.csv', usecols= ['player_url', 'long_name', 'player_positions', 'overall', 'potential', 'age', 'club_name', 'league_name', 'attacking_finishing', 'passing', 'defending', 'short_name'])
    eng_league = "English Premier League"
    compared_team = "Chelsea"
    crystal_plc = "Crystal Palace"
    col1Pot, col2Pot, col3Pot = st.columns(3)

    with col1Pot:
        #Average player rate by role
        average.getAveragePlayerOverallRateByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), uuid.uuid1())
    # Crystal palace histogram
    fig, ax = plt.subplots(figsize =(8, 5))
    ax.hist(difference_crystal, bins = [0, 5, 10, 15, 20], color="#92B4EC")

    plt.xlabel("Potential")
    plt.ylabel("Number of players")
    plt.title("Distribution of the potential of the {} players".format(crystal_plc))

    # Show plot
    with col2Pot:
        st.pyplot(fig)


    fig, ax = plt.subplots(figsize =(8, 5))
    ax.hist(difference_compared, bins = [0, 5, 10, 15, 20], color="#FFE69A")

    plt.xlabel("Potential")
    plt.ylabel("Number of players")
    plt.title("Distribution of the potential of the {} players".format(compared_team))

    # Show plot
    with col3Pot:
        st.pyplot(fig)

def calcPotentialOverallDiff(potential_list, overall_list, difference):
    zip_object = zip(potential_list, overall_list)
    
    for potential_i, overall_i in zip_object:
        if potential_i > overall_i: 
            difference.append(potential_i-overall_i)
    return difference

def listDescendingOrder(list_values):
    return list_values.sort(reverse=True)

def format_name_list(list_name):
    formatted_list = []
    for el in list_name:
        formatted_list.append(el[:4])
    return formatted_list

def displayPotentialList(team_name, dictionary_potential):
    option = st.selectbox(
        '{} players potential'.format(team_name),
        ['Select a potential range', [0, 5], [5, 10], [10, 15], [15, 20], [20, 25]])

    if option != 'Select a potential range':
        for key in dictionary_potential:
            if dictionary_potential[key] >= option[0] and dictionary_potential[key] <= option[1]:
                st.write('{}: '.format(key), dictionary_potential[key])
