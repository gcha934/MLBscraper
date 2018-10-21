##1/2/3/4/5/6/7/8
##6/6/5/5/4/4/3/2
##i also want another rule: when the original differential occurs, send alert when the score differential decreases
# -*- coding: utf8 -*-
from __future__ import print_function
from pushbullet import Pushbullet
from settings import PB_KEY
pb = Pushbullet(PB_KEY)
import mlbgame
import datetime
import time

import lxml.etree as etree
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)



#create a list of games where notifications have been sent
Notiflist=[]
PreviousState={}

while True:
	try:
		now=datetime.datetime.now()-datetime.timedelta(1)
		games = mlbgame.day(now.year, now.month,now.day )
		print(now)

		for game in games:
	##	print(mlbgame.game.box_score(x.game_id)) #list of all games and its box score
			print(game)
			logging.info(now)


			 ## first game


			if(str(game.game_status) != "PRE_GAME" ):
				data = mlbgame.data.get_box_score(game.game_id)
				inning_state = str(mlbgame.game.overview(game.game_id).get('inning_state'))
				
				parsed = etree.parse(data)

				root = parsed.getroot()

				linescore = root.find('linescore')
				result = dict()
				result['game_id'] = game.game_id
				#get information of the current inning
				inning = int(linescore[-1].attrib['inning'])
				
				#get information of current score
				home_score=0
				away_score=0
				home_team=game.home_team
				away_team=game.away_team
				home_score=game.home_team_runs
				away_score=game.away_team_runs
				# 
				# only notify if its home team winning mid inning.
				# 
				score_difference=home_score-away_score

				if game.game_id not in Notiflist:
					if PreviousState.get(game.game_id)!= inning_state:
						if (inning==1 or inning==2) and (score_difference >=6) and inning_state == 'Bottom':
							print('bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif(inning==3 or inning ==4) and (score_difference >=5) and inning_state =='Bottom':
							print('bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif(inning==5 or inning ==6) and (score_difference >=4) and inning_state == 'Bottom':
							print('bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif inning==7 and (score_difference >=3) and inning_state == 'Bottom':
							print('bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif inning==8 and (score_difference >=2) and inning_state =='Bottom':
							print('bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (home_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")

						if (inning==1 or inning==2) and (score_difference <=-6) and inning_state == 'End':
							print('bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif(inning==3 or inning ==4) and (score_difference <=-5) and inning_state =='End':
							print('bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif(inning==5 or inning ==6) and (score_difference <=-4) and inning_state == 'End':
							print('bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif inning==7 and (score_difference <=-3) and inning_state == 'End':
							print('bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")
						elif inning==8 and (score_difference <=-2) and inning_state == 'End':
							print('bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							pb.push_note('bet','bet on %s. inning:%d %d:%d %s:%s'% (away_team,inning,home_score,away_score,home_team,away_team))
							Notiflist.append(game.game_id)
							logging.info("notified")

				PreviousState.update({game.game_id:inning_state})
				logging.info('inning:%d %d:%d %s:%s %s'% (inning,home_score,away_score,home_team,away_team,inning_state))


	except Exception as e:
		print(e)

	print("-----")
	time.sleep(60)


