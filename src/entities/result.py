class Result:

    def __init__(self, user_id, points, time, result_id=None):
        self.result_id = result_id
        self.user_id = user_id
        self.points = points
        self.time = time

    def __str__(self):
        return f"id: {self.result_id}, user_id: {self.user_id}, \
                points: {self.points}, time: {self.time}"
