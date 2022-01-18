def split_location(loc: str):
	if " (" in loc and ")" in loc:
		part = loc.partition(" (")
		node = part[0]
		part = part[2].partition(")")
		planet = part[0]
	elif "/" in loc:
		part = loc.partition("/")
		node = part[2]
		planet = part[0]

	return node, planet

def fix_thumbnail(name: str) -> str:
	if name == "Equinox":
		return "https://static.wikia.nocookie.net/warframe/images/e/ee/EquinoxSolo.png"
	return None

def fix_passive(passive: str, name: str) -> str:
	if name.startswith("Ash"):
		passive = passive.replace("|DAMAGE|", "25")
		passive = passive.replace("|DURATION|", "50")
	elif name.startswith("Baruuk"):
		passive = passive.replace("|PERCENT|", "50")
	elif name.startswith("Caliban"):
		passive = passive.replace("|PCT|", "50")
	elif name.startswith("Ember"):
		passive = passive.replace("|STRENGTH|", "5")
		passive = passive.replace("|RANGE|", "50")
		passive = passive.replace("<DT_FIRE>", "")
	elif name.startswith("Equinox"):
		passive = passive.replace("|PERCENT|", "10")
	elif name.startswith("Excalibur"):
		passive = passive.replace("|DAMAGE|", "10")
		passive = passive.replace("|SPEED|", "10")
	elif name.startswith("Frost"):
		passive = passive.replace("|CHANCE|", "10")
		passive = passive.replace("|DURATION|", "20")
	elif name.startswith("Gara"):
		passive = passive.replace("lasting |DURATION|s", "within 12m, lasting 10s,")
	elif name.startswith("Garuda"):
		passive = passive.replace("|DAMAGE|%.S", "100%. S")
	elif name.startswith("Gauss"):
		passive = passive.replace("|SPEED|", "120")
		passive = passive.replace("|DELAY|", "80")
	elif name.startswith("Grendel"):
		passive = passive.replace("|ARMOUR|", "50")
	elif name.startswith("Harrow"):
		passive = passive.replace("d.S", "d (maximum 2400) .S")
	elif name.startswith("Hydroid"):
		passive = passive.replace("|CHANCE|", "50")
		passive = passive.replace("|DURATION|", "15")
	elif name.startswith("Ivara"):
		passive = passive.replace("|RADIUS|", "20")
	elif name.startswith("Khora"):
		passive = passive.replace("|SPEED|", "15")
		passive = passive.replace("|DURATION|", "45")
	elif name.startswith("Lavos"):
		passive = passive.replace("|DURATION|s.H", "10s. H")
	elif name.startswith("Limbo"):
		passive = passive.replace("|DURATION|s.", "5s. Others can use the portal to enter the rift for 15s.")
		passive = passive.replace("|ENERGY|", "10")
	elif name.startswith("Loki"):
		passive = passive.replace("|MULT|", "10")
		passive = passive.replace(".", ", up to 60 seconds.")
	elif name.startswith("Mesa"):
		passive = passive.replace("|SPEED|", "15")
		passive = passive.replace("|RELOAD|", "25")
		passive = passive.replace("|HEALTH|", "50")
	elif name.startswith("Mirage"):
		passive = passive.replace("|DURATION|", "85")
		passive = passive.replace("|SPEED|", "50")
	elif name.startswith("Nekros"):
		passive = passive.replace("|HEALTH|", "5")
		passive = passive.replace("|RADIUS|", "10")
	elif name.startswith("Nezha"):
		passive = passive.replace("|SPEED|", "60")
		passive = passive.replace("|RANGE|", "35")
	elif name.startswith("Nidus"):
		passive = passive.replace("|STACKS|", "15")
		passive = passive.replace("|DURATION|", "5")
		passive = passive.replace("|HEAL|", "50")
	elif name.startswith("Nova"):
		passive = passive.replace("|RANGE|", "6")
		passive = passive.replace("|DAMAGE|", "250")
	elif name.startswith("Nyx"):
		passive = passive.replace("|PERCENT|", "20")
	elif name.startswith("Oberon"):
		passive = passive.replace("|HEALTH|", "25")
		passive = passive.replace("buffs", "links")
	elif name.startswith("Octavia"):
		passive = passive.replace("|ENERGY|", "1")
		passive = passive.replace("|DURATION|", "30")
		passive = passive.replace("|RANGE|", "15")
	elif name.startswith("Protea"):
		passive = passive.replace("|CASTS|", "4")
		passive = passive.replace("|STRENGTH|", "100")
	elif name.startswith("Revenant"):
		passive = passive.replace("|RANGE|", "7.5")
		passive = passive.replace("|DAMAGE|", "100")
	elif name.startswith("Rhino"):
		passive = passive.replace("|DAMAGE| damage", "damage in a 6m radius")
	elif name.startswith("Saryn"):
		passive = passive.replace("|DURATION|", "25")
	elif name.startswith("Trinity"):
		passive = passive.replace("|SPEED|", "25")
		passive = passive.replace("|RANGE|", "50")
	elif name.startswith("Valkyr"):
		passive = passive.replace("|PERCENT|", "50")
	elif name.startswith("Vauban"):
		passive = passive.replace("|DAMAGE|", "25")
	elif name.startswith("Volt"):
		passive = passive.replace("|DAMAGE| Damage per meter ", "5 damage per meter, maximum 1000, ")
	elif name.startswith("Xaku"):
		passive = passive.replace("|CHANCE|", "25")
	elif name.startswith("Yareli"):
		passive = passive.replace("|CHANCE|", "200")
		passive = passive.replace("|TIME|", "5")
	elif name.startswith("Zephyr"):
		passive = passive.replace("|CRIT|", "150")

	return passive

def fix_ability(ability: str, name: str) -> str:
	#General Changes
	if "<DT_POISON>" in ability:
		ability = ability.replace("<DT_POISON>", "")
	if "<DT_FREEZE>" in ability:
		ability = ability.replace("<DT_FREEZE>", "")
	if "<DT_ELECTRICITY>" in ability:
		ability = ability.replace("<DT_ELECTRICITY>", "")
	if "<DT_FIRE>" in ability:
		ability = ability.replace("<DT_FIRE>", "")
	if "<DT_CORROSIVE>" in ability:
		ability = ability.replace("<DT_CORROSIVE>", "")
	if "<DT_VIRAL>" in ability:
		ability = ability.replace("<DT_VIRAL>", "")
	#Specific Changes
	if name == "Magnetize":
		ability = ability.replace(".(", ".\n(")
	elif name == "Grenade Fan":
		ability = ability.replace(".(", ".\n(")
		ability = ability.replace("XC", "X: C")
		ability = ability.replace("SP", "S: P")
	elif name == "Temporal Anchor":
		ability = ability.replace(".D", ". D")
	elif (	name == "Ophidian Bite" or name == "Vial Rush" or 
			name == "Transmutation Probe" or name == "Catalyze"):
		ability = ability.replace(".H", ". H")
	
	
	return ability