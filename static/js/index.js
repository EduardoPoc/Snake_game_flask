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
async function enviar_tecla(event) {
    const direcao = keys[event.key];
    if (!direcao) return;

    fetch("/tecla", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ direcao }),
    })
}

document.addEventListener('keydown', enviar_tecla(event));