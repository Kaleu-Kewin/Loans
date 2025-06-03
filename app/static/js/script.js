document.addEventListener('DOMContentLoaded', () => {
  ocultarElementoComDelay('resultado', 5000);
});

function ocultarElementoComDelay(id, delay = 5000) {
  const elemento = document.getElementById(id);

  if (!elemento) return;
  elemento.style.transition = 'opacity 0.5s ease';

  setTimeout(() => {
    elemento.style.opacity = '0';

    setTimeout(() => {
      elemento.remove();
    }, 500);
  }, delay);
}
