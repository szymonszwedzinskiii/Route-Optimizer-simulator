from optimizer_simulator.load_points import load_points, get_data
from optimizer_simulator.visualizer import print_map

class optimize_routes:
    def __init__(self, path):
        self.data = load_points(path)
        self.paths = get_data(self.data)

    def run(self):
        coords, best_path = get_data(self.data)
        print_map(coords)

