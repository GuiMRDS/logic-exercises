const resquest = (obj) => {
  const xhr = new XMLHttpRequest();
  xhr.open(obj.method, obj.url, true);
  xhr.send();

  xhr.addEventListener("load", () => {
    if (xhr.status >= 200 && xhr.status < 300) {
      obj.sucess(xhr.responseText);
    } else {
      obj.errorxhr.statusText;
    }
  });
};

document.addEventListener("click", (e) => {
  const el = e.target;
  const tag = el.tagName.toLowerCase();

  if (tag === "a") {
    e.preventDefault();
    carragarPagina(el);
  }
});

function carragarPagina(el) {
  const href = el.getAttribute("href");

  const objConfig = {
    method: "GET",
    url: href,
    sucess(responseText) {
      carragarResultado(response);
    },
    error(errorText) {
      console.log(errorText);
    },
  };
  resquest(objConfig);
}

function carragarResultado(response) {
  const resultado = document.querySelector(".resultado");
  resultado.innerHTML = response;
}
