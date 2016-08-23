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
to change the file type in the <a target="_blank" href="\images\2016\8\22\01.png">save dialog</a> to change the format the file is saved in.
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
<h5><b>BlockstateAPI</b></h5>
With Minecraft moving away from IDs and using a string/name system for identifying blocks, you can now
have blocks inputs based on a Blockstate string. Example:
<br>
{% highlight python %}
from pymclevel.materials import alphaMaterials
inputs = (
	("Block Method #1", ("block", "minecraft:stone[variant=granite]"),
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
<h4>Block Info Summaries</h4>
Hovering over a block now gives a summary of important information about the Block. <a target="_blank" href="\images\2016\8\22\02.png">Example</a>
