# strategy.py

class StrategyManager:
    def __init__(self):
        # Initialize equal scores for each strategy
        self.scores = {"logical": 1, "analytical": 1}

    def best(self):
        # Return the strategy with the highest score
        return max(self.scores, key=self.scores.get)

    def update(self, winner):
        # Increment the winning strategy's score
        self.scores[winner] = self.scores.get(winner, 0) + 1

    def get_scores(self):
        return self.scores
