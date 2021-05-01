class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        i = 0
        j = 0
        while i < m + n and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                i += 1
                j += 1
            else:
                i += 1

        if j < n:
            nums1[j - n:] = nums2[j:]
