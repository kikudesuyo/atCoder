package main

import (
	"fmt"
	"strings"
)

func reverseArr(arr []string) []string{
	var rArr []string
	for i := len(arr)-1; i > -1; i-- {
		rArr = append(rArr, arr[i])
}
	return rArr
}

func main() {
	var n int
	fmt.Scan(&n)
	var arr []string
	for n >0 {
		if n % 2 == 0 {
			arr = append(arr, "B")
			n /= 2
		} else {
			arr = append(arr, "A")
			n -= 1
		}
	}
	result := reverseArr(arr)
	fmt.Println(strings.Join(result, ""))
}