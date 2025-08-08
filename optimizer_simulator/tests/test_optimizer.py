from optimizer_simulator.optimizer import optimize_routes
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_PATH = os.path.join(BASE_DIR,"test_points.csv")


def fake_get_data(points):
    coords = [(50.0, 20.0), (52.0, 22.0), (48.0, 21.5)]
    best_path = [0,2,1]
    return coords,best_path

def fake_print_map(coords):
    print(f"Fake map  with points: {coords}")

def test_init_and_run(monkeypatch):
    monkeypatch.setattr("optimizer_simulator.load_points.get_data", fake_get_data)
    monkeypatch.setattr("optimizer_simulator.optimizer.print_map", fake_print_map)

    optimizer = optimize_routes(TEST_PATH)

    assert optimizer.data is not None
    assert hasattr(optimizer, "paths")

    optimizer.run()