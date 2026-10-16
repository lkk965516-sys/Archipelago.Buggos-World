# Archipelago.Buggos-World

An [Archipelago](https://archipelago.gg) world package that lets **Buggos** be played as part of an [Archipelago](https://archipelago.gg) multiworld session. Archipelago is a multiworld randomizer framework. For more information, visit the website or join the Discord.

> **Status:** early development. Only the **campaign** is supported. Survival and challenges are not implemented.

## Gameplay

**Checks** are sent when you:
- beat a mission for the first time

- collect evolution points


**Items** in the pool are:
- every evolution tree talent

- your starting unit

- filler stat increases

- traps


### Traps

| Trap | Effect |
| --- | --- |
| Damage Zero | Your units deal no damage for a while (default 30 s) |
| Leave Mission | Kicks you out of the current mission |
| Lock Swarmer | Temporarily locks the Swarmer (default 120 s) |

Trap durations can be changed in the config file.

## Achieving Victory

Currently the only goal is to **beat every mission in the game**. Clearing the final area triggers the victory cutscene and completes your goal.

## Installation

1. Download the latest `buggos.apworld` release.

2. Place `buggos.apworld` into your Archipelago `custom_worlds/` folder.
3. Restart your Archipelago launcher.

## Example YAML

A YAML for this game looks as follows:

```yaml
name: Player{number}
game: Buggos
Buggos:
  starting_unit: 0
  trap_chance: 33
```

## Known Issues

- Early development balancing is ongoing.

## AI Disclaimer
No AI was used for the creation of the apworld

## Credits

Iggy and the Archipelago community. 
