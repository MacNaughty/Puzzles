def get_next_step(nums):
    mid_index = len(nums) // 2
    head = TreeNode(nums[mid_index], None, None)
    left_nums = nums[:mid_index]
    right_nums = nums[mid_index + 1:]

    return head, left_nums, right_nums
  
  
def build_tree(node, left_nums, right_nums):
    if (left_nums is not None) and len(left_nums) == 1:
        node.left = TreeNode(left_nums[0])
    if (right_nums is not None) and len(right_nums) == 1:
        node.right = TreeNode(right_nums[0])

    if len(left_nums) > 1:
        mid_left, left_left, left_right = get_next_step(left_nums)
        node.left = mid_left
        build_tree(mid_left, left_left, left_right)

    if len(left_nums) > 1:
        mid_right, right_left, right_right = get_next_step(right_nums)
        node.right = mid_right
        build_tree(mid_right, right_left, right_right)
        

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if len(nums) == 1:
            return TreeNode(nums[0], None, None)

        (head, left_nums, right_nums) = get_next_step(nums)

        build_tree(head, left_nums, right_nums)

        return head
