class Solution(object):
   def findMedianSortedArrays(self, nums1, nums2):
       pre,curr,ptr1,ptr2=0,0,0,0
       cnt=(len(nums1)+len(nums2))//2 + 1
       ptr1,ptr2=0,0
       while(cnt):
          if ptr1==len(nums1):
              val1=float('inf')
          else:
              val1=nums1[ptr1]
          if ptr2==len(nums2):
              val2=float('inf')
          else:
              val2=nums2[ptr2]
          if val1<val2:
              prev=curr
              curr=val1
              ptr1+=1
          else:
              prev=curr
              curr=val2
              ptr2+=1
          cnt-=1
   return([curr,(prev+curr)/2][(len(nums1)+len(nums2))%2==0])