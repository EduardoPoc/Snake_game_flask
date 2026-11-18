const keys = {
    ArrowUp: "up",
    w: "up",
    ArrowDown: "down",
    s: "down",
    ArrowLeft: "left",
    a: "left",
    ArrowRight: "right",
    d: "right",
    Enter: "enter"
};
let jogoEncerrado = false;
let direcaoAtual = "right";

function desenharTabuleiro(tabuleiro) {
    const area = document.querySelector(".area");
    area.replaceChildren();
    tabuleiro.forEach(linha => linha.forEach(valor => {
        const celula = document.createElement("div");
        celula.className = valor === "cabeca_cobra" || valor === "corpo_cobra" ? "snake" : "celula";
        celula.id = valor === "cabeca_cobra" ? "cabeca" : valor === "corpo_cobra" ? "corpo" : valor;
        celula.setAttribute("role", "gridcell");
        celula.setAttribute("aria-label", `Posição ${valor}`);
        area.appendChild(celula);
    }));
}

async function moverCobra() {
    if (jogoEncerrado) return;
    const resposta = await fetch("/tecla", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ direcao: direcaoAtual }),
    });
    if (!resposta.ok) return;

    const resultado = await resposta.json();
    desenharTabuleiro(resultado.area);
    if (resultado.fim) {
        jogoEncerrado = true;
        alert("Fim de jogo!");
        document.querySelector("#reiniciar").hidden = false;
    }
}

document.addEventListener("keydown", event => {
    const direcao = keys[event.key];
    if (direcao && direcao !== "enter") direcaoAtual = direcao;
});

setInterval(moverCobra, 300);
