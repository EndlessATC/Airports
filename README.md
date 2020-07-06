# EndlessATCAirports
[startgrid](https://startgrid.itch.io/), developer of the most excellent game [Endless ATC](https://startgrid.itch.io/endlessatc) (also on [Steam](http://store.steampowered.com/app/666610/Endless_ATC/) and [Android](https://play.google.com/store/apps/details?id=com.dirgtrats.atcradar)) has recently added the ability to import custom airports as well as provided about 3000 raw airport configuration files. They're not intended as ready-to-play airports, but more as a starting point to create a new airport file. The files in this collection are automatically composed out of free databases, and the quality and completeness may differ per file. In any case, the files are not finished, so you'll have to add more properties (like SIDs and runway configurations) yourself. Best practice would be to pick one airport you would like to work on from the collection, copy that file to the game, and start expanding it, bit by bit, with more data. You can also start from scratch, googling all data and properties yourself.

## Usage
Use a text editor, together with the included example.txt file as a guide, to create a working file in the locations folder of the game. The example file is pretty big, but most of the properties in it are only optional. In theory, just a runway and an airport code is enough data to create a minimal, playable file. You can always decide to add more detail later. First thing to do is to make sure  the '#code = ' item in the [airport1] section is un-commented to make the airport appear in-game at the bottom of the airport menu. So just remove the # at the beginning of that line. Carefully put each item in the correct section, in the same format as the example. Start the game every now and then to make sure it still works as expected.

## Contributing
1. Open an issue describing the work you want to do (or want done, but it will be faster if you participate!)
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits
[startgrid](https://startgrid.itch.io/)

## License
TODO: Write license
