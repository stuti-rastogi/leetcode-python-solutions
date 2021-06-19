class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # construct_adjacency
        adjacency_list = {}
        num_tickets = len(tickets)
        for ticket in tickets:
            adjacency_list[ticket[0]] = []
            adjacency_list[ticket[1]] = []
        for ticket in tickets:
            adjacency_list[ticket[0]].append(ticket[1])

        visited = {}
        for src in adjacency_list:
            adjacency_list[src].sort()
            visited[src] = [False] * len(adjacency_list[src])

        def dfs(curr, itinerary, curr_itinerary):
            if len(curr_itinerary) == num_tickets+1:
                itinerary[:] = curr_itinerary
                return True
            for i, neighbor in enumerate(adjacency_list[curr]):
                if not visited[curr][i]:
                    visited[curr][i] = True
                    if dfs(neighbor, itinerary, curr_itinerary+[neighbor]):
                        return True
                    visited[curr][i] = False
            return False

        curr_itinerary = ["JFK"]
        itinerary = []
        dfs("JFK", itinerary, curr_itinerary)
        return itinerary

