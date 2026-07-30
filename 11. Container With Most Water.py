-------------------------------------------------CORE IDEA----------------------------------------------

1. The height of the container is determined by the shorter of the two bars.

2. The width is the distance between the two bars (right - left).

3. Area = width × height (where height = the shorter bar).

4. Move the pointer that points to the shorter bar — because keeping the shorter bar will never give a larger area.

5. Keep track of the maximum area found.

6. Stop when the two pointers meet.




class Solution:
    def maxArea(self, height):
        left, right = 0, len(height)-1

        max_area = 0

        while left<right:
            area = right - left
            current_height = min(height[left], height[right])

            max_area = max(max_area, area*current_height)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area
