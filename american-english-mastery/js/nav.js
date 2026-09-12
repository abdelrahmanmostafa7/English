(function () {
  const sidebar = document.getElementById("sidebar");
  const toggle = document.getElementById("tocToggle");
  const links = sidebar ? sidebar.querySelectorAll("a[data-nav]") : [];
  const progressPart = document.getElementById("progressPart");
  const progressTitle = document.getElementById("progressTitle");
  const progressPct = document.getElementById("progressPct");
  const progressFill = document.getElementById("progressFill");
  const progressStatus = document.getElementById("progressStatus");
  const cover = document.getElementById("cover");
  const parts = Array.prototype.slice.call(document.querySelectorAll(".part[id]"));
  const coverTitle = cover && cover.querySelector("h1")
    ? cover.querySelector("h1").textContent.trim()
    : "American English Mastery Reference";

  if (toggle && sidebar) {
    toggle.addEventListener("click", function () {
      const open = sidebar.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    links.forEach(function (link) {
      link.addEventListener("click", function () {
        sidebar.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  function setActiveLink(id) {
    links.forEach(function (a) {
      a.classList.toggle("active", a.getAttribute("data-nav") === id);
    });
  }

  function sectionProgress(el, markerY) {
    const rect = el.getBoundingClientRect();
    const height = Math.max(el.offsetHeight, 1);
    const scrolled = markerY - rect.top;
    return Math.min(100, Math.max(0, (scrolled / height) * 100));
  }

  function showCover() {
    if (progressPart) progressPart.textContent = "Cover";
    if (progressTitle) progressTitle.textContent = coverTitle;
    if (progressPct) progressPct.textContent = "0%";
    if (progressFill) progressFill.style.width = "0%";
    if (progressStatus) {
      progressStatus.textContent = "Cover: " + coverTitle + " — 0%";
    }
    setActiveLink(null);
  }

  function updateReadingProgress() {
    const header = document.querySelector(".site-header");
    const headerH = header ? header.offsetHeight : 0;
    const markerY = headerH + Math.min(window.innerHeight * 0.22, 140);

    // Progress starts at Part 1 — stay on Cover at 0% until then.
    if (cover) {
      const firstPart = parts[0];
      const beforeParts = !firstPart || firstPart.getBoundingClientRect().top > markerY;
      if (beforeParts) {
        showCover();
        return;
      }
    }

    let current = null;
    let pct = 0;

    for (let i = 0; i < parts.length; i++) {
      const part = parts[i];
      const rect = part.getBoundingClientRect();
      if (rect.top <= markerY && rect.bottom > markerY) {
        current = part;
        pct = sectionProgress(part, markerY);
        break;
      }
    }

    if (!current && parts.length) {
      const last = parts[parts.length - 1];
      if (last.getBoundingClientRect().bottom <= markerY) {
        current = last;
        pct = 100;
      } else {
        current = parts[0];
        pct = sectionProgress(current, markerY);
      }
    }

    if (!current) {
      showCover();
      return;
    }

    const partLabel = "Part " + (current.getAttribute("data-part") || "");
    const titleEl = current.querySelector(".part-title");
    const title = titleEl ? titleEl.textContent.trim() : partLabel;
    const rounded = Math.round(pct);

    if (progressPart) progressPart.textContent = partLabel;
    if (progressTitle) progressTitle.textContent = title;
    if (progressPct) progressPct.textContent = rounded + "%";
    if (progressFill) progressFill.style.width = pct.toFixed(2) + "%";
    if (progressStatus) {
      progressStatus.textContent = partLabel + ": " + title + " — " + rounded + "%";
    }

    setActiveLink(current.id);
  }

  let ticking = false;
  function onScrollOrResize() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      updateReadingProgress();
      ticking = false;
    });
  }

  window.addEventListener("scroll", onScrollOrResize, { passive: true });
  window.addEventListener("resize", onScrollOrResize);
  updateReadingProgress();
})();
