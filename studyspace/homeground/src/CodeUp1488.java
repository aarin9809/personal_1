import java.util.Scanner;

public class CodeUp1488 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();       //2
        int b = sc.nextInt();       //3
        int[][] arr = new int[a][b];        //arr배열의 총 길이를 [a][b]로 지정
        int i=a-1, j=b, num=0 ,t = 1, anoA=a, anoB=b;
        // i = 1, j = 3, num = 0, t = 1, anoA = 2, anoB = 3

        //달팽이
        while(true) {
            t*=-1; //방향 전환      현재 t상태는 -1
            for (int l = 0; l < b; l++) {       //l을 3번 반복, 여기서 l은 for문을 돌리기 위한 지역 변수일뿐임.
                num++;      //num이 0부터 1씩 증가함
                j+=t;       //j값을 -1씩 죽여나감       3 2 1 0
                arr[i][j] = num;
            }
                /*
                arr[1][2] 위치에서 1부터 채워 나가기 시작함. 왜 j값이 3이 아니고 2냐면
                17번째 줄 코드에서 j값이 t = -1에 의해 값이 1 줄었기 때문에 3에서 2가 된 것이다.
                그러므로 arr[i][j]의 출발 위치는 1,2 위치에서 num = 1 부터 시작된다.
                0,0  0,1 0,2

                1,0  1,1  1,2
                 3    2    1
                 */
            a--;        //a값을 하나 줄이고  1 --> 0
            b--;        //b값을 하나 줄이고  ????????????

            for (int l = 0; l < a; l++) {       //i는 ++ j는 b-1고정
                num++;
                i+=t;
                arr[i][j] = num;
            }
            if(a<=0||b<=0)
                break; //while 탈출조건
        }

        //2차원 배열 출력
        for (int l = 0; l < anoA; l++) {
            for (int k = 0; k < anoB; k++) {
                System.out.print(arr[l][k] +" ");
            }
            System.out.println();
        }
        sc.close();
    }
}