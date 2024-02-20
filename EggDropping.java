public class EggDropping {
    public static void main(String[] args) {
        System.out.println("test");

//        int res = minDrops(22, 2);
//        System.out.println(res);

//        int res = minEggs(22, 7);
//        System.out.println(res);

        int N = 32;
        int K = 32;
        int[][] minDrops = new int[N+1][K+1];
        for(int i=0; i<=N; i++) {
            for(int j=0; j<=K; j++) {
                minDrops[i][j] = getMinDrops(i, j);
            }
        }

        /*for(int i=0; i<=N; i++) {
            for(int j=0; j<=K; j++) {
                System.out.print(minDrops[i][j] + " ");
            }
            System.out.println();
        }*/

        int D = 32;
        int[][] minEggsFromMinDrops = new int[N+1][D+1];
        for(int i=0; i<=N; i++) {
            for(int j=0; j<=K; j++) {
                minEggsFromMinDrops[i][j] = getMinEggsFromMinDrops(i, j, minDrops);
            }
        }

        int[][] minEggs = new int[N+1][D+1];
        for(int i=0; i<=N; i++) {
            for(int j=0; j<=K; j++) {
                minEggs[i][j] = getMinEggs(i, j);
            }
        }

        for(int i=0; i<=N; i++) {
            for(int j=0; j<=D; j++) {
                System.out.print(minEggsFromMinDrops[i][j] + "-" + minEggs[i][j] + " ");
                if(minEggs[i][j] != minEggsFromMinDrops[i][j]) {
                    System.out.println("not equal");
                    return;
                }
            }
            System.out.println();
        }

        System.out.println("both are equal");

    }

    public static int getMinEggsFromMinDrops(int n, int d, int[][] minDrops) {
        if(n==0) {
            return 0;
        }

        if(d>=n) {
            return 1;
        }

        double val = (Math.log(n+1) / Math.log(2));
        if(d < val) {
            return 9999;
        }

        int res = n;

        int colSize = minDrops[0].length;

        // Linear search
        for(int i=1; i<colSize; i++) {
            int curr = minDrops[n][i];
            if(curr <= d) {
                res = i;
                break;
            }
        }

        // Binary search
        /*int low = 1;
        int high = colSize-1;

        while(low <= high) {
            int mid = low + (high-low)/2;
            if(minDrops[n][mid] <= d) {
                res = mid;
                high = mid-1;
            } else {
                low = mid+1;
            }
        }*/

        return res;
    }

    public static int getMinEggs(int n, int d) {

        int[][] dp = new int[n+1][d+1];

        return solveMinEggs(n, d, dp);

    }

    private static int solveMinEggs(int n, int d, int[][] dp) {

        if(dp[n][d] != 0) {
            return dp[n][d];
        }

        if(n==0) {
            return 0;
        }

        if(d>=n) {
            return 1;
        }

        double val = (Math.log(n+1) / Math.log(2));
        if(d < val) {
            return 9999;
        }

        int res = n;
        for(int i=1; i<=n; i++) {
            int temp = Math.max(1 + solveMinEggs(i-1, d-1, dp), solveMinEggs(n-i, d-1, dp));
            res = Math.min(temp, res);
        }

        /*int start = 1;
        int end = n;

        while(start <= end) {
            int i = start+(end-start)/2;
            int low = 1+solveMinEggs(i-1, d-1, dp);
            int high = solveMinEggs(n-i, d-1, dp);
            int temp;
            if(low < high) {
                temp = high;
                start = i+1;
            } else {
                temp = low;
                end = i-1;
            }
            res = Math.min(temp, res);
        }*/

        dp[n][d] = res;
        return res;
    }

    public static int getMinDrops(int n, int k) {

        int[][] dp = new int[n+1][k+1];

        return solveMinDrops(n, k, dp);

    }

    private static int solveMinDrops(int n, int k, int[][] dp) {
        if(n==0 || k==0) {
            return 0;
        }

        if(n==1) {
            return 1;
        }

        if(k==1) {
            return n;
        }

        if(dp[n][k] != 0) {
            return dp[n][k];
        }

        int res = n;
        for(int i=1; i<=n; i++) {
            int temp = 1 + Math.max(solveMinDrops(i-1, k-1, dp), solveMinDrops(n-i, k, dp));
            res = Math.min(temp, res);
        }

        /*int start = 1;
        int end = n;

        while(start <= end) {
            int i = start+(end-start)/2;
            int low = solveMinDrops(i-1, k-1, minDrops);
            int high = solveMinDrops(n-i, k, minDrops);
            int temp;
            if(low < high) {
                temp = 1 + high;
                start = i+1;
            } else {
                temp = 1 + low;
                end = i-1;
            }
            res = Math.min(temp, res);
        }*/

        dp[n][k] = res;
        return res;
    }

    private static int[][] solveMinEggsPy(int n, int d) {
        int[][] minEggs = new int[n + 1][d + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= d; j++) {
                if (i == 0) {
                    minEggs[i][j] = 0;
                } else if (j >= i) {
                    minEggs[i][j] = 1;
                } else {
                    double val = (Math.log(i + 1) / Math.log(2));
                    if (j < val) {
                        minEggs[i][j] = 9999;
                    } else {
                        int min_eggs = i;
                        for (int x = 1; x <= i; x++) {
                            int x_eggs = Math.max(1 + minEggs[x - 1][j - 1], minEggs[i - x][j - 1]);
                            min_eggs = Math.min(x_eggs, min_eggs);
                        }
                        minEggs[i][j] = min_eggs;
                    }
                }
            }
        }
        return minEggs;
    }




}
