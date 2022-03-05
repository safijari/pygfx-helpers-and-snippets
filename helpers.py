import pygfx as gfx
# from wgpu.gui.auto import WgpuCanvas, run
from wgpu.gui.offscreen import WgpuCanvas, run
from abc import ABC, abstractmethod
import glfw


class StandardScene(ABC):
    def __init__(self, perspective=True):
        self.canvas = WgpuCanvas(max_fps=1000)
        self.renderer = gfx.renderers.WgpuRenderer(self.canvas)
        self.scene = gfx.Scene()
        self.camera = (
            gfx.PerspectiveCamera(70, 16 / 9)
            if perspective
            else gfx.OrthographicCamera()
        )
        self.controls = gfx.OrbitControls()
        self.controls.add_default_event_handlers(self.canvas, self.camera)

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def animate_fn(self):
        pass

    def animate(self):
        self.animate_fn()
        self.controls.update_camera(self.camera)
        self.renderer.render(self.scene, self.camera)
        print("got here")
        self.canvas.request_draw()

    def start(self):
        self.setup()
        self.canvas.request_draw(self.animate)
        run()
