class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, costumer, order, day):
        self.data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes_count = {}
        highest_count = 0
        most_ordered_dish = None
        for order in self.data:
            if order[0] == costumer:
                if order[1] not in dishes_count:
                    dishes_count[order[1]] = 1
                else:
                    dishes_count[order[1]] += 1
                    if dishes_count[order[1]] > highest_count:
                        most_ordered_dish = order[1]
        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
