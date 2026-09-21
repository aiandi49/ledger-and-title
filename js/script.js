(function () {
  "use strict";

  var root = document.documentElement;
  var THEME_KEY = "llhub-theme";
  var FONT_KEY = "llhub-font-step";
  var steps = [0.9, 1, 1.1, 1.2];

  function safeGet(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function safeSet(key, val) {
    try { window.localStorage.setItem(key, val); } catch (e) { /* ignore */ }
  }

  /* ---- Theme (defaults to light) ---- */
  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    var toggles = document.querySelectorAll("[data-theme-toggle]");
    toggles.forEach(function (btn) {
      btn.setAttribute("aria-pressed", theme === "dark");
      btn.setAttribute("aria-label", theme === "dark" ? "Switch to light mode" : "Switch to dark mode");
    });
  }

  var storedTheme = safeGet(THEME_KEY);
  applyTheme(storedTheme === "dark" ? "dark" : "light");

  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-theme-toggle]");
    if (!btn) return;
    var current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
    var next = current === "dark" ? "light" : "dark";
    applyTheme(next);
    safeSet(THEME_KEY, next);
  });

  /* ---- Font-size stepper ---- */
  function stepIndexFromValue(val) {
    var idx = steps.indexOf(parseFloat(val));
    return idx === -1 ? 1 : idx;
  }

  function applyFontStep(idx) {
    idx = Math.max(0, Math.min(steps.length - 1, idx));
    root.style.setProperty("--step-font", steps[idx]);
    document.querySelectorAll("[data-font-dec]").forEach(function (b) { b.disabled = idx === 0; });
    document.querySelectorAll("[data-font-inc]").forEach(function (b) { b.disabled = idx === steps.length - 1; });
    safeSet(FONT_KEY, steps[idx]);
    return idx;
  }

  var storedFont = safeGet(FONT_KEY);
  var currentStep = applyFontStep(stepIndexFromValue(storedFont || 1));

  document.addEventListener("click", function (e) {
    if (e.target.closest("[data-font-inc]")) {
      currentStep = applyFontStep(currentStep + 1);
    } else if (e.target.closest("[data-font-dec]")) {
      currentStep = applyFontStep(currentStep - 1);
    } else if (e.target.closest("[data-font-reset]")) {
      currentStep = applyFontStep(1);
    }
  });

  /* ---- Mobile nav ---- */
  document.addEventListener("click", function (e) {
    var toggle = e.target.closest("[data-nav-toggle]");
    if (!toggle) return;
    var header = document.querySelector(".site-header");
    var expanded = header.classList.toggle("nav-open");
    toggle.setAttribute("aria-expanded", expanded);
  });

  document.addEventListener("click", function (e) {
    var header = document.querySelector(".site-header");
    if (!header || !header.classList.contains("nav-open")) return;
    if (e.target.closest(".primary-nav a")) {
      header.classList.remove("nav-open");
    }
  });

  /* ---- FAQ analytics-free single-open behavior (optional, per group) ---- */
  document.querySelectorAll("[data-faq-group]").forEach(function (group) {
    group.addEventListener("toggle", function (e) {
      if (!e.target.open) return;
      group.querySelectorAll("details[open]").forEach(function (d) {
        if (d !== e.target) d.removeAttribute("open");
      });
    }, true);
  });
})();
