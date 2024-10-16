package main

import (
	"fmt"
	"strconv"
	"strings"
)


func main()  {
	var n int
	fmt.Scan(&n)
	pArr := make([]int, n)
	for i:=0; i<n; i++ {
		var p int
		fmt.Scan(&p)
		pArr[i] = p
	}
	qArr := make([]int, n)
	for i := 0; i < n; i++ {
		qArr[pArr[i]-1] = i + 1
	}
	var sb strings.Builder //文字列の連結では、strings.Builderを使うと高速
	for i := 0; i < n; i++ {
		sb.WriteString(strconv.Itoa(qArr[i]))
		if i < n-1 {
			sb.WriteString(" ")
		} 

	}
	answer := sb.String()
	fmt.Println(answer)
}
