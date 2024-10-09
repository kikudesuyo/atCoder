package main

import (
	"fmt"
)

func isBlackColor(row int, col int) bool {
	if row == 0 || col== 0 || row == 14 || col ==14 {
		return true
	}
	if row == 2 || row==12 {
		if 2<=col && col<=12 {
			return true
		}
	}
	if row == 3 || row == 11 {
		if col == 2 || col == 12{
		return true
		}
	}
	if row ==4 || row == 10 {
		if col == 2 || col == 12 || 4<=col && col<=10 {
		return true
		}	
	}
	if row== 5 || row == 9 {
		if col == 2 || col==4 ||col == 10 || col==12  {
		return true
		}
	}
	if row == 6 || row == 8 {
		if col ==2 || col==4 || 6<=col && col <=8 || col == 10 || col == 12 {
			return true
		}
	}
	if row == 7 {
		if col%2 == 0 {
			return true
		}
	}
	return false
}

func main() {
	var r, c int
	fmt.Scan(&r, &c)
	if isBlackColor(r-1, c-1) {
		fmt.Println("black")
	} else {
		fmt.Println("white")
	}
}
