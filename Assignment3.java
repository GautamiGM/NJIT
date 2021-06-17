package Assignment3;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
//import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
public class LSDsorting2 {
	public static void LSDRadixSort(String[] arr, int w) {
        int n = arr.length;
        int R = 300;
        String[] aux = new String[n];

        for (int x = w - 1; x >= 0; x--) {
            int[] count = new int[R + 1];
            for (int i = 0; i < n; i++) {
                count[arr[i].charAt(x) + 1]++;
            }

            for (int r = 0; r < R; r++) {
                count[r + 1] += count[r];
            }

            for (int i = 0; i < n; i++) {
                aux[count[arr[i].charAt(x)]++] = arr[i];
            }

            for (int i = 0; i < n; i++) {
                arr[i] = aux[i];
            }
        }
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BufferedReader reader = null; 
        BufferedWriter writer = null;        
        ArrayList<String> lines = new ArrayList<String>(); 
        try
        {  
        	Scanner user = new Scanner( System.in ); 
            String  inputFileName, outputFileName;
            
            System.out.print("Please specify the input file (default = f.txt ): ");
            inputFileName = user.nextLine().trim();
            File input = new File( inputFileName );      
            Scanner scan = new Scanner( inputFileName );      
            reader = new BufferedReader(new FileReader(inputFileName));
            
            String currentLine = reader.readLine();
             
            while (currentLine != null) 
            {
                lines.add(currentLine);
                 
                currentLine = reader.readLine();
            }
           
            Collections.sort(lines);
            System.out.print("Please specify the output file (default = g.txt ): ");
            outputFileName = user.nextLine().trim();
            PrintWriter output = new PrintWriter( outputFileName ); 
            writer = new BufferedWriter(new FileWriter(outputFileName));
           
            for (String line : lines)
            {
                writer.write(line);
                 
                writer.newLine();
            }
        } 
        catch (IOException e) 
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                if (reader != null)
                {
                    reader.close();
                } 
                if(writer != null)
                {
                    writer.close();
                }
            } 
            catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
        
    }   
	}
