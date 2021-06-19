class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        possible_restaurants = []
        for restaurant in restaurants:
            if (restaurant[3] <= maxPrice and
               restaurant[4] <= maxDistance):
                if not veganFriendly or (restaurant[2] == veganFriendly):
                    possible_restaurants.append(restaurant)

        possible_restaurants.sort(key=lambda x: (-x[1], -x[0]))
        return [restaurant[0] for restaurant in possible_restaurants]
