exports.middlewaresGlobal = (req, res, next) => {
  res.locals.umaVariavelGlobal = "Este é o valor da variavel local";
  next();
};

exports.outroMiddlewares = (req, res, next) => {
  next();
};

exports.checkCsrfError = (err, req, res, next) => {
  if (err && err.code === "EBADCSRFTOKEN") {
    return res.render("404");
  }

  next(err);
};

exports.csrfMiddleware = (req, res, next) => {
  res.locals.csrfToken = req.csrfToken();
  next();
};
