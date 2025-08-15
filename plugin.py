class BeaconPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        position = sender.getLocation()
        position.setX(position.getX() + 2)

        world = sender.getWorld()
        for i in range(0, 10):
            block = world.getBlockAt(position)
            block.setType(bukkit.Material.GOLD_BLOCK)
            position.setY(position.getY() + 1)

        return True