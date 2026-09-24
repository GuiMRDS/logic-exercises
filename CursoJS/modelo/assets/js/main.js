const inputTarefa = document.querySelector(".input-tarefa");
const btnTarefa = document.querySelector(".btn-tarefa");
const tarefas = document.querySelector(".tarefas");

inputTarefa.addEventListener("keypress", function (e) {
  if (e.keyCode === 13) {
    if (!inputTarefa.value) return;
    criarTarefa(inputTarefa.value);
  }
});

document.addEventListener("click", function (e) {
  const el = e.target;

  if (el.classList.contains("apagar")) {
    el.parentElement.remove();
    salvarTarefas();
  }
});

function criarLi() {
  const li = document.createElement("li");
  return li;
}

function criarBotaoApagar(li) {
  li.innerText += " ";
  const botaoApagar = document.createElement("button");
  botaoApagar.innerText = "Apagar";
  // botaoApagar.classList.add("apagar");
  botaoApagar.setAttribute("class", "apagar");
  botaoApagar.setAttribute("title", "Apagar essa Tarefa");
  li.appendChild(botaoApagar);
}

function limparInput() {
  inputTarefa.value = "";
  inputTarefa.focus();
}

function criarTarefa(textoInput) {
  const li = criarLi();
  li.innerHTML = textoInput;
  tarefas.appendChild(li);
  limparInput();
  criarBotaoApagar(li);
  salvarTarefas(li);
}

function salvarTarefas() {
  const liTarefas = tarefas.querySelectorAll("li");
  const listaDeTarefas = [];

  for (let tarefa of liTarefas) {
    let tarefaTexto = tarefa.innerText;
    tarefaTexto = tarefaTexto.replace("Apagar", "").trim();
    listaDeTarefas.push(tarefaTexto);
  }

  const tarefasJSON = JSON.stringify(listaDeTarefas);
  localStorage.setItem("tarefas", tarefasJSON);
}

function adicionaTarefasSalvas() {
  const tarefas = localStorage.getItem("tarefas");
  const listaDeTarefas = JSON.parse(tarefas);

  for (let tarefa of listaDeTarefas) {
    criarTarefa(tarefa);
  }
}

adicionaTarefasSalvas();

btnTarefa.addEventListener("click", function (e) {
  if (!inputTarefa.value) return false;
  criarTarefa(inputTarefa.value);
});
