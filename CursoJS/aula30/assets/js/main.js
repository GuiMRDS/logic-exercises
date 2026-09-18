const h1 = document.querySelector(".container h1");

const data = new Date();

h1.innerHTML = data.toLocaleString("pt-BR", {
  weekday: "long",
  year: "numeric",
  month: "long",
  day: "numeric",
  hour: "2-digit",
  minute: "2-digit",
});
