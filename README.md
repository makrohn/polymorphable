Laurelia's Polymorphable Citizens
=================================

Originally created for the 2012 Liberated Pixel Cup, this game is based upon Clint Bellanger's FLARE engine.  Our goal is to create a game which draws upon several different classics in the genre, with a heavy emphasis on polymorphable main character.

Laurelia's Polymorphable Citizen (or just Polymorphable for short) is an action-rpg based on the Flare engine. We're aiming a little more towards an 8-bit adventure classic feel, only with more RPG aspects (ie. attribute choices on level up!)

The core mechanic in Polymorphable is using different talismans to polymorph into different forms so you can reach different areas. Imagine being blocked by a pit, so you transform into a bat to fly across. Or perhaps there's a wall of fire in front of you, so you turn into ghost form to phase right through.

Installation and Use
====================

Polymorphable is a total conversion mod based upon the Flare engine, v1.x.  If you'd like to play Polymorphable, install Flare v1.x, and then put the mods/polymorphable folder into Flare's mod folder.

Mac OSX and Windows
- A pre-packaged Polymorphable binary with Flare 0.18 Engine can be found here: https://sourceforge.net/projects/polymorphable/files/?source=navbar

Linux
- Install Flare v1.x using your favorite package manager, or compile from source from https://github.com/clintbellanger/flare-engine/tree/master
- Copy the entire mods/polymorphable folder into the Flare-game mods/ directory.

All distributions
- At the Flare launch screen, enter "Configuration"
- Click the "Mods" tabs
- Make sure that "polymorphable" is the only item in the right-hand column

Savefile Change!
================

On 2/21/2013, the savefile mechanic was changed.  If you want to use your old savefiles from before the change, copy them from your Polymorphable save directory to your Flare save directory, and rename them from save#.txt to poly_save#.txt

Packaging and Distributing
==========================

If you are packaging Polymorphable for release (e.g. on an operating system's software repo), we suggest creating two packages.

* flare-engine the package that contains the single engine reused by several games
* polymorphable, a package that requires flare-engine that only contains this game data

When distributing flare-game you may elect to omit these folders which are not used at runtime.

* art_src contains the raw files (e.g. Blender files) used to generate Flare's art.
* tiled contains the Tiled-native map files used to export Flare's maps
