package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var (
	C_PATTERN = "dependentTxs_C_use_time"
)

func main() {
	// make a file to write the result
	avgF, err := os.Create("avgTime.txt")
	if err != nil {
		log.Fatalf("failed to create file: %s", err)
	}

	// match file name in this directory
	CTimeFiles := matchFileInDir(".", C_PATTERN)

	for _, f := range CTimeFiles {
		avgT := calcTimeAverage(f)
		fmt.Printf("file: %s\n", f)
		fmt.Printf("Average time: %d\n", avgT)

		_, err := avgF.WriteString(fmt.Sprintf("%s: %d\n", f, avgT))
		if err != nil {
			log.Fatalf("failed to write file: %s", err)
		}
	}
}

func calcTimeAverage(fileName string) int64 {
	// Open the file
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	var sum int64
	var count int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) != 3 {
			continue
		}
		num, err := strconv.ParseInt(parts[1], 10, 64)
		if err != nil {
			log.Fatalf("failed to parse number: %s", err)
		}
		sum += num
		count++
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("failed to read file: %s", err)
	}

	return sum / int64(count)
}

func matchFileInDir(dir string, pattern string) (fileNames []string) {
	files, err := os.ReadDir(dir)
	if err != nil {
		log.Fatal(err)
	}

	for _, f := range files {
		if strings.Contains(f.Name(), pattern) {
			fileNames = append(fileNames, f.Name())
		}
	}

	return
}
