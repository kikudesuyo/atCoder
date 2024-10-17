package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	aArr:= make([]int,n)
	for i:=0;i<n;i++{
		fmt.Scan(&aArr[i])
	}
	var x int
	fmt.Scan(&x)
	sumA := 0
	for i:=0;i<n;i++{
		sumA += aArr[i]
	}
	answer := 0
	q, r := x/sumA, x%sumA
	rCount := 0
	for i:=0;i<n;i++{
		r -= aArr[i]
		if r < 0{
			fmt.Println(q*n+i+1)
			return
		}
		rCount++
	}
	answer = q*n + rCount
	fmt.Println(answer)
}
