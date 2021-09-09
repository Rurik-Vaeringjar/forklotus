# pylotus/wf_api.py

from . import session
from .exceptions import *

class wf_api(object):
	_platforms = ['pc', 'ps4', 'xb1', 'swi']
	server = "https://api.warframestat.us"

	@staticmethod
	def get_platforms():
		return wf_api._platforms

	def __init__(self, platform):
		if platform not in self._platforms:
			raise NonPlatformError(platform)
		self.platform = platform


	########################################################################################################################################################## WORLDSTATE INFO
	def get_all_worldstate_info(self):
		path = "{server}/{platform}".format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_all_worldstate_info')
		return response.json()

	def get_alert_info(self):
		path = '{server}/{platform}/alerts'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_alert_info')
		return response.json()

	def get_cetus_info(self):
		path = '{server}/{platform}/cetusCycle'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_cetus_info')
		return response.json()

	def get_vallis_info(self):
		path = '{server}/{platform}/vallisCycle'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_vallis_info')
		return response.json()

	def get_deimos_info(self):
		path = "{server}/{platform}/cambionCycle".format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_deimos_info')
		return response.json()

	def get_conclave_challenge_info(self):
		path = '{server}/{platform}/conclaveChallenges'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_conclave_challenge_info')
		return response.json()

	def get_construction_progress_info(self):
		path = '{server}/{platform}/constructionProgress'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_construction_progress_info')
		return response.json()

	def get_daily_deals_info(self):
		path = '{server}/{platform}/dailyDeals'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_daily_deals_info')
		return response.json()

	def get_event_info(self):
		path = '{server}/{platform}/events'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_event_info')
		return response.json()

	def get_fissure_info(self):
		path = '{server}/{platform}/fissures'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_fissure_info')
		return response.json()

	def get_flash_sale_info(self):
		path = '{server}/{platform}/flashSales'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_flash_sale_info')
		return response.json()

	def get_invasion_info(self):
		path = '{server}/{platform}/invasions'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_invasion_info')
		return response.json()

	def get_news_info(self):
		path = '{server}/{platform}/news'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_news_info')
		return response.json()

	def get_nightwave_info(self):
		path = '{server}/{platform}/nightwave'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_nightwave_info')
		return response.json()

	def get_persistent_enemy_info(self):
		path = '{server}/{platform}/persistentEnemies'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_persistent_enemy_info')
		return response.json()

	def get_sentient_outpost_info(self):
		path = '{server}/{platform}/sentientOutposts'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_sentient_outpost_info')
		return response.json()

	def get_sanctuary_status_info(self):
		path = '{server}/{platform}/simaris'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_sanctuary_status_info')
		return response.json()

	def get_sortie_info(self):
		path = '{server}/{platform}/sortie'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_sortie_info')
		return response.json()

	def get_syndicate_info(self):
		path = '{server}/{platform}/syndicateMissions'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_syndicate_info')
		return response.json()

	def get_timestamp_info(self):
		path = '{server}/{platform}/timestamp'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_timestamp_info')
		return response.json()

	def get_void_trader_info(self):
		path = "{server}/{platform}/voidTrader".format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_void_trader_info')
		return response.json()

	def get_steelpath_info(self):
		path = "{server}/{platform}/steelPath".format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_steelpath_info')
		return response.json()

	########################################################################################################################################################## SEARCHABLE INFO
	def get_riven_info(self):
		path = '{server}/{platform}/rivens'.format(server=self.server, platform=self.platform)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_riven_info')
		return response.json()

	def get_specific_riven_info(self, weaponName):
		path = '{server}/{platform}/rivens/search/{query}'.format(server=self.server, platform=self.platform, query=weaponName)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_specific_riven_info')
		return response.json()

	def get_weapon_info(self, weapon):
		path = "{server}/weapons/search/{query}".format(server=self.server, query=weapon)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_weapon_info")
		return response.json()

	def get_warframe_info(self, warframe):
		path = "{server}/warframes/search/{query}".format(server=self.server, query=warframe)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_warframe_info")
		return response.json()

	def get_drop_info(self, item):
		path = "{server}/drops/search/{query}".format(server=self.server, query=item)
		response = session.get(path)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_drop_info")
		return response.json()

