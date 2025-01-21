


class Lab1ColorConvertModel:
    def __init__(self) -> None:
        self.curr_r: int = 255
        self.curr_g: int = 0
        self.curr_b: int = 0

        self.previous_rgb = [self.curr_r, self.curr_g, self.curr_b]

    @property
    def rgb(self):
        return self.curr_r, self.curr_b, self.curr_g

    
    def update_color(self, values: list[float], mode:str = "rgb"):
        # print(f"Color {values} {mode}")
        r, g, b = values
        self.curr_r = r
        self.curr_g = g
        self.curr_b = b
        return self.curr_r, self.curr_g, self.curr_b
    

    def confirm_color_changes(self):
        self.previous_rgb = [self.curr_r, self.curr_g, self.curr_b]
    

    def revert_color_changes(self):
        r, g, b = self.previous_rgb
        self.curr_r = r
        self.curr_g = g
        self.curr_b = b
        return self.curr_r, self.curr_g, self.curr_b