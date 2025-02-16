package main

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/chinuy/zipf"
)

func main() {
	// 定义 Zipf 分布参数
	s := 0.0           // 幂指数
	n := uint64(10000) // 支持范围 [1, n]

	// 创建 Zipf 分布生成器
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	z := zipf.NewZipf(r, s, uint64(n))

	// 调整生成值的范围到 [1, n]
	fmt.Println("Zipf 分布随机样本：")
	for i := 0; i < 160; i++ {
		fmt.Printf("%d ", z.Uint64()+1)
	}
}
