import java.util.Scanner;

public class CodeUp1490 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int[][] arr = new int[a][b];
        int i=a, j=0, n=0, t = -1, anoA=a, anoB=b;

        while(true) {
            for (int l = 0; l < a; l++) {
                n++;
                i+=t;
                arr[i][j] = n;
            }

            t*=-1; //방향 전환
            a--;
            b--;

            for (int l = 0; l < b; l++) {
                n++;
                j+=t;
                arr[i][j] = n;
            }
            if(a<=0||b<=0)
                break; //while 탈출조건
        }
        //출력
        for (int l = 0; l < anoA; l++) {
            for (int l2 = 0; l2 < anoB; l2++) {
                System.out.print(arr[l][l2] +" ");
            }
            System.out.println();
        }
        sc.close();
    }
}