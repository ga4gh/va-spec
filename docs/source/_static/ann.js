// Custom JS for the annotated-code-block directive, adding tooltip functionality.

function closeAllTooltips(exceptTip) {
  document.querySelectorAll(".ann-tip").forEach((tip) => {
    if (tip !== exceptTip) tip.hidden = true;
  });
}

document.addEventListener("click", (e) => {
  const btn = e.target.closest(".ann-btn");

  if (!btn) {
    closeAllTooltips(null);
    return;
  }

  const wrap = btn.closest(".ann-wrap");
  if (!wrap) return;

  const tip = wrap.querySelector(".ann-tip");
  if (!tip) return;

  const newState = !tip.hidden;
  closeAllTooltips(tip);
  tip.hidden = newState;
});
