temp = nums1[:m]
nums1[:m+n] = temp + nums2[:n]
nums1.sort()