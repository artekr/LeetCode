from typing import List

# Hint: Calculate the gap between each bar and the highest bar.
class Solution1:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_height = max(height)
        gap_to_max_height = []
        water_trap = 0
        for h in height:
            gap_to_max_height.append(max_height - h)
        
        current = 0
        forward = current + 1
        while forward < len(gap_to_max_height):
            if gap_to_max_height[current] == 0 or gap_to_max_height[forward] == 0:
                # When encounter the highest bar, break the loop and going backward
                break
            if gap_to_max_height[current] >= gap_to_max_height[forward]:
                current = forward
                forward = current + 1
            else:
                water_trap += (gap_to_max_height[forward] - gap_to_max_height[current])
                forward += 1
        current = len(gap_to_max_height) - 1
        backward = current - 1
        while backward >= forward:
            if gap_to_max_height[current] >= gap_to_max_height[backward]:
                current = backward
                backward = current - 1
            else:
                water_trap += (gap_to_max_height[backward] - gap_to_max_height[current])
                backward -= 1
        return water_trap

class Solution2:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_height = max(height)
        gap_to_max_height = []
        water_trap = 0
        for h in height:
            gap_to_max_height.append(max_height - h)
        
        current = 0
        forward = current + 1
        change_backward = False
        while forward < len(gap_to_max_height):
            if gap_to_max_height[current] == 0 or gap_to_max_height[forward] == 0:
                current = forward
                forward = current + 1
                change_backward = True
            
            if not change_backward:
                if gap_to_max_height[current] >= gap_to_max_height[forward]:
                    current = forward
                    forward = current + 1
                else:
                    water_trap += (gap_to_max_height[forward] - gap_to_max_height[current])
                    forward += 1
            else:
                if gap_to_max_height[current] < gap_to_max_height[forward]:
                    current = forward
                    forward = current + 1
                else:
                    water_trap += (gap_to_max_height[current] - gap_to_max_height[forward])
                    forward += 1
        return water_trap


print(Solution1().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# expected: 6

print(Solution2().trap([4, 2, 3]))
# expected: 1