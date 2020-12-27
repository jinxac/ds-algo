class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0]
        end = start + customers[0][1]

        t = end - start

        for i in range(1, len(customers)):
            customer = customers[i]
            start = max(customer[0], end)
            end = start + customer[1]

            t += end - customer[0]

            start = customer[0]

        return t / len(customers)
