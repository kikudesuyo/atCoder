package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func reverse(s string)string {
	rs:=[]rune(s)
	for i,j:=0,len(rs)-1;i<j;i,j=i+1,j-1{
		rs[i],rs[j]=rs[j],rs[i]
	}
	return string(rs)
}



func main() {
	var n int
	var s string
	fmt.Scan(&n, &s)
	count := 0
	tmp := 0
	for i := 0; i < n; i++ {
		if s[i] == 'o' {
			tmp++
		} else {
				count = max(count, tmp)
				tmp = 0
			}
	}
	rCount := 0
	rTmp := 0
	rs := reverse(s)	
	for i := 0; i < n; i++ {
		if rs[i] == 'o' {
			rTmp++
		} else {
				rCount = max(rCount, tmp)
				tmp = 0
			}
	}
	ans := max(count, rCount)
	if ans == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(ans)
	}
}
