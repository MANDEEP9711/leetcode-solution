class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = 0
        y = 0
        ans = []
        if len(nums1) == 0 or len(nums2) == 0:
            if len(nums2) == 0:
                while x <= len(nums1) - 1:
                    ans.append(nums1[x])
                    x += 1
            else:
                while y <= len(nums2) - 1:
                    ans.append(nums2[y])
                    y += 1

            i = len(ans)
            if i % 2 == 0:
                i = i // 2 - 1
                a = (ans[i] + ans[i + 1]) / 2
            else:
                i = i // 2
                a = ans[i]
            return a

        while x <= len(nums1) - 1 and y <= len(nums2) - 1:
            if nums1[x] <= nums2[y]:
                ans.append(nums1[x])
                x += 1
            else:
                ans.append(nums2[y])
                y += 1

        while x <= len(nums1) - 1:
            ans.append(nums1[x])
            x += 1

        while y <= len(nums2) - 1:
            ans.append(nums2[y])
            y += 1
        i = len(ans)
        if i % 2 == 0:
            i = i // 2 - 1
            a = (ans[i] + ans[i + 1]) / 2
        else:
            i = i // 2
            a = ans[i]
        return a