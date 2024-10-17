package main

import (
	"fmt"
	"math/big"
	"strconv"
)

func main() {
	var k int
	fmt.Scan(&k)
	binaryStr := strconv.FormatInt(int64(k), 2)
	bigNum := new(big.Int)
	bigNum.SetString(binaryStr, 10)
	bigNum.Mul(bigNum, big.NewInt(2))
	fmt.Println(bigNum)
}