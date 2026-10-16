from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class BuggosWebWorld(WebWorld):
    game = "Buggos"

    theme = "stone"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to set up Buggos for MultiWorld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Iggy"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
