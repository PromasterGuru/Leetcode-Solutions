class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        r = 0
        l = 0
        arr = []
        while r < len(nums1) and l < len(nums2):
            if nums1[r] < nums2[l]:
                arr.append(nums1[r])
                r += 1
            else:
                arr.append(nums2[l])
                l += 1
        arr += nums1[r:] + nums2[l:]
        if len(arr) % 2 == 0:
            return (arr[len(arr)//2-1] + arr[len(arr)//2])/2
        else:
            return (arr[(len(arr)+1)//2-1])
        return arr


if __name__ == "__main__":
    sol = Solution()
    nums1 = [[1, 3], [1, 2, 3, 4], [], [1, 3], [1, 2], [1, 3], [
        3], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4]]
    nums2 = [[1], [1, 2, 3, 4, 5], [1], [2], [3, 4], [2, 7], [1, 2, 4],
             [-1, 0, 0, 0, 0, 0, 1], [1, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

    for i in range(len(nums1)):
        print(sol.findMedianSortedArrays(nums1[i], nums2[i]))
