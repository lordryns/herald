if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

document.getElementById("request-form").addEventListener("submit", (e) => {
  document.getElementById("request-btn").innerHTML = Spinner();
})


function Spinner() {
  return `<svg
  aria-label="Loading"
  role="img"
  viewBox="0 0 16 16"
  version="1.1"
  width="16"
  height="16"
  class="anim-spin"
  >
  <path fill="#0969da" d="M8 0a8 8 0 1 0 8 8h-2a6 6 0 1 1-6-6v2z"/>
</svg>

<style>
  .anim-spin {
    animation: spin 1s linear infinite;
    transform-origin: center center;
  }

  @keyframes spin {
    0% { transform: rotate(0deg);}
    100% { transform: rotate(360deg);}
  }
</style>`
}
