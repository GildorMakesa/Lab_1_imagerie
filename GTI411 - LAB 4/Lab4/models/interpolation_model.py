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
            return  # Pas assez de points pour une courbe

        def linear_bezier(p0, p1, t):
            x = (1 - t) * p0[0] + t * p1[0]
            y = (1 - t) * p0[1] + t * p1[1]
            return int(x), int(y)

        def quadratic_bezier(p0, p1, p2, t):
            x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
            y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
            return int(x), int(y)

        def cubic_bezier(p0, p1, p2, p3, t):
            x = ((1 - t)**3 * p0[0] +
                3 * (1 - t)**2 * t * p1[0] +
                3 * (1 - t) * t**2 * p2[0] +
                t**3 * p3[0])
            y = ((1 - t)**3 * p0[1] +
                3 * (1 - t)**2 * t * p1[1] +
                3 * (1 - t) * t**2 * p2[1] +
                t**3 * p3[1])
            return int(x), int(y)

        curve = []
        for t in [i / 100 for i in range(101)]:
            if len(self.points) == 2:
                pt = linear_bezier(self.points[0], self.points[1], t)
            elif len(self.points) == 3:
                pt = quadratic_bezier(self.points[0], self.points[1], self.points[2], t)
            elif len(self.points) == 4:
                pt = cubic_bezier(self.points[0], self.points[1], self.points[2], self.points[3], t)
            else:
                break  # Optionnel : gérer +4 points avec De Casteljau ou ignorer
            curve.append(pt)

        for i in range(len(curve) - 1):
            cv2.line(self.canvas, curve[i], curve[i + 1], (0, 255, 255), 2)  # Jaune

    """
    def draw_bezier(self):
        
        if len(self.points) < 2:
            return  # Il faut au moins 2 points

        def bezier_point(t, points):
            "Calcule un point de Bézier en utilisant l'algorithme de De Casteljau."
            while len(points) > 1:
                points = [(1 - t) * np.array(p1) + t * np.array(p2) for p1, p2 in zip(points[:-1], points[1:])]
            return tuple(map(int, points[0]))  # Convertit le dernier point en coordonnées entières

        curve_resolution = 100  # Plus la valeur est élevée, plus la courbe est lisse
        bezier_curve = [bezier_point(t, self.points) for t in np.linspace(0, 1, curve_resolution)]

        # Dessiner la courbe de Bézier
        for i in range(len(bezier_curve) - 1):
            cv2.line(self.canvas, bezier_curve[i], bezier_curve[i + 1], (0, 255, 255), thickness=2)  # Jaune
        """

        # return points


    def draw_hermite(self):
        if len(self.points) < 4 or len(self.points) % 2 != 0:
            return  # Il faut un nombre pair de points (minimum 4)

        # Regrouper les points deux par deux pour former des vecteurs
        vectors = []
        centers = []
        for i in range(0, len(self.points) - 1, 2):
            p1 = np.array(self.points[i])
            p2 = np.array(self.points[i + 1])
            center = (p1 + p2) / 2
            tangent = p2 - p1
            centers.append(center)
            vectors.append(tangent)

            # Dessiner les vecteurs pour la visualisation
            cv2.line(self.canvas, tuple(p1.astype(int)), tuple(p2.astype(int)), (0, 255, 0), 1)
            cv2.circle(self.canvas, tuple(center.astype(int)), 4, (255, 255, 0), -1)

        # Dessiner les courbes Hermite entre les centres
        for i in range(len(centers) - 1):
            P0 = centers[i]
            P1 = centers[i + 1]
            T0 = vectors[i] * 0.5  # On peut ajuster l'influence avec ce facteur
            T1 = vectors[i + 1] * 0.5

            previous = None
            for t in np.linspace(0, 1, 100):
                h00 = 2 * t**3 - 3 * t**2 + 1
                h10 = t**3 - 2 * t**2 + t
                h01 = -2 * t**3 + 3 * t**2
                h11 = t**3 - t**2

                point = h00 * P0 + h10 * T0 + h01 * P1 + h11 * T1
                point = tuple(point.astype(int))

                if previous:
                    cv2.line(self.canvas, previous, point, (255, 0, 255), 2)  # Magenta
                previous = point


    def draw_spline(self):
        if len(self.points) < 4:
            return  # Il faut au moins 4 points pour une B-spline cubique

        def bspline_point(t, p0, p1, p2, p3):
            t2 = t * t
            t3 = t2 * t

            b0 = (-t3 + 3*t2 - 3*t + 1) / 6.0
            b1 = (3*t3 - 6*t2 + 4) / 6.0
            b2 = (-3*t3 + 3*t2 + 3*t + 1) / 6.0
            b3 = (t3) / 6.0

            x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
            y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
            return (int(x), int(y))

        # Générer la courbe pour chaque segment de 4 points consécutifs
        for i in range(len(self.points) - 3):
            p0 = self.points[i]
            p1 = self.points[i + 1]
            p2 = self.points[i + 2]
            p3 = self.points[i + 3]

            prev = bspline_point(0, p0, p1, p2, p3)
            for t in np.linspace(0, 1, 100):
                pt = bspline_point(t, p0, p1, p2, p3)
                cv2.line(self.canvas, prev, pt, (0, 165, 255), 2)  # Orange
                prev = pt

        
    def get_canvas(self):
        self.draw()
        return self.canvas