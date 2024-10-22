package main

import "fmt"


func cnt(arr []string, target string) int {
	count := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] == target {
			count++
		}
	}
	return count
}

func main() {
	var n,m int
	fmt.Scan(&n,&m)
	var s string
	fmt.Scan(&s)
	logoShirtNum := 0
	tmp := 0
	for i := 0; i < n; i++ {
		if string(s[i]) == "0" {
			if logoShirtNum < tmp {
				logoShirtNum = tmp
			}
			tmp = 0
		}
		if string(s[i]) == "2" {
			tmp++
		}
	}
	if logoShirtNum < tmp {
		logoShirtNum = tmp
	}
	shirts := make([][]string,0)
	tmpShirts:= make([]string,0)
	for i:=0 ; i < n; i++ {
		if string(s[i]) == "0" {
			shirts = append(shirts, tmpShirts)
			tmpShirts = make([]string,0)
		} else {
			tmpShirts = append(tmpShirts, string(s[i]))
		}
	}
	shirts = append(shirts, tmpShirts)
	maxPlainNUm := 0
	for i:=0; i < len(shirts); i++ {
		plainCount := cnt(shirts[i], "1")
		logocnt := cnt(shirts[i], "2")
		if logocnt < logoShirtNum {
			plainCount -= (logoShirtNum - logocnt)
		}
		if maxPlainNUm < plainCount {
			maxPlainNUm = plainCount
		}
	}
	plainDiff := maxPlainNUm - m
	if plainDiff < 0 {
		plainDiff = 0
	}
	fmt.Println(plainDiff+logoShirtNum)
}