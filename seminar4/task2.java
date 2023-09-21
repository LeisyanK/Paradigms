int [] mas = {1,2,3,4,5,6,7,8,9};
long n = Arrays.stream(mas).filter(x -> x >= 5).count();
System.out.println(n);