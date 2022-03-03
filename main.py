import time
import numpy as np
from helpers import StandardScene
import pygfx as gfx

ss = StandardScene()

# Populate a scene with a cube
scene = ss.scene
geometry = gfx.box_geometry(200, 200, 200)
material = gfx.MeshPhongMaterial(color=(1, 1, 0, 1))
cube = gfx.Mesh(geometry, material)
scene.add(cube)


def update():
    rot = gfx.linalg.Quaternion().set_from_euler(gfx.linalg.Euler(0.005, 0.01))
    cube.rotation.multiply(rot)


ss.animate_fn = update

ss.start()
