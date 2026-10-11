class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 0:
            return ""

        n = len(encodedText)
        if n == 0:
            return ""

        cols = n // rows

        mat = []
        idx = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(encodedText[idx])
                idx += 1
            mat.append(row)

        result = []

        for startCol in range(cols):
            i, j = 0, startCol
            while i < rows and j < cols:
                result.append(mat[i][j])
                i += 1
                j += 1

        return "".join(result).rstrip()