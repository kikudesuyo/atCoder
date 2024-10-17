package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n,t int
	fmt.Scan(&n)
	fmt.Scan(&t)
	var aArr []int
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		aArr = append(aArr, a)
	}
	var sumPlaylist int
	for _, a := range aArr {
			sumPlaylist += a
	}
	reminder := t % sumPlaylist
	for idx, a := range aArr {
		if reminder < a {
			fmt.Println(strconv.Itoa(idx + 1)+ " "+ strconv.Itoa(reminder))
			break
		}
		reminder -= a
	}
}