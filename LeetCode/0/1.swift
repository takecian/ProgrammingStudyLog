class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dic = [Int: Int]()
        for (idx, val) in nums.enumerated() {
            let expected = target - val
            if let first = dic[expected] {
                return [first, idx]
            } else {
                dic[val] = idx
            }
        }

        return []
    }
}
