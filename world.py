from panda3d.core import Vec4
from panda3d.core import TextureStage
from panda3d.core import Fog, AmbientLight,DirectionalLight

### Load World; Coded by Darren Kent
def load(zone):
    if zone == 'prisonCrater':
        loadPrisonCrater()


### Prison Crater; Coded by Darren Kent
def loadPrisonCrater():
    ## Sky color
    base.win.setClearColor(Vec4(.46,.824,.904,1))

    ## Load Ground
    sand = loader.loadModel("data/models/sand.bam")
    sand.reparentTo(render)
    sand.setTexScale(TextureStage.getDefault(),5000,5000)

    craterwalls = loader.loadModel("data/models/craterwalls.bam")
    craterwalls.reparentTo(render)
    craterwalls.setTexScale(TextureStage.getDefault(),500,50)

    ## World Effects
    fog = Fog("Fog")
    fog.setColor(255,215,143)
    fog.setExpDensity(.0000001)
    render.setFog(fog)

    alight = render.attachNewNode(AmbientLight("Abient"))
    alight.node().setColor(Vec4(.9,.9,.9,1))
    render.setLight(alight)

    sun = DirectionalLight('Sun')
    sun.setColor(Vec4(1,1,1,1))
    sunNP = render.attachNewNode(sun)
    sunNP.setPos(0,0,4000)
    sunNP.setHpr(0,-90,0)
    render.setLight(sunNP)
