class UnionFind:
    def __init__(self):
        self.parent = list(range(10001))
        self.rank = [0 for _ in range(10001)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind()
        # map every email to name
        email_name_map = {}
        # map every email to id
        email_id_map = {}
        id_count = 0

        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                email_name_map[email] = name
                if email not in email_id_map:
                    email_id_map[email] = id_count
                    id_count += 1
                union_find.union(email_id_map[emails[0]], email_id_map[email])

        merged_accounts = collections.defaultdict(list)
        for email in email_name_map:
            merged_accounts[union_find.find(email_id_map[email])].append(email)

        output_list = []
        for id_val in merged_accounts:
            curr_account = []
            account_name = email_name_map[merged_accounts[id_val][0]]
            curr_account.append(account_name)
            curr_account += sorted(merged_accounts[id_val])
            output_list.append(curr_account)

        return output_list
