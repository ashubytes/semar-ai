# metrics.py

class Metrics:
    def __init__(self):
        self.total = 0
        self.strategy_counts = {"logical": 0, "analytical": 0}

    def log(self, winner):
        # Increment total runs and the winning strategy count
        self.total += 1
        self.strategy_counts[winner] = self.strategy_counts.get(winner, 0) + 1

    def report(self):
        return {"total_runs": self.total, "strategy_counts": self.strategy_counts}
