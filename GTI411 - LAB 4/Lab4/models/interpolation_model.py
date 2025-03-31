import cv2
import numpy as np



class InterpolationModel:
    width = 1245
    height = 440

    point_radius = 6
    
    def __init__(self):
        self.curve_type = "Linear"
        self.reset()


    def reset_canvas(self):
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)


    def reset(self):
        self.points = []
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)


    def add_point(self, x, y):
        print(f"Adding point x={x} y={y}")
        self.points.append([x, y])
        cv2.circle(self.canvas, (round(x), round(y)), 5, (255, 0, 0), thickness=-1)


    def set_curve_type(self, curve:str):
        print(f"Changed curve type to {curve}")
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.curve_type = curve


    def try_to_move_point(self, start_pt:tuple[int], end_pt:tuple[int]):
        print(f"Start = {start_pt} | End = {end_pt}")

        x, y = start_pt
        clicked_point_idx = None
        for idx, (xc, yc) in enumerate(self.points):
            if np.sqrt((x - xc)**2 + (y - yc)**2) < self.point_radius:
                clicked_point_idx = idx
                break
        
        if clicked_point_idx is not None:
            self.points[clicked_point_idx] = end_pt


    
    def draw(self):
        self.reset_canvas()

        if self.curve_type == "Linear":
            self.draw_linear()
        elif self.curve_type == "Bezier":
            self.draw_bezier()
        elif self.curve_type == "Hermite":
            self.draw_hermite()
        elif self.curve_type == "BSpline":
            self.draw_spline()

        for x, y in self.points:
            cv2.circle(self.canvas, (round(x), round(y)), self.point_radius, (255, 0, 0), -1)

    
    def draw_linear(self):
        if len(self.points) < 2:
            return  # Il faut au moins 2 points pour tracer une ligne

        for i in range(len(self.points) - 1):
            pt1 = tuple(map(round, self.points[i]))
            pt2 = tuple(map(round, self.points[i + 1]))
            cv2.line(self.canvas, pt1, pt2, (0, 255, 0), thickness=2)  # Vert



    def draw_bezier(self):
        
        if len(self.points) < 2:
            return  # Il faut au moins 2 points

        def bezier_point(t, points):
            """Calcule un point de Bézier en utilisant l'algorithme de De Casteljau."""
            while len(points) > 1:
                points = [(1 - t) * np.array(p1) + t * np.array(p2) for p1, p2 in zip(points[:-1], points[1:])]
            return tuple(map(int, points[0]))  # Convertit le dernier point en coordonnées entières

        curve_resolution = 100  # Plus la valeur est élevée, plus la courbe est lisse
        bezier_curve = [bezier_point(t, self.points) for t in np.linspace(0, 1, curve_resolution)]

        # Dessiner la courbe de Bézier
        for i in range(len(bezier_curve) - 1):
            cv2.line(self.canvas, bezier_curve[i], bezier_curve[i + 1], (0, 255, 255), thickness=2)  # Jaune


        # return points


    # TODO
    def draw_hermite(self):
        pass

    # TODO
    def draw_spline(self):
        pass
        
    def get_canvas(self):
        self.draw()
        return self.canvas