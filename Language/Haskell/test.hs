hi n = "hello " ++ n

check n = if 10 < n then "big" else "small"

include :: (Eq a) => a -> [a] -> Bool
include a [] = False
include a (x:xs)
    | a == x = True
    | otherwise = a `include` xs


quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    let smallOrEqual = [a | a <- xs, a <= x]
        larger = [a | a <- xs, a > x]
    in quicksort smallOrEqual ++ [x] ++ quicksort larger

multiThree x y z = x * y * z

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

