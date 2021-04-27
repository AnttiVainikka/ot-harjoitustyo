# **Dungeon Crawler**

## About

### Premise
Choose your team and venture a deadly labyrinth filled with monsters. Find the boss and defeat it to beat the game.

### Guide
Use the arrowkeys to move while exploring and use the numpad to give commands during battle. Currently, all characters are automatically leveled to their max level so there is no need to farm experience before challenging the boss.

## Documentation
- [Vaatimusmäärittely](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/arkkitehtuuri.md)

## Installing
Download the Game-folder and activate poetry on it. Then you can start the game by running the command "poetry run invoke start". You can also activate automatic tests with the command "poetry run invoke test" and get the test coverage report with "poetry run invoke coverage-report".

## Pylint
In some files I have used "pylint: disable=no-member". This is to prevent lines such as pygame.init() and pygame.KEYDOWN from registering as problems.
