import pygfx as gfx
from wgpu.gui.auto import WgpuCanvas, run


class StandardScene:
    def __init__(self, perspective=True, animate_fn=None):
        self.canvas = WgpuCanvas()
        self.renderer = gfx.renderers.WgpuRenderer(self.canvas)
        self.scene = gfx.Scene()
        self.camera = (
            gfx.PerspectiveCamera(70, 16 / 9)
            if perspective
            else gfx.OrthographicCamera()
        )
        self.controls = gfx.OrbitControls()
        self.controls.add_default_event_handlers(self.canvas, self.camera)
        self.animate_fn = animate_fn

    def animate(self):
        assert self.animate_fn is not None
        self.animate_fn()
        self.controls.update_camera(self.camera)
        self.renderer.render(self.scene, self.camera)
        self.canvas.request_draw()

    def start(self):
        self.canvas.request_draw(self.animate)
        run()
