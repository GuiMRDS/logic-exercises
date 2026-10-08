require("dotenv").config();

const express = require("express");
const app = express();
const mongoose = require("mongoose");

const connectionString = process.env.CONNECTIONSSTRING;

mongoose
  .connect(connectionString)
  .then(() => {
    console.log("Agora a conexão ocorreu");
  })
  .catch((err) => {
    console.log("Erro ao conectar:", err);
  });

const session = require("express-session");
const { MongoStore } = require("connect-mongo");
const flash = require("connect-flash");

const routes = require("./routes.js");
const path = require("path");
const helmet = require("helmet");
const csrf = require("csurf");
const {
  middlewaresGlobal,
  checkCsrfError,
  csrfMiddleware,
} = require("./src/middlewares/middlewares.js");

app.use(helmet());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.resolve(__dirname, "public")));

const sessionOptions = session({
  secret: "asdadadasdasdasasd",
  store: MongoStore.create({
    mongoUrl: process.env.CONNECTIONSSTRING,
  }),
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 * 7,
    httpOnly: true,
  },
});
app.use(sessionOptions);
app.use(flash());

app.set("views", path.resolve(__dirname, "src", "views"));
app.set("view engine", "ejs");

app.use(csrf());
app.use(middlewaresGlobal);
app.use(checkCsrfError);
app.use(csrfMiddleware);
app.use(routes);

app.listen(3000, () => {
  console.log("Acessar http://localhost:3000");
  console.log("Servidor está executando na porta 3000");
});
