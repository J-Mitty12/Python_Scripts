import maya.cmds as cmds

# Create body
cmds.polyCube(width=7, height=10, depth=3.5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(0, 10, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

# create leg (r)
cmds.polyCube(width=1, height=5, depth=2, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(1.5, 5, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

# create leg (l)
cmds.polyCube(width=1, height=5, depth=2, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(-1.5, 5, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

# create arm (r)
cmds.polyCube(width=1, height=5, depth=2, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(4, 10.5, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

# create arm (l)
cmds.polyCube(width=1, height=5, depth=2, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(-4, 10.5, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

# create head
cmds.polyCube(width=4, height=3, depth=3, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(0, 17, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

# create eyes
cmds.polySphere(radius=1, subdivisionsX=10, subdivisionsY=10, axis=[0, 1, 0], constructionHistory=1)
cmds.move(0.88, 17.5, -1.2, relative=True)
cmds.scale(0.6, 0.6, 0.6, relative=True)

cmds.polySphere(radius=1, subdivisionsX=10, subdivisionsY=10, axis=[0, 1, 0], constructionHistory=1)
cmds.move(-0.99, 17.5, -1.2, relative=True)
cmds.scale(0.6, 0.6, 0.6, relative=True)

# create base cylinder for mouth
cmds.polyCylinder(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, constructionHistory=1)
cmds.rotate(0, 0, 90, relative=True, objectSpace=True)
cmds.move(0.03, 16.2, -1.5, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.scale(0.37, 0.85, 0.37, relative=True)

# create base front piece
cmds.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(0, 11, -1.7, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.scale(4.5, 5.15, 0.9, relative=True)

# create front buttons
cmds.polyCylinder(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, constructionHistory=1)
cmds.move(1, 12.6, -2, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.rotate(-90, 0, 0, relative=True, objectSpace=True)
cmds.scale(0.7, 0.7, 0.7, relative=True)

cmds.polyCylinder(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], roundCap=0, constructionHistory=1)
cmds.move(1, 9.8, -2, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.rotate(-90, 0, 0, relative=True, objectSpace=True)
cmds.scale(0.7, 0.7, 0.7, relative=True)

# create front long piece
cmds.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], constructionHistory=1)
cmds.move(-0.9, 11.2, -2.3, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.scale(1.2, 4.08, 0.9, relative=True)
