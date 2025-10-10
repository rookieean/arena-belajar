
// Lampu Lalu Lintas
const int PIN_MERAH = 9;
const int PIN_KUNING = 10;
const int PIN_HIJAU = 11;

// Seven Segment
const int SEG_PINS[] = {2, 3, 4, 5, 6, 7, 8}; 

// Pin COM
const int COM_SATUAN = A0;
const int COM_PULUHAN = A1;


// sinyal untuk aktifkan setiap segment
const byte DIGITS[10][7] = {
  {LOW, LOW, LOW, LOW, LOW, LOW, HIGH}, // 0
  {HIGH, LOW, LOW, HIGH, HIGH, HIGH, HIGH}, // 1
  {LOW, LOW, HIGH, LOW, LOW, HIGH, LOW}, // 2
  {LOW, LOW, LOW, LOW, HIGH, HIGH, LOW}, // 3
  {HIGH, LOW, LOW, HIGH, HIGH, LOW, LOW}, // 4
  {LOW, HIGH, LOW, LOW, HIGH, LOW, LOW}, // 5
  {LOW, HIGH, LOW, LOW, LOW, LOW, LOW}, // 6
  {LOW, LOW, LOW, HIGH, HIGH, HIGH, HIGH}, // 7
  {LOW, LOW, LOW, LOW, LOW, LOW, LOW}, // 8
  {LOW, LOW, LOW, LOW, HIGH, LOW, LOW} // 9
};

// konfigurasi waktu
const int WAKTU_HIJAU = 20; 
const int WAKTU_KUNING = 3;  
const int WAKTU_MERAH = 23; 

// Waktu tunggu untuk ms
const int MUX_DELAY = 4;


void setup() {
  // Atur pin lampu
  pinMode(PIN_MERAH, OUTPUT);
  pinMode(PIN_KUNING, OUTPUT);
  pinMode(PIN_HIJAU, OUTPUT);

  // Atur pin segmen (A-G)
  for (int i = 0; i < 7; i++) {
    pinMode(SEG_PINS[i], OUTPUT);
  }

  // Atur pin Common (COM)
  pinMode(COM_SATUAN, OUTPUT);
  pinMode(COM_PULUHAN, OUTPUT);

  // Matikan semua di awal (HIGH untuk Common Anode = OFF)
  digitalWrite(COM_SATUAN, HIGH);
  digitalWrite(COM_PULUHAN, HIGH);
  changeLights(LOW, LOW, LOW);
}

// fungsi mengganti status lampu
void changeLights(int merah, int kuning, int hijau) {
  digitalWrite(PIN_MERAH, merah);
  digitalWrite(PIN_KUNING, kuning);
  digitalWrite(PIN_HIJAU, hijau);
}

//fungsi menampilkan angka pada satu digit
void setSegments(int digit_value) {
  // Tampilkan segmen berdasarkan angka (0-9)
  for (int i = 0; i < 7; i++) {
    digitalWrite(SEG_PINS[i], DIGITS[digit_value][i]);
  }
}

// fungsi utama dalam countdown
void countdown(int duration) {
  unsigned long startTime = millis();
  unsigned long currentTime = startTime;
  
  // Hitung mundur (i)
  for (int i = duration; i >= 1; i--) {
    int puluhan = i / 10;
    int satuan = i % 10;

    // Loop ini berjalan selama 1 detik (1000ms) untuk setiap hitungan (i)
    while (currentTime - startTime < 1000) {
      
      // 1. Tampilkan Digit Puluhan
      digitalWrite(COM_SATUAN, HIGH); // Matikan Satuan
      setSegments(puluhan);
      digitalWrite(COM_PULUHAN, LOW); // Nyalakan Puluhan
      delay(MUX_DELAY); 

      // 2. Tampilkan Digit Satuan
      digitalWrite(COM_PULUHAN, HIGH); // Matikan Puluhan
      setSegments(satuan);
      digitalWrite(COM_SATUAN, LOW); // Nyalakan Satuan
      delay(MUX_DELAY);
      
      // Update waktu
      currentTime = millis();
    }
    
    // Siapkan waktu mulai untuk hitungan berikutnya
    startTime = currentTime;
  }
}

void loop() {
  // --- FASE LAMPU HIJAU ---
  changeLights(LOW, LOW, HIGH); 
  countdown(WAKTU_HIJAU);

  // --- FASE LAMPU KUNING ---
  changeLights(LOW, HIGH, LOW); 
  countdown(WAKTU_KUNING);

  // --- FASE LAMPU MERAH ---
  changeLights(HIGH, LOW, LOW); 
  countdown(WAKTU_MERAH);
}