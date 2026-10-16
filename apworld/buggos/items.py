from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:

    from .world import BuggosWorld

TALENT_NAME_TO_ID = {
    "Adrenaline": 1,
    "Aggressive Fertilization": 2,
    "A Mother's Touch": 3,
    "Armor Shredding": 4,
    "Artistic Zen": 5,
    "Best Parent": 6,
    "Boom Slug Explosion Radius": 7,
    "Boom Slug Explosion Radius II": 8,
    "Boom Slug Influence": 9,
    "Boom Slug Move Speed": 10,
    "Boom Slug Move Speed II": 11,
    "Boom Slug Thicker Skin": 12,
    "Builder Influence": 13,
    "Builder Legs": 14,
    "Goo on Death": 15,
    "Burrow Deeper": 16,
    "Carnivorous Floor Traps": 17,
    "Caustic Chemicals": 18,
    "Chew Faster": 19,
    "Chitinous Plates": 20,
    "Compressed Acid Glands": 21,
    "Construction Squad": 22,
    "Corrosive Chemicals": 23,
    "Dash Attack": 24,
    "Defender Influence": 25,
    "Defender Legs": 26,
    "Defensive Goo Tactics": 27,
    "Double Spines": 28,
    "Efficient Builders": 29,
    "Egg Twins": 30,
    "Enormous Belly": 31,
    "Enormous Belly II": 32,
    "Enormous Swarm Capacity": 33,
    "Extreme Swarm Capacity": 34,
    "Fast Twitch Muscles": 35,
    "Final Farewell": 36,
    "Flesh Walls": 37,
    "Flesh Wall Armor": 38,
    "Flesh Wall Health": 39,
    "Frenzied Egg Laying": 40,
    "Greater Compression": 41,
    "Greater Goo": 42,
    "Healthy Digestion": 43,
    "Hexagonal Breeding": 44,
    "Hooked Spines": 45,
    "Huge Spawn Size": 46,
    "Huge Swarm Capacity": 47,
    "Hunker Down": 48,
    "Infestation": 49,
    "Infestation II": 50,
    "Inorganic Nutrient Harvest": 51,
    "Insane Spawn Size": 52,
    "Insane Swarm Capacity": 53,
    "Interlocking Plates": 54,
    "Large Spawn Size": 55,
    "Large Swarm Capacity": 56,
    "Massive Swarm Capacity": 57,
    "Medium Spawn Size": 58,
    "Medium Swarm Capacity": 59,
    "More Acidic Spit": 60,
    "More Motherly": 61,
    "More Pus": 62,
    "Nutrient Gooier": 64,
    "Nutrient Pustules": 66,
    "Offensive Goo Tactics": 67,
    "Organic Nutrient Harvest": 68,
    "Overeating": 69,
    "Rapid Egg Laying": 70,
    "Razor Spines": 71,
    "Rebuilding": 72,
    "Regen Aura": 73,
    "Selective Breeding Program": 74,
    "Speed Goo": 76,
    "Speed Hooks": 77,
    "Spiked Carapace": 78,
    "Spiked Carapace II": 79,
    "Spiner Health": 80,
    "Spiner Influence": 81,
    "Spiner Legs": 82,
    "Spiner Range I": 83,
    "Spiner Range II": 84,
    "Spore Artillery": 85,
    "Spore Launchers": 86,
    "Spore Launchers Range": 87,
    "Spore Launchers Range II": 88,
    "Starting Nutrients": 89,
    "Starting Nutrients II": 90,
    "Starting Nutrients III": 91,
    "Starting Nutrients IV": 92,
    "Starting Nutrients V": 93,
    "Swarm Mother Influence": 94,
    "Swarm Mother Legs": 95,
    "Swarm Attack Speed": 96,
    "Swarm Attack Speed II": 97,
    "Swarm Attack Speed III": 98,
    "Swarmer Armor": 99,
    "Swarmer Guidance": 100,
    "Swarmer Health": 101,
    "Swarmer Influence": 102,
    "Swarm Health": 103,
    "Swarm Health II": 104,
    "Swarm Health III": 105,
    "Swarm Speed": 106,
    "Tearing Claws": 107,
    "The Defender": 108,
    "The Spiner": 109,
    "The Wasp": 110,
    "The Boom Slug": 111,
    "The Builder": 112,
    "The Swarm Mother": 113,
    "The Titan": 114,
    "The Warrior": 115,
    "Titan Legs": 116,
    "Titan Influence": 117,
    "Twin Juices": 118,
    "Uber Swarm Capacity": 119,
    "Warrior Endurance": 120,
    "Warrior Influence": 121,
    "Warrior Legs": 122,
    "Wasp Influence": 123,
    "Wasp Legs": 124,
    "Well Fed": 125,
    "Nutrient Recycle": 126,
    "Building Regeneration": 127,
    "Survival Instinct": 128,
    "Wasp Infestation": 129,
    "Radiation Resistant": 130,

    "The Swarmer" : 999,
}

FILLER_NAME_TO_ID = {
    "HP Increase": 131,
    "Armor Increase": 132,
    "Damage Increase": 133,
    "Attack Speed Increase": 134,
    "Move Speed Increase": 135,
    "Cost Decrease": 136,
}

TRAP_NAME_TO_ID = {
    "Set Damage to Zero for 30s" : 137,
    "Leave Current Mission" : 138,
    "Lock Swarmer for 2m" : 139
}

ITEM_NAME_TO_ID = {**TALENT_NAME_TO_ID, **FILLER_NAME_TO_ID, **TRAP_NAME_TO_ID}

UNIT_ITEM_NAMES = {
    0: "The Swarmer",
    1: "The Defender",
    2: "The Spiner",
    3: "The Wasp",
    4: "The Boom Slug",
    5: "The Builder",
    6: "The Swarm Mother",
    7: "The Warrior",
}

DEFAULT_ITEM_CLASSIFICATION = {
    "Adrenaline": ItemClassification.progression,
    "Aggressive Fertilization": ItemClassification.progression,
    "A Mother's Touch": ItemClassification.progression,
    "Armor Shredding": ItemClassification.progression,
    "Artistic Zen": ItemClassification.progression,
    "Best Parent": ItemClassification.progression,
    "Boom Slug Explosion Radius": ItemClassification.progression,
    "Boom Slug Explosion Radius II": ItemClassification.progression,
    "Boom Slug Influence": ItemClassification.progression,
    "Boom Slug Move Speed": ItemClassification.progression,
    "Boom Slug Move Speed II": ItemClassification.progression,
    "Boom Slug Thicker Skin": ItemClassification.progression,
    "Builder Influence": ItemClassification.progression,
    "Builder Legs": ItemClassification.progression,
    "Goo on Death": ItemClassification.progression,
    "Burrow Deeper": ItemClassification.progression,
    "Carnivorous Floor Traps": ItemClassification.progression,
    "Caustic Chemicals": ItemClassification.progression,
    "Chew Faster": ItemClassification.progression,
    "Chitinous Plates": ItemClassification.progression,
    "Compressed Acid Glands": ItemClassification.progression,
    "Construction Squad": ItemClassification.progression,
    "Corrosive Chemicals": ItemClassification.progression,
    "Dash Attack": ItemClassification.progression,
    "Defender Influence": ItemClassification.progression,
    "Defender Legs": ItemClassification.progression,
    "Defensive Goo Tactics": ItemClassification.progression,
    "Double Spines": ItemClassification.progression,
    "Efficient Builders": ItemClassification.progression,
    "Egg Twins": ItemClassification.progression,
    "Enormous Belly": ItemClassification.progression,
    "Enormous Belly II": ItemClassification.progression,
    "Enormous Swarm Capacity": ItemClassification.progression,
    "Extreme Swarm Capacity": ItemClassification.progression,
    "Fast Twitch Muscles": ItemClassification.progression,
    "Final Farewell": ItemClassification.progression,
    "Flesh Walls": ItemClassification.progression,
    "Flesh Wall Armor": ItemClassification.progression,
    "Flesh Wall Health": ItemClassification.progression,
    "Frenzied Egg Laying": ItemClassification.progression,
    "Greater Compression": ItemClassification.progression,
    "Greater Goo": ItemClassification.progression,
    "Healthy Digestion": ItemClassification.progression,
    "Hexagonal Breeding": ItemClassification.progression,
    "Hooked Spines": ItemClassification.progression,
    "Huge Spawn Size": ItemClassification.progression,
    "Huge Swarm Capacity": ItemClassification.progression,
    "Hunker Down": ItemClassification.progression,
    "Infestation": ItemClassification.progression,
    "Infestation II": ItemClassification.progression,
    "Inorganic Nutrient Harvest": ItemClassification.progression,
    "Insane Spawn Size": ItemClassification.progression,
    "Insane Swarm Capacity": ItemClassification.progression,
    "Interlocking Plates": ItemClassification.progression,
    "Large Spawn Size": ItemClassification.progression,
    "Large Swarm Capacity": ItemClassification.progression,
    "Massive Swarm Capacity": ItemClassification.progression,
    "Medium Spawn Size": ItemClassification.progression,
    "Medium Swarm Capacity": ItemClassification.progression,
    "More Acidic Spit": ItemClassification.progression,
    "More Motherly": ItemClassification.progression,
    "More Pus": ItemClassification.progression,
    "Nutrient Gooier": ItemClassification.progression,

    "Nutrient Pustules": ItemClassification.progression,
    # Made progression to avoid unwinnable seeds

    "Offensive Goo Tactics": ItemClassification.progression,
    "Organic Nutrient Harvest": ItemClassification.progression,
    "Overeating": ItemClassification.progression,
    "Rapid Egg Laying": ItemClassification.progression,
    "Razor Spines": ItemClassification.progression,
    "Rebuilding": ItemClassification.progression,
    "Regen Aura": ItemClassification.progression,

    "Selective Breeding Program": ItemClassification.progression,
    # made progression as the game is much less interesting from a rando prespective without it early, may make it a setting later to start with it instead

    "Speed Goo": ItemClassification.progression,
    "Speed Hooks": ItemClassification.progression,
    "Spiked Carapace": ItemClassification.progression,
    "Spiked Carapace II": ItemClassification.progression,
    "Spiner Health": ItemClassification.progression,
    "Spiner Influence": ItemClassification.progression,
    "Spiner Legs": ItemClassification.progression,
    "Spiner Range I": ItemClassification.progression,
    "Spiner Range II": ItemClassification.progression,
    "Spore Artillery": ItemClassification.progression,
    "Spore Launchers": ItemClassification.progression,
    "Spore Launchers Range": ItemClassification.progression,
    "Spore Launchers Range II": ItemClassification.progression,
    "Starting Nutrients": ItemClassification.progression,
    "Starting Nutrients II": ItemClassification.progression,
    "Starting Nutrients III": ItemClassification.progression,
    "Starting Nutrients IV": ItemClassification.progression,
    "Starting Nutrients V": ItemClassification.progression,
    "Swarm Mother Influence": ItemClassification.progression,
    "Swarm Mother Legs": ItemClassification.progression,
    "Swarm Attack Speed": ItemClassification.progression,
    "Swarm Attack Speed II": ItemClassification.progression,
    "Swarm Attack Speed III": ItemClassification.progression,
    "Swarmer Armor": ItemClassification.progression,
    "Swarmer Guidance": ItemClassification.progression,
    "Swarmer Health": ItemClassification.progression,
    "Swarmer Influence": ItemClassification.progression,
    "Swarm Health": ItemClassification.progression,
    "Swarm Health II": ItemClassification.progression,
    "Swarm Health III": ItemClassification.progression,
    "Swarm Speed": ItemClassification.progression,
    "Tearing Claws": ItemClassification.progression,

    "The Defender": ItemClassification.progression,
    "The Spiner": ItemClassification.progression,
    "The Wasp": ItemClassification.progression,
    "The Boom Slug": ItemClassification.progression,
    "The Builder": ItemClassification.progression,
    "The Swarm Mother": ItemClassification.progression,
    "The Titan": ItemClassification.progression,
    "The Warrior": ItemClassification.progression,
    "The Swarmer": ItemClassification.progression,
    # most other talents require 1 or more of these to function, forcing 1-2 early allows rando to function

    "Titan Legs": ItemClassification.progression,
    "Titan Influence": ItemClassification.progression,
    "Twin Juices": ItemClassification.progression,
    "Uber Swarm Capacity": ItemClassification.progression,
    "Warrior Endurance": ItemClassification.progression,
    "Warrior Influence": ItemClassification.progression,
    "Warrior Legs": ItemClassification.progression,
    "Wasp Influence": ItemClassification.progression,
    "Wasp Legs": ItemClassification.progression,
    "Well Fed": ItemClassification.progression,
    "Nutrient Recycle": ItemClassification.progression,
    "Building Regeneration": ItemClassification.progression,
    "Survival Instinct": ItemClassification.progression,
    "Wasp Infestation": ItemClassification.progression,
    "Radiation Resistant": ItemClassification.progression,

    "HP Increase": ItemClassification.filler,
    "Armor Increase": ItemClassification.filler,
    "Damage Increase": ItemClassification.filler,
    "Attack Speed Increase": ItemClassification.filler,
    "Move Speed Increase": ItemClassification.filler,
    "Cost Decrease": ItemClassification.filler,

    "Set Damage to Zero for 30s": ItemClassification.trap,
    "Leave Current Mission": ItemClassification.trap,
    "Lock Swarmer for 2m": ItemClassification.trap,
}

TRAP_NAMES = ["Set Damage to Zero for 30s", "Leave Current Mission", "Lock Swarmer for 2m"]

FILLER_NAMES = ["HP Increase", "Armor Increase", "Damage Increase", "Attack Speed Increase", "Move Speed Increase", "Cost Decrease"]

class BuggosItem(Item):
    game = "Buggos"


def get_random_filler_item_name(world: BuggosWorld) -> str:

    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(TRAP_NAMES)

    return world.random.choice(FILLER_NAMES)

def create_item_with_correct_classification(world: BuggosWorld, name: str) -> BuggosItem:
    classification = DEFAULT_ITEM_CLASSIFICATION[name]

    return BuggosItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def get_starting_unit_names(world: BuggosWorld) -> list[str]:
    choice = world.options.starting_unit.value

    if choice == 8:
        return[world.random.choice(list(UNIT_ITEM_NAMES.values()))]

    elif choice == 9:
        other_units = {
                1: "The Defender",
                2: "The Spiner",
                3: "The Wasp",
                4: "The Boom Slug",
                5: "The Builder",
                6: "The Swarm Mother",
                7: "The Warrior",
        }

        return[world.random.choice(list(other_units.values())), UNIT_ITEM_NAMES[0]]
    return [UNIT_ITEM_NAMES[choice]]


def create_all_items(world: BuggosWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Adrenaline"),
        world.create_item("Aggressive Fertilization"),
        world.create_item("A Mother's Touch"),
        world.create_item("Armor Shredding"),
        world.create_item("Artistic Zen"),
        world.create_item("Best Parent"),
        world.create_item("Boom Slug Explosion Radius"),
        world.create_item("Boom Slug Explosion Radius II"),
        world.create_item("Boom Slug Influence"),
        world.create_item("Boom Slug Move Speed"),
        world.create_item("Boom Slug Move Speed II"),
        world.create_item("Boom Slug Thicker Skin"),
        world.create_item("Builder Influence"),
        world.create_item("Builder Legs"),
        world.create_item("Goo on Death"),
        world.create_item("Burrow Deeper"),
        world.create_item("Carnivorous Floor Traps"),
        world.create_item("Caustic Chemicals"),
        world.create_item("Chew Faster"),
        world.create_item("Chitinous Plates"),
        world.create_item("Compressed Acid Glands"),
        world.create_item("Construction Squad"),
        world.create_item("Corrosive Chemicals"),
        world.create_item("Dash Attack"),
        world.create_item("Defender Influence"),
        world.create_item("Defender Legs"),
        world.create_item("Defensive Goo Tactics"),
        world.create_item("Double Spines"),
        world.create_item("Efficient Builders"),
        world.create_item("Egg Twins"),
        world.create_item("Enormous Belly"),
        world.create_item("Enormous Belly II"),
        world.create_item("Enormous Swarm Capacity"),
        world.create_item("Extreme Swarm Capacity"),
        world.create_item("Fast Twitch Muscles"),
        world.create_item("Final Farewell"),
        world.create_item("Flesh Walls"),
        world.create_item("Flesh Wall Armor"),
        world.create_item("Flesh Wall Health"),
        world.create_item("Frenzied Egg Laying"),
        world.create_item("Greater Compression"),
        world.create_item("Greater Goo"),
        world.create_item("Healthy Digestion"),
        world.create_item("Hexagonal Breeding"),
        world.create_item("Hooked Spines"),
        world.create_item("Huge Spawn Size"),
        world.create_item("Huge Swarm Capacity"),
        world.create_item("Hunker Down"),
        world.create_item("Infestation"),
        world.create_item("Infestation II"),
        world.create_item("Inorganic Nutrient Harvest"),
        world.create_item("Insane Spawn Size"),
        world.create_item("Insane Swarm Capacity"),
        world.create_item("Interlocking Plates"),
        world.create_item("Large Spawn Size"),
        world.create_item("Large Swarm Capacity"),
        world.create_item("Massive Swarm Capacity"),
        world.create_item("Medium Swarm Capacity"),
        world.create_item("More Acidic Spit"),
        world.create_item("More Motherly"),
        world.create_item("More Pus"),
        world.create_item("Nutrient Gooier"),
        world.create_item("Nutrient Pustules"),
        world.create_item("Offensive Goo Tactics"),
        world.create_item("Organic Nutrient Harvest"),
        world.create_item("Overeating"),
        world.create_item("Rapid Egg Laying"),
        world.create_item("Razor Spines"),
        world.create_item("Rebuilding"),
        world.create_item("Regen Aura"),
        world.create_item("Selective Breeding Program"),
        world.create_item("Speed Goo"),
        world.create_item("Speed Hooks"),
        world.create_item("Spiked Carapace"),
        world.create_item("Spiked Carapace II"),
        world.create_item("Spiner Health"),
        world.create_item("Spiner Influence"),
        world.create_item("Spiner Legs"),
        world.create_item("Spiner Range I"),
        world.create_item("Spiner Range II"),
        world.create_item("Spore Artillery"),
        world.create_item("Spore Launchers"),
        world.create_item("Spore Launchers Range"),
        world.create_item("Spore Launchers Range II"),
        world.create_item("Starting Nutrients"),
        world.create_item("Starting Nutrients II"),
        world.create_item("Starting Nutrients III"),
        world.create_item("Starting Nutrients IV"),
        world.create_item("Starting Nutrients V"),
        world.create_item("Swarm Mother Influence"),
        world.create_item("Swarm Mother Legs"),
        world.create_item("Swarm Attack Speed"),
        world.create_item("Swarm Attack Speed II"),
        world.create_item("Swarm Attack Speed III"),
        world.create_item("Swarmer Armor"),
        world.create_item("Swarmer Guidance"),
        world.create_item("Swarmer Health"),
        world.create_item("Swarmer Influence"),
        world.create_item("Swarm Health"),
        world.create_item("Swarm Health II"),
        world.create_item("Swarm Health III"),
        world.create_item("Swarm Speed"),
        world.create_item("Tearing Claws"),
        world.create_item("Titan Legs"),
        world.create_item("Titan Influence"),
        world.create_item("Twin Juices"),
        world.create_item("Uber Swarm Capacity"),
        world.create_item("Warrior Endurance"),
        world.create_item("Warrior Influence"),
        world.create_item("Warrior Legs"),
        world.create_item("Wasp Influence"),
        world.create_item("Wasp Legs"),
        world.create_item("Well Fed"),
        world.create_item("Nutrient Recycle"),
        world.create_item("Building Regeneration"),
        world.create_item("Survival Instinct"),
        world.create_item("Wasp Infestation"),
        world.create_item("Radiation Resistant"),
    ]
    # world.create_item("Medium Spawn Size"), ADD TO PRECOLLECTeD IF DEFENDER OR ANOTHER EXPENSIVE UNIT
    
    itempool += [world.create_item("The Titan")]
    starting_units = get_starting_unit_names(world)
    for unit in UNIT_ITEM_NAMES.values():
        unit = world.create_item(unit)
        if unit.name in starting_units:
            world.push_precollected(unit)
        else:
            itempool += [unit]

    spawn_capacity_units = ["The Boom Slug", "The Swarm Mother", "The Warrior"]

    mss = world.create_item("Medium Spawn Size")
    if any(name in spawn_capacity_units for name in starting_units):
        world.push_precollected(mss)
    else:
        itempool += [mss]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items


    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    world.multiworld.itempool += itempool