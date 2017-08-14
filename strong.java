import java.util.*;
import java.util.Arrays;

class strong {
	
	int arg_len(String[] arg) {
		int sum = 0;
		for (int i=0; i<arg.length; ++i) {
			sum = sum + arg[i].length();
		}
		return sum;
	}

	String upper_lower(String s) {
		String s1="";
    	for (int i = 0; i < s.length(); ++i) {
    		if (i%2 == 0) {
    			s1 = s1 + Character.toUpperCase(s.charAt(i));
    		} else {
    			s1 = s1 + Character.toLowerCase(s.charAt(i));
    		}
  	 	}
  	 	return s1;
	}

	String join_arg(String[] arg) {
		String s1="";
		int i = 0;
    	for(i = 0; i < arg.length; ++i) {
			s1 = s1 + Integer.toString(i) + arg[i];
    	}
    	return s1 + Integer.toString(i+1); 
	}

	public String reverse(String input){
    	char[] in = input.toCharArray();
    	int begin=0;
    	int end=in.length-1;
    	char temp;
    	while(end>begin){
        	temp = in[begin];
        	in[begin]=in[end];
        	in[end] = temp;
        	end--;
        	begin++;
    	}
    	return new String(in);
	}

	String ins_symbols(String s) {
		String ch="$%/()=";
    	String s1="";
    	int j=0;
    	for(int i = 0; i < s.length(); ++i) {
    		s1 = s1 + s.charAt(i);
    		if ((i+1)%2 == 0) {
    			s1 = s1 + ch.charAt(j);
    			j = j+1;
    			if (j==ch.length()) {
    				j = 0;
    			}
    		}
    	}
    	return s1;
	}

	public static void main(String[] args) {
		strong obj = new strong();
		if (args.length > 0) {
			int t = 0;
			String[] arg = args;
			if (obj.arg_len(arg) < 9) {
      			System.out.println("I need at least 9 characters!");
      		} else {
      			for (int i = 0; i < arg.length; ++i) {
      				arg[i] = obj.upper_lower(obj.reverse(arg[i]));
      			}
      			System.out.println(obj.ins_symbols(obj.join_arg(arg)));
      		}
		}
	}

} 
