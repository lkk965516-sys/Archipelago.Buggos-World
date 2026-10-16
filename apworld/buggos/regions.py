from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BuggosWorld




def create_and_connect_regions(world: BuggosWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: BuggosWorld) -> None:
    pass
    menu = Region("Menu", world.player, world.multiworld)

    area_1 = Region("Area 1", world.player, world.multiworld)
    area_2 = Region("Area 2", world.player, world.multiworld)
    area_3 = Region("Area 3", world.player, world.multiworld)
    area_4 = Region("Area 4", world.player, world.multiworld)
    area_5 = Region("Area 5", world.player, world.multiworld)
    area_6 = Region("Area 6", world.player, world.multiworld)
    area_7 = Region("Area 7", world.player, world.multiworld)
    area_8 = Region("Area 8", world.player, world.multiworld)
    area_9 = Region("Area 9", world.player, world.multiworld)
    victory_cutscene = Region("Victory Cutscene", world.player, world.multiworld)


    regions = [menu, area_1, area_2, area_3, area_4, area_5, area_6, area_7, area_8, area_9, victory_cutscene]

    # ADD AN OPTION TO ADD SURVIVAL TO CHECKS?? FUTURE IDEA

    world.multiworld.regions += regions


def connect_regions(world: BuggosWorld) -> None:
    menu = world.get_region("Menu")

    area_1 = world.get_region("Area 1")
    area_2 = world.get_region("Area 2")
    area_3 = world.get_region("Area 3")
    area_4 = world.get_region("Area 4")
    area_5 = world.get_region("Area 5")
    area_6 = world.get_region("Area 6")
    area_7 = world.get_region("Area 7")
    area_8 = world.get_region("Area 8")
    area_9 = world.get_region("Area 9")
    victory_cutscene = world.get_region("Victory Cutscene")

    menu.connect(area_1, "Menu to Area 1")

    area_1.connect(area_2, "Area 1 to Area 2")
    area_2.connect(area_3, "Area 2 to Area 3")
    area_3.connect(area_4, "Area 3 to Area 4")
    area_4.connect(area_5, "Area 4 to Area 5")
    area_5.connect(area_6, "Area 5 to Area 6")
    area_6.connect(area_7, "Area 6 to Area 7")
    area_7.connect(area_8, "Area 7 to Area 8")
    area_8.connect(area_9, "Area 8 to Area 9")
    area_9.connect(victory_cutscene, "Area 9 to Victory Cutscene")

    # POSSIBLY MORE TO ADD SUCH AS Survival, Challenges, and checks/keys from accesing and doing them