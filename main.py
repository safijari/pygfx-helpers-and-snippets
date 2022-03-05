import time
import numpy as np
from helpers import StandardScene
import pygfx as gfx
import trimesh

import imageio


class Test(StandardScene):
    def setup(self):
        self.keycap_geom = gfx.trimesh_geometry(
            trimesh.load("/home/jari/Downloads/xda_keycap_v5.stl")
        )
        im = imageio.imread("imageio:bricks.jpg")
        self.tex = gfx.Texture(im, dim=2).get_view(filter="linear", address_mode="repeat")
        # self.keycap_geom.texcoords.data[:, 0] *= 10  # stretch the texture
        self.keycap = gfx.Mesh(self.keycap_geom, gfx.MeshPhongMaterial(color="red"))
        self.scene.add(self.keycap)
        self.prev_time = time.time()

    def animate_fn(self):
        # rot = gfx.linalg.Quaternion().set_from_euler(gfx.linalg.Euler(0.005, 0.01))
        # self.cube.rotation.multiply(rot)
        print(time.time() - self.prev_time)
        self.prev_time = time.time()


Test().start()

while True:
    pass