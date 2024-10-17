package main

import "fmt"

func main() {
	var n,m int
	fmt.Scan(&n, &m)
	var sArr, tArr []string
	for i:=0; i<n; i++ {
		var s string
		fmt.Scan(&s)
		sArr = append(sArr, s)
	}
	for i:=0; i<m; i++ {
		var t string
		fmt.Scan(&t)
		tArr = append(tArr, t)
	}
	var expressIdx int
	for _, station := range sArr {
		if expressIdx == m {
			fmt.Println("No")
			continue
		}
		if station == tArr[expressIdx] {
			fmt.Println("Yes")
			expressIdx++
		} else {
			fmt.Println("No")
		}
	}

}