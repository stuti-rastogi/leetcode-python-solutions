class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        # O(m)
        for index, restaurant in enumerate(list1):
            index_map[restaurant] = index
        common_restaurants = collections.defaultdict(list)
        # O(n)
        for index, restaurant in enumerate(list2):
            # O(1)
            if restaurant in index_map:
                index_sum = index+index_map[restaurant]
                common_restaurants[index_sum].append(restaurant)
        return common_restaurants[min(common_restaurants)]