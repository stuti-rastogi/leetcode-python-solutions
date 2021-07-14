class Solution:
    def convertToBase7Helper(self, num: int, base_7_repr: List[str]) -> None:
        if num >= 7:
            self.convertToBase7Helper(num // 7, base_7_repr)
        base_7_repr.append(str(num % 7))

    def convertToBase7(self, num: int) -> str:
        base_7_repr = ['-'] if num < 0 else []
        self.convertToBase7Helper(abs(num), base_7_repr)
        return "".join(base_7_repr)
