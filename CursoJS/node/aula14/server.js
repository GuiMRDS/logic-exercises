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

const routes = require("./routes.js");
const path = require("path");
const { middlewaresGlobal } = require("./src/middlewares/middlewares.js");

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.resolve(__dirname, "public")));

app.set("views", path.resolve(__dirname, "src", "views"));
app.set("view engine", "ejs");

app.use(middlewaresGlobal);
app.use(routes);

app.listen(3000, () => {
  console.log("Acessar http://localhost:3000");
  console.log("Servidor está executando na porta 3000");
});
