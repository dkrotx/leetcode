package main

import "sort"

type point struct {
	x, y int
}

func minAreaRect(points [][]int) int {
	projectionX := make(map[int][]int)
	projectionY := make(map[int][]int)
	pointSet := make(map[point]bool)

	for _, pair := range points {
		x := pair[0]
		y := pair[1]
		projectionX[x] = append(projectionX[x], y)
		projectionY[y] = append(projectionY[y], x)
		pointSet[point{x, y}] = true
	}

	for _, list := range projectionX {
		sort.Ints(list)
	}
	for _, list := range projectionY {
		sort.Ints(list)
	}

	var minArea int
	updateMinArea := func(x1, y1, x2, y2 int) {
		area := (x2 - x1) * (y2 - y1)
		if minArea == 0 || minArea > area {
			minArea = area
		}
	}

	for ybottom, xlist := range projectionY {
		for ix, xleft := range xlist {
			for _, xright := range xlist[ix+1:] {
				for _, ytop := range projectionX[xright] {
					if ytop <= ybottom || !pointSet[point{xleft, ytop}] {
						continue
					}
					updateMinArea(xleft, ybottom, xright, ytop)
					break // all further will be larger
				}
			}
		}
	}

	return minArea
}
