from PyQt5 import QtWidgets
from Lab4.models import InterpolationModel, TransformationModel

from Lab4.views import Ui_Lab4_Window
from Lab4.events import event_manager



class Lab4Controller:
    def __init__(self) -> None:
        self.interp_model = InterpolationModel()
        self.transf_model  = TransformationModel()

        self.window = QtWidgets.QMainWindow()
        self.start_point, self.end_point = None, None
        ui = Ui_Lab4_Window()

        ui.setupUi(self.window)

        # ui.interpolation_tab.update_canvas(self.interp_model.get_canvas())

        event_manager.register("on_load_image", self.load_image)
        event_manager.register("on_canvas_click", self.canvas_click)
        event_manager.register("on_reset_canvas", self.reset_canvas)
        event_manager.register("on_curve_type_changed", self.change_curve_type)
        event_manager.register("on_apply_transformation", self.apply_transformation)
        event_manager.register("on_update_transformation_param", self.update_trans_param)
        event_manager.register("on_mouse_click_move", self.on_mouse_click_move)
        event_manager.register("on_mouse_click_released", self.mouse_click_released)
        event_manager.trigger("on_draw_canvas", self.interp_model.get_canvas())

        self.window.show()


    def mouse_click_released(self):
        if self.start_point is None or self.end_point is None:
            return
        self.interp_model.try_to_move_point(self.start_point, self.end_point)
        self.start_point = None
        self.end_point = None
        event_manager.trigger("on_draw_canvas", self.interp_model.get_canvas())


    def on_mouse_click_move(self, x, y):
        if self.start_point is None:
            self.start_point = (x, y)
        self.end_point = (x, y)
        

    def update_trans_param(self, value, param:str):
        self.transf_model.update_param(value, param)


    def load_image(self, filepath:str):
        import cv2

        image = cv2.imread(filepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = self.transf_model.set_image(image)
        event_manager.trigger("on_image_loaded", image, "all")


    def apply_transformation(self, transformation:str):
        image = self.transf_model.apply_transformation(transformation)
        if image is not None:
            event_manager.trigger("on_image_loaded", image, transformation)


    def change_curve_type(self, curve:str):
        self.interp_model.set_curve_type(curve)
        event_manager.trigger("on_draw_canvas", self.interp_model.get_canvas())


    def reset_canvas(self):
        self.interp_model.reset()
        event_manager.trigger("on_draw_canvas", self.interp_model.get_canvas())

    def canvas_click(self, x, y):
        self.interp_model.add_point(x, y)
        event_manager.trigger("on_draw_canvas", self.interp_model.get_canvas())

