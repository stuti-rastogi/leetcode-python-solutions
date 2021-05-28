# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # O(n) solution
    def findCelebrity(self, n: int) -> int:
        possibleCelebrity = 0
        for person in range(n):
            if knows(possibleCelebrity, person):
                possibleCelebrity = person

        # now confirm possibleCelebrity is actually celebrity
        for person in range(n):
            if person == possibleCelebrity:
                continue
            if not knows(person, possibleCelebrity) or knows(possibleCelebrity, person):
                return -1
        return possibleCelebrity


        # O(n^2) solution
#         possibleCelebs = []
#         for person in range(n):
#             countPeopleKnowing = 0
#             for other in range(n):
#                 if not knows(other, person):
#                     break
#                 else:
#                     countPeopleKnowing += 1
#             if countPeopleKnowing == n:
#                 possibleCelebs.append(person)

#         for celeb in possibleCelebs:
#             count = 0
#             for other in range(n):
#                 if knows(celeb, other) and celeb != other:
#                     break
#                 else:
#                     count += 1
#             if count == n:
#                 return celeb

#         return -1