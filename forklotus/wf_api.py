# pylotus/wf_api.py

from . import session
from .exceptions import NonPlatformError, NonLanguageError, StatusCodeError

class wf_api(object):
	_platforms = ['pc', 'ps4', 'xb1', 'swi']
	_languages = ['en', 'de', 'es', 'fr', 'it']
	server = "https://api.warframestat.us"
	

	@staticmethod
	def get_platforms():
		return wf_api._platforms

	def __init__(self, platform, language='en'):
		if platform not in self._platforms:
			raise NonPlatformError(platform)
		self.platform = platform

		if language not in self._languages:
			raise NonLanguageError(language)
		self.language = language


	########################################################################################################################################################## WORLDSTATE INFO
	def get_all_worldstate_info(self):
		path = "{server}/{platform}/?language={language}".format(server=self.server, platform=self.platform, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_all_worldstate_info')
		return response.json()
	
	def get_worldstate_info(self, info):
		path = '{server}/{platform}/{info}/?language={language}'.format(server=self.server, platform=self.platform, info=info, language=self.language)
		response = session.get(path, timeout=1.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, f"get_worldstate_info({info})")
		return response.json()
	
	def get_alert_info(self):
		return self.get_worldstate_info("alerts")
		
	def get_arbitration_info(self):
		return self.get_worldstate_info("arbitration")

	def get_cetus_info(self):
		return self.get_worldstate_info("cetusCycle")
		
	def get_vallis_info(self):
		return self.get_worldstate_info("vallisCycle")

	def get_deimos_info(self):
		return self.get_worldstate_info("cambionCycle")

	def get_conclave_challenge_info(self):
		return self.get_worldstate_info("conclaveChallenges")

	def get_construction_progress_info(self):
		return self.get_worldstate_info("constructionProgress")

	def get_daily_deals_info(self):
		return self.get_worldstate_info("dailyDeals")

	def get_event_info(self):
		return self.get_worldstate_info("events")
	
	def get_fissure_info(self):
		return self.get_worldstate_info("fissures")
	
	def get_flash_sale_info(self):
		return self.get_worldstate_info("flashSales")
	
	def get_invasion_info(self):
		self.get_worldstate_info("invasions")
	
	def get_news_info(self):
		return self.get_worldstate_info("news")

	def get_nightwave_info(self):
		return self.get_worldstate_info("nightwave")

	def get_persistent_enemy_info(self):
		return self.get_worldstate_info("persistentEnemies")

	def get_sentient_outpost_info(self):
		return self.get_worldstate_info("sentientOutposts")

	def get_sanctuary_status_info(self):
		return self.get_worldstate_info("simaris")

	def get_sortie_info(self):
		return self.get_worldstate_info("sortie")
	
	def get_archon_hunt_info(self):
		return self.get_worldstate_info("archonHunt")
	
	def get_syndicate_info(self):
		return self.get_worldstate_info("syndicateMissions")
	
	def get_timestamp_info(self):
		return self.get_worldstate_info("timestamp")
		
	def get_void_trader_info(self):
		return self.get_worldstate_info("voidTrader")

	def get_steelpath_info(self):
		return self.get_worldstate_info("steelPath")

	########################################################################################################################################################## SEARCHABLE INFO
	def get_riven_info(self):
		path = '{server}/{platform}/rivens/?language={language}'.format(server=self.server, platform=self.platform, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_riven_info')
		return response.json()

	def get_specific_riven_info(self, weaponName):
		path = '{server}/{platform}/rivens/search/{query}?language={language}'.format(server=self.server, platform=self.platform, query=weaponName, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, 'get_specific_riven_info')
		return response.json()

	def get_weapon_info(self, weapon):
		path = "{server}/weapons/search/{query}?language={language}".format(server=self.server, query=weapon, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_weapon_info")
		return response.json()

	def get_weapon_info_sr(self, weapon):
		path = "{server}/weapons/{query}?language={language}".format(server=self.server, query=weapon, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_weapon_info")
		return response.json()

	def get_warframe_info(self, warframe):
		path = "{server}/warframes/search/{query}?language={language}".format(server=self.server, query=warframe, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_warframe_info")
		return response.json()

	def get_warframe_info_sr(self, warframe):
		path = "{server}/warframes/{query}?language={language}".format(server=self.server, query=warframe, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_warframe_info_sr")
		return response.json()

	def get_drop_info(self, item):
		path = "{server}/drops/search/{query}?language={language}".format(server=self.server, query=item, language=self.language)
		response = session.get(path, timeout=3.0)
		if response.status_code != 200:
			raise StatusCodeError(response.status_code, "get_drop_info")
		return response.json()

