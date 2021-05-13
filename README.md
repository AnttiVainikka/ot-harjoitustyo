# **Dungeon Crawler**

## About

### Premise
Choose your team and venture a deadly labyrinth filled with monsters. Find the boss and defeat it to beat the game.

### Guide
Use the arrowkeys to move while exploring and use the numpad to give commands during battle. You might want to defeat many enemies to make your characters stronger but do beware, the boss also gains strength by the minute.

## Documentation
- [Vaatimusmäärittely](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/kayttoohje.md)
- [Testausdokumentti](https://github.com/AnttiVainikka/ot-harjoitustyo/blob/master/game/documentation/testaus.md)

## Releases
- [First Release](https://github.com/AnttiVainikka/ot-harjoitustyo/releases/tag/Viikko5)
- [Second Release](https://github.com/AnttiVainikka/ot-harjoitustyo/releases/tag/viikko6)

## Installing
After extracting the Source code, navigate to the game-folder and run the command "poetry install" Then you can start the game by running the command "poetry run invoke start" on the game-folder. You can also activate automatic tests with the command "poetry run invoke test" and get the test coverage report with "poetry run invoke coverage-report". With "poetry run invoke lint" you can get the code's pylint grade.

## Pylint
In some files I have used "pylint: disable=no-member". This is to prevent lines such as pygame.init() and pygame.KEYDOWN from registering as problems.
