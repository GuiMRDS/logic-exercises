exports.paginaInicial = (req, res) => {
  res.send(`
    <form action="/" method=POST>
    Nome: <input type='text' name='nome'><br>
    Outro Campo: <input type="text" name="outroCampo">
    <button>Enviar</button>
    </form>
    `);
};

exports.trataPost = (req, res) => {
  res.send("Ei, sou um nova rota de POST.");
};
