package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	dubbleZeroCount := 0
	idx :=0
	for idx < len(s)-1{
		if s[idx:idx+2] == "00"{
			dubbleZeroCount++
			idx+=2
		} else {
			idx++
		}
	}
	fmt.Println(len(s)-dubbleZeroCount)
}