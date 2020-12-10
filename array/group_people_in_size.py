class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        def chunks(arr, key):
            for i in range(0, len(arr), key):
                yield arr[i:i+key]


        temp = {}
        res = []
        for i in range(len(groupSizes)):
            if not groupSizes[i] in temp:
                temp[groupSizes[i]] = []

            temp[groupSizes[i]].append(i)


        for key, value in temp.items():
            if len(value) > key:
                split_arr = chunks(value, key)
                res.extend(split_arr)

            else:
                res.append(value)

        return res