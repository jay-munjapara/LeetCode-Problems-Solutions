class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            # Using '#' as delimiter after length
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            # Find the '#' that separates the length and actual string
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # Extract the length
            word = s[j+1: j+1 + length]  # Extract the word using the length
            decoded.append(word)
            i = j+1 + length  # Move to the next encoded word
        return decoded
