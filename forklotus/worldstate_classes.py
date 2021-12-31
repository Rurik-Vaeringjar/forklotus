# forklotus/worldstate_classes.py

from .exceptions import *
from pprint import pprint

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
	
	#Unused with recent API change (addition of isStorm bool), kept for reference.
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
	
	def to_string(self):
		self_string = ""
		for k, v in vars(self).items():
			self_string += k + ": " + str(v) + "\n"
		return self_string

	def get_expected_keys(self):
		return _invasion_keys

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

		def to_string(self):
			self_string = ""
			for k, v in vars(self).items():
				self_string += k + ": " + str(v) + "\n"
			return self_string

		def get_expected_keys(self):
			return _reward_keys

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

	def __init__(self, trader_dict):
		if not isinstance(trader_dict, dict):
			raise DictTypeError('VoidTrader', trader_dict)
		for key in self._trader_keys:
			if key not in trader_dict.keys():
				raise DictKeyError('VoidTrader', key)
		self.id = trader_dict['id']
		self.activation = trader_dict['activation']
		self.expiry = trader_dict['expiry']
		self.character = trader_dict['character']
		self.location = trader_dict['location']
		self.relay, self.planet = split_location(self.location)
		self.psId = trader_dict['psId']
		self.active = trader_dict['active']
		self.startString = trader_dict['startString']
		self.endString = trader_dict['endString']
		self.inventory = []
		if trader_dict['inventory']:
			self.inventory = [self.Item(item) for item in trader_dict['inventory']]

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

#WARNING: untested!
class Sortie:
	_sortie_keys = ['id', 'activation', 'expiry', 'rewardPool', 'variants', 'boss', 'faction', 'expired', 'eta']

	def __init__(self, sortie_dict):
		if not isinstance(sortie_dict, dict):
			raise DictTypeError('Sortie', sortie_dict)
		for key in self._sortie_keys:
			if key not in sortie_dict.keys():
				raise DictKeyError('Sortie', key)
		self.id = sortie_dict['id']
		self.activation = sortie_dict['activation']
		self.expiry = sortie_dict['expiry']
		self.rewardPool = sortie_dict['rewardPool']
		self.variants = [self.Variant(variant) for variant in sortie_dict['variants']]
		self.boss = sortie_dict['boss']
		self.faction = sortie_dict['faction']
		self.expired = sortie_dict['expired']
		self.eta = sortie_dict['eta']

	def to_string(self):
		self_string = ""
		for k, v in vars(self).items():
			self_string += k + ": " + str(v) + "\n"
		return self_string

	def get_expected_keys(self):
		return _sortie_keys

	class Variant:
		_variant_keys = ['node', 'missionType', 'modifier', 'modifierDescription']

		def __init__(self, variant_dict):
			if not isinstance(variant_dict, dict):
				raise DictTypeError('Variant', variant_dict)
			for key in self._variant_keys:
				if key not in variant_dict.keys():
					raise DictKeyError('Variant', key)
			self.mission = variant_dict['node']
			self.node, self.planet = split_location(self.mission)
			self.missionType = variant_dict['missionType']
			self.modifier = variant_dict['modifier']
			self.modifierDescription = variant_dict['modifierDescription']

		def to_string(self):
			self_string = ""
			for k, v in vars(self).items():
				self_string += k + ": " + str(v) + "\n"
			return self_string

		def get_expected_keys(self):
			return _variant_keys

class SteelPath:
	_steelpath_keys = ['activation', 'expiry', 'currentReward', 'remaining', 'rotation', 'evergreens', 'incursions']

	def __init__(self, steelpath_dict):
		if not isinstance(steelpath_dict, dict):
			raise DictTypeError('SteelPath', steelpath_dict)
		for key in self._steelpath_keys:
			if key not in steelpath_dict.keys():
				raise DictKeyError('SteelPath', key)
		self.activation = steelpath_dict['activation']
		self.expiry = steelpath_dict['expiry']
		self.currentReward = self.Reward(steelpath_dict['currentReward'])
		self.remaining = steelpath_dict['remaining']
		self.rotation = [self.Reward(reward) for reward in steelpath_dict['rotation']]
		self.evergreen = [self.Reward(reward) for reward in steelpath_dict['evergreens']]
		#I have no idea what the hell the incursions in the api actually do, there isn't much information there.
		#self.incursions = [self.Incursion(incursion) for incursion in steelpath_dict['incursions']]
	
	def to_string(self):
		self_string = ""
		for k, v in vars(self).items():
			self_string += k + ": " + str(v) + "\n"
		return self_string

	def get_expected_keys(self):
		return _steelpath_keys

	class Reward:
		_reward_keys = ['name', 'cost']

		def __init__(self, reward_dict):
			if not isinstance(reward_dict, dict):
				raise DictTypeError('Reward', reward_dict)
			for key in self._reward_keys:
				if key not in reward_dict.keys():
					raise DictKeyError('Reward', key)
			self.name = reward_dict['name']
			self.cost = reward_dict['cost']
		
		def to_string(self):
			self_string = ""
			for k, v in vars(self).items():
				self_string += k + ": " + str(v) + "\n"
			return self_string

		def get_expected_keys(self):
			return _reward_keys

	#WARNING: Untested!
#	class Incursion:
#		_incursion_keys = ['id', 'activation', 'expiry']
#
#		def __init__(self, incursion_dict):
#			if not isinstance(incursion_dict, dict):
#				raise DictTypeError('Incursion', incursion_dict)
#			for key in self._incursion_keys:
#				if key not in incursion_dict.keys():
#					raise DictKeyError('Incursion', key)
#			self.id = incursion_dict['id']
#			self.activation = incursion_dict['activation']
#			self.expiry = incursion_dict['expiry']
#
#		def to_string(self):
#			self_string = ""
#			for k, v in vars(self).items():
#				self_string += k + ": " + str(v) + "\n"
#			return self_string
#
#		def get_expected_keys(self):
#			return _incursion_keys				
