package main

type LandInfo struct {
	grid          [][]int
	visited       [][]bool
	width, height int
}

const LAND = 1

func NewLandInfo(grid [][]int) *LandInfo {
	land := &LandInfo{grid: grid, height: len(grid), width: len(grid[0])}

	land.visited = make([][]bool, land.height)

	for i := 0; i < land.height; i++ {
		land.visited[i] = make([]bool, land.width)
	}

	return land
}

func maxAreaOfIsland(grid [][]int) int {
	return NewLandInfo(grid).findMaxIsland()
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func (land *LandInfo) findMaxIsland() int {
	var maxArea int

	for row := 0; row < land.height; row++ {
		for col := 0; col < land.width; col++ {
			maxArea = max(maxArea, land.discoverIsland(row, col))
		}
	}

	return maxArea
}

// return: area of the island
func (land *LandInfo) discoverIsland(row, col int) int {
	if land.grid[row][col] == LAND {
		return land.dfs(row, col)
	}
	return 0
}

type point struct {
	row, col int
}

func (land *LandInfo) getNeighbour(row, col int) []point {
	var points []point

	addIfValid := func(r, c int) {
		if (r >= 0 && r < land.height) &&
			(c >= 0 && c < land.width) &&
			land.grid[r][c] == LAND && !land.visited[r][c] {
			points = append(points, point{r, c})
		}
	}

	addIfValid(row-1, col)
	addIfValid(row+1, col)
	addIfValid(row, col-1)
	addIfValid(row, col+1)

	return points
}

func (land *LandInfo) dfs(row, col int) int {
	if land.visited[row][col] {
		return 0
	}

	land.visited[row][col] = true
	area := 1

	for _, point := range land.getNeighbour(row, col) {
		area += land.dfs(point.row, point.col)
	}

	return area
}
