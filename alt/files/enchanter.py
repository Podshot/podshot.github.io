from pymclevel.nbt import *

def perform(level, box, options):

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Trap" or t["id"].value == "Dropper":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    for item in t["Items"]:
                        if "tag" not in item:
                            item["tag"] = TAG_Compound()
                        if "ench" not in item["tag"]:
                            item["tag"]["ench"] = TAG_List()

                            bre = TAG_Compound()
                            bre["id"] = TAG_Short(34)
                            bre["lvl"] = TAG_Short(10)
                            item["tag"]["ench"].append(bre)

                    chunk.dirty = True
