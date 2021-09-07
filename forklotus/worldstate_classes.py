# forklotus/worldstate_classes.py

from .exceptions import *

def split_location(loc: str):
	if " (" in loc and ")" in loc:
		part = loc.partition(" (")
		node = part[0]
		part = part[2].partition(")")
		planet = part[0]

	return node, planet

class Fissure:
	_fissure_keys = ['id', 'activation', 'startString',
					 'expiry', 'active', 'node', 'missionType',
					 'enemy', 'tier', 'tierNum', 'expired',
					 'eta']
	
	#Depreciated with recent API change (addition of isStorm bool), kept for reference.
	"""_void_storms = [["Sover Strait (Earth)", "Iota Temple (Earth)", "Ogal Cluster (Earth)", "Korm's Belt (Earth)", "Bendar Cluster (Earth)", 
				"Beacon Shield Ring (Venus)", "Vesper Strait (Venus)", "Luckless Expanse (Venus)", "Falling Glory (Venus)", "Bifrost Echo (Venus)", "Orvin-Haarc (Venus)"],
				["Mordo Cluster (Saturn)", "Lupal Pass (Saturn)", "Nodo Gap (Saturn)", "Vand Cluster (Saturn)", "Kasio's Rest (Saturn)"],
				["Arva Vector (Neptune)", "Nu-Gua Mines (Neptune)", "Mammon's Prospect (Neptune)", "Brom Cluster (Neptune)", "Enkidu Ice Drifts (Neptune)", "Sovereign Grasp (Neptune)"],
				["Khufu Envoy (Pluto)", "Obol Crossing (Pluto)", "Profit Margin (Pluto)", "Peregrine Axis (Pluto)", "Seven Sirens (Pluto)", "Fenton's Field (Pluto)", 
				"Calabash (Veil)", "Numina (Veil)", "Arc Silver (Veil)", "Erato (Veil)", "Lu-Yan (Veil)", "Sabmir Cloud (Veil)", 
				"R-9 Cloud (Veil)", "Nsu Grid (Veil)", "H-2 Cloud (Veil)", "Flexa (Veil)"]]"""

	def __init__(self, fissure_dict):
		if not isinstance(fissure_dict, dict):
			raise DictTypeError('Fissure', fissure_dict)
		for key in self._fissure_keys:
			if key not in fissure_dict.keys():
				raise DictKeyError('Fissure', key)
		self.id = fissure_dict['id']
		self.activation = fissure_dict['activation']
		self.startString = fissure_dict['startString']
		self.expiry = fissure_dict['expiry']
		self.active = fissure_dict['active']
		self.location = fissure_dict['node']
		self.node, self.planet = split_location(self.location)
		self.missionType = fissure_dict['missionType']
		self.enemy = fissure_dict['enemy']
		self.tier = fissure_dict['tier']
		self.tierNum = fissure_dict['tierNum']
		self.expired = fissure_dict['expired']
		self.eta = fissure_dict['eta']
		self.isStorm = fissure_dict['isStorm']

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _fissure_keys

class Invasion:
	_invasion_keys = ['desc', 'attackingFaction', 'attackerReward', 'defendingFaction', 'defenderReward', 
					'nodeKey', 'vsInfestation', 'completion']

	def __init__(self, invasion_dict):
		if not isinstance(invasion_dict, dict):
			raise DictTypeError('Invasion', invasion_dict)
		for key in self._invasion_keys:
			if key not in invasion_dict.keys():
				raise DictKeyError('Invasion', key)
		self.desc = invasion_dict['desc']
		self.attackingFaction = invasion_dict['attackingFaction']
		self.attackerReward = self.Reward(invasion_dict['attackerReward'])
		self.defendingFaction = invasion_dict['defendingFaction']
		self.defenderReward = self.Reward(invasion_dict['defenderReward'])
		self.location = invasion_dict['node']
		self.node, self.planet = split_location(self.location)
		self.vsInfestation = invasion_dict['vsInfestation']
		self.completion = invasion_dict['completion']
	
	class Reward:
		_reward_keys = ['asString', 'countedItems', 'thumbnail']

		def __init__(self, reward_dict):
			if not isinstance(reward_dict, dict):
				raise DictTypeError('Reward', reward_dict)
			for key in self._reward_keys:
				if key not in reward_dict.keys():
					raise DictKeyError('Reward', key)
			self.asString = reward_dict['asString']
			reward = reward_dict['countedItems']
			self.count = reward[0]['count'] if reward else None
			self.type = reward[0]['type'] if reward else None
			self.thumbnail = reward_dict['thumbnail']

class CetusInfo:
	_cetus_keys = ['id', 'activation', 'isDay','expiry', 
				   'state', 'timeLeft', 'isCetus', 'shortString']

	def __init__(self, cetus_dict):
		if not isinstance(cetus_dict, dict):
			raise DictTypeError('CetusInfo', cetus_dict)
		for key in self._cetus_keys:
			if key not in cetus_dict.keys():
				raise DictKeyError('CetusInfo', key)
		self.id = cetus_dict['id']
		self.activation = cetus_dict['activation']
		self.shortString = cetus_dict['shortString']
		self.expiry = cetus_dict['expiry']
		self.isDay = cetus_dict['isDay']
		self.state = cetus_dict['state']
		self.timeLeft = cetus_dict['timeLeft']
		self.isCetus = cetus_dict['isCetus']

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _cetus_keys


class VallisInfo:
	_vallis_keys = ['id', 'isWarm','expiry','timeLeft']

	def __init__(self, vallis_dict):
		if not isinstance(vallis_dict, dict):
			raise DictTypeError('VallisInfo', vallis_dict)
		for key in self._vallis_keys:
			if key not in vallis_dict.keys():
				raise DictKeyError('VallisInfo', key)		
		self.id = vallis_dict['id']
		self.expiry = vallis_dict['expiry']
		self.isWarm = vallis_dict['isWarm']
		self.timeLeft = vallis_dict['timeLeft']

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _vallis_keys


class DeimosInfo:
	_deimos_keys = ["id", "expiry", "activation", "active"]

	def __init__(self, deimos_dict):
		if not isinstance(deimos_dict, dict):
			raise DictTypeError("DeimosInfo", deimos_dict)
		for key in self._deimos_keys:
			if key not in deimos_dict.keys():
				raise DictKeyError("DeimosInfo", key)
		self.id = deimos_dict["id"]
		self.expiry = deimos_dict["expiry"]
		self.activation = deimos_dict["activation"]
		self.active = deimos_dict["active"]
		self.isFass = True if self.active == "fass" else False

	def to_string(self):
		self_string = ""
		for k, v in vars(self).items():
			self_string += k + ": " + str(v) + "\n"
		return self_string

	def get_expected_keys(self):
		return _deimos_keys


class NewsInfo:
	_news_keys = ["date", "imageLink", "eta", "primeAccess",
				  "stream", "translations", "link", "update",
				  "id", "asString", "message", "priority"]

	def __init__(self, news_dict):
		if not isinstance(news_dict, dict):
			raise DictTypeError('NewsInfo', news_dict)
		for key in self._news_keys:
			if key not in news_dict.keys():
				raise DictKeyError('NewsInfo', key)
		self.date = news_dict["date"]
		self.imageLink = news_dict["imageLink"]
		self.eta = news_dict["eta"]
		self.primeAccess = news_dict["primeAccess"]
		self.stream = news_dict["stream"]
		self.translations = news_dict["translations"]
		self.link = news_dict["link"]
		self.update = news_dict["update"]
		self.id = news_dict["id"]
		self.asString = news_dict["asString"]
		self.message = news_dict["message"]
		self.priority = news_dict["priority"]

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _news_keys

class VoidTrader:
	_trader_keys = ['id', 'activation', 'expiry', 'character', 'location', 
					'inventory', 'psId', 'active', 'startString', 'endString']

	def __init__(self, trader_dic):
		#Yes, I broke convention calling it trader_dic instead of trader_dict.
		#The chance to make a stupid dick joke was too tempting to resist.
		if not isinstance(trader_dic, dict):
			raise DictTypeError('VoidTrader', trader_dic)
		for key in self._trader_keys:
			if key not in trader_dic.keys():
				raise DictKeyError('VoidTrader', key)
		self.id = trader_dic['id']
		self.activation = trader_dic['activation']
		self.expiry = trader_dic['expiry']
		self.character = trader_dic['character']
		self.location = trader_dic['location']
		self.relay, self.planet = split_location(self.location)
		self.psId = trader_dic['psId']
		self.active = trader_dic['active']
		self.startString = trader_dic['startString']
		self.endString = trader_dic['endString']
		self.inventory = []
		if trader_dic['inventory']:
			self.inventory = [self.Item(item) for item in trader_dic['inventory']]


	def to_string(self):
		self_string = ""
		for k, v in vars(self).items():
			self_string += k + ": " + str(v) + "\n"
		return self_string

	def get_expected_keys(self):
		return _trader_keys

	class Item:
		_item_keys = ['item', 'ducats', 'credits']

		def __init__(self, item_dict):
			if not isinstance(item_dict, dict):
				raise DictTypeError('Item', item_dict)
			for key in self._item_keys:
				if key not in item_dict.keys():
					raise DictKeyError('Item', key)
			self.name = item_dict['item']
			self.ducats = item_dict['ducats']
			self.credits = item_dict['credits']

		def to_string(self):
			self_string = ""
			for k, v in vars(self).items():
				self_string += k + ": " + str(v) + "\n"
			return self_string

		def get_expected_keys(self):
			return _trader_keys

