import math

class KEggAlgorithms:

  def __init__(self, smallestBuildingSize, largestBuildingSize):
    self.building_sizes = [i for i in range(smallestBuildingSize, largestBuildingSize + 1)]
    self.buildings = self.generate_buildings()

  def generate_buildings(self):
    buildings = []
    for n in self.building_sizes:
      temp = []
      for i in range(n+1):
        temp.append([0]*i + [1]*(n-i))
      buildings.append(temp)
    return buildings

  def findThresholdFloorMinEggs(self, n, d, building, first_floor):
    seq = []
    threshold_floor = 0
    resDrops = 0

    while n >= 1 and d >= 1:
      z = first_floor[n][d]  # one-indexed
      seq.append(z + threshold_floor)  # one indexed
      resDrops += 1

      if building[z + threshold_floor - 1] == 1:
        n = z - 1
        d = d - 1
      else:
        threshold_floor += z
        n = n - z
        d = d - 1

    return seq, threshold_floor, resDrops


  ### minEggs Algorithm 0
  def minEggsAlgo0(self, n, d, minDrops):
      eggs = [[0] * (d + 1) for _ in range(n + 1)]

      for i in range(n + 1):
          for j in range(d + 1):
              if i == 0:
                  eggs[i][j] = 0
              elif j >= i:
                  eggs[i][j] = 1
              else:
                  val = math.log(i + 1, 2)
                  if j < val:
                      eggs[i][j] = 9999
                  else:
                      col_size = len(minDrops[0])

                      # Linear Search
                      # for k in range(1, col_size-1):
                      #     curr = minDrops[i][k]
                      #     if curr <= j:
                      #         eggs[i][j] = k
                      #         break

                      # Binary Search
                      min_eggs = i
                      l = 1
                      r = col_size - 1
                      while (l <= r):
                          mid = l + (r - l) // 2
                          if (minDrops[i][mid] <= j):
                              min_eggs = mid
                              r = mid - 1
                          else:
                              l = mid + 1

                      eggs[i][j] = min_eggs

      return eggs

  ### minEggs Algorithm 1
  def minEggsAlgo1(self, n, d):
      eggs = [[0] * (d + 1) for _ in range(n + 1)]
      first_floor = [[0 for j in range(d + 1)] for i in range(n + 1)]  # one indexed

      for i in range(n + 1):
          for j in range(d + 1):
              if i == 0:
                  eggs[i][j] = 0
                  first_floor[i][j] = 0
              elif j >= i:
                  eggs[i][j] = 1
                  first_floor[i][j] = 1
              else:
                  val = math.log(i + 1, 2)
                  if j < val:
                      eggs[i][j] = 9999
                      first_floor[i][j] = 1
                  else:
                      min_eggs = i
                      xopt = 1
                      for x in range(1, i + 1):
                          x_eggs = max(1 + eggs[x - 1][j - 1], eggs[i - x][j - 1])
                          if x_eggs <= min_eggs:
                              min_eggs = x_eggs
                              xopt = x
                      eggs[i][j] = min_eggs
                      first_floor[i][j] = xopt

      return eggs, first_floor

  def queryMinEggsAlgo1(self, building, n, d):
    eggs, first_floor = self.minEggsAlgo1(n, d)
    min_eggs = eggs[n][d]
    if min_eggs == 9999:
      return (0, 0, [], min_eggs)
    else:
      seq, threshold_floor, resDrops = self.findThresholdFloorMinEggs(n, d, building, first_floor)
      return (threshold_floor, resDrops, seq, min_eggs)

  ### minEggs Algorithm 2
  def minEggsAlgo2(self, n, d):
      eggs = [[0] * (d + 1) for _ in range(n + 1)]
      first_floor = [[0 for j in range(d + 1)] for i in range(n + 1)]  # one indexed

      for i in range(n + 1):
          for j in range(d + 1):
              if i == 0:
                  eggs[i][j] = 0
                  first_floor[i][j] = 0
              elif j >= i:
                  eggs[i][j] = 1
                  first_floor[i][j] = 1
              else:
                  val = math.log(i + 1, 2)
                  if j < val:
                      eggs[i][j] = 9999
                      first_floor[i][j] = 9999
                  else:
                      l = 1
                      r = i
                      while (r - l >= 2):
                          mid = l + (r - l) // 2;
                          if (1 + eggs[mid - 1][j - 1] > eggs[i - mid][j - 1]):
                              r = mid
                          elif (1 + eggs[mid - 1][j - 1] < eggs[i - mid][j - 1]):
                              l = mid
                          else:
                              l = mid
                              r = mid

                      val1 = max(1 + eggs[l - 1][j - 1], eggs[i - l][j - 1])
                      val2 = max(1 + eggs[r - 1][j - 1], eggs[i - r][j - 1])

                      if val1 < val2:
                          eggs[i][j] = val1
                          first_floor[i][j] = l
                      else:
                          eggs[i][j] = val2
                          first_floor[i][j] = r


      return eggs, first_floor

  def queryMinEggsAlgo2(self, building, n, d):
    eggs, first_floor = self.minEggsAlgo2(n, d)
    min_eggs = eggs[n][d]
    if min_eggs == 9999:
      return (0, 0, [], min_eggs)
    else:
      seq, threshold_floor, resDrops = self.findThresholdFloorMinEggs(n, d, building, first_floor)
      return (threshold_floor, resDrops, seq, min_eggs)

  ### minEggs Algorithm 3
  def minEggsAlgo3(self, n, d):
      eggs = [[0] * (d + 1) for _ in range(n + 1)]
      first_floor = [[0 for j in range(d + 1)] for i in range(n + 1)]  # one indexed

      for i in range(n + 1):
          for j in range(d + 1):
              if i == 0:
                  eggs[i][j] = 0
                  first_floor[i][j] = 0
              elif j >= i:
                  eggs[i][j] = 1
                  first_floor[i][j] = 1
              else:
                  val = math.log(i + 1, 2)
                  if j < val:
                      eggs[i][j] = 9999
                      first_floor[i][j] = 9999

      for d1 in range(2, d + 1):
          n1 = 2
          i = 1
          while (n1 <= n):
              if (1 + eggs[i - 1][d1 - 1] >= eggs[n1 - i][d1 - 1]):
                  val1 = max(1 + eggs[i - 1][d1 - 1], eggs[n1 - i][d1 - 1])
                  eggs[n1][d1] = val1
                  first_floor[n1][d1] = i

                  if (i >= 2):
                      val2 = max(1 + eggs[i - 2][d1 - 1], eggs[n1 - i + 1][d1 - 1])
                      if val2 < val1:
                          eggs[n1][d1] = val2
                          first_floor[n1][d1] = i - 1
                  n1 += 1
              else:
                  i += 1

      return eggs, first_floor

  def queryMinEggsAlgo3(self, building, n, d):
    eggs, first_floor = self.minEggsAlgo3(n, d)
    min_eggs = eggs[n][d]
    if min_eggs == 9999:
      return (0, 0, [], min_eggs)
    else:
      seq, threshold_floor, resDrops = self.findThresholdFloorMinEggs(n, d, building, first_floor)
      return (threshold_floor, resDrops, seq, min_eggs)

  ### Sniedovich Algorithm

  def kEggsSniedovich(self, n, k):
    drops=[[0 for j in range(k+1)] for i in range(n+1)]
    first_floor = [[0 for j in range(k+1)] for i in range(n+1)] # one indexed

    for i in range(1,n+1):
      drops[i][1]=i
      first_floor[i][1] = 1

    for j in range(1,k+1):
      drops[0][j]=0
      drops[1][j]=1
      first_floor[1][j] = 1

    for i in range(2,n+1):
      for j in range(2,k+1):
        min_drops = i
        xopt = 1
        for x in range(1, i+1):
          x_drops = max(drops[x-1][j-1],drops[i-x][j])
          if x_drops <= min_drops:
            min_drops = x_drops
            xopt = x
        drops[i][j] = min_drops + 1
        first_floor[i][j] = xopt

    return drops, first_floor

### Print Function

  def printResult(self):
    for idx, building_array in enumerate(self.buildings):
      for d in range(10):
        print('')
        print('n = ', idx+1)
        print('d = ', d)

        thresholdFloors = []
        drops = []
        dpeggs = 0
        isPossible = True

        for building in building_array:
          thresholdfloor, drop, seq, dpeggs = self.queryMinEggsAlgo1(building, len(building), d)
          # thresholdfloor, drop, seq, dpeggs = self.queryMinEggsAlgo2(building, len(building), d)
          # thresholdfloor, drop, seq, dpeggs = self.queryMinEggsAlgo3(building, len(building), d)

          if dpeggs == 9999:
            isPossible = False
            print('n = ', idx+1, ', d = ', d, ', minEggs = ', dpeggs, 'impossible')
            break

          thresholdFloors.append(thresholdfloor)
          drops.append(drop)
          print('t = ', thresholdfloor, ', drops = ', drop, ', sequence = ', seq)

        if isPossible:
          maxdrops = max(drops)
          temp = []

          for id, floor in enumerate(thresholdFloors):
            if drops[id] == maxdrops:
              temp.append(floor)

          print('dp answer = ', dpeggs, ', maxDrops = ', maxdrops, ', t = ', temp)

    # print('min eggs table 0')
    # drops, first_floor = self.kEggsSniedovich(32, 32)
    # minEggs = self.minEggsAlgo0(32, 32, drops)
    # print('minEggs ', minEggs)
    # for r in minEggs:
    #     for c in r:
    #         print(c, end=" ")
    #     print()
    # print()
    #
    # # print('min eggs table 1')
    # minEggs, first_floor = self.minEggsAlgo1(32, 32)
    # print('minEggs ', minEggs)
    # for r in minEggs:
    #   for c in r:
    #     print(c, end=" ")
    #   print()
    # print()
    #
    # print('firstFloor ', first_floor)
    # for r in first_floor:
    #   for c in r:
    #     print(c, end=" ")
    #   print()
    # print()

def kEggMain():
  obj = KEggAlgorithms(1, 10)
  obj.printResult()

kEggMain()