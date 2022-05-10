import streamlit as st
import pandas as pd
import functions.getAverage as average
import functions.common as common
import functions.getAttribute as attribute

st.set_page_config(layout="wide")
fifa_15_players = pd.read_csv('players_15.csv', usecols= ['player_url', 'long_name', 'player_positions', 'overall', 'potential', 'age', 'club_name', 'league_name', 'attacking_finishing', 'passing', 'defending', 'short_name'])
eng_league = "English Premier League"
compared_team = "Chelsea"
crystal_plc = "Crystal Palace"

#Average player rate by role
# average.getAveragePlayerOverallRateByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players))

#Get finishing attribute for strikers
crystal_finishing = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'attacking_finishing')
compared_finishing = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'attacking_finishing')
crystal_finishing_name = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'short_name')
compared_finishing_name = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'short_name')

#Get passing attribute for midfields
crystal_passing = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'passing')
compared_passing = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'passing')
crystal_passing_name = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'short_name')
compared_passing_name = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'short_name')

#Get defending attribute for backs
crystal_defending = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'defending')
compared_defending = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'defending')
crystal_defending_name = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'short_name')
compared_defending_name = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'short_name')

#FINISHING and name sorted
Crystal_finishing_list = attribute.getTeam(crystal_finishing_name, crystal_finishing)
Compared_finishing_list = attribute.getTeam(compared_finishing_name, compared_finishing)
st.pyplot(attribute.displayMainAttributeByRole(Crystal_finishing_list, Compared_finishing_list, 'TEST', 'TEST', 'TEST', 1))

#PASSING and name sorted
Crystal_passing_list = attribute.getTeam(crystal_passing_name, crystal_passing)
Compared_passing_list = attribute.getTeam(compared_passing_name, compared_passing)
st.pyplot(attribute.displayMainAttributeByRole(Crystal_passing_list, Compared_passing_list, 'TEST', 'TEST', 'TEST', 2))

#DEFENDING and name sorted
Crystal_defending_list = attribute.getTeam(crystal_defending_name, crystal_defending)
Compared_defending_list = attribute.getTeam(compared_defending_name, compared_defending)
st.pyplot(attribute.displayMainAttributeByRole(Crystal_defending_list, Compared_defending_list, 'TEST', 'TEST', 'TEST', 3))
