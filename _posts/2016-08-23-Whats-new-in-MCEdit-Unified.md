---
layout: post
title:  "What's New in MCEdit-Unified"
date:   2016-08-23
comments: true
categories: mcedit
---
Since there has been a decent amount of time since our last release, I decided to
write a quick summary of all the features/changes that have been made. Please note
that some of these changes are internal, so you won't necessarily notice them. This
is probably not an exhaustive list, and is mostly just the feature I worked on.

<br>
<h4>Structure Blocks</h4>
In Minecraft 1.10, Structure Blocks were introduced to save in-game buildings to files, 
where you could them share them with friends or reimport them in another location
in the world in-game via another Structure Block. (IE: Vanilla Minecraft's version of Schematics)
Well, MCEdit-Unified now has the ability to import and export .nbt files! Importing them
is the same way as importing a regular schematic. However, for exporting, you will need
to change the file type in the <a target="_blank" rel="noopener noreferrer" href="\images\2016\8\23\01.png">save dialog</a> to change the format the file is saved in.
(Schematic vs. Structure .nbt)

Filter creators can also use Structure files in their filters, but this will be detailed in a later section.

<br>
<h4>Blockstates</h4>
Blockstates have been present in Minecraft for a few versions, however, they way they would
be saved wasn't, until Structure .nbt files were introduced. To achieve this, I created an 
API to convert from Integer-based IDs to Blockstates. Here is a very brief and bare-bones snippet
of how to use it:
<br>
{% highlight python %}
from pymclevel import materials

api = materials.alphaMaterials.blockstate_api # Recommened way to access the API
api = BlockstateAPI.material_map[materials.alphaMaterials] # Another way

api.block_map[<id>] # Same as it's always been, give an ID and it will give the basename for the block
print api.block_map[3] # Prints "minecraft:dirt"

example_1 = api.idToBlockState(1, 2) # Give the ID and Data values, returns the Blockstate as a tuple
print example_1 # Prints "('stone', {'variant': 'smooth_granite'})"
# First index is the basename without the "minecraft:", the second is a dict with the Properties of that Blockstate

example_2 = api.blockstateToID("minecraft:stone", {"variant": "andesite"}))
# Give it the basename and a dict of properties
print example_2 # Prints a tuple of (<id>, <data>) In this case: (1, 5)

example_3 = materials.idToBlockstate(1, 2) # Same as "example_1", but this is not recommened
{% endhighlight %}

<em>Note: This currently only works with PC Blocks, but materials.\<function\> 
(like the way in example_3) will always point
to PC Block definitions/"alphaMaterials"</em>

<br>
<h4>Additions to Filters</h4>
<a name="Filters.Blockstates"></a>
<h5><b>BlockstateAPI</b></h5>
With Minecraft moving away from IDs and using a string/name system for identifying blocks, you can now
have blocks inputs based on a Blockstate string. Example:
<br>
{% highlight python %}
from pymclevel.materials import alphaMaterials
inputs = (
	("Block Method #1", ("block", "minecraft:stone[variant=granite]")),
	("Block Method #2", alphaMaterials["minecraft:stone[variant=granite]"]),
	("Another Option", true),<br>
    )
{% endhighlight %}
<br>
This will still present a regular Block picker option to the user
<br>
<h5><b>StructureNBT</b></h5>
You can also now interact with Structure NBT files by using the StructureNBT class in pymclevel.schematics.
Here is an example:
<br>
{% highlight python %}
from pymclevel.schematic import StructureNBT

structure = StructureNBT(filename="/Some/Test/File.nbt")

structure.Blocks[0,0,0] = (5, 3) # Coordinate order is x,y,z, values are (\<id\>, \<data\>) tuples

structure.Palette # List of Blockstates in complete form. IE: minecraft:planks[variant=jungle]

schem = structure.toSchematic() # Converts and returns the StructureNBT in Schematic format

new_schem = Structure.fromSchematic("/Some/Schematic.Schematic") # Converts a Schematic to StructureNBT

structure.save("/New_Structure.nbt") # I'll let you figure out what this one does...
{% endhighlight %}

<br>
<a name="Static_Definitions"></a>
<h4>Block Info Summaries</h4>
Hovering over a block now gives a summary of important information about the Block. <a target="_blank" rel="noopener noreferrer" href="\images\2016\8\23\02.png">Example</a>

<br>
<h4>Static Block Definitions</h4>
Due to various reasons, I am (unofficially) stating that accessing the static block definitions
is deprecated and shouldn't be used. They will still work, however. I've come to this decision
due to the following reasons:

- Static Block definitions are missing lots of blocks
  - It's hard to find which blocks are missing
<br>
- Naming and Data values are inconsistent
  - Some Blocks have all of their various Data values present, others have none
  - Facing Direction Data values are also inconsistent (in Minecraft)
<br>
- Blocks with Data values are sometimes hard to name (IE: Blocks that can face different directions)
<br>
- Blockstates/names can exist across various editions, while Static definitions don't
  - IE: "minecraft:grass_path" points to 208 for PC/Java, while it points to 198 for Pocket Edition
    - We actually have this problem with our renderer, to check it out, open up a MCPE world and look at a Grass Path block or <a target="_blank" href="\images\2016\8\23\04.png">here</a>
- Aren't based off of our definition files
  - They have to manually added to pymclevel/materials.py
- Requires knowledge of what kind of materials are being used
  - While PC (Java) edition supports Command Blocks, MCPE doesn't, so if a filter puts a Command Block in a MCPE world, it could cause the game to crash or perform unexpected behaviour
  
 Here's an example of why using Static Block Definitions is bad:
 {% highlight python %}
 from pymclevel.materials import alphaMaterials
 
 inputs = (
	("Block", alphaMaterials.EndRod),
 )
 
 def perform(level, box, options):
	
	block = options["Block"].ID
	origin_x = box.minx + 1
	origin_y = box.miny + 1
	origin_z = box.minz + 1
	
	level.setBlockAt(origin_x, origin_y, origin_z, alphaMaterials.Purpur.ID)
	
	level.setBlockAt(origin_x, origin_y + 1, origin_z, block)
	level.setBlockAt(origin_x, origin_y - 1, origin_z, block)
	
	level.setBlockAt(origin_x + 1, origin_y, origin_z, block)
	level.setBlockAt(origin_x - 1, origin_y, origin_z, block)
	
	level.setBlockAt(origin_x, origin_y, origin_z + 1, block)
	level.setBlockAt(origin_x, origin_y, origin_z - 1, block)
{% endhighlight %}
As you could probably tell, this is a simple filter, it just puts End Rods on every side of a Purpur block.
However, it places completely different blocks if it's in a PC world vs. a Pocket Edition world:
<br>
<a target="_blank" rel="noopener noreferrer" href="\images\2016\8\23\03.png"><b>PC World Output</b></a>
<br>
<a target="_blank" rel="noopener noreferrer" href="\images\2016\8\23\04.png"><b>Pocket Edition World Output</b></a> (This is renderer issue I mentioned earlier, those wierdly
textured End Rods are actually Grass path blocks, and would be so if opened in MCPE)

This is not only inconsistent behaviour (the Grass Path block vs. the End Rod), but it introduces a Unknown Block
into the world, which could cause a crash. It also makes the output unpredicatable, if the filter is ran
with default inputs (and in a MCPE world), the block picked is not the block actually placed, which would confuse the user.

So in conclusion, I would like to ask filter creators to use the <a href="#Filters.Blockstates">Blockstate API</a> for any new filters they create after the
next release (preferably use the way used in "Block Method #1"). Again, <b>the old way will still work</b>, so your filters
won't break, at least until PC switches completely from IDs to Blockstates.
 