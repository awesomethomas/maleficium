### Imports; Coded by Darren Kent
from direct.showbase.ShowBase import ShowBase
from panda3d.core import ConfigVariableString,ConfigVariableDouble, loadPrcFileData
from panda3d.core import NodePath
from panda3d.core import CollisionTraverser,CollisionNode,CollisionHandlerFloor,CollisionHandlerPusher
from panda3d.core import CollisionSphere,CollisionRay
from direct.actor.Actor import Actor
import sys,math
import debug,world


### Game Settings; Coded by Darren Kent
loadPrcFileData('', 'fullscreen 1') # Full Screen
loadPrcFileData('', 'win-size 1366 768') # Screen Size
#loadPrcFileData('', 'sync-video #f') # Vertical Sync

### Main Game; Coded by Darren Kent
class Maleficium(ShowBase):
    def __init__(self):
        compressedTextures = ConfigVariableString('compressed-textures','1') # Compresses Textures on load (increases loadtime / framerate)
        ShowBase.__init__(self)
        
        ## Debug Values (True/False)
        self.fpsMeter = True
        
        debug.checkDebugSettings(self)

        self.KeyBindings()

        ## Load World
        world.load('prisonCrater')

        ## Add Player to World
        self.playerBox = NodePath('player')
        self.player = Actor("data/models/hm.bam",
                            {"run":"data/models/hm-run.bam",
                             "idle":"data/models/hm.bam"})
        self.player.reparentTo(self.playerBox)
        self.player.setScale(.01)
        self.playerBox.reparentTo(render)
        self.isMoving = False

        ## Create Camera
        base.disableMouse()
        self.cameratarget = self.render.attachNewNode('Camera Target')
        base.camera.setPos(self.playerBox.getX(),self.playerBox.getY()+20,self.playerBox.getZ()+5)
        self.cameratarget.setPos(self.playerBox.getX(),self.playerBox.getY(),self.playerBox.getZ()+6)
        self.radius = 10
        self.XYAngle = .028
        self.ZAngle = .01

        ## Set Up Ground Collisions
        ## Player Collision
        base.cTrav = CollisionTraverser()
        self.ColHandler = CollisionHandlerFloor()       
        self.colGroundRay = CollisionNode('colGroundRay')
        self.colGroundRay.addSolid(CollisionRay(0,0,2,0,0,-1))
        self.playerCol = self.playerBox.attachNewNode(self.colGroundRay)
        base.cTrav.addCollider(self.playerCol,self.ColHandler)
        self.ColHandler.addCollider(self.playerCol,self.playerBox)
                                       
        ## Add main Game Loop to taskmanager
        taskMgr.add(self.gameLoop,'mainLoop')


    ### Input Structure; Coded by Darren Kent (Modeled after Roaming-Ralph by Ryan Myers)
    def KeyBindings(self):
        ## Setup Map
        self.startRightClick = True
        
        self.keyMap = {
            "forward":0,
            "backward":0,
            "turn_left":0,
            "turn_right":0,
            "strafe_left":0,
            "strafe_right":0,
            "cam_up":0,
            "cam_down":0,
            "cam_right":0,
            "cam_left":0,
            "zoom_in":0,
            "zoom_out":0,
            "right_click":0,
            "wheel_zoom_in":0,
            "wheel_zoom_out":0,
            }

        ## Accept Keys
        self.accept('escape',sys.exit)
        self.accept('w', self.setKey, ['forward',1])
        self.accept('w-up', self.setKey, ['forward',0])
        self.accept('s', self.setKey, ['backward',1])
        self.accept('s-up', self.setKey, ['backward',0])
        self.accept('a', self.setKey, ['turn_left',1])
        self.accept('a-up', self.setKey, ['turn_left',0])
        self.accept('d', self.setKey, ['turn_right',1])
        self.accept('d-up', self.setKey, ['turn_right',0])
        self.accept('q', self.setKey, ['strafe_left',1])
        self.accept('q-up', self.setKey, ['strafe_left',0])
        self.accept('e', self.setKey, ['strafe_right',1])
        self.accept('e-up', self.setKey, ['strafe_right',0])
        self.accept('arrow_up', self.setKey, ['cam_down',1])
        self.accept('arrow_up-up', self.setKey, ['cam_down',0])
        self.accept('arrow_down', self.setKey, ['cam_up',1])
        self.accept('arrow_down-up', self.setKey, ['cam_up',0])
        self.accept('arrow_right', self.setKey, ['cam_right',1])
        self.accept('arrow_right-up', self.setKey, ['cam_right',0])
        self.accept('arrow_left', self.setKey, ['cam_left',1])
        self.accept('arrow_left-up', self.setKey, ['cam_left',0])
        self.accept('[', self.setKey, ['zoom_in',1])
        self.accept('[-up', self.setKey, ['zoom_in',0])
        self.accept(']', self.setKey, ['zoom_out',1])
        self.accept(']-up', self.setKey, ['zoom_out',0])

        ## Accept Mouse
        self.accept('mouse3',self.setKey, ['right_click',1])
        self.accept('mouse3-up',self.setKey, ['right_click',0])
        self.accept('wheel_up',self.setKey, ['wheel_zoom_in',1])
        self.accept('wheel_down',self.setKey, ['wheel_zoom_out',1])

    ### Set Key Presses; Coded by Darren Kent (Modeled after Roaming-Ralph by Ryan Myers)
    def setKey(self,key,value):
        self.keyMap[key] = value        
            


    ### Main Game Loop; Coded by Darren Kent
    def gameLoop(self,task):

        ## Keyboard Camera Controls
        if (self.keyMap["cam_left"]!=0):
            self.XYAngle += .002
        if (self.keyMap["cam_right"]!=0):
            self.XYAngle -= .002
        if (self.keyMap["cam_up"] != 0):
            if self.ZAngle <= .045:
                self.ZAngle += .001
        if (self.keyMap["cam_down"] != 0):
            if self.ZAngle >= .002:
                self.ZAngle -= .001
        if (self.keyMap["zoom_in"] != 0):
            if self.radius >= 4:
                self.radius -= 1
                self.setRadius = self.radius
        if (self.keyMap["zoom_out"] != 0):
            if self.radius <= 40:
                self.radius += 1
                self.setRadius = self.radius
                
        ## Mouse Camera Controls
        if (self.keyMap["right_click"]!=0):
            if self.startRightClick == True:
                self.startRightClick = False
                self.tempMouseX = base.mouseWatcherNode.getMouseX()
                self.tempMouseY = base.mouseWatcherNode.getMouseY()
                self.tempXAngle = self.XYAngle
                self.tempZAngle = self.ZAngle
                self.tempPlayerH = self.playerBox.getH()
            elif self.startRightClick == False:
                Ztemp = self.tempZAngle + (base.mouseWatcherNode.getMouseY() - self.tempMouseY) / 20
                self.XYAngle = self.tempXAngle - (base.mouseWatcherNode.getMouseX() - self.tempMouseX) / 20
                if Ztemp >= .045:
                    Ztemp = .045
                if Ztemp <= 0.002:
                    Ztemp = 0.002
                self.ZAngle = Ztemp
        else:
            self.startRightClick = True
       
        if (self.keyMap["wheel_zoom_in"] != 0):
            if self.radius >= 7:
                self.radius -= 3
                self.setRadius = self.radius
        if (self.keyMap["wheel_zoom_out"] != 0):
            if self.radius <= 38:
                self.radius += 2
                self.setRadius = self.radius
        self.setKey("wheel_zoom_out",0)
        self.setKey("wheel_zoom_in", 0)

        ## Reposition Camera
        x = self.cameratarget.getX() + self.radius * math.sin(math.degrees(self.ZAngle)) * math.cos(math.degrees(self.XYAngle))
        y = self.cameratarget.getY() + self.radius * math.sin(math.degrees(self.ZAngle)) * math.sin(math.degrees(self.XYAngle))
        z = self.cameratarget.getZ() + self.radius * math.cos(math.degrees(self.ZAngle))
        base.camera.setPos(x,y,z)
        base.camera.lookAt(self.cameratarget)
        self.cameratarget.setPos(self.playerBox.getX(),self.playerBox.getY(),self.playerBox.getZ()+6)


        ## Keyboard Movement Controls
        if (self.keyMap["turn_left"]!=0):
            self.playerBox.setH(self.playerBox.getH() + 200 * globalClock.getDt())
        if (self.keyMap["turn_right"]!=0):
            self.playerBox.setH(self.playerBox.getH() - 200 * globalClock.getDt())
        if (self.keyMap["strafe_left"]!=0):
            self.playerBox.setX(self.playerBox, +20 * globalClock.getDt())
        if (self.keyMap["strafe_right"]!=0):
            self.playerBox.setX(self.playerBox, -20 * globalClock.getDt())
        if (self.keyMap["forward"]!=0):
            self.playerBox.setY(self.playerBox, -25 * globalClock.getDt())
        if (self.keyMap["backward"] != 0):
            self.playerBox.setY(self.playerBox, +15 * globalClock.getDt())

        if (self.keyMap["forward"]!=0):
            if self.isMoving == False:
                self.player.setPlayRate(2.5,'run')
                self.player.loop('run')
                self.isMoving = True
        else:
            if self.isMoving:
                self.player.setPlayRate(1,'idle')
                self.player.loop('idle')
                self.isMoving = False

        ## Check Collisions
            

        return task.cont

# Start the Game on Run
start = Maleficium()
start.run()
