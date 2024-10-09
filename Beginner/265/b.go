package main

import "fmt"

func main() {
	var n, m, t int
	fmt.Scan(&n, &m, &t)
	a_n := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		fmt.Scan(&a_n[i])
	}
	xy_m := make([][2]int, m)
	for i := 0; i < m; i++ {
		fmt.Scan(&xy_m[i][0], &xy_m[i][1])
	}
	if m == 0 {
		sum_a_n := 0
		for i := 0; i < n-1; i++ {
			sum_a_n += a_n[i]
		}
		if sum_a_n >= t {
			fmt.Println("No")
			return
		} else {
			fmt.Println("Yes")
			return
		}
	}
	var currentTime = t
	var bounusIdx = 0
	for i := 0; i < n-1; i++ {
		if xy_m[bounusIdx][0]-1 == i {
			currentTime += xy_m[bounusIdx][1]
			if bounusIdx < m-1 {
				bounusIdx++
			}
		}
		currentTime -= a_n[i]
		if currentTime <= 0 {
			fmt.Println("No")
			return
		}
	}
	fmt.Println("Yes")
}
