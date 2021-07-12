class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # we can end with a final value of k to k+maxPts-1
        if k == 0 or n >= (k + maxPts):
            return 1

        # prob[i] is the probability of getting i points
        prob = [0.0 for _ in range(n+1)]
        prob[0] = 1.0

        # prob of drawing every card is 1/maxPts
        # so if the prob of previous card was p[j] then p[k] = p[j] * (1/maxPts)
        # for every combination that can take j to k
        # we need to add all these possibilities
        # prob[k] = (1/maxPts) * (P(k-1) + P(k-2) + ... + P(k-maxPts))
        # anything beyond k-maxPts, we cannot reach k
        # curr_prob_sum (at iteration i) = (P(i-1) + P(i-2) + ... + P(i-maxPts))
        curr_prob_sum = 1.0
        for i in range(1, n+1):
            prob[i] = curr_prob_sum / maxPts
            if i < k:
                # if where we are is less than k, we haven't reached k yet so need to keep going
                # add the curr prob to the running sum
                curr_prob_sum += prob[i]
            if i-maxPts >= 0:
                # we don't need to count anything from i-maxPts (for i+1) so remove that
                curr_prob_sum -= prob[i-maxPts]

        return sum(prob[k:])
