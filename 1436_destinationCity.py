class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_cities = set()
        all_cities = set()
        for path in paths:
            src, dst = path
            all_cities.add(src)
            all_cities.add(dst)
            src_cities.add(src)
        return (all_cities - src_cities).pop()