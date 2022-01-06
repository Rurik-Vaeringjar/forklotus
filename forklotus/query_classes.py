# forklotus/query_classes.py

from .exceptions import *

from pprint import pprint

def split_location(loc: str):
	if "/" in loc:
		part = loc.partition("/")
		return part[2], part[0]

#This is the only one that works right now
class RivenInfo:
	_riven_keys = ['unrolled', 'rerolled']

	def __init__(self, riven_dict):
		if not isinstance(riven_dict, dict):
			raise DictTypeError('Riven', riven_dict)
		for key in self._trader_keys:
			if key not in riven_dict.keys():
				raise DictKeyError('Riven', key)
		self.unrolled = self.Rolled(riven_dict['unrolled'])
		self.rerolled = self.Rolled(riven_dict['rerolled'])

	class Rolled:
		_rolled_keys = ['median', 'avg', 'stddev', 'min', 'max']

		def __init__(self, rolled_dict):
			if not isinstance(rolled_dict, dict):
				raise DictTypeError('Rolled', rolled_dict)
			for key in self._trader_keys:
				if key not in rolled_dict.keys():
					raise DictKeyError('Rolled', key)
			self.median = rolled_dict['median']
			self.avg = rolled_dict['avg']
			self.stddev = rolled_dict['stddev']
			self.min = rolled_dict['min']
			self.max = rolled_dict['max']

# WARNING: UNSTABLE AS ALL HELL
# This is another jacked up one, api documentation clearly isn't right for this one, going to have to do it manually.
class WarframeInfo:
	_warframe_keys = [	'abilities', 'armor', 'components', 'description', 'health', 
						'imageName', 'introduced', 'masteryReq', 'name', 'passiveDescription', 'patchlogs',
						'polarities', 'power', 'releaseDate', 'shield', 'sprint', 'sprintSpeed', 'stamina',
						'uniqueName', 'wikiaThumbnail', 'wikiaUrl']

	def __init__(self, warframe_dict):
		if not isinstance(warframe_dict, dict):
			raise DictTypeError('Warframe', warframe_dict)
		for key in self._warframe_keys:
			if key not in warframe_dict.keys():
				raise DictKeyError('Warframe', key)
		
		#pprint(warframe_dict)

		self.abilities = warframe_dict['abilities']
		self.armor = warframe_dict['armor']
		self.aura = warframe_dict['aura'] if 'aura' in warframe_dict.keys() else None
		#self.buildPrice = warframe_dict['buildPrice']
		#self.buildQuantity = warframe_dict['buildQuantity']
		#self.buildTime = warframe_dict['buildTime']
		#self.category = warframe_dict['category']
		#self.color = warframe_dict['color']
		self.components = warframe_dict['components']
		self.conclave = warframe_dict['conclave'] if 'conclave' in warframe_dict.keys() else None
		self.description = warframe_dict['description']
		self.exalted = warframe_dict['exalted'] if 'exalted' in warframe_dict.keys() else None
		self.health = warframe_dict['health']
		self.imageName = warframe_dict['imageName']
		self.introduced = warframe_dict['introduced']
		self.masteryReq = warframe_dict['masteryReq']
		self.name = warframe_dict['name']
		self.passiveDescription = warframe_dict['passiveDescription']
		self.patchlogs = warframe_dict['patchlogs']
		self.polarities = warframe_dict['polarities']
		self.power = warframe_dict['power']
		self.releaseDate = warframe_dict['releaseDate']
		self.shield = warframe_dict['shield']
		self.sprint = warframe_dict['sprint']
		self.sprintSpeed = warframe_dict['sprintSpeed']
		self.stamina = warframe_dict['stamina']
		self.uniqueName = warframe_dict['uniqueName']
		self.wikiaThumbnail = warframe_dict['wikiaThumbnail']
		self.wikiaUrl = warframe_dict['wikiaUrl']



#WORK IN PROGRESS: Abandon all hope ye who enter here.
#This nonsense doesn't work because the weapon information is a tangled web of madness, or I'm just very dumb...
class WeaponInfo:
	_weapon_keys = ['name', 'description', 'type', 'tradable', 'category', 'wikiaThumbnail', 'masteryReq', 'disposition', 'attacks']

	def __init__(self, weapon_dict):
		if not isinstance(weapon_dict, dict):
			raise DictTypeError("Weapon", weapon_dict)
		for key in self._weapon_keys:
			if key not in weapon_dict.keys():
				raise DictKeyError('Weapon', key)
		self.name = weapon_dict['name']
		self.description = weapon_dict['description']
		self.type = weapon_dict['type']
		self.tradable = weapon_dict['tradable']
		self.category = weapon_dict['category']
		self.thumbnail = weapon_dict['wikiaThumbnail']
		self.masteryReq = weapon_dict['masteryReq']
		self.disposition = weapon_dict['disposition']

		#weapon stats
		self.attacks = [self.Attack(attack) for attack in weapon_dict['attacks']]

	class Attack:
		_perm_attack_keys = ['crit_chance', 'crit_mult', 'status_chance', 'damage']		

		def __init__(self, attack_dict):
			if not isinstance(attack_dict, dict):
				raise DictTypeError('Attack', attack_dict)
			for key in self._perm_attack_keys:
				if key not in attack_dict.keys():
					raise DictKeyError('Attack', key)
			self.name = attack_dict['name'] if 'name' in attack_dict.keys() else None
			self.duration = attack_dict['duration'] if 'duration' in attack_dict.keys() else None
			self.radius = attack_dict['radius'] if 'radius' in attack_dict.keys() else None
			self.speed = attack_dict['speed']
			self.pellet = Pellet(attack_dict['pellet']) if 'pellet' in attack_dict.keys() else None
			self.crit_chance = attack_dict['crit_chance']
			self.crit_mult = attack_dict['crit_mult']
			self.status_chance = attack_dict['status_chance']
			self.charge_time = attack_dict['charge_time'] if 'charge_time' in attack_dict.keys() else None
			self.shot_time = attack_dict['shot_time'] if 'shot_time' in attack_dict.keys() else None
			self.shot_type = attack_dict['shot_type'] if 'shot_type' in attack_dict.keys() else None
			self.flight = attack_dict['flight'] if 'flight' in attack_dict.keys() else None
			self.damage = self.Damage(attack_dict['damage'])
		
		class Damage:
			#Can't rely on these keys being present in damage_dict
			"""_damage_keys = ['impact', 'puncture', 'slash', 'heat', 'cold', 'electric', 'toxin', 
							'gas', 'viral', 'corrosive', 'blast', 'magnetic', 'radiation', 
							'true', 'void']"""
			
			def __init__(self, damage_dict):
				if not isinstance(damage_dict, dict):
					raise DictTypeError('Damage', damage_dict)
				self.impact = damage_dict['impact'] if 'impact' in damage_dict.keys() else 0.0
				self.puncture = damage_dict['puncture'] if 'puncture' in damage_dict.keys() else 0.0
				self.slash = damage_dict['slash'] if 'slash' in damage_dict.keys() else 0.0
				self.heat = damage_dict['heat'] if 'heat' in damage_dict.keys() else 0.0
				self.cold = damage_dict['cold'] if 'cold' in damage_dict.keys() else 0.0
				self.electric = damage_dict['electric'] if 'electric' in damage_dict.keys() else 0.0
				self.toxin = damage_dict['toxin'] if 'toxin' in damage_dict.keys() else 0.0
				self.gas = damage_dict['gas'] if 'gas' in damage_dict.keys() else 0.0
				self.viral = damage_dict['viral'] if 'viral' in damage_dict.keys() else 0.0
				self.corrosive = damage_dict['corrosive'] if 'corrosive' in damage_dict.keys() else 0.0
				self.blast = damage_dict['blast'] if 'blast' in damage_dict.keys() else 0.0
				self.magnetic = damage_dict['magnetic'] if 'magnetic' in damage_dict.keys() else 0.0
				self.radiation = damage_dict['radiation'] if 'radiation' in damage_dict.keys() else 0.0
				self.true = damage_dict['true'] if 'true' in damage_dict.keys() else 0.0
				self.void = damage_dict['void'] if 'void' in damage_dict.keys() else 0.0

		class Pellet:
			_pellet_keys = ['name', 'count']
			
			def __init__(self, pellet_dict):
				if not isinstance(pellet_dict, dict):
					raise DictTypeError('Pellet', pellet_dict)
				for key in self._pellet_keys:
					if key not in pellet_dict.keys():
						raise DictTypeError('Pellet', pellet_dict)
				self.name = pellet_dict['name']
				self.count = pellet_dict['count']

#Doesn't work great yet, mainly because of how many ways the syntax changes in 'place'
class DropInfo:
	_drop_keys = ['item', 'place', 'rarity', 'chance']

	def __init__(self, drop_dict):
		if not isinstance(drop_dict, dict):
			raise DictTypeError('Drop', drop_dict)
		for key in self._drop_keys:
			if key not in drop_dict.keys():
				raise DictTypeError('Drop', drop_dict)
		self.item = drop_dict['item']
		self.place = drop_dict['place']
		self.rarity = drop_dict['rarity']
		self.chance = drop_dict['chance']
		self.node = None
		self.planet = None
		self.mission = None
		self.rotation = None
		self.isMob = True
		if " (" in self.place and ")" in self.place:
			self.isMob = False
			part = self.place.partition(" (")
			self.node, self.planet = split_location(part[0])
			if "), " in part[2]:
				part = part[2].partition("), ")
				self.mission = part[0]
				self.rotation = part[2]
			else:
				self.mission = part[2][0:len(part[2])-1]
		elif ", " in self.place:
			self.isMob = False
			part = self.place.partition(", ")
			self.mission = part[0]
			self.rotation = part[2]