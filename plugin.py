# This Python file uses the following encoding: utf-8
import os, sys

import bukkit


class BeaconPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        position = sender.getLocation()
        position.setX(position.getX() + 2)

        world = sender.getWorld()
        block = world.getBlockAt(position)
        block.setType(bukkit.Material.GOLD_BLOCK)

        return True