class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            n = len(record)

            if operations[i] == "+" and n >= 2:
                record.append(record[-1] + record[-2])

            elif operations[i] == "D" and n >= 1:
                record.append(record[-1] * 2)

            elif operations[i] == "C" and n >= 1:
                record.pop()

            else:
                record.append(int(operations[i]))
                
        return sum(record)
