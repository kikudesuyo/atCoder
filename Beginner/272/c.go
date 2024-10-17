package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	var aArr []int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		aArr = append(aArr, a)
	}
	sort.Slice(aArr, func(i, j int) bool {
		return aArr[i] > aArr[j]
	})
	maxEven := -1
	secondMaxEven := -1
	maxOdd := -1
	secondMaxOdd := -1
	for _,  v := range aArr {
		if v % 2 == 0 {
			if maxEven ==-1 {
				maxEven = v
			}else if secondMaxEven == -1 {
				secondMaxEven = v
			}
		} else {
      if maxOdd == -1 {
				maxOdd = v
			}else if secondMaxOdd == -1 {
				secondMaxOdd = v
			}
		}
	}
	//条件を満たすのは偶数同士、奇数同士の組み合わせ
	var evenSum int
	var oddSum int
	if maxEven !=-1 && secondMaxEven!=-1{
		evenSum = maxEven + secondMaxEven
	}
	if maxOdd !=-1 && secondMaxOdd!=-1{
		oddSum = maxOdd + secondMaxOdd
	}
	if evenSum == 0 && oddSum == 0 {
		fmt.Println(-1)
		return
	}
	if evenSum > oddSum {
		fmt.Println(evenSum)
	} else {
		fmt.Println(oddSum)
	}
}

