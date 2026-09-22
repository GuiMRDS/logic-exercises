// 705.484.450-52
// 070.987.720-03

class ValidaCpf {
  constructor(cpfEnviado) {
    Object.defineProperty(this, "cpfLimpo", {
      writable: false,
      enumerable: false,
      configurable: false,
      value: cpfEnviado.replace(/\D+/g, ""),
    });
  }

  éSequencia() {
    return this.cpfLimpo.charAt(0).repeat(11) === this.cpfLimpo;
  }

  gerarNovoCpf() {
    const cpfSemDigitos = this.cpfLimpo.slice(0, -2);
    const digito1 = this.geraDigito(cpfSemDigitos);
  }

  geraDigito(cpfSemDigitos) {
    let total = 0;
    let reverso = cpfSemDigitos.length + 1;

    for (let stringNumerica of cpfSemDigitos) {
      total += reverso * Number();
      reverso--;
    }
  }

  valida() {
    if (!this.cpfLimpo) return;
    if (typeof this.cpfLimpo !== "string") return false;
    if (this.cpfLimpo.length !== 11) return false;
    if (this.éSequencia()) return false;
    if (!this.gerarNovoCpf()) return false;

    return "CHEGUEI AQUI";
  }
}

let validaCpf = new ValidaCpf("070.987.720-03");
console.log(validaCpf.valida());
