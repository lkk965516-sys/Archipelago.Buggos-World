from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import *

if TYPE_CHECKING:
    from .world import BuggosWorld

ALL = [
    "The Swarmer", "The Builder", "The Defender", "The Spiner", "The Wasp",
    "The Warrior", "The Boom Slug", "The Swarm Mother", "The Titan",
]


TALENT_COMPATIBILITY = {
    "Adrenaline": ALL,
    "Aggressive Fertilization": ALL,
    "A Mother's Touch": ["The Swarm Mother"],
    "Armor Shredding": ["The Defender"],
    "Artistic Zen": ["The Builder"],
    "Best Parent": ["The Swarm Mother"],
    "Boom Slug Explosion Radius": ["The Boom Slug"],
    "Boom Slug Explosion Radius II": ["The Boom Slug"],
    "Boom Slug Influence": ["The Boom Slug"],
    "Boom Slug Move Speed": ["The Boom Slug"],
    "Boom Slug Move Speed II": ["The Boom Slug"],
    "Boom Slug Thicker Skin": ["The Boom Slug"],
    "Builder Influence": ["The Builder"],
    "Builder Legs": ["The Builder"],
    "Goo on Death": ["The Builder"],
    "Burrow Deeper": ["The Builder"],
    "Carnivorous Floor Traps": ["The Builder"],
    "Caustic Chemicals": ALL,
    "Chew Faster": ["The Builder"],
    "Chitinous Plates": ["The Warrior"],
    "Compressed Acid Glands": ["The Defender"],
    "Construction Squad": ["The Builder"],
    "Corrosive Chemicals": ALL,
    "Dash Attack": ["The Wasp"],
    "Defender Influence": ["The Defender"],
    "Defender Legs": ["The Defender"],
    "Defensive Goo Tactics": ["The Builder"],
    "Double Spines": ["The Spiner"],
    "Efficient Builders": ["The Builder"],
    "Egg Twins": ALL,
    "Enormous Belly": ["The Titan"],
    "Enormous Belly II": ["The Titan"],
    "Enormous Swarm Capacity": ALL,
    "Extreme Swarm Capacity": ALL,
    "Fast Twitch Muscles": ["The Swarmer"],
    "Final Farewell": ["The Swarm Mother"],
    "Flesh Walls": ["The Builder"],
    "Flesh Wall Armor": ["The Builder"],
    "Flesh Wall Health": ["The Builder"],
    "Frenzied Egg Laying": ALL,
    "Greater Compression": ["The Defender"],
    "Greater Goo": ["The Builder"],
    "Healthy Digestion": ALL,
    "Hexagonal Breeding": ["The Wasp"],
    "Hooked Spines": ["The Spiner"],
    "Huge Spawn Size": ALL,
    "Huge Swarm Capacity": ALL,
    "Hunker Down": ["The Warrior"],
    "Infestation": ["The Swarm Mother"],
    "Infestation II": ["The Swarm Mother"],
    "Inorganic Nutrient Harvest": ALL,
    "Insane Spawn Size": ALL,
    "Insane Swarm Capacity": ALL,
    "Interlocking Plates": ALL,
    "Large Spawn Size": ALL,
    "Large Swarm Capacity": ALL,
    "Massive Swarm Capacity": ALL,
    "Medium Spawn Size": ALL,
    "Medium Swarm Capacity": ALL,
    "More Acidic Spit": ["The Defender"],
    "More Motherly": ["The Swarm Mother"],
    "More Pus": ["The Builder"],
    "Nutrient Gooier": ["The Builder"],
    "Nutrient Pustules": ["The Builder"],
    "Offensive Goo Tactics": ["The Builder"],
    "Organic Nutrient Harvest": ALL,
    "Overeating": ["The Warrior"],
    "Rapid Egg Laying": ALL,
    "Razor Spines": ALL,
    "Rebuilding": ["The Builder"],
    "Regen Aura": ["The Titan"],
    "Selective Breeding Program": ALL,
    "Speed Goo": ["The Builder"],
    "Speed Hooks": ["The Swarmer"],
    "Spiked Carapace": ["The Titan"],
    "Spiked Carapace II": ["The Titan"],
    "Spiner Health": ["The Spiner"],
    "Spiner Influence": ["The Spiner"],
    "Spiner Legs": ["The Spiner"],
    "Spiner Range I": ["The Spiner"],
    "Spiner Range II": ["The Spiner"],
    "Spore Artillery": ["The Builder"],
    "Spore Launchers": ["The Builder"],
    "Spore Launchers Range": ["The Builder"],
    "Spore Launchers Range II": ["The Builder"],
    "Starting Nutrients": ALL,
    "Starting Nutrients II": ALL,
    "Starting Nutrients III": ALL,
    "Starting Nutrients IV": ALL,
    "Starting Nutrients V": ALL,
    "Swarm Mother Influence": ["The Swarm Mother"],
    "Swarm Mother Legs": ["The Swarm Mother"],
    "Swarm Attack Speed": ALL,
    "Swarm Attack Speed II": ALL,
    "Swarm Attack Speed III": ALL,
    "Swarmer Armor": ["The Swarmer"],
    "Swarmer Guidance": ["The Swarmer"],
    "Swarmer Health": ["The Swarmer"],
    "Swarmer Influence": ["The Swarmer"],
    "Swarm Health": ALL,
    "Swarm Health II": ALL,
    "Swarm Health III": ALL,
    "Swarm Speed": ALL,
    "Tearing Claws": ["The Swarmer"],
    "The Defender": ["The Defender"],
    "The Spiner": ["The Spiner"],
    "The Wasp": ["The Wasp"],
    "The Boom Slug": ["The Boom Slug"],
    "The Builder": ["The Builder"],
    "The Swarm Mother": ["The Swarm Mother"],
    "The Titan": ["The Builder"],
    "The Warrior": ["The Warrior"],
    "The Swarmer": ["The Swarmer"],
    "Titan Legs": ["The Titan"],
    "Titan Influence": ["The Titan"],
    "Twin Juices": ALL,
    "Uber Swarm Capacity": ALL,
    "Warrior Endurance": ["The Warrior"],
    "Warrior Influence": ["The Warrior"],
    "Warrior Legs": ["The Warrior"],
    "Wasp Influence": ["The Wasp"],
    "Wasp Legs": ["The Wasp"],
    "Well Fed": ["The Swarm Mother"],
    "Nutrient Recycle": ALL,
    "Building Regeneration": ["The Builder"],
    "Survival Instinct": ALL,
    "Wasp Infestation": ["The Wasp"],
    "Radiation Resistant": ALL,
}




def set_all_rules(world: BuggosWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BuggosWorld) -> None:

    menu_to_area_1 = world.get_entrance("Menu to Area 1")
    area_1_to_area_2 = world.get_entrance("Area 1 to Area 2")
    area_2_to_area_3 = world.get_entrance("Area 2 to Area 3")
    area_3_to_area_4 = world.get_entrance("Area 3 to Area 4")
    area_4_to_area_5 = world.get_entrance("Area 4 to Area 5")
    area_5_to_area_6 = world.get_entrance("Area 5 to Area 6")
    area_6_to_area_7 = world.get_entrance("Area 6 to Area 7")
    area_7_to_area_8 = world.get_entrance("Area 7 to Area 8")
    area_8_to_area_9 = world.get_entrance("Area 8 to Area 9")
    area_9_to_victory_cutscene = world.get_entrance("Area 9 to Victory Cutscene")
    

    has_increase_spawn_capacity = Has("Medium Spawn Size") | Has("Large Spawn Size") | Has("Huge Spawn Size") | Has("Insane Spawn Size")

    has_swarmer = Has("The Swarmer")
    has_builder = Has("The Builder")
    has_boom_slug = Has("The Boom Slug") & has_increase_spawn_capacity
    has_wasp = Has("The Wasp")
    has_spiner = Has("The Spiner")
    has_defender = Has("The Defender")
    has_swarm_mother = Has("The Swarm Mother") & has_increase_spawn_capacity
    has_titan: Rule = HasAll("The Titan", "The Builder")
    has_warrior = Has("The Warrior") & has_increase_spawn_capacity

    unit_rules = {
        "The Swarmer": has_swarmer,
        "The Builder": has_builder,
        "The Boom Slug": has_boom_slug,
        "The Wasp": has_wasp,
        "The Spiner": has_spiner,
        "The Defender": has_defender,
        "The Swarm Mother": has_swarm_mother,
        "The Titan": has_titan,
        "The Warrior": has_warrior,
    }

    active_talent_rules = []

    for talent, compatible_units in TALENT_COMPATIBILITY.items():
        compatible_unit_rule = AtLeast( 1, *(unit_rules[unit] for unit in compatible_units))

        active_talent_rules.append( Has(talent) & compatible_unit_rule )

    at_least_5_active_talents = AtLeast( 5, *active_talent_rules )
    at_least_10_active_talents = AtLeast( 10, *active_talent_rules )
    at_least_15_active_talents = AtLeast( 15, *active_talent_rules )
    at_least_20_active_talents = AtLeast( 20, *active_talent_rules )
    at_least_25_active_talents = AtLeast( 25, *active_talent_rules )
    at_least_30_active_talents = AtLeast( 30, *active_talent_rules )
    at_least_35_active_talents = AtLeast( 35, *active_talent_rules )
    at_least_40_active_talents = AtLeast( 40, *active_talent_rules )

    has_selective_breeding_program = Has("Selective Breeding Program")
    

    at_least_one_units = AtLeast(
        1,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
    )

    at_least_two_units = AtLeast(
        2,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
    )

    at_least_three_units = AtLeast(
        3,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
    )

    at_least_four_units = AtLeast(
        4,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
    )

    at_least_five_units = AtLeast(
        5,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
    )

    at_least_six_units = AtLeast(
        6,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
    )

    at_least_seven_units = AtLeast(
        7,
        has_swarmer,
        has_builder,
        has_boom_slug,
        has_wasp,
        has_spiner,
        has_defender,
        has_swarm_mother,
        has_titan,
        has_warrior
        )
    
    world.set_rule(menu_to_area_1, at_least_one_units)

    world.set_rule(area_1_to_area_2, at_least_two_units & at_least_5_active_talents)

    world.set_rule(area_2_to_area_3, at_least_three_units & has_selective_breeding_program & at_least_10_active_talents)

    world.set_rule(area_3_to_area_4, at_least_four_units & at_least_15_active_talents)

    world.set_rule(area_4_to_area_5, at_least_five_units & at_least_20_active_talents)

    world.set_rule(area_5_to_area_6, at_least_six_units & at_least_25_active_talents)

    world.set_rule(area_6_to_area_7, at_least_seven_units & at_least_30_active_talents)

    world.set_rule(area_7_to_area_8, at_least_35_active_talents)

    world.set_rule(area_8_to_area_9, at_least_40_active_talents)




def set_all_location_rules(world: BuggosWorld) -> None:
    pass

def set_completion_condition(world: BuggosWorld) -> None:
    world.set_completion_rule(Has("Victory"))