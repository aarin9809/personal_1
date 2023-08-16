import java.util.Hashtable;
public class HashTableDemo {
    public static void main(String[] args) {
        Hashtable<Integer, String> ht = new Hashtable<Integer, String>();

        ht.put(0, "철수");
        ht.put(1, "영희");
        ht.put(2, "영수");
        ht.replace(2, "수철");
        ht.remove(2);

        for (int i=0; i<ht.size(); i++) {
            System.out.println(ht.get(i));  //Hashtable 값 출력
        }
        System.out.println(ht.size());
        System.out.println(ht.containsKey(2));
        System.out.println(ht.containsValue("수철"));
        System.out.println(ht.isEmpty());       //boolean
        System.out.println(ht.keySet());
    }
}
