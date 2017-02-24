public class ReverseString {
    public String reverseString(String s) {
        StringBuilder sb = new StringBuilder();
        sb.append(s);
        sb = sb.reverse();
        return sb.toString();
    }
}