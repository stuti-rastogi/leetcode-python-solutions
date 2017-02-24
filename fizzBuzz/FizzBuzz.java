public class FizzBuzz {
    public List<String> fizzBuzz(int n) {
        //list cannot be instantiated
        List<String> result = new ArrayList<String>();

        for (int i = 1; i <= n; i++) {
            //multiple of 3 and 5
            if (i % 3 == 0 && i % 5 == 0)
                result.add("FizzBuzz");

            //multiple of 3
            else if (i % 3 == 0)
                result.add("Fizz");

            //multiple of 5 
            else if (i % 5 == 0)
                result.add("Buzz");

            //convert int to string
            else
               result.add(String.valueOf(i));
        }
        
        return result;
    }
}