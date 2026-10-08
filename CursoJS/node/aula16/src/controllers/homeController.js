exports.paginaInicial = (req, res, next) => {
  res.render("index.ejs", {
    // titulo: "Este será o título da página",
    numero: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  });
  return;
};

exports.trataPost = (req, res, next) => {
  res.send(req.body);
  return;
};
