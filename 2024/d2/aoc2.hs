import System.IO

checkDiff :: Int -> Int -> Bool
checkDiff a b = abs (a - b) < 4

isInc :: Int -> Int -> Bool
isInc a b = a < b

isDec :: Int -> Int -> Bool
isDec a b = a > b

check :: (Int -> Int -> Bool) -> [Int] -> Bool
check checkFn (a:b:[]) = checkFn a b && checkDiff a b
check checkFn (a:b:rest) = checkFn a b && checkDiff a b && check checkFn (b:rest)

checkInc :: [[Int]] -> [Bool]
checkInc = map (check isInc)

checkDec :: [[Int]] -> [Bool]
checkDec = map (check isDec)

-- very bad implementation but it works :) 
checkWithTol :: (Int -> Int -> Bool) -> Int -> Int -> Int -> [Int] -> Bool
checkWithTol checkFn tol count prev (a:b:[]) =
    if not (checkFn a b) || not (checkDiff a b) then 
        if count < tol then
            if prev /= -1 then (checkFn prev b && checkDiff prev b) || (checkFn prev a && checkDiff prev a)
            else True
        else False
    else True

checkWithTol checkFn tol count prev (a:b:rest) =
    if not (checkFn a b) || not (checkDiff a b) then
        if count < tol then 
            if prev /= -1 then (checkWithTol checkFn tol (count + 1) prev (a:rest) || checkWithTol checkFn tol (count + 1) (-1) (prev:b:rest))
            else checkWithTol checkFn tol (count + 1) (-1) (a:rest) || checkWithTol checkFn tol (count + 1) a (b:rest)
        else False
    else checkWithTol checkFn tol count a (b:rest)

checkIncWithTol :: [[Int]] -> [Bool]
checkIncWithTol = map (checkWithTol isInc 1 0 (-1))

checkDecWithTol :: [[Int]] -> [Bool]
checkDecWithTol = map (checkWithTol isDec 1 0 (-1))

getPartA :: [[Int]] -> Int
getPartA reports = sum $ map fromEnum $ zipWith (||) (checkInc reports) (checkDec reports)

getPartB :: [[Int]] -> Int
getPartB reports = sum $ map fromEnum $ zipWith (||) (checkIncWithTol reports) (checkDecWithTol reports)

main :: IO()
main = do
    contents <- readFile "aoc2.txt"
    let reports :: [[Int]] = map (map read) $ map words $ lines contents
    print $ getPartA reports
    print $ getPartB reports
