class AI:

    def __init__(self, state):
        self.state = state

    def check_winner(self, mark):
        if self.state[1] == self.state[2] and self.state[1] == self.state[3] and self.state[1] == mark:
            return True
        elif self.state[4] == self.state[5] and self.state[4] == self.state[6] and self.state[4] == mark:
            return True
        elif self.state[7] == self.state[8] and self.state[7] == self.state[9] and self.state[7] == mark:
            return True
        elif self.state[1] == self.state[4] and self.state[1] == self.state[7] and self.state[1] == mark:
            return True
        elif self.state[2] == self.state[5] and self.state[2] == self.state[8] and self.state[2] == mark:
            return True
        elif self.state[3] == self.state[6] and self.state[3] == self.state[9] and self.state[3] == mark:
            return True
        elif self.state[1] == self.state[5] and self.state[1] == self.state[9] and self.state[1] == mark:
            return True
        elif self.state[7] == self.state[5] and self.state[7] == self.state[3] and self.state[7] == mark:
            return True
        else:
            return False

    def check_draw(self):
        for key in self.state.keys():
            if self.state[key] == 0:
                return False
        return True

    def next_move(self):
        best_score = -1000
        best_move = 0

        for key, value in self.state.items():
            if value == 0:
                self.state[key] = -1
                score = self.minimax(False)
                self.state[key] = 0
                if score > best_score:
                    best_score = score
                    best_move = key

        return best_move - 1

    def minimax(self, is_maximizing):
        if self.check_winner(mark=1):
            return -1
        elif self.check_winner(mark=-1):
            return 1
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = -1000
            for key, value in self.state.items():
                if value == 0:
                    self.state[key] = -1
                    score = self.minimax(False)
                    self.state[key] = 0
                    if score > best_score:
                        best_score = score

            return best_score
        else:
            best_score = 1000
            for key, value in self.state.items():
                if value == 0:
                    self.state[key] = 1
                    score = self.minimax(True)
                    self.state[key] = 0
                    if score < best_score:
                        best_score = score

            return best_score
