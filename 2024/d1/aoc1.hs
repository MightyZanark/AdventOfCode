import System.IO
import Data.List (sort)

processInput :: [Int] -> [Int] -> [Int] -> ([Int], [Int])
processInput (l:r:[]) leftAcc rightAcc = (leftAcc ++ [l], rightAcc ++ [r])
processInput (l:r:rest) leftAcc rightAcc = processInput rest (leftAcc ++ [l]) (rightAcc ++ [r])

process :: [Int] -> ([Int], [Int])
process input = processInput input [] []

getSorted :: ([Int], [Int]) -> ([Int], [Int])
getSorted (left, right) = (sort left, sort right)

getPartA :: ([Int], [Int]) -> Int
getPartA (left, right) = sum $ map abs $ zipWith (-) left right

count :: Int -> [Int] -> Int
count x = length . filter (x==)

getPartB :: ([Int], [Int]) -> Int
getPartB (left, right) = sum $ zipWith (*) left $ map (\x -> count x right) left

main :: IO()
main = do
    contents <- readFile "aoc1.txt"
    let intList :: [Int] = map read $ words contents
    let inputLists = process intList
    let sortedLists = getSorted inputLists
    print $ "Part A: " ++ (show $ getPartA sortedLists)
    print $ "Part B: " ++ (show $ getPartB inputLists)
