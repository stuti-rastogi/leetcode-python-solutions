class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for idx, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
            s = s[:idx] + tgt + s[idx + len(src):] if s[idx:idx+len(src)] == src else s
        return s

        # NOT WORKING COMPLETELY
        # Test Case that fails:
        # "mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"
        # [46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18]
        # ["rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"]
        # ["gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"]

        # mod = sorted([item for item in zip(indices, sources, targets)])
        # len_mod = len(mod)
        # mod_ptr = 0

        # output_list = []
        # len_s = len(s)
        # s_idx = 0

        # while s_idx < len_s:
        #     index, src, target = mod[mod_ptr]
        #     src_len = len(src)
        #     if s_idx == index and s[s_idx:s_idx+src_len] == src:
        #         output_list.append(target)
        #         mod_ptr += 1
        #         s_idx += src_len
        #         if mod_ptr == len(indices):
        #             break
        #     else:
        #         output_list.append(s[s_idx])
        #         s_idx += 1

        # if s_idx < len_s:
        #     output_list.append(s[s_idx:])

        # return "".join(output_list)
