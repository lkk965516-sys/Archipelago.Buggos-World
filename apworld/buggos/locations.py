from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BuggosWorld

LOCATION_NAME_TO_ID = {
    "Scum Laden Outpost Conquered": 1,
    "Scum Laden Outpost Evo Point 1": 2,

    "Filthy Peasant Village Conquered": 3,
    "Filthy Peasant Village Evo Point 1": 4,
    "Filthy Peasant Village Evo Point 2": 5,

    "Defensive Dirt Town Conquered": 6,
    "Defensive Dirt Town Evo Point 1": 7,
    "Defensive Dirt Town Evo Point 2": 8,

    "Disgusting Hamlet Conquered": 9,
    "Disgusting Hamlet Evo Point 1": 10,
    "Disgusting Hamlet Evo Point 2": 11,

    "Regrettable Looking City Conquered": 12,
    "Regrettable Looking City Evo Point 1": 13,
    "Regrettable Looking City Evo Point 2": 14,
    "Regrettable Looking City Evo Point 3": 15,

    "Protective Trash Heap Conquered": 16,
    "Protective Trash Heap Evo Point 1": 17,
    "Protective Trash Heap Evo Point 2": 18,

    "Makeshift Barricade Conquered": 19,
    "Makeshift Barricade Evo Point 1": 20,
    "Makeshift Barricade Evo Point 2": 21,

    "Fortified Settlement Conquered": 22,
    "Fortified Settlement Evo Point 1": 23,
    "Fortified Settlement Evo Point 2": 24,

    "Rat-Like Large City Conquered": 25,
    "Rat-Like Large City Evo Point 1": 26,
    "Rat-Like Large City Evo Point 2": 27,

    "Shifty Military Outpost Conquered": 28,
    "Shifty Military Outpost Evo Point 1": 29,
    "Shifty Military Outpost Evo Point 2": 30,
    "Shifty Military Outpost Evo Point 3": 31,

    "Tasty looking Morsel Conquered": 32,
    "Tasty looking Morsel Evo Point 1": 33,
    "Tasty looking Morsel Evo Point 2": 34,

    "Simpleton Housing Conquered": 35,
    "Simpleton Housing Evo Point 1": 36,

    "Forward Military Base Conquered": 37,
    "Forward Military Base Evo Point 1": 38,
    "Forward Military Base Evo Point 2": 39,
    "Forward Military Base Evo Point 3": 40,

    "Very large Peasant City Conquered": 41,
    "Very large Peasant City Evo Point 1": 42,
    "Very large Peasant City Evo Point 2": 43,

    "Cockroach Town Conquered": 44,
    "Cockroach Town Evo Point 1": 45,

    "Hidden Flea Village Conquered": 46,
    "Hidden Flea Village Evo Point 1": 47,
    "Hidden Flea Village Evo Point 2": 48,

    "Curious Technology Center Conquered": 49,
    "Curious Technology Center Evo Point 1": 50,
    "Curious Technology Center Evo Point 2": 51,

    "Fortified Military Command Center Conquered": 52,
    "Fortified Military Command Center Evo Point 1": 53,
    "Fortified Military Command Center Evo Point 2": 54,

    "High Tech Human City Conquered": 55,
    "High Tech Human City Evo Point 1": 56,
    "High Tech Human City Evo Point 2": 57,

    "Human Garbage Village Conquered": 58,
    "Human Garbage Village Evo Point 1": 59,

    "Civilian Power Reactor Conquered": 60,
    "Civilian Power Reactor Evo Point 1": 61,
    "Civilian Power Reactor Evo Point 2": 62,

    "Military Weapon Facility Conquered": 63,
    "Military Weapon Facility Evo Point 1": 64,
    "Military Weapon Facility Evo Point 2": 65,
    "Military Weapon Facility Evo Point 3": 66,

    "Creepy Technology Center Conquered": 67,
    "Creepy Technology Center Evo Point 1": 68,
    "Creepy Technology Center Evo Point 2": 69,

    "Simple Military Outpost Conquered": 70,
    "Simple Military Outpost Evo Point 1": 71,
    "Simple Military Outpost Evo Point 2": 72,

    "Human Government Capital Conquered": 73,
    "Human Government Capital Evo Point 1": 74,
    "Human Government Capital Evo Point 2": 75,

    "Pathetic Fusion Reactor Conquered": 76,
    "Pathetic Fusion Reactor Evo Point 1": 77,
    "Pathetic Fusion Reactor Evo Point 2": 78,

    "High Security Outpost Conquered": 79,
    "High Security Outpost Evo Point 1": 80,

    "Gross Residential Compound Conquered": 81,
    "Gross Residential Compound Evo Point 1": 82,
    "Gross Residential Compound Evo Point 2": 83,

    "Affluent Human City Conquered": 84,
    "Affluent Human City Evo Point 1": 85,
    "Affluent Human City Evo Point 2": 86,
    "Affluent Human City Evo Point 3": 87,

    "Inferior Human Religious Site Conquered": 88,
    "Inferior Human Religious Site Evo Point 1": 89,
    "Inferior Human Religious Site Evo Point 2": 90,

    "Sad Military Capital Conquered": 91,
    "Sad Military Capital Evo Point 1": 92,
    "Sad Military Capital Evo Point 2": 93,

    "Last Human City Conquered": 94,
    "Last Human City Evo Point 1": 95,
    "Last Human City Evo Point 2": 96,

    "Quivering Human Bastion Conquered": 97,
    "Quivering Human Bastion Evo Point 1": 98,
    "Quivering Human Bastion Evo Point 2": 99,

    "Emergency Distress Beacon Conquered": 100,
    "Emergency Distress Beacon Evo Point 1": 101,
    "Emergency Distress Beacon Evo Point 2": 102,

    "Impressive Explosives Facility Conquered": 103,
    "Impressive Explosives Facility Evo Point 1": 104,
    "Impressive Explosives Facility Evo Point 2": 105,

    "Communications Relay Conquered": 106,
    "Communications Relay Evo Point 1": 107,
    "Communications Relay Evo Point 2": 108,

    "Arrival Conquered": 109,
    "Arrival Evo Point 1": 110,

    "Listening Post Conquered": 111,
    "Listening Post Evo Point 1": 112,

    "Barracks Conquered": 113,
    "Barracks Evo Point 1": 114,
    "Barracks Evo Point 2": 115,

    "Logistics Hub Conquered": 116,
    "Logistics Hub Evo Point 1": 117,
    "Logistics Hub Evo Point 2": 118,

    "Landing Pad Conquered": 119,
    "Landing Pad Evo Point 1": 120,
    "Landing Pad Evo Point 2": 121,

    "Forward Command Conquered": 122,
    "Forward Command Evo Point 1": 123,
    "Forward Command Evo Point 2": 124,
    "Forward Command Evo Point 3": 125,

    "Solar Arrays Conquered": 126,
    "Solar Arrays Evo Point 1": 127,
    "Solar Arrays Evo Point 2": 128,

    "Mech Processing Conquered": 129,
    "Mech Processing Evo Point 1": 130,
    "Mech Processing Evo Point 2": 131,

    "Mile 3 Fortification Conquered": 132,
    "Mile 3 Fortification Evo Point 1": 133,
    "Mile 3 Fortification Evo Point 2": 134,

    "Radio Labs Conquered": 135,
    "Radio Labs Evo Point 1": 136,
    "Radio Labs Evo Point 2": 137,

    "Robot Testing Facility Conquered": 138,
    "Robot Testing Facility Evo Point 1": 139,
    "Robot Testing Facility Evo Point 2": 140,

    "Drop Pods Conquered": 141,
    "Drop Pods Evo Point 1": 142,
    "Drop Pods Evo Point 2": 143,

    "Final Military Compound Conquered": 144,
    "Final Military Compound Evo Point 1": 145,
    "Final Military Compound Evo Point 2": 146,

    "Medical Center Conquered": 147,
    "Medical Center Evo Point 1": 148,
    "Medical Center Evo Point 2": 149,

    "Radiation Wall Conquered": 150,
    "Radiation Wall Evo Point 1": 151,
    "Radiation Wall Evo Point 2": 152,

    "Research Lab Conquered": 153,
    "Research Lab Evo Point 1": 154,
    "Research Lab Evo Point 2": 155,

    "Energy Generator Conquered": 156,
    "Energy Generator Evo Point 1": 157,
    "Energy Generator Evo Point 2": 158,

    "Invasion Ship Conquered": 159,
    "Invasion Ship Evo Point 1": 160,
    "Invasion Ship Evo Point 2": 161,
}

class BuggosLocation(Location):
    game = "Buggos"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: BuggosWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: BuggosWorld) -> None:
    area_1 = world.get_region("Area 1")
    area_2 = world.get_region("Area 2")
    area_3 = world.get_region("Area 3")
    area_4 = world.get_region("Area 4")
    area_5 = world.get_region("Area 5")
    area_6 = world.get_region("Area 6")
    area_7 = world.get_region("Area 7")
    area_8 = world.get_region("Area 8")
    area_9 = world.get_region("Area 9")

    area_1_locations = get_location_names_with_ids([
        "Scum Laden Outpost Conquered", 
        "Scum Laden Outpost Evo Point 1",

        "Filthy Peasant Village Conquered",
        "Filthy Peasant Village Evo Point 1",
        "Filthy Peasant Village Evo Point 2",
    
        "Defensive Dirt Town Conquered",
        "Defensive Dirt Town Evo Point 1",
        "Defensive Dirt Town Evo Point 2",
    
        "Disgusting Hamlet Conquered",
        "Disgusting Hamlet Evo Point 1",
        "Disgusting Hamlet Evo Point 2",
    
        "Regrettable Looking City Conquered",
        "Regrettable Looking City Evo Point 1",
        "Regrettable Looking City Evo Point 2",
        "Regrettable Looking City Evo Point 3",
    
        "Protective Trash Heap Conquered",
        "Protective Trash Heap Evo Point 1",
        "Protective Trash Heap Evo Point 2",
        ])

    area_2_locations = get_location_names_with_ids([
        "Makeshift Barricade Conquered",
        "Makeshift Barricade Evo Point 1",
        "Makeshift Barricade Evo Point 2",

        "Fortified Settlement Conquered",
        "Fortified Settlement Evo Point 1",
        "Fortified Settlement Evo Point 2",

        "Rat-Like Large City Conquered",
        "Rat-Like Large City Evo Point 1",
        "Rat-Like Large City Evo Point 2",

        "Shifty Military Outpost Conquered",
        "Shifty Military Outpost Evo Point 1",
        "Shifty Military Outpost Evo Point 2",
        "Shifty Military Outpost Evo Point 3",

        "Tasty looking Morsel Conquered",
        "Tasty looking Morsel Evo Point 1",
        "Tasty looking Morsel Evo Point 2",

        "Simpleton Housing Conquered",
        "Simpleton Housing Evo Point 1",
    ])

    area_3_locations = get_location_names_with_ids([
        "Forward Military Base Conquered",
        "Forward Military Base Evo Point 1",
        "Forward Military Base Evo Point 2",
        "Forward Military Base Evo Point 3",

        "Very large Peasant City Conquered",
        "Very large Peasant City Evo Point 1",
        "Very large Peasant City Evo Point 2",

        "Cockroach Town Conquered",
        "Cockroach Town Evo Point 1",

        "Hidden Flea Village Conquered",
        "Hidden Flea Village Evo Point 1",
        "Hidden Flea Village Evo Point 2",

        "Curious Technology Center Conquered",
        "Curious Technology Center Evo Point 1",
        "Curious Technology Center Evo Point 2",

        "Fortified Military Command Center Conquered",
        "Fortified Military Command Center Evo Point 1",
        "Fortified Military Command Center Evo Point 2",
    ])

    area_4_locations = get_location_names_with_ids([
        "High Tech Human City Conquered",
        "High Tech Human City Evo Point 1",
        "High Tech Human City Evo Point 2",

        "Human Garbage Village Conquered",
        "Human Garbage Village Evo Point 1",

        "Civilian Power Reactor Conquered",
        "Civilian Power Reactor Evo Point 1",
        "Civilian Power Reactor Evo Point 2",

        "Military Weapon Facility Conquered",
        "Military Weapon Facility Evo Point 1",
        "Military Weapon Facility Evo Point 2",
        "Military Weapon Facility Evo Point 3",

        "Creepy Technology Center Conquered",
        "Creepy Technology Center Evo Point 1",
        "Creepy Technology Center Evo Point 2",

        "Simple Military Outpost Conquered",
        "Simple Military Outpost Evo Point 1",
        "Simple Military Outpost Evo Point 2",
    ])

    area_5_locations = get_location_names_with_ids([
        "Human Government Capital Conquered",
        "Human Government Capital Evo Point 1",
        "Human Government Capital Evo Point 2",

        "Pathetic Fusion Reactor Conquered",
        "Pathetic Fusion Reactor Evo Point 1",
        "Pathetic Fusion Reactor Evo Point 2",

        "High Security Outpost Conquered",
        "High Security Outpost Evo Point 1",

        "Gross Residential Compound Conquered",
        "Gross Residential Compound Evo Point 1",
        "Gross Residential Compound Evo Point 2",

        "Affluent Human City Conquered",
        "Affluent Human City Evo Point 1",
        "Affluent Human City Evo Point 2",
        "Affluent Human City Evo Point 3",

        "Inferior Human Religious Site Conquered",
        "Inferior Human Religious Site Evo Point 1",
        "Inferior Human Religious Site Evo Point 2",
    ])

    area_6_locations = get_location_names_with_ids([
        "Sad Military Capital Conquered",
        "Sad Military Capital Evo Point 1",
        "Sad Military Capital Evo Point 2",

        "Last Human City Conquered",
        "Last Human City Evo Point 1",
        "Last Human City Evo Point 2",

        "Quivering Human Bastion Conquered",
        "Quivering Human Bastion Evo Point 1",
        "Quivering Human Bastion Evo Point 2",

        "Emergency Distress Beacon Conquered",
        "Emergency Distress Beacon Evo Point 1",
        "Emergency Distress Beacon Evo Point 2",

        "Impressive Explosives Facility Conquered",
        "Impressive Explosives Facility Evo Point 1",
        "Impressive Explosives Facility Evo Point 2",

        "Communications Relay Conquered",
        "Communications Relay Evo Point 1",
        "Communications Relay Evo Point 2",
    ])

    area_7_locations = get_location_names_with_ids([
        "Arrival Conquered",
        "Arrival Evo Point 1",

        "Listening Post Conquered",
        "Listening Post Evo Point 1",

        "Barracks Conquered",
        "Barracks Evo Point 1",
        "Barracks Evo Point 2",

        "Logistics Hub Conquered",
        "Logistics Hub Evo Point 1",
        "Logistics Hub Evo Point 2",

        "Landing Pad Conquered",
        "Landing Pad Evo Point 1",
        "Landing Pad Evo Point 2",

        "Forward Command Conquered",
        "Forward Command Evo Point 1",
        "Forward Command Evo Point 2",
        "Forward Command Evo Point 3",
    ])

    area_8_locations = get_location_names_with_ids([
        "Solar Arrays Conquered",
        "Solar Arrays Evo Point 1",
        "Solar Arrays Evo Point 2",

        "Mech Processing Conquered",
        "Mech Processing Evo Point 1",
        "Mech Processing Evo Point 2",

        "Mile 3 Fortification Conquered",
        "Mile 3 Fortification Evo Point 1",
        "Mile 3 Fortification Evo Point 2",

        "Radio Labs Conquered",
        "Radio Labs Evo Point 1",
        "Radio Labs Evo Point 2",

        "Robot Testing Facility Conquered",
        "Robot Testing Facility Evo Point 1",
        "Robot Testing Facility Evo Point 2",

        "Drop Pods Conquered",
        "Drop Pods Evo Point 1",
        "Drop Pods Evo Point 2",
    ])

    area_9_locations = get_location_names_with_ids([
        "Final Military Compound Conquered",
        "Final Military Compound Evo Point 1",
        "Final Military Compound Evo Point 2",

        "Medical Center Conquered",
        "Medical Center Evo Point 1",
        "Medical Center Evo Point 2",

        "Radiation Wall Conquered",
        "Radiation Wall Evo Point 1",
        "Radiation Wall Evo Point 2",

        "Research Lab Conquered",
        "Research Lab Evo Point 1",
        "Research Lab Evo Point 2",

        "Energy Generator Conquered",
        "Energy Generator Evo Point 1",
        "Energy Generator Evo Point 2",

        "Invasion Ship Conquered",
        "Invasion Ship Evo Point 1",
        "Invasion Ship Evo Point 2",
    ])

    area_1.add_locations(area_1_locations, BuggosLocation)
    area_2.add_locations(area_2_locations, BuggosLocation)
    area_3.add_locations(area_3_locations, BuggosLocation)
    area_4.add_locations(area_4_locations, BuggosLocation)
    area_5.add_locations(area_5_locations, BuggosLocation)
    area_6.add_locations(area_6_locations, BuggosLocation)
    area_7.add_locations(area_7_locations, BuggosLocation)
    area_8.add_locations(area_8_locations, BuggosLocation)
    area_9.add_locations(area_9_locations, BuggosLocation)

def create_events(world: BuggosWorld) -> None:
    victory_check = world.get_region("Victory Cutscene")

    victory_check.add_event(
        "Final Area Complete", "Victory", location_type=BuggosLocation, item_type=items.BuggosItem
    )