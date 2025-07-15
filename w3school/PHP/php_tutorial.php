<!DOCTYPE html>
<html>
<body>
 
<?php
echo "My first PHP script!";
?>

</body>
</html>

<?php
// INTRO PHP
// PHP = Hypertext Preprocessor
// php tidak peka dengan huruf besar kecil
// echo atau ECHO = sama
// variabel peka huruf besar kecil
// echo $color; = echo $COLOR; = echo $coLor; = echo $cOLOR;


// COMMENT
// This is a single-line comment

# This is also a single-line comment

/* This is a
multi-line comment */







/* ----------------------VARIABEL PHP---------------------- */

// ~~~~~~~~~~~~~~ membuat variabel ~~~~~~~~~~~~~~~
$x = 5;
$y = 6;

//~~~~~~~~~~~~~~~~ variabel keluaran ~~~~~~~~~~~~~~~~~~~~
$bruh = "apaan tuh!";
echo "i love u $bruh"; // sama kek print di python

$txt = "W3Schools.com";
echo "I love " . $txt . "!";

$x = 5;
$y = 4;
echo $x + $y;

//~~~~~~~~~~~~~~~~~~~ jenis variabel ~~~~~~~~~~~~~~~~~~~~
$x = 5;      // $x is an integer
$y = "John"; // $y is a string
echo $x;
echo $y;

//~~~~~~~~~~~~~~~~ dapatkan tipe datanya ~~~~~~~~~~~~~~~~~
$x = 5;
var_dump($x);

var_dump(5); // int
var_dump("john"); // string
var_dump(3.14); // float
var_dump(true); // boolean
var_dump([2, 3, 56]); // array
var_dump(NULL); // NULL

//~~~~~~~~~~~~~~~~~~~ menetapkan string ke variabel ~~~~~~~~~~~~~~~~~~~~
$x ="John";
echo $x;

//~~~~~~~~~~~~~~~~~ tetapkan beberapa nilai ~~~~~~~~~~~~~~~~~~~~~
$x = $y = $z = "fruit";







/* ----------------------- VARIABEL SCOPE ----------------------- */

// lokal, global, dan statis

//~~~~~~~~~~~~~~~~~ cakupan global~~~~~~~~~~~~~~~~~
$x = 5; // global scope

function myTest() {
  // using x inside this function will generate an error
  global $x;
  echo "<p>Variable x inside function is: $x</p>";
}
myTest();

echo "<p>Variable x outside function is: $x</p>";

//~~~~~~~~~~~~~~~~~~~~~ cakupan lokal ~~~~~~~~~~~~~~~~~~~~~~~
function myLocalTest() {
    $x = 5; // local scope
    echo "<p>Variable x inside function is: $x</p>";
  }
  myLocalTest();
  
  // using x outside the function will generate an error
  echo "<p>Variable x outside function is: $x</p>";


// ~~~~~~~~~~~~ php kata kunci global ~~~~~~~~~~~~~~~
$x = 5;
$y = 10;

function my3Test(){
    global $x, $y;
    $y = $x + $y;
}

my3Test();
echo $y; // output 15

$x = 5;
$y = 10;

function my4Test(){
    $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['z'];
}

myTest();
echo $y; // output 15



//~~~~~~~~~~~~~~~ php kata kunci statis ~~~~~~~~~~~~~~~~

// Biasanya, saat suatu fungsi selesai/dieksekusi, semua variabelnya dihapus. Namun, terkadang kita ingin variabel lokal TIDAK dihapus. Kita memerlukannya untuk pekerjaan selanjutnya.
function my5Test(){
    static $x = 0; // contoh statis kata kunci
    echo $x;
    $x++;
}

my5Test();







/* ---------------------PHP Echo and print statement ---------------*/

// echo dan print sama
// echo lebih cepat
// print hanya dapat mencetak satu string dan selalu mengembalikan 1
// echo dapat mencetak beberapa string sekaligus


//~~~~~~~~~~~~~~~~~~~~~~~~~~`~~ pernyataan PHP echo ~~~~~~~~~~~~~~~~~~~~~
echo "Hello";
// sama kek....
echo ("Hello");

//~~~~~~~~~~~~~~~~~~~~~~~menampilkan teks ~~~~~~~~~~~~~~~~~
echo "<h2>PHP is Fun!</h2>"; // dapat berisi tag html
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "im about to learn PHP! <br>";
echo "This", "string", "was";

//~~~~~~~~~~~~~~~~~~~~~~~~variabel tampilan ~~~~~~~~~~~~~~~~~~~~~~~~~~
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";

echo "<h2>$txt</h2>";
echo "<p>Study PHP at $txt2</p>";

//~~~~~~~~~~~~~~~~~~~~ menggunakan tanda kutip tunggal ~~~~~~~~~~~~~~~~~
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";

echo '<h2>' . $txt1 . '</h2>';
echo '<p>Study PHP at ' . $txt2 . '</p>';

//~~~~~~~~~~~~~~~~~~~~~~~~ pernyataan cetak PHP ~~~~~~~~~~~~~~~
print "Hello";
//same as:
print("Hello");

//~~~~~~~~~~~~~~~~~~~~~~~~~ menampilkan teks ~~~~~~~~~~~~~~~~~~~~~~~
print "<h2>PHP is Fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";

//~~~~~~~~~~~~~~~~~~~~~~~~~ menampilkan variabel ~~~~~~~~~~~~~~~~~~~~~
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";

print "<h2>$txt1</h2>";
print "<p>Study PHP at $txt2</p>";

//~~~~~~~~~~~~~~~~~~~~ menggunakan tanda kutip tunggal ~~~~~~~~~~~~~~~~
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";

print '<h2>' . $txt1 . '</h2>';
print '<p>Study PHP at ' . $txt2 . '</p>';
// penggunaan tanda kutip tunggal dan ganda akan beda output









/* ----------------------PHP Data Types---------------------- */


// ~~~~~~~~~~~~~~~~~~~~~~ mendapatkan tipe data ~~~~~~~~~~~~~~
$x = 5;
var_dump($x);


// ~~~~~~~~~~~~~~~~~~~~~~ rangkaian PHP ~~~~~~~~~~~~~~~~~~~~
$x = "Hello world!"; // boleh tanda kutip ganda
$y = 'Hello world!'; // boleh tanda kutip tunggal

var_dump($x);
echo "<br>";
var_dump($y);


// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP bILANGAN BULAT ~~~~~~~~~~~~~~~
$x = 399746;
var_dump($x);

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP Mengapung ~~~~~~~~~~~~~~~~~~
$x = 10.497865;
var_dump($x);

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP Boolean ~~~~~~~~~~~~~~~~~~~~~
$x = true;
var_dump($x);

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP Array ~~~~~~~~~~~~~~~~~~~~~
$cars = array("volvo", "BMW", "Toyota");
var_dump($cars);

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP Object ~~~~~~~~~~~~~~~~~~~~~
class Car {
    public $color;
    public $model;
    public function __construct($color, $model) {
      $this->color = $color;
      $this->model = $model;
    }
    public function message() {
      return "My car is a " . $this->color . " " . $this->model . "!";
    }
  }
  
  $myCar = new Car("red", "Volvo");
  var_dump($myCar);



// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP NULL ~~~~~~~~~~~~~~~~~~~~~
$x = "Hello world!";
$x = null;
var_dump($x);

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ubah tipe data ~~~~~~~~~~~~~~~~~~~~~
$x = 5;
var_dump($x);

$x = "Hello";
var_dump($x);

$x = 5;
$x = (string) $x;
var_dump($x);





/* ----------------------PHP String---------------------- */

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PHP String ~~~~~~~~~~~~~~~~~~~~~
echo "Hello";
echo "Hello";

// Ada perbedaan besar antara tanda kutip ganda dan tanda kutip tunggal dalam PHP.
// Tanda kutip ganda memproses karakter khusus, sedangkan tanda kutip tunggal tidak.

// ~~~~~~~~~~~~~~~~~~ Perbedaan tanda kutip tunggal dan ganda ~~~~~~~~~~~~~~

// ganda
$x = "John";
echo "Hello $x"; // output: Hello John

// tunggal
$x = "John";
echo 'Hello $x'; // output: Hello $x


// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ panjang String ~~~~~~~~~~~~~~~~~~~~~

echo strlen("Hello"); // output: 5


// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ jumlah kata ~~~~~~~~~~~~~~~~~~~~~

echo str_word_count("Hello"); // output: 1

// ~~~~~~~~~~~~~~~~~~~~~~~~~~ mencari teks dalam string ~~~~~~~~~~~~~~

echo  strpos("hello world", "world"); // output: 6 (index dimulai dari 0)






/* ---------------------- Ubah String PHP ---------------------- */

// huruf besar
$x = "hello world";
echo strtoupper($x); // output: HELLO WORLD

// huruf kecil
$x = "HELLO WORDL";
echo strtolower($x); // output: hello world

// ganti string
$x = "hello world";
echo str_replace("world", "bernand", $x); // output: hello dolly

// membalikan string
$x = "hello world";
echo strrev($x); // output: dlrow olleh

// hapus spasi
$x = "h  ello yoiii";
echo trim($x); // output: hello yoiii

// mengubah string menjadi array
$x = "hello";
$y = explode("", $x);

print_r($y); // output: Array ( [0] => h [1] => e [2] => l [3] => l [4] => o )
// penggunaan print_r untuk menampilkan array







/* ---------------------- menggabungkan string ---------------------- */

// penggabungan string
$x = "hello";
$y = "World";
$z = $x . $y;
echo $z; // output helloworld

$x = "hello";
$y = "World";
$z = $x ." ". $y; // tambah spasi
echo $z; // output hello world

// ----> cara paling mudah dari pengabungan
$x = "hello";
$y = "World";
$z = "$x $y"; // tambah spasi dgn kutip ganda
echo $z; // output hello world





/* ---------------------------- memotong string ----------------- */

// mengiris
$x = "hello world";
echo substr($x, 6, 5); // output world
// offset -> indek setelahnya

// potong sampai akhir
$x = "hello world!";
echo substr($x, 6); // output world!

// potongan dari akhir
$x = "hello world!";
echo substr($x, -5, 3); // output orl

// panjang negatif
$x = "hi, how are u?";
echo substr($x, 5, -3); // output ow ar







/* -------------------------- karakter escape ---------------- */

// karakter melarikan diri - menyisipkan benda asing
$x = "We are the so-called \"Vikings\" from the north.";

// karakter pelarian:

// ------ \'        single quote
// ------ \"        double quote
// ------ \$        PHP variabels
// ------ \n        new line
// ------ \r        carriage return
// ------ \t        tab
// ------ \f        form feed
// ------ \ooo      octal value
// ------ \xhh        hex value







/* ----------------------------- PHP Numbers ----------------- */

// angka php -> integer, float, number strings
// tipe data php lagi -> infinity, NaN

// tipe numerik
$a = 5;
$b = 5.98;
$c = "34";

// phpNan -> bukan angka
// operasi mtk yg mustahil
$x = acos(8);
var_dump($x); // output float(NAN)

// string numerik PHP
$x = 5985;
var_dump(is_numeric($x));

$x = "5985";
var_dump(is_numeric($x));
$x = "59.85" + 100;
var_dump(is_numeric($x));

$x = "Hello";
var_dump(is_numeric($x));

// PHP casting string dan float ke integer
// Cast float to int
$x = 23465.768;
$int_cast = (int)$x;
echo $int_cast;

echo "<br>";

// Cast string to int
$x = "23465.768";
$int_cast = (int)$x;
echo $int_cast;


/* ----------------------- Merubah Variabel -------------- */

// ubah tipe data

// (string)- Mengonversi ke tipe data String
// (int)- Mengonversi ke tipe data Integer
// (float)- Mengonversi ke tipe data Float
// (bool)- Mengonversi ke tipe data Boolean
// (array)- Mengonversi ke tipe data Array
// (object)- Mengonversi ke tipe data Objek
// (unset)- Mengonversi ke tipe data NULL

// dilemparkan ke string
$a = 5;       // Integer
$b = 5.34;    // Float
$c = "hello"; // String
$d = true;    // Boolean
$e = NULL;    // NULL

$a = (string) $a;
$b = (string) $b;
$c = (string) $c;
$d = (string) $d;
$e = (string) $e;

//To verify the type of any object in PHP, use the var_dump() function:
var_dump($a);
var_dump($b);
var_dump($c);
var_dump($d);
var_dump($e);


// ubah ke integer
$a = 5;       // Integer
$b = 5.34;    // Float
$c = "25 kilometers"; // String
$d = "kilometers 25"; // String
$e = "hello"; // String
$f = true;    // Boolean
$g = NULL;    // NULL

$a = (int) $a;
$b = (int) $b;
$c = (int) $c;
$d = (int) $d;
$e = (int) $e;
$f = (int) $f;
$g = (int) $g;

// ubah ke float
$a = 5;       // Integer
$b = 5.34;    // Float
$c = "25 kilometers"; // String
$d = "kilometers 25"; // String
$e = "hello"; // String
$f = true;    // Boolean
$g = NULL;    // NULL

$a = (float) $a;
$b = (float) $b;
$c = (float) $c;
$d = (float) $d;
$e = (float) $e;
$f = (float) $f;
$g = (float) $g;

// ubah ke boolean
$a = 5;       // Integer
$b = 5.34;    // Float
$c = 0;       // Integer
$d = -1;      // Integer
$e = 0.1;     // Float
$f = "hello"; // String
$g = "";      // String
$h = true;    // Boolean
$i = NULL;    // NULL

$a = (bool) $a;
$b = (bool) $b;
$c = (bool) $c;
$d = (bool) $d;
$e = (bool) $e;
$f = (bool) $f;
$g = (bool) $g;
$h = (bool) $h;
$i = (bool) $i;

// ubah ke array
$a = 5;       // Integer
$b = 5.34;    // Float
$c = "hello"; // String
$d = true;    // Boolean
$e = NULL;    // NULL

$a = (array) $a;
$b = (array) $b;
$c = (array) $c;
$d = (array) $d;
$e = (array) $e;

// ubah objek ke array
class mobil {
  public $color;
  public $model;
  public function __construct($color, $model) {
    $this->color = $color;
    $this->model = $model;
  }
  public function message() {
    return "My car is a " . $this->color . " " . $this->model . "!";
  }
}

$myCar = new Car("red", "Volvo");

$myCar = (array) $myCar;
var_dump($myCar);


// ubah ke objek
$a = 5;       // Integer
$b = 5.34;    // Float
$c = "hello"; // String
$d = true;    // Boolean
$e = NULL;    // NULL

$a = (object) $a;
$b = (object) $b;
$c = (object) $c;
$d = (object) $d;
$e = (object) $e;

// array menjadi objek
$a = array("Volvo", "BMW", "Toyota"); // indexed array
$b = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43"); // associative array

$a = (object) $a;
$b = (object) $b;

// ubah ke NULL
$a = 5;       // Integer
$b = 5.34;    // Float
$c = "hello"; // String
$d = true;    // Boolean
$e = NULL;    // NULL

$a = (unset) $a;
$b = (unset) $b;
$c = (unset) $c;
$d = (unset) $d;
$e = (unset) $e;




/* ---------------------- PHP Math --------------------- */

// PHP pi() function
echo (pi()); // mengembalikan nilai pi

// PHP min() dan max()
echo (min(0, 150, 89, 40, 20, -200));
echo (max(0, 150, 89, 40, 20, -200));
// menemukan nilai terendah dan tertinggi

// abs() -> mengembalikan nilai absolut (postif) angka
echo (abs(-39.89));

// sqrt() -> mengembalikan akar kuadrat
echo(sqrt(76));

// round() -> membulatkan angka floating
echo (round(76.97));

// angka acak -> rand()
echo (rand());
echo (rand(10, 100)) // dari 10 sampe 100








/* ---------------------- Konstanta PHP --------------- */

// konstanta -> pengenal nama utk nilai sederhana, tdk dapat diubah selama skrip berlangsung
// konstanta bersifat global

// membuat konstanta PHP
define("NAME", "value");
echo NAME;
// nama -> nama konstanta
// nilai -> nilai konstanta

define("GREETING", "Welcome to my world");
echo GREETING;

// const -> bisa pake ini juga
const MYCAR = "BMW";
echo MYCAR;

// BEDANYA define() dan const
// define() -> bisa dibuat di dalam cakupan blok
// const    -> gak bisa dibuat dalam cakupan lain, kek di fungsi/ if


// Array konstan PHP
define("cars", [
  "Toyota",
  "BMW",
  "Brugg"

]);
echo cars[0];

// KONSTANTA BERSIFAT GLOBAL
// global, dan bisa digunakan di seluruh skrip
define("GREETING", "Welcome hoiii");

function myTest(){
  echo GREETING;
}

myTest();






/*------------------------ Konstanta Ajaib PHP ----------------*/

// __CLASS__	If used inside a class, the class name is returned.	
// __DIR__	The directory of the file.	
// __FILE__	The file name including the full path.	
// __FUNCTION__	If inside a function, the function name is returned.	
// __LINE__	The current line number.	
// __METHOD__	If used inside a function that belongs to a class, both class and function name is returned.	
// __NAMESPACE__	If used inside a namespace, the name of the namespace is returned.	
// __TRAIT__	If used inside a trait, the trait name is returned.	
// ClassName::class	Returns the name of the specified class and the name of the namespace, if any.





/*----------------------------------- Operator PHP --------------------------*/

// OPERATOR ARITMATIKA
//       +	Addition	      $x + $y	      Sum of $x and $y	
//       -	Subtraction	    $x - $y	      Difference of $x and $y	
//       *	Multiplication	$x * $y	      Product of $x and $y	
//       /	Division	      $x / $y	      Quotient of $x and $y	
//       %	Modulus	        $x % $y	      Remainder of $x divided by $y	
//      **	Exponentiation	$x ** $y	    Result of raising $x to the $y'th power

// OPERATOR PENUGASAN
// x = y      	x = y	          The left operand gets set to the value of the expression on the right	
// x += y	      x = x + y	      Addition	
// x -= y	      x = x - y	      Subtraction	
//  x *= y	    x = x * y	      Multiplication	
// x /= y	      x = x / y	      Division	
// x %= y	      x = x % y     	Modulus


// OPERATOR PERBANDINGAN
//    ==	   Equal	      $x == $y   	Returns true if $x is equal to $y	
//    ===	   Identical 	  $x === $y	  Returns true if $x is equal to $y, and they are of the same type	
//    !=	   Not equal	  $x != $y	  Returns true if $x is not equal to $y	
//    <>	   Not equal	  $x <> $y    Returns true if $x is not equal to $y	
//   !==	   Not ident	  $x !== $y	  Returns true if $x is not equal to $y, or they are not of the same type	
//    >	     Greater than	$x > $y	   Returns true if $x is greater than $y	
//    <	     Less than	  $x < $y	   Returns true if $x is less than $y	
//    >=	   Greater than or equal to	$x >= $y	Returns true if $x is greater than or equal to $y	
//    <=	   Less than or equal to	$x <= $y	Returns true if $x is less than or equal to $y	
//    <=>   	Spaceship	$x <=> $y	Returns an integer less than, equal to, or greater than zero, depending on if $x is less than, equal to, or greater than $y. Introduced in PHP 7.


// OPERATOR INCREMENT / DECREMENT
//   ++$x	   Pre-increment	Increments $x by one, then returns $x	
//   $x++	   Post-increment	Returns $x, then increments $x by one	
//   --$x	   Pre-decrement	Decrements $x by one, then returns $x	
//   $x--	   Post-decrement	Returns $x, then decrements $x by one


// OPERATOR LOGIKA PHP
//     and	  And	    $x and $y	      True if both $x and $y are true	
//     or	    Or	    $x or $y	      True if either $x or $y is true	
//     xor	  Xor	    $x xor $y	      True if either $x or $y is true, but not both	
//     &&	    And	    $x && $y	       True if both $x and $y are true	
//     ||	    Or	    $x || $y	       True if either $x or $y is true	
//     !	   Not	   !$x	             True if $x is not true

// OPERATOR STRING PHP
//    .	    Concatenation	            $txt1 . $txt2	  Concatenation of $txt1 and $txt2	
//    .=	  Concatenation assignment	$txt1 .= $txt2	Appends $txt2 to $txt1

// OPERATOR ARRAY PHP
//  +	    Union	        $x + $y	      Union of $x and $y	
//  ==	  Equality	    $x == $y	    Returns true if $x and $y have the same key/value pairs	
//  ===	  Identity	    $x === $y	    Returns true if $x and $y have the same key/value pairs in the same order and of the same types	
//  !=	  Inequality	  $x != $y	    Returns true if $x is not equal to $y	
//  <>	  Inequality	  $x <> $y	    Returns true if $x is not equal to $y	
//  !==	  Non-identity	$x !== $y	    Returns true if $x is not identical to $y

// OPERATOR PENUGASAN
//    ?:	      Ternary	
//    ??	       Null coalescing	





?>