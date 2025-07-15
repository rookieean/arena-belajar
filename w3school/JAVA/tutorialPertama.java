package w3school.java;

public class tutorialPertama {
    public static void main(String[] args) {
        System.out.println("Hello World!"); // cetak string
        System.out.println(876); // cetak angka
        System.out.println( 6 + 6 ); // cetak angka aritmatika dalam print

    String nama = "Budi"; // bikin string
    int angka = 10; // bikin angka
    System.out.println(angka); // gunakan nilai awal angka

    int jejal = 50; // assign a value to jejal
    angka = 80; // bisa dibikin gini juga

    final int siapa;
    siapa = 230; // konstanta nilai

    
    System.out.println(nama); //cetak string
    System.out.println(angka); //cetak angka
    System.out.println(jejal); //cetak angka2
    System.out.println(siapa); //cetak angka2

    // print -> mencetak tanpa ada filter tab, nanti dia gabung dgn yg dibawah
    // print -> mencetak tanpa ada filter tab, nanti dia gabung dgn yg dibawah
    // println -> mencetak baris secara per line

    /* multiline comment */

    

    int myNum = 5;
    float myFloatNum = 5.99f;
    char myLetter = 'D';
    boolean myBool = true;
    String myText = "Hello";

    System.out.println(myNum); // Output: 5
    System.out.println(myFloatNum); // Output: 5.99
    System.out.println(myLetter); // Output: D
    System.out.println(myBool); // Output: true
    System.out.println(myText); // Output: Hello

    String name = "John";
    System.out.println("Hello " + name); // bisa pake + untuk gabung string

    int x = 4, y = 38, j = 49;
    System.out.println(x + y + j); // bisa gini juga biar ringkas


    // contoh yang bagus ketika pilih nama
    // Student data
String studentName = "John Doe";
int studentID = 15;
int studentAge = 23;
float studentFee = 75.25f;
char studentGrade = 'B';

// Print variables
System.out.println("Student name: " + studentName);
System.out.println("Student id: " + studentID);
System.out.println("Student age: " + studentAge);
System.out.println("Student fee: " + studentFee);
System.out.println("Student grade: " + studentGrade);



// contoh hitung luas persegi panjang
// Create integer variables
int length = 4;
int width = 6;
int area;

// Calculate the area of a rectangle
area = length * width;

// Print variables
System.out.println("Length is: " + length);
System.out.println("Width is: " + width);
System.out.println("Area of the rectangle is: " + area);












/*------------------------------- TIPE DATA ------------------------------ */

int angk = 5;
float desimal = 2.67e3f; // e3f -> 3 nol dibelakang koma => 2670.0
double desimal2 = 4.287d; // double lebih besar dari float
char huruf = 'a';
boolean benar = true;
String teksku = "hai";

System.err.println(angk);
System.err.println(desimal);
System.err.println(desimal2);
System.err.println(huruf);
System.err.println(benar);
System.err.println(teksku);


// contoh penggunaan dunia nyata
// Create variables of different data types
int items = 50;
float costPerItem = 9.99f;
float totalCost = items * costPerItem;
char currency = '$';

// Print variables
System.out.println("Number of items: " + items);
System.out.println("Cost per item: " + costPerItem + currency);
System.out.println("Total cost = " + totalCost + currency);













/* -------------------------- CASTING JAVA -------------------- */


// pelebaran - dari kecil ke besar
// byte -> short -> char -> int -> long -> float -> double

// penyempitan - dari  besar ke kecil
// double -> float -> long -> int -> char -> short -> byte

// contoh pelebaran
int myint = 9;
double mydouble = myint; // otomatis casting

System.err.println(myint); // Output: 9");
System.err.println(mydouble); // Output: 9.0");

// contoh penyempitan
double mydoublee = 5.3487d;
int myintt = (int) mydoublee; // otomatis casting

System.err.println(mydoublee); // Output: 5.3487d
System.err.println(myintt); // Output: 5");


// contoh kehidupan nyata
int maxScore = 500;
int userScore = 423;

float precentage = (float) userScore / maxScore * 100.0f;

System.err.println("Percentage: " + precentage + "%"); // Output: Percentage: 84.6%

















/* -------------------------- OPERATOR JAVA -------------------- */

// operator aritmatika -> +, -, *, /, %
// operator penugasan -> =, +=, -=, *=, /=, %=
// operator perbandingan -> ==, !=, >, <, >=, <=
// operator logika -> &&, ||, !
// operator bitwise -> &, |, ^, ~, <<, >>

// operator unary -> ++, --, +, -
// operator ternary -> ? :















/*------------------------ String Java ------------------------------- */

// mencari panjang string
String anotherNama = "bambang";
System.err.println(anotherNama.length()); // mencari panjang string;
System.out.println(anotherNama.toUpperCase()); // mengubah ke huruf kapital
System.out.println(anotherNama.toLowerCase()); // mengubah ke huruf kecil
System.out.println(anotherNama.indexOf("b")); // mencari index dari huruf b







// pengabungan string java

String pertamaNama = "Buni";
String keduaNama = "Jamala";
System.out.println(pertamaNama + " " + keduaNama); // gabung string cara pertama
System.out.println(pertamaNama.concat (keduaNama)); // gabung string cara kedua







// angka dan string java
/*
String x = "10";
int y = 20;
String z = x + y;  // z will be 1020 (a String)

string akan digabungkan
angka  akan ditambah. tergantung bentuk tipe datanya

*/








// string dalam string java
String str = "Hyundai \"adalah\" sebuah nama"; // escape character \"
String str2 = "Hyundai \'adalah' sebuah nama"; // escape character \'
String str3 = "Hyundai \\ adalah sebuah nama"; // escape character \\
System.out.println(str); // output: Hyundai "adalah" sebuah nama
System.out.println(str2); // output: Hyundai 'adalah' sebuah nama
System.out.println(str3); // output: Hyundai \ adalah sebuah nama












/*------------------------- Java Math --------------------------------- */

Math.max(desimal2, mydouble); // mencari nilai max dari dua angka
Math.min(desimal2, mydouble); // mencari nilai min dari dua angka
Math.sqrt(16); // mencari akar dari angka
Math.abs(-2.89); // mencari nilai absolut (positif) dari angka
Math.random(); // menghasilkan angka random dari 0.0 - 1.0










/*------------------- Boolean Java ---------------------- */

int myage = 20;
int myage2 = 29;

if (myage >= myage2) {
    System.out.println("Old enough to vote!");
  } else {
    System.out.println("Not old enough to vote.");
  }










/*----------------------if else java -------------------------- */

int num = 20;
if (num > 0) {
    System.out.println("Benar yah bung");
}

// else if
if (condition1) {
    // block of code to be executed if condition1 is true
  } else if (condition2) {
    // block of code to be executed if the condition1 is false and condition2 is true
  } else {
    // block of code to be executed if the condition1 is false and condition2 is false
  }

  // kalau kondisi 1 false, maka lanjut ke kondisi 2


  // contohnya
int time = 22;
if (time < 10) {
  System.out.println("Good morning.");
} else if (time < 18) {
  System.out.println("Good day.");
} else {
  System.out.println("Good evening.");
}
// Outputs "Good evening."





// ternary operator -> mempersingkat tulisan

int time2 = 20;
if (time2 < 18) {
  System.out.println("Good day.");
} else {
  System.out.println("Good evening.");
}

// jadi begini
int time4 = 20;
String result = (time4 < 18) ? "Good day." : "Good evening.";
System.out.println(result);




// contoh dunia nyata
// program membuka pintu
int doorCode = 1337;

if (doorCode == 1337) {
  System.out.println("Correct code. The door is now open.");
} else {
  System.out.println("Wrong code. The door remains closed.");
}



// mencari nilai positif
int myNum5 = 10; // Is this a positive or negative number?

if (myNum5 > 0) {
  System.out.println("The value is a positive number.");
} else if (myNum5 < 0) {
  System.out.println("The value is a negative number.");
} else {
  System.out.println("The value is 0.");
}



// mencari persyaratan voting
int myAge = 25;
int votingAge = 18;

if (myAge >= votingAge) {
  System.out.println("Old enough to vote!");
} else {
  System.out.println("Not old enough to vote.");
}



// mencari angka ganjil atau genap
int myNum10 = 5;

if (myNum10 % 2 == 0) {
  System.out.println(myNum10 + " is even");
} else {
  System.out.println(myNum10 + " is odd");
} 















/*------------------------- Switch ------------------------------ */

int day = 4;
String dayName = switch (day) {
  case 1 -> "Monday";
  case 2 -> "Tuesday";
  case 3 -> "Wednesday";
  case 4 -> "Thursday";
  case 5 -> "Friday";
  case 6 -> "Saturday";
  case 7 -> "Sunday";
  default -> "Invalid day";
};
System.out.println(dayName);
// Outputs "Thursday" (day 4)
/*
Ekspresi switch dievaluasi satu kali.
Nilai ekspresi dibandingkan dengan nilai masing-masing case.
Jika ada kecocokan, blok kode terkait dieksekusi.
 */















 /*-------------------- while  Perulangan Java ------------------------------ */

 int i = 0;
 while (i < 5) {
   System.out.println(i);
   i++;
 }

// do while
do { 
    
} while (true); // do while akan dieksekusi minimal 1x, walaupun false

// contoh do while
int o = 0;
do {
  System.out.println(o);
  o++;
}
while (i < 5);

// bedanya while dan do while
// while -> jika false, tidak akan dieksekusi
// do while -> dijalankan setidaknya 1x




// contoh kehidiupan nyata

// menghitung mundur
int countdown = 3;

while (countdown > 0) {
  System.out.println(countdown);
  countdown--;
}

System.out.println("Happy New Year!!");



// game
int dice = 1;

while (dice <= 6) {
  if (dice < 6) {
    System.out.println("No Yatzy.");
  } else {
    System.out.println("Yatzy!");
  }
  dice = dice + 1;
}



















/*------------------------ Java for Loop ------------------------------ */

// jika kamu tau berapa kali mau melakukan perulangan, gunakan for loop
for (statement 1; statement 2; statement 3) {
    // code block to be executed
  }

/*
 Pernyataan 1 dieksekusi (satu kali) sebelum eksekusi blok kode.

Pernyataan 2 mendefinisikan kondisi untuk mengeksekusi blok kode.

Pernyataan 3 dieksekusi (setiap kali) setelah blok kode dieksekusi.
 */


 // contoh for loop
for (int b = 0; b < 5; b++) {
    System.out.println(b);
  }


// contoh lain
for (int c = 0; c <= 10; c = c + 2) {
    System.out.println(c);
  }























/* ---------------------- Nested Loop --------------------- */

// nested loop -> loop di dalam loop
// Outer loop
for (int outer = 1; outer <= 2; outer++) {
    System.out.println("Outer: " + outer); // Executes 2 times
    
    // Inner loop
    for (int inner = 1; inner <= 3; inner++) {
      System.out.println(" Inner: " + inner); // Executes 6 times (2 * 3)
    }
  } 

// inner loop akan dieksekusi setiap kali outer loop dieksekusi









// for each loop -> elemen array
// for (type variable : arrayName) {
//     // code block to be executed
// }

// contoh
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (String g : cars) {
  System.out.println(g);
}
// Outputs Volvo, BMW, Ford, Mazda (4 times)








// contoh kehidupan nyata
int number = 2;

// Print the multiplication table for the number 2
for (int m = 1; m <= 10; m++) {
  System.out.println(number + " x " + m + " = " + (number * m));
} 





// break and continue
// break -> keluar dari loop
// continue -> skip ke iterasi berikutnya






















/*--------------------------- ARRAY JAVA ------------------------ */


String[] mobil = {"Volvo", "BMW", "Ford", "Mazda"}; // array string
System.out.println(mobil[0]); // cetak array no 0
cars[1] = "manak"; // ubah isi array no 1
System.out.println(mobil.length); // panjang array





// looping array

String[] motorya ={"Vario", "Beat", "Scoopy", "Nmax"};
for (int l = 0; l < motorya.length; l++){
    System.err.println(cars[l]);
}


// pakai array for each
String[] mobil2 = {"Vario", "Beat", "Scoopy", "Nmax"};
for (String h : mobil2) {
    System.out.println(h);
}









// contoh kehidupan nyata

// menghitung rata-rata umur
int ages[] = {20, 22, 18, 35, 48, 26, 87, 70};

float avg, sum = 0;

// Get the length of the array
int length = ages.length;

// Loop through the elements of the array
for (int age : ages) {
  sum += age;
}

// Calculate the average by dividing the sum by the length
avg = sum / length;

// Print the average
System.out.println("The average age is: " + avg);




// An array storing different ages
int ages[] = {20, 22, 18, 35, 48, 26, 87, 70};

// Get the length of the array
int length = ages.length;

// Create a 'lowest age' variable and assign the first array element of ages to it
int lowestAge = ages[0];

// Loop through the elements of the ages array to find the lowest age
for (int age : ages) {
  // Check if the current age is smaller than the current 'lowest age'
  if (lowestAge > age) {
    // If the smaller age is found, update 'lowest age' with that element
    lowestAge = age;
  }
}

// Output the value of the lowest age
System.out.println("The lowest age in the array is: " + lowestAge);












/*-------------------- multidimensional arrays ---------------- */
// array dalam array
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} }; // cara  ulisnya
myNumbers[1][2] = 9;
System.out.println(myNumbers[1][2]); // Outputs 7 atau aksesnya



// loop array 
for (int r = 0; r < myNumbers.length; ++r) {
  for (int f = 0; f < myNumbers[r].length; ++f) {
    System.out.println(myNumbers[r][f]);
  }
}




    }
}

