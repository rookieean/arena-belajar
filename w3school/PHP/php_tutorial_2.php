<?php

/*-------------------------if <else---------------></else--------------->

// if -> mengeksekusi beberapa kode jika salah satu kondisinya benar
// if..else -> mengeksekusi beberapa kode jika suatu kondisi benar dan kode lain jika kondisi itu salah
// if..elseif.. -> mengeksekusi kode yang berbeda untuk lebih dari dua kondisi
// switch -> memilih salah satu dari banyak blok kode yang akan dieksekusi

// if PHP
if (condition) {
  // code yg dieksekusi, klo true;
}

if (6 > 9) {
   echo "Have a good day!";
}


$t = 14;

if ($t < 20) {
  echo "Have a good day!";
}







/*----------------------------- PHP if Operators ------------------------ */

// operator perbandingan
$t = 14;

if ($t == 14) {
  echo "Have a good day!";
}

// operator logika
$a = 200;
$b = 33;
$c = 500;

if ($a > $b && $a < $c ) {
  echo "Both conditions are true";
}

$a = 5;

if ($a == 2 || $a == 3 || $a == 4 || $a == 5 || $a == 6 || $a == 7) {
  echo "$a is a number between 2 and 7";
}







/*------------------------ if else statement -------------- */

if (condition) {
    // code to be executed if condition is true;
  } else {
    // code to be executed if condition is false;
  }



  $t = date("H");

  if ($t < "20") {
    echo "Have a good day!";
  } else {
    echo "Have a good night!";
  }

// if elseif else
if (condition) {
   // code to be executed if this condition is true;
  } elseif (condition) {
    // code to be executed if first condition is false and this condition is true;
  } else {
    // code to be executed if all conditions are false;
  }

  $t = date("H");

  if ($t < "10") {
    echo "Have a good morning!";
  } elseif ($t < "20") {
    echo "Have a good day!";
  } else {
    echo "Have a good night!";
  }






/*-------------------pernyataan if singkat PHP ---------------*/

// singkatan jika
$a = 5;

if ($a < 10) $b = "Hello";

echo $b


// singkatan if... else ternary operator
$m = 13;

$b = $m < 10 ? "Hello" : "Good Bye";

echo $b;
$m = 13;
// teknik ini dikenal dgn operator terner, 










/*------------------ pernyataan if bersarang ------------*/

// bersarang jika, if dalam if
$a = 18;

if ($a > 10) {
  echo "Above 10";
  if ($a > 20){
    echo "end also above 20";
  } else {
    echo " but not above 20";
  }
}





/*---------------- pernyataan switch PHP ---------------*/

// pernyataan PHP switch
switch (expression){
  case label1:
    // code block
    break;
  case label2:
    // code block
    break;
  case label3:
    // code block
    break;
  default:
    // code block
}

// contoh..........................
$favcolor = "red";

switch ($favcolor){
  case "red":
    echo "your favorite color is red!";
    break;
  case "blue":
    echo "your favorite color is blue!";
    break;
  case "green":
    echo "your favorite color is green!";
    break;
  default:
    echo "your favorite color is neither red, blue, or green";
}


// klo breaknya diilangin gimana?
$favcolor = "red";

switch ($favcolor){
  case "red":
    echo "your favorite color is red!";
              // break hilang..
  case "blue":
    echo "your favorite color is blue!";
    break;
  case "green":
    echo "your favorite color is green!";
    break;
  default:
    echo "your favorite color is neither red, blue, or green";
}
// outputnya akan "ur favorite color is red! ur favorite color is blue!"


// default penjelasan -> jika gak ada yg cocok ya di eksekusi
$d = 4;

switch ($d){
  case 6:
    echo "Today is Sturday";
    break;
  case 0:
    echo "Today is Sunday";
    break;
  default:
    echo "lookin at sky";
}

// default gk harus di taruh di belakang
switch ($d){
  default:
    echo "lookin at sky"; // boleh default di awal
    break; // harus pake break ya... cara ini kurang recomend
  case 6:
    echo "Today is Sturday";
    break;
  case 0:
    echo "Today is Sunday";
    break;
}

// blok kode umum
$d = 3;

switch ($d) {
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
    echo "The weeks feels so long!";
    break;
  case 6:
  case 0:
    echo "Weeknds ar the best!";
    break;
  default:
    echo "something went wrong";
  
} // output the weeks feels so long!







/*------------------------- PHP LOOPS -----------------------*/

// PHP loops
// kita nulis kode pengen berulang-ulang, tapi capek nulis terus, pake loop biar bisa di ulang dalam jumlah yang kita inginkan


// while -> mengulang blok kode selama kondisi benar
$i = 1;
while ($i < 6) {
  echo $i;
  $i++;
}

// while - break -> stop bahkan ketika kondisinya benar
$i = 1;
while ($i < 6) {
  if ($i == 3) break;
  echo $i;
  $i++;
}

// while - continue -> berhenti di baris ini, lanjut setelanya
$i = 0;
while ($i < 6) {
  $i++;
  if ($i == 3) continue;
  echo $i;
}

// sintaksis alternatif
$i = 1;
while ($i < 6):
  echo $i;
  $i++;
endwhile;

// langkah 10 -> pengen loop  100, tapi setiap loop 10?
$i = 0;
while ($i < 100) {
  $i+= 10;
  echo $i "<br>";
}




// do while -> perulangan blok kode sekali, dan akan mengulang selama kondisi masih berlaku
$i = 1;

do {
  echo $i;
  $i++;
}while ($i < 6);


$i = 8; // var 8 atau lebih dari 6

do {
  echo $i;
  $i++;
}while ($i < 6);
// Kode akan dieksekusi satu kali, sekalipun kondisinya tidak pernah benar.
// output akan 8


// do while - break -> berhenti, walaupun kondisi benar
$i = 1;

do {
  if ($i == 3);
  break;
  $i++;
} while ($i < 6);


// do while - continue -> berhenti saat ini, lanjut setelahnya
$i = 0;

do {
  $i++;
  if ($i == 3) continue ;
  echo $i;
} while ($i < 6);




// PHP for Loop

// perulangan PHP for
for (expression1, expression2, expression3) {
  // code block
}
// ekspresi 1 di evaluasi, ekspresi 2 lanjut evaluasi, ekspresi 3 evaluasi, jadi hasilnya adalah evaluasi dari ketiga ekspresi

// contoh ................
for ($x = 0; $x <= 10; $x++) {
  echo "The number is: $x <br> "; 
}

// for loop -> break 
for ($x = 0; $x <= 10; $x++) {
  if ($x == 3) break;
  echo "The number is: $x <br>";
}

// for loop -> lanjutan
for ($x = 0; $x <= 10; $x++) {
  if ($x == 3) continue;
  echo "The number is: $x <br>";
}

// hitung sampe angka 100 tapi pake puluhan
for ($x = 0; $x <= 100; $x+=10) {
  echo "The number is: $x <br>";
}




// perulangan foreach -> perulangan untuk array

// perulangan foreach dalam array
$colors = array("red", "green", "blue", "black");

foreach ($colors as $x) {
  echo "$x <br>";
}

// array asosiatif -> diulang juga dengan nilai pada array trsbt
$members = array("Peter"=>"35", "Ben"=>"97", "Gaun"=>"75");

foreach ($members as $x => $y) {
  echo "$x : $y <br>";
}

// perulangan foreach dalam objek -> mengulang properti dalam objek
class Car {
  public $color;
  public $model;
  public function __construct($color, $model) {
    $this->color = $color;
    $this->model = $model;
  }
}

$myCar = new Car("red", "Volvo");

foreach ($myCar as $x => $y) {
  echo "$x: $y <br>";
}


// foreach - break
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $x) {
  if ($x == "blue") break;
  echo "$x <br>";
}

// foreach - lanjut
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $x) {
  if ($x == "blue") continue;
  echo "$x <br>";
}

// foreach - oleh Ref
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $x) { // gak pake $....
  if ($x == "blue") $x = "pink";
}

var_dump($colors);

// pake $................
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as &$x) { // pake $
  if ($x == "blue") $x = "pink";
}

var_dump($colors);
// kalo pake $, kita juga bisa ngubah array itu sendiri  dgn yg kita mau


// sintaksis alternatife
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $x) :
  echo "$x <br>";
endforeach;









/*----------------------- PHP  fUNCTIONS ---------------*/

// membuat fungsi PHP
function myMessage() {
  echo "Hello world!";
}

myMessage(); // memanggil fungsi



// argumen fungsi PHP
function familyName($fname) {
  echo "$fname Refsnes.<br>";
}

familyName("Jani"); // satu argumen
familyName("Hege", "8373"); // dua argumen
familyName(); // argumen default



// mengembalikan nilai
function sum($x, $y) {
  $z = $x +$y;
  return $z;
}

echo "3 + 10 = " . sum(3, 10). "<br>";
echo "6 + 8 = " . sum(6, 8). "<br>";
echo "2 + 5 = " . sum(4, 5);



// melewati argumen dengan referensi
function add_five(&$value) { // pake &.. utk merubah sesuatu
  $value += 5;
}

$num = 2;
add_five($num);
echo $num;



// jumlah argumen yang bervariasi
function sumMyNumbers(...$x) { // pake ... klau kita gk tau berapa argumennya
  $n = 0;
  $len = count($x);
  for($i = 0; $i < $len; $i++) {
    $n += $x[$i];
  }
  return $n;
}

$a = sumMyNumbers(5, 2, 6, 2, 7, 7);
echo $a;

function myFamily($lastname, ...$firstname) { // argumen variadic, nulisnya juga harus gtu
  txt = "";
  $len = count($firstname);
  for($i = 0; $i < $len; $i++) {
    $txt = $txt."Hi, $firstname[$i] $lastname.<br>";
  }
  return $txt;
}

$a = myFamily("Doe", "Jane", "John", "Joey");
echo $a;



// PHP bahasa yg longgar ketika di ketik
function addNumbers(int $a, int $b) {
  return $a + $b;
}
echo addNumbers(5, "5 days");
// since strict is not enabled "5 days" is changed to int(5), and it will return 10


<?php declare(strict_types=1); // strict requirements

function addNumbers(int $a, int $b) {
  return $a + $b;
}
echo addNumbers(5, "5 days");
// since strict is enabled and "5 days" is not an integer, an error will be thrown
// Deklarasi tersebut strictmemaksa segala sesuatunya digunakan sesuai dengan tujuannya.



// deklarasi tipe pengembalian PHP
<?php declare(strict_types=1); // strict requirement
function addNumbers(float $a, float $b) : float {
  return $a + $b;
}
echo addNumbers(1.2, 5.2);
?>



// 
<?php declare(strict_types=1); // strict requirement
function addNumbers(float $a, float $b) : int {
  return (int)($a + $b);
}
echo addNumbers(1.2, 5.2);










/*-------------------------- Array PHP ----------------- */

$a = array("valva", "mgtr", "jdud");

// item array -> dapat berupa tipe data apapun
$myArr = array("volvo", 15, ["apples", "banana", "corn"], myFunction)

// fungsi array - untuk menghitung
$cars = array("volvo", "BMW", "Toyota");
echo count($cars); 










/*----------------- Array yg diindeks ---------------------- */

// PHP indexed arrays
$cars = array("volvo", "bmw", "toyota");
var_dump($cars);

echo $cars[0]; // akses array

$cars[1] = "Ford"; // ubah nilai array

foreach ($cars as $s) { // looping array
  echo "$s <br>";
}

array_push($cars, "Laguna"); // nambah item baru di akhir
// walaupun punya array dgn nomor acak, dia akan tetap menambahkan di akhir










/*------------------------- Asosiatif Array ----------------*/

// asosiatif array -> menggunakan kunci ternama yang kamu tetapkan
$car = array("barand"=>"Ford", "model"=>"Mustang", "year"=>1987)
var_dump($car);

// mengakse item array
$car = array("barand"=>"Ford", "model"=>"Mustang", "year"=>1987)
echo $car["model"];

// ubah nilai
$car = array("barand"=>"Ford", "model"=>"Mustang", "year"=>1987)
$car["year"]=2005;
var_dump($car);

// lopping array
$car = array("barand"=>"Ford", "model"=>"Mustang", "year"=>1987)
foreach ($car as $x => $y) {
    echo "$x : $y <br>";
  }














/*--------------------------- Membuat array PHP -------------------*/

// membuat array
$car = array("mcad", "bmw", "leghing");
$cars = ["macsh", "jedudn", "ajgss"]; // cara lain pake []

// array asosiatif -> berupa nama, bukan nomor indeks 0 , 1, 2


// bikin array
$myCar = []; // kosongan
$myCar["brand"] = "Ford"; // baru di isi
$myCar["model"] = "Mustang";
$myCar["year"] = 1964;

// mencampur kunci array
$myArr = [];
$myArr[0] = "apples";
$myArr[1] = "bananas";
$myArr["fruit"] = "cherries"; // like this, no indeksnya, adalh nama array













/*----------------------------- Array akses PHP -------------------- */

// akses item array -> rujuk nama indeksnya
$cars = array("Volvo", "BMW", "Toyota");
echo $cars[2]; // indeks no 2
echo $cars["year"]; // merujuk nama kunci arraynya

// bisa pake ganda / atau tunggal
echo $cars["model"];
echo $cars['model']; // sama aja buat bisa akses array


// menjalankan item fungsi 
// array dapat berupa fungsi, contoh....
function myFunction() {
  echo "I come from a function!";
}
 $myArr = array("Volvo", 16, myFunction);

 $myArr[2]();



// menjalankan fungsi merujuk pada nama kunci
function myFunction() {
  echo "I come from a function!";
}

$myArr = array("car" => "volvo", "age" => "bran", "year" => 1977, "fungsi" => myFunction);

$myArr["fungsi"]();


// melakukan looping melalui array asosiatif
$car = array("brand"=>"ford", "model"=>"HONDA",)

foreach ($car asa $x => $y) {
  echo "$x: $y <br>";
}


// melakukan looping melalui array indeks
$cars = array("Volvo", "BMW", "Toyota");
foreach ($cars as $x) {
  echo "$x <br>";
}
















/*------------------------memperbarui item array --------------*/

// perbarui item array -> bisa nama kunci/ no indeks
$cars = array("Volvo", "BMW", "Toyota");
$cars[1] = "Ford";
$cars["year"] = 2024;


// mengubah semua menjadi satu kubu
$cars = array("Volvo", "BMW", "Toyota");
foreach ($cars as &$x) {
  $x = "Ford";
}
unset($x); // ingat... tambahkan ini, jgan lupa
var_dump($cars);














/*-----------------------------tambahkan item array ------------------*/


// tambahkan item array
$buah = array("manga", "pelem", "cherry");
$fruits[] = "strawberry";

// asosiatif
$cars = array("brand" => "Ford", "model" => "Mustang");
$cars["color"] = "Red";

// tambahkan beberapa item array
$fruits = array("Apple", "Banana", "Cherry");
array_push($fruits, "Orange", "Kiwi", "Lemon");

// menambahkan beberapa item ke asosiatif
$cars = array("brand" => "Ford", "model" => "Mustang");
$cars += ["color" => "red", "year" => 1964];











/*------------------------- hapus item array ------------------ */

// hapus item array
$cars = array("Volvo", "BMW", "Toyota");
array_splice($cars, 1, 1);

// menggunakan unset
$cars = array("Volvo", "BMW", "Toyota");
unset($cars[1]);

// hapus beberapa
$cars = array("Volvo", "BMW", "Toyota");
array_splice($cars, 1, 2); // hapus 2 itm, dimulai dari item kedua

// hapus pertama dan kedua
$cars = array("Volvo", "BMW", "Toyota");
unset($cars[0], $cars[1]);

// pake fungsi diff
$cars = array("brand" => "Ford", "model" => "Mustang", "year" => 1964);
$newarray = array_diff($cars, ["Mustang", 1964]);

// hapus item terakhir -> pop
$cars = array("Volvo", "BMW", "Toyota");
array_pop($cars);

// hapus item pertama -> shif
$cars = array("Volvo", "BMW", "Toyota");
array_shift($cars);















/*--------------------------- mengurutkan array -------------------*/

/*
sort()- mengurutkan array dalam urutan menaik
rsort()- mengurutkan array dalam urutan menurun
asort()- mengurutkan array asosiatif dalam urutan menaik, menurut nilainya
ksort()- mengurutkan array asosiatif dalam urutan menaik, menurut kuncinya
arsort()- mengurutkan array asosiatif dalam urutan menurun, menurut nilainya
krsort()- mengurutkan array asosiatif dalam urutan menurun, menurut kuncinya
*/

// contoh:
$cars = array("Volvo", "BMW", "Toyota");
sort($cars);

$numbers = array(4, 6, 2, 22, 11);
sort($numbers);


/*-------------------------------- multidimensi array -----------------------*/


/*
Name	        Stock	        Sold
Volvo	          22	        18
BMW	            15	        13
Saab	          5	          2
Land Rover	    17	        15
*/



$cars = array (
  array("Volvo",22,18),
  array("BMW",15,13),
  array("Saab",5,2),
  array("Land Rover",17,15)
);



echo $cars[0][0].": In stock: ".$cars[0][1].", sold: ".$cars[0][2].".<br>";
echo $cars[1][0].": In stock: ".$cars[1][1].", sold: ".$cars[1][2].".<br>";
echo $cars[2][0].": In stock: ".$cars[2][1].", sold: ".$cars[2][2].".<br>";
echo $cars[3][0].": In stock: ".$cars[3][1].", sold: ".$cars[3][2].".<br>";


// contoh loop 
for ($row = 0; $row < 4; $row++) {
  echo "<p><b>Row number $row</b></p>";
  echo "<ul>";
    for ($col = 0; $col < 3; $col++) {
      echo "<li>".$cars[$row][$col]."</li>";
    }
  echo "</ul>";
}














/*----------------------------- SUPER GLOBALS --------------------*/

// superglobals -> variabel global yang bisa diakses di seluruh file PHP, tanpa mendeklarasikan variabel tersebut

// $GLOBALS -> variabel super global PHP yang menyimpan semua variabel global dalam bentuk array asosiatif.
$x = 75;
  
function myfunction() {
  echo $GLOBALS['x']; // harus pake ini
}

myfunction()


// contoh lain
$x = 75;
  
function myfunction() {
  global $x; // bisa pake ini juga
  echo $x;
}

myfunction()

// contoh lain juga
function myfunction() {
  $GLOBALS["x"] = 100;
}

myfunction();

echo $GLOBALS["x"];
echo $x;




// $ SERVER ->variabel super global PHP yang menyimpan informasi tentang header, jalur, dan lokasi skrip.
echo $_SERVER['PHP_SELF'];
echo $_SERVER['SERVER_NAME'];
echo $_SERVER['HTTP_HOST'];
echo $_SERVER['HTTP_REFERER'];
echo $_SERVER['HTTP_USER_AGENT'];
echo $_SERVER['SCRIPT_NAME'];




// $_REQUEST -> super global PHP yang berisi data formulir yang dikirimkan, dan semua data cookie.
// $_REQUESTadalah array yang berisi data dari $_GET, $_POST, dan $_COOKIE.
$_REQUEST['firstname']





// $_POST -> super global PHP yang berisi data formulir yang dikirimkan dengan metode POST.






// $_GET -> super global PHP yang berisi data formulir yang dikirimkan dengan metode GET.



















/*-------------------------REG EX ----------------*/

// ekspresi reguler -> pola pencarian yang digunakan untuk mencocokkan karakter dalam string






?>

