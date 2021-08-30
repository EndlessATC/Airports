# EndlessATCAirports

[startgrid](https://startgrid.itch.io/), developer of the most excellent game [Endless ATC](https://startgrid.itch.io/endlessatc) (also on [Steam](http://store.steampowered.com/app/666610/Endless_ATC/) and [Android](https://play.google.com/store/apps/details?id=com.dirgtrats.atcradar)) has recently added the ability to import custom airports as well as provided about 3000 raw airport configuration files. They're not intended as ready-to-play airports, but more as a starting point to create a new airport file. The files in this collection are automatically composed out of free databases, and the quality and completeness may differ per file. In any case, the files are not finished, so you'll have to add more properties (like SIDs and runway configurations) yourself. Best practice would be to pick one airport you would like to work on from the collection, copy that file to the game, and start expanding it, bit by bit, with more data. You can also start from scratch, googling all data and properties yourself.

## Usage

Use a text editor, together with the included example.txt file as a guide, to create a working file in the locations folder of the game. The example file is pretty big, but most of the properties in it are only optional. In theory, just a runway and an airport code is enough data to create a minimal, playable file. You can always decide to add more detail later. First thing to do is to make sure  the '#code = ' item in the [airport1] section is un-commented to make the airport appear in-game at the bottom of the airport menu. So just remove the # at the beginning of that line. Carefully put each item in the correct section, in the same format as the example. Start the game every now and then to make sure it still works as expected.

## Contributing

1. Open an issue describing the work you want to do (or want done, but it will be faster if you participate!)
2. Fork this repository
3. Clone your fork to your computer so you can work on it
4. Set this repository to be the upstream repository of your fork
5. Ensure your repository has the most recent changes from upstream
6. Create a branch in your repository: `git checkout -b iss#/desc` where the open issue and description are both included
7. Make local changes until your repository contains all completed work
8. Commit your changes: `git commit -am 'iss#/desc - closes iss#'` Use [keywords](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to assist with linking issues and pull requests
9. Push to your branch: `git push origin iss#/desc`
10. Submit a pull request from your fork to the upstream repository

Note, many editors and GUI git clients will help and even combine many of these commands. Refer to the documentation for whichever application you are using as well as [this guide](https://www.dataschool.io/how-to-contribute-on-github/) with any questions. If you are connected to our [Discord server](https://discord.gg/v4wDGh3), feel free to ask for help in #github-help

We are thrilled to accept new and updated airports. We also would welcome markdown files in the [GitHub wiki](https://github.com/AdamJCavanaugh/EndlessATCAirports/wiki) with gameplay tips - especially for more advanced usage (such as STAR) - and development tips/guidelines. Those who wish to volunteer to test updates before they are finalized should open an issue to volunteer.

Finally, all players, testers, and developers are encouraged to join our [Discord server](https://discord.gg/v4wDGh3) for extra assistance and information.

## Directory/file naming

1. All files that have been customized should be placed in the final folder.
2. The directory structure below that follows the continent abbreviation found [here](https://datahub.io/core/continent-codes)
3. The directory structure should have the four character [ICAO code](https://airportcodes.aero/-/list-icao-codes)
4. The file should have the four character [ICAO code](https://airportcodes.aero/-/list-icao-codes), with a .txt extension.
5. Alternate configurations should be differentiated by adding "_description", such as IACO_27s.txt
6. "Fantasy" or other airports that cannot be placed in this structure should go into final/custom
For example, Zurich airport is placed in `final/EU/LSZH/LSZH.txt`. Hong Kong has both `final/AS/VHHH/VHHH_mobile.txt` and `final/AS/VHHH/VHHH_PC.txt`

## Extra file information

It is highly encourage to remove the first seven lines of comments, since we are no longer using an "automatically generated airport file" at this point.

Is it encouraged to cite any references that you used while creating your file, including the airchart, airliner data, and even airport website.

If you wish to include personal information (such as your contact information), this is allowed, although not necessary.

It may be best to add a markdown file with the same airport code in the same directory with references, information, and a change log (e.g. `final/EU/LSZH/LSZH.md`)

## Credits

[startgrid](https://startgrid.itch.io/)
