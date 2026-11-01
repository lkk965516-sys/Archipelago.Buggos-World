# Archipelago.Buggos-World

An [Archipelago](https://archipelago.gg) world package that lets **Buggos** be played as part of an [Archipelago](https://archipelago.gg) multiworld session. Archipelago is a multiworld randomizer framework. For more information, visit the website or join the Discord.

**This is the Archipelago world.** To play, you also need the game-side mod: [Archipelago.Buggos](https://github.com/lkk965516-sys/Archipelago.Buggos).

## Gameplay

**Checks** are sent when you:
- beat a mission for the first time
- collect evolution points

There are **161 locations** in total.

**Items** in the pool are:
- every evolution tree talent
- your starting unit, and the other units to unlock
- filler stat increases (HP, armor, damage, attack speed, move speed, cost decrease)
- traps

### Traps

| Trap | Effect |
| --- | --- |
| Damage Zero | Your units deal no damage for a while (default 30 s) |
| Leave Mission | Kicks you out of the current mission |
| Lock Swarmer | Temporarily locks the Swarmer (default 120 s) |

### Progression

Missions are grouped into areas that you clear in order. Logic dictates a required amount of checks.

## Achieving Victory

Currently the only goal is to beat every mission in the game, clearing the final area triggers the victory cutscene and completes your goal.

## Options

| Option | Default | Description |
| --- | --- | --- |
| `trap_chance` | `33` | Percentage chance (0 to 100) that a filler item is replaced by a trap |
| `starting_unit` | `swarmer` | The unit you start with: `swarmer`, `defender`, `spiner`, `wasp`, `boom_slug`, `builder`, `swarm_mother`, `warrior`, `random_unit` or `swarmer_plus_random` |

The standard Archipelago options (`progression_balancing`, `accessibility`, `start_inventory`, `exclude_locations` and so on) also work.

## Installation

Requires Archipelago **0.6.8 or newer**.

1. Download the latest `buggos.apworld` from the [Releases](https://github.com/lkk965516-sys/Archipelago.Buggos-World/releases) page.
2. Place `buggos.apworld` into your Archipelago `custom_worlds/` folder. (You can also open the file with the Archipelago launcher to install it.)
3. Restart your Archipelago launcher.

## Setting up your YAML

Download `Buggos_Template.yaml` from the [Releases](https://github.com/lkk965516-sys/Archipelago.Buggos-World/releases) page, set your `name`, adjust the options, and put it in your Archipelago `Players` folder.

A YAML for this game looks as follows:

```yaml
name: Player{number}
game: Buggos
Buggos:
  starting_unit: swarmer
  trap_chance: 33
```

You can check that your YAML is valid at [archipelago.gg/check](https://archipelago.gg/check).

## Playing

1. Generate your multiworld with the Archipelago launcher and host it (or give your YAML to the host).
2. Install the [game-side mod](https://github.com/lkk965516-sys/Archipelago.Buggos#installing-the-mod) and connect to the server using the slot name from your YAML.

## Known Issues
- Early development: balancing is ongoing, leaned on easier for now.
  
## Credits

Iggy and the Archipelago community.
