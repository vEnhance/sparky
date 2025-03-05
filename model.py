import datetime
import yaml
import config

# Bet format
# {weight, name, birthdate, outcome}


class Manager:
    def __init__(self, path=None):
        self.path = path
        try:
            with open(self.path, "r") as f:
                self.bets = yaml.load(f)
        except IOError:
            self.bets = None
            self.save()
            print("Created {} because it was not found.".format(self.path))
        if self.bets is None:
            self.bets = []
        self.commit()

    def save(self):
        """Saves the current bets into the YAML file."""
        with open(self.path, "w") as f:
            f.write(yaml.dump(self.bets))

    def commit(self):
        self.refresh_indices()
        self.save()

    def refresh_indices(self):
        """Assigns indices to each of the bets properly."""
        for i, bet in enumerate(self.bets):
            bet["index"] = i

    def add_bet(self, **kwargs):
        self.add_bet_arg(kwargs)

    def add_bet_arg(self, data):
        data["birthdate"] = data.get("birthdate", datetime.datetime.now())
        data["outcome"] = data.get("outcome", None)
        assert "weight" in data, data
        assert data["weight"] in config.WEIGHTS, "Invalid Weight {0} not in {1}".format(
            data["weight"], config.WEIGHTS
        )
        assert "name" in data, data
        self.bets.append(data)
        self.commit()

    def edit_bet(self, index, **kwargs):
        self.edit_bet_arg(index, kwargs)

    def edit_bet_arg(self, index, kwargs):
        for key in kwargs.keys():
            if kwargs[key] is not None:
                self.bets[index][key] = kwargs[key]
        self.commit()

    def rm_bet(self, index):
        del self.bets[index]
        self.commit()

    def resolve_bet(self, index, outcome):
        """Sets the outcome of a bet."""
        self.bets[index]["outcome"] = outcome
        self.commit()

    def get_outcome_tier(self, weight):
        """Gets all resolved bets with the specified weight."""
        return [
            bet
            for bet in self.bets
            if bet["weight"] == weight and bet["outcome"] is not None
        ]

    def provide_stats(self, limit):
        for w in config.WEIGHTS:
            candidate_bets = [
                bet
                for bet in self.bets
                if bet["weight"] == w and bet["outcome"] is not None
            ][-limit:]
            num_correct = len([bet for bet in candidate_bets if bet["outcome"] is True])
            num_incorrect = len(
                [bet for bet in candidate_bets if bet["outcome"] is False]
            )
            if num_correct + num_incorrect != 0:
                accuracy = (1.0 * num_correct) / (num_correct + num_incorrect)
                yield (w, accuracy, num_correct, num_incorrect)
