import sys

from optimizer_simulator.optimizer import optimize_routes

if __name__ == "__main__":
    if len(sys.argv) <2:
        print("Usage: python main.py <path to input data>")
        sys.exit(1)

    csv_path = sys.argv[1]
    optimize_routes(csv_path)