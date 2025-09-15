// prosedural
function setor(uang) {
    saldo += uang;
}

function tarik(uang) {
    if (uang <= saldo) {
        saldo -= uang;
    }else {
        console.log("Saldo tidak mencukupi")
    }
}

function cekSaldo() {
    console.log("Saldo saat ini: " + saldo);
}

setor(1000);
tarik(500);
cekSaldo(); // output: saldo saat ini:500









// OOP
class rekening{
    constructor() {
        this.saldo = 0;
    }

    setor(uang) {
        this.saldo += uang;
    }

    tarik(uang) {
        if (uang <= this.saldo) {
            this.saldo -= uang;
        } else {
            console.log("saldo tidak cukup");
        }
    }

    cekSaldo() {
        console.log("saldo saat ini: + this.saldo");
    }
}

const rekening = new rekening();
rekening.setor(1000);
rekening.tarik(500);
rekening.cekSaldo(); // saldo saat ini: 500











