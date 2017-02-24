public class KeyboardRow {
    public String[] findWords(String[] words) {
        char[] top = {'q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p'};
		char[] middle = {'a', 's', 'd', 'f', 'g', 'h','j', 'k', 'l'};
		char[] bottom = {'z', 'x', 'c', 'v', 'b', 'n','m'};
		        
		ArrayList<String> result = new ArrayList();
		        
		char[] current = {};
		for (String word : words) {
			String element = word.trim().toLowerCase();
			char firstLetter = element.charAt(0);
			if (new String(top).indexOf(firstLetter) != -1) {
				current = top;
			}
			else if (new String(middle).indexOf(firstLetter) != -1) {
				current = middle;
			}
			else if (new String(bottom).indexOf(firstLetter) != -1) {
				current = bottom;
			}
			else {
				System.out.println("Error");
				System.exit(1);
			}
			
			boolean present = true;
			for (int i = 1; i < word.length(); i++) {
				if (new String(current).indexOf(element.charAt(i)) == -1) {
					present = false;
					break;
				}
			}
			if (present)
				result.add(word);
		}
		
		return result.toArray(new String[result.size()]);
    }
}