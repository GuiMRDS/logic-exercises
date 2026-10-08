exports.middlewaresGlobal = (req, res, next) => {
  res.locals.umaVariavelGlobal = "Este é o valor da variavel local";
  next();
};

exports.outroMiddlewares = (req, res, next) => {
  next();
};
