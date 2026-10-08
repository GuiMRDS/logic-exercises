exports.paginaInicial = (req, res, next) => {
  res.render("index.ejs");
  return;
};

exports.trataPost = (req, res, next) => {
  res.send(req.body);
  return;
};
