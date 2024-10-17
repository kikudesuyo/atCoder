package main

import "fmt"

func main() {
	var s string
	var t string
	fmt.Scan(&s)	
	fmt.Scan(&t)
	for i := 0; i < len(s); i++ {
		if s[i] != t[i] {
			fmt.Println(i+1)
			return
		}
	}
	fmt.Println(len(t))

}