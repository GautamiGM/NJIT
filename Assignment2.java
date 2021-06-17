package Assignment2;

import java.security.SecureRandom; //for secure Random
import java.util.Arrays;

public class sorting {
	int COMPCOUNT = 0;
	int[] array;
	int size;
	
/*  ex:
	 * 
	 * 
	 * public class TargetClass { ~Attributes~ 
    private byte[][] array;

    ~ Constructor ~
    public TargetClass (byte[][] array) {
        this.array = array;
    }
}

//first is setting up then receiving
	 * 
	 *
	 */
	public sorting(int[] array, int size) {
		this.array = array;
		this.size = size; 
	}
	
	public void Array1(int[] array) {
		this.array = array;
	}
	
	public int[] Array2() {
		return array;
	}
	
	public void Size1(int size) {
		this.size = size;
	}
	
	public int Size2() {
		return size;
	}
	
	public void setCOMPCOUNT(int COMPCOUNT) {
		this.COMPCOUNT = COMPCOUNT;
	}
	
	public int getCOMPCOUNT() {
		return COMPCOUNT;
	}
	
	public int[] Mergesort(int[] array, int startofIndex, int endofIndex, 
			int size) {
		if(startofIndex == endofIndex || size < 2) {
			return array;
		}else {
			int mid = array.length/2;
			int[] left = extract(array, 0, size/2);
			int[] right = extract(array, size/2, size);
			
			/*
			 * int mid = input.length / 2;
        	int[] left = Arrays.copyOfRange(input, 0, mid);
        	int[] right = Arrays.copyOfRange(input, mid, input.length);
        	return merge(mergeSort(left), mergeSort(right));
			 * 
			 */
			
			int[] leftArray = Mergesort(left, startofIndex, mid, size/2);
			int[] rightArray = Mergesort(right, mid + 1, endofIndex, size/2);
			int[] result = new int[size];
			
			array = merge(leftArray, leftArray.length, rightArray, rightArray.length, 
					result);
			return array;
		}
	}

	private int[] extract(int[] elements, int start, int end) {
		int[] toArray = new int[end - start];
		int size = toArray.length;
		for(int i = 0; i < size; i++) {
			toArray[i] = elements[start + i];
		}
		return toArray;
	}

	
	private int[] merge(int[] leftArray, int LeftLength, int[] rightArray, 
			int RightLength, int[] result) {
		int x = 0;int y = 0;int z = 0;
		
		while(x<LeftLength && y < RightLength) {
			if(isLessThanOrEqualTo(leftArray[x], rightArray[y])) {
				result[z] = leftArray[x];
				x++;
			}else {
				result[z] = rightArray[y];
				y++;
			}
			z++;
		}
		
		while(LeftLength - 1 >= x) {
			result[z] = leftArray[x];
			x++;z++;
		}
		
		
		while( RightLength - 1 >= y) {
			result[z] = rightArray[y];
			y++;z++;
		}
		return result;
	}
	
	public int[] Heapsort(int[] array, int size) {
		buildHeap(array, size);
		int[] result = new int[size];
		for (int i = 0; i <= size - 1; i++) {
			result[i] = deleteMin(array, size - i - 1);  
		}
		return result;
	}

	private int deleteMin(int[] array, int endIndex) {
		int temp = array[0];
		array[0] = array[endIndex];
		endIndex = endIndex - 1;
		pushDown(array, 0, endIndex);
		return temp;
	}


	private void buildHeap(int[] array, int size) {
		for (int i = size / 2; i >= 1; i--) {
			pushDown(array, i - 1, size - 1); 
		}
	}

	private void pushDown(int[] array, int root, int size) {
		if (2 * root + 1 > size) { // Leaf
			return;
		}

		int smallerChild;
		if ((2 * root + 1 == size) || isLessThanOrEqualTo(array[2 * root + 1], 
				array[2 * root + 2])) {
			smallerChild = 2 * root + 1;
		} else {
			smallerChild = 2 * root + 2;
		}

		if (isLessThanOrEqualTo(array[root], array[smallerChild])) {
			return;
		}

		int temp = array[root];
		array[root] = array[smallerChild];
		array[smallerChild] = temp;

		pushDown(array, smallerChild, size);
	}

	public void Quicksort(int[] array, int start, int end) {
		if(start >= end) {
			return;
		}
		
		SecureRandom r = new SecureRandom();
	
		int m = r.nextInt(end - start + 1) + start;
		
		int pivot = array[m];		
	
		int temp = array[start];
		array[start] = array[m];
		array[m] = temp;
		
		int left = start + 1;
		int right = end;

		while(left <= right) {
			while(left <= right && isLessThanOrEqualTo(array[left], pivot)) {
				left = left + 1;
			}
			
			while(left <= right && isGreaterThan(array[right], pivot)) {
				right = right - 1;
			}
			
			if(left < right) {
				
				int temp2 = array[left];
				array[left] = array[right];
				array[right] = temp2;
				
				left = left + 1;
				right = right - 1;
			}
		}
	
		int temp3 = array[start];
		array[start] = array[right];
		array[right] = temp3;
		
		Quicksort(array, start, right - 1);
		Quicksort(array, right + 1, end);
	}

	private boolean isLessThanOrEqualTo(int i, int j) {
		COMPCOUNT++;
		return i <= j;
	}
	

	private boolean isGreaterThan(int i, int j) {
		COMPCOUNT++;
		return i > j;
	}
	
	private static final int n32 = 32;
	private static final int n1024 = 1024;
	private static final int n32768 = 32768;
	private static final int n1048576 = 1048576;

	public static void main(String[] args) {
		int[] sorted = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
				20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32};
		int[] Rsorted = {32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19,
				18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		
		int[] sorted2 = new int[n32];
		int[] Rsorted2 = new int[n32];
		
		copy(sorted, sorted2, 32);
		MergeSort(sorted);
		HeapSort(sorted);
		QuickSort(sorted2);
		
		System.out.println(' ');
		
		copy(Rsorted, Rsorted2, n32);
		MergeSort(Rsorted);
		HeapSort(Rsorted);
		QuickSort(Rsorted2);

		int[] madeArray = new int[n32];
		
		SecureRandom sr = new SecureRandom();
		for(int i = 0; i < 32; i++) {
			madeArray[i] = sr.nextInt(32);
		}
		System.out.println(' ');
		System.out.println("Random array: " + Arrays.toString(madeArray));
		
		int[] madeArray2 = new int[n32];
		copy(madeArray, madeArray2, n32);
		MergeSort(madeArray);
		HeapSort(madeArray);
		QuickSort(madeArray2);

		Random_array(n1024);
		Random_array(n32768);
		Random_array(n1048576);
	}
	
	private static void Random_array(int size) {
		System.out.println(' ');
		System.out.println("Array: " + size);
		
		int[] madeArray = new int[size];
		//System.out.println(' ');
		SecureRandom sr = new SecureRandom();
		for(int i = 0; i < size; i++) {
			madeArray[i] = sr.nextInt(size);
		}
		
		int[] madeArray2 = new int[size];
		copy(madeArray, madeArray2, size);
		Mergesort(madeArray);
		Heapsort(madeArray);
		Quicksort(madeArray2);
	}
	
	private static void MergeSort(int[] array) {
		sorting as = new sorting(array, array.length);
		as.Mergesort(as.Array2(), 0, as.Size2() - 1, as.Size2());
		
		System.out.println("Mergesort Array: " + Arrays.toString(array));
		System.out.println("COMPCOUNT: " + as.getCOMPCOUNT());
	}
	private static void HeapSort(int[] array) {
		sorting as = new sorting(array, array.length);
		as.Heapsort(array, array.length);
		
		System.out.println("Heapsort Array: " + Arrays.toString(array));
		System.out.println("COMPCOUNT: " + as.getCOMPCOUNT());
	}
	private static void QuickSort(int[] array) {
		sorting as = new sorting(array, array.length);
		
		as.Quicksort(array, 0, as.Size2() - 1);
		
		System.out.println("Quicksort Array: " + Arrays.toString(array));
		System.out.println("COMPCOUNT: " + as.getCOMPCOUNT());
	}

	private static void Mergesort(int[] array) {
		sorting as = new sorting(array, array.length);
		long startTime = System.currentTimeMillis();
		as.Mergesort(as.Array2(), 0, as.Size2() - 1, as.Size2());
		long endtime = System.currentTimeMillis();
		
		System.out.println("Mergesort Time: " + (endtime - startTime));
		System.out.println("COMPCOUNT: " + as.getCOMPCOUNT());
	}
	private static void Heapsort(int[] array) {
		sorting as = new sorting(array, array.length);
		long startTime = System.currentTimeMillis();
		as.Heapsort(array, array.length);
		long endtime = System.currentTimeMillis();
		
		System.out.println("Heapsort Time: " + (endtime - startTime));
		System.out.println("COMPCOUNT: " + as.getCOMPCOUNT());
	}
	
	private static void Quicksort(int[] array) {
		sorting as = new sorting(array, array.length);
		long startTime = System.currentTimeMillis();
		as.Quicksort(array, 0, as.Size2() - 1);
		long endtime = System.currentTimeMillis();
		
		System.out.println("Quicksort iTme: " + (endtime - startTime));
		System.out.println("COMPCOUNT: " + as.getCOMPCOUNT());
		
	}

	private static void copy(int[] array, int[] array2, int size) {
		for(int i = 0; i < size; i++) {
			array2[i] = array[i];
		}
	}
}
