// Site-wide listener that lets an embedded diagram iframe (see the
// va-spec-class-diagram skill) report its own rendered height back to this
// page via postMessage, so the iframe never needs a static/guessed height.
//
// Same-origin deployments (the built RTD site) don't need this: the
// diagram's own script can reach the iframe directly via
// window.frameElement. But a locally-opened `file://` build -- how
// contributors typically preview docs before pushing -- gives every
// file:// document its own opaque origin, so window.frameElement is null
// there (blocked as cross-origin) and that direct path silently no-ops.
// postMessage works regardless of origin, so it's the fallback every
// diagram iframe should use when window.frameElement isn't available.
(function () {
  window.addEventListener("message", function (event) {
    if (!event.data || event.data.type !== "va-spec-diagram-height") return;
    var iframes = document.getElementsByTagName("iframe");
    for (var i = 0; i < iframes.length; i++) {
      if (iframes[i].contentWindow === event.source) {
        var px = Math.ceil(event.data.height) + "px";
        if (iframes[i].style.height !== px) {
          iframes[i].style.height = px;
        }
        break;
      }
    }
  });
})();
