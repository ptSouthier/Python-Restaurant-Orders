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
        all_dishes = set()
        dishes_ordered_by_costumer = set()
        for order in self.data:
            if order[1] not in all_dishes:
                all_dishes.add(order[1])
            if order[0] == costumer:
                dishes_ordered_by_costumer.add(order[1])
        return all_dishes.difference(dishes_ordered_by_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        workdays = set()
        days_visited_by_costumer = set()
        for order in self.data:
            if order[2] not in workdays:
                workdays.add(order[2])
            if order[0] == costumer:
                days_visited_by_costumer.add(order[2])
        return workdays.difference(days_visited_by_costumer)

    def get_busiest_day(self):
        workdays_count = {}
        highest_visits_count = 0
        busiest_day = None
        for order in self.data:
            if order[2] not in workdays_count:
                workdays_count[order[2]] = 1
            else:
                workdays_count[order[2]] += 1
                if workdays_count[order[2]] > highest_visits_count:
                    highest_visits_count = workdays_count[order[2]]
                    busiest_day = order[2]
        return busiest_day

    def get_least_busy_day(self):
        workdays_count = {}
        for order in self.data:
            if order[2] not in workdays_count:
                workdays_count[order[2]] = 1
            else:
                workdays_count[order[2]] += 1
        min_visits = min(workdays_count.values())
        least_busiest_day = [
            key for key, value in workdays_count.items() if value == min_visits
            ]
        return least_busiest_day[0]
