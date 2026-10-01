// Superclass
function ContaCorrente(agencia, conta, saldo) {
  this.agencia = agencia;
  this.conta = conta;
  this.saldo = saldo;
}

ContaCorrente.prototype.sacar = function (valor) {
  if (this.saldo >= valor) {
    this.verSaldo();
    return;
  }

  this.saldo -= valor;
};

ContaCorrente.prototype.despositar = function (valor) {
  this.saldo += valor;
};
ContaCorrente.prototype.verSaldo = function (valor) {
  console.log(
    `Ag/c: ${this.agencia}/${this.conta} | ` +
      `Saldo: R$${this.saldo.ToFixed(2)}`,
  );
};

const conta1 = new Conta(11, 22, 10);
conta1.despositar(11);
conta1.despositar(10);
conta1.sacar(30);
conta1.sacar(0.01);

function ContaCorrente(agencia, conta, saldo, limite) {
  Conta.call(this, agencia, conta, saldo);
  this.limite = limite;
}

ContaCorrente.prototype = Object.create(Conta.prototype);
