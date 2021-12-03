package count;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class count {

    public static void main(String[] args) throws IOException {
        // This code was developed in collaboration with [Parya Derakhshan](https://github.com/pder00) which works smoothly
        List<String> words = new ArrayList<String>();
        List<Integer> counts = new ArrayList<Integer>();
        File file = new File("C:/Users/shakil/count.txt");

        try (Scanner sc = new Scanner(new BufferedReader(new FileReader(file)))) {
            while (sc.hasNextLine()) {
                String line = sc.nextLine().toLowerCase();
                if (line.equals("")) {
                    continue;
                }
                for (String word : line.split(" ")) {
                    if (words.contains(word)) {
                        int index = words.indexOf(word);
                        int count = counts.get(index) + 1;
                        counts.set(index, count);
                    } else { //new word
                        words.add(word);
                        counts.add(1);
                    }
                }
            }
        }
        for (int i = 0; i < words.size(); i++) {
            System.out.println(words.get(i) + ": " + counts.get(i));
        }

    }
}
