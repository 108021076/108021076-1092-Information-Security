import java.util.Scanner;
/**
 * cipher
 */
public class cipher {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String o = scn.next();
        String p = scn.next();
        String fr = "";
        
        char or[] = o.toCharArray();
        char op[] = p.toCharArray();

        for(int i = 0 ; i < or.length ; i++){
            if(or[i] == op[i]){
                fr = fr + "0";
            }else{
                fr = fr + "1";
            }
        }
        System.out.println(fr);
    }
}