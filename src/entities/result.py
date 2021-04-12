# Useless right now. Needs to be removed.
class Result:

    def __init__(self, user_id, points, time, result_id=None):
        self.result_id = result_id
        self.user_id = user_id
        self.points = points
        self.time = time
