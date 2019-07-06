class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1 = rec1[0]
        rec1_y1 = rec1[1]
        rec1_x2 = rec1[2]
        rec1_y2 = rec1[3]
        rec1_width_half = (rec1_x2 - rec1_x1) / 2
        rec1_height_half = (rec1_y2 - rec1_y1) / 2
        rec1_x_center = (rec1_x2 + rec1_x1) / 2
        rec1_y_center = (rec1_y2 + rec1_y1) / 2

        rec2_x1 = rec2[0]
        rec2_y1 = rec2[1]
        rec2_x2 = rec2[2]
        rec2_y2 = rec2[3]
        rec2_width_half = (rec2_x2 - rec2_x1) / 2
        rec2_height_half = (rec2_y2 - rec2_y1) / 2
        rec2_x_center = (rec2_x2 + rec2_x1) / 2
        rec2_y_center = (rec2_y2 + rec2_y1) / 2

        if abs(rec2_x_center - rec1_x_center) < rec1_width_half + rec2_width_half and abs(
                rec2_y_center - rec1_y_center) < rec1_height_half + rec2_height_half:
            return True
        else:
            return False
