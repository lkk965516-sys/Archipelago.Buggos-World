from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle



class TrapChance(Range):
    """
    Percentage chance that any filler item is replaced by a trap.
    """

    display_name = "Trap Chance"
    
    range_start = 0
    range_end = 100
    default = 33

class StartingUnit(Choice):
    """
    The starting unit for the run, default is Swarmer
    """

    display_name = "Starting Unit"

    option_swarmer = 0
    option_defender = 1
    option_spiner = 2
    option_wasp = 3
    option_boom_slug = 4
    option_builder = 5
    option_swarm_mother = 6
    option_warrior = 7
    option_random_unit = 8
    option_swarmer_plus_random = 9

    default = option_swarmer

@dataclass
class BuggosOptions(PerGameCommonOptions):
    starting_unit: StartingUnit 
    trap_chance: TrapChance

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [
            TrapChance, StartingUnit
        ]
    ),

]

option_presets = {
    "Default": {
        "trap chance": 33,
        "starting unit": 0,
    }
}