from PyQt5 import QtCore, QtGui, QtWidgets

from Lab1.views import Lab1_UI
from Lab1.models import Lab1ColorConvertModel, Lab1DecompositionModel, Lab1ImageTransformsModel
from Lab1.events import event_manager


class Lab1Controller:
    def __init__(self) -> None:

        self.model = Lab1ColorConvertModel()
        self.decomposition_model = Lab1DecompositionModel()
        self.transform_model = Lab1ImageTransformsModel()

        event_manager.register("on_confirm_color_change", self.revert_color_update)
        event_manager.register("on_color_update", self.update_color)
        event_manager.register("on_add_shape", self.add_shape)
        event_manager.register("on_open_interpolation_window", self.open_window)
        event_manager.register("on_image_loaded", self.set_image)
        event_manager.register("on_decompose_image", self.image_decomposition)
        event_manager.register("on_update_decomp_method", self.update_image_decomp_method)

        event_manager.register("on_apply_image_transform", self.transform_image)

        self.window = QtWidgets.QMainWindow()
        self.ui = Lab1_UI()
        self.ui.setupUi(self.window)

        self.window.show()


    def set_image(self, image):
        self.decomposition_model.set_image(image)
        self.transform_model.set_image(image)


    def transform_image(self, constrast, luminosity):
        image = self.transform_model.transform_image(constrast, luminosity)
        event_manager.trigger("on_image_updated", image)


    def update_image_decomp_method(self, method:str):
        self.decomposition_model.set_color_space(method)


    def image_decomposition(self):
        print("Decompose")
        fig = self.decomposition_model.decompose_image()


    def revert_color_update(self, confirm:bool):
        if confirm:
            self.model.confirm_color_changes()
            return
        r, g, b = self.model.revert_color_changes()
        event_manager.trigger("on_color_update_ready", r, g, b)


    def open_window(self):
        r, g, b = self.model.rgb
        self.ui.openWindowInterpolation(r, g, b)


    def add_shape(self, shape:str):
        r, g, b = self.model.rgb
        event_manager.trigger("on_add_shape_ready", r, g, b, shape)
    

    def update_color(self, values: list[float], mode:str):
        r, g, b = self.model.update_color(values, mode)
        event_manager.trigger("on_color_update_ready", r, g, b)
        # event_manager.trigger("on_color_updated", r, g, b)
        