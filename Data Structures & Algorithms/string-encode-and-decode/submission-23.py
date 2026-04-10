class Solution:

    def encode(self, strs: List[str]) -> str:
        return "-?a£" if strs == [] else  "-?a".join(strs)

    def decode(self, s: str) -> List[str]:
        return [] if s == "-?a£" else s.split("-?a")
