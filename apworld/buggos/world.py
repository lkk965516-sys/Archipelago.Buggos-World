from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as buggos_options 

class BuggosWorld(World):
    """
    Buggos is a RTS, AutoBattler game.
    Developing this was so much work
    """

    game = "Buggos"

    web = web_world.BuggosWebWorld()

    options_dataclass = buggos_options.BuggosOptions
    options: buggos_options.BuggosOptions


    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self):
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self):
        rules.set_all_rules(self)

    def create_items(self):
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BuggosItem:
            return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
         return items.get_random_filler_item_name(self)

    def fill_slot_data(self):
        return self.options.as_dict(
        "trap_chance", "starting_unit"
        )

    