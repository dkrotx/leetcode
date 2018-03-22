class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def pos2id(pos):
            return pos - 1
        
        if not nums:
            return []
        
        dupes = set()
        
        for pos in range(1, len(nums)+1):
            if nums[pos2id(pos)] != pos:
                mem = nums[pos2id(pos)]
                nums[pos2id(pos)] = 0 # mark as empty place-holder
                    
                while mem:
                    if nums[pos2id(mem)] == mem:
                        dupes.add(mem)
                        mem = None
                    else:
                        nums[pos2id(mem)], mem = mem, nums[pos2id(mem)]
                        
        return list(dupes)
