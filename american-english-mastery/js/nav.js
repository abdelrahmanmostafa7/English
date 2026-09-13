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
  const STORAGE_KEY = "aem-sidebar-collapsed";
  const mq = window.matchMedia("(max-width: 900px)");

  let backdrop = document.querySelector(".sidebar-backdrop");
  if (!backdrop) {
    backdrop = document.createElement("div");
    backdrop.className = "sidebar-backdrop";
    backdrop.setAttribute("aria-hidden", "true");
    document.body.appendChild(backdrop);
  }

  function isMobile() {
    return mq.matches;
  }

  function isExpanded() {
    if (isMobile()) return sidebar.classList.contains("open");
    return !document.body.classList.contains("sidebar-collapsed");
  }

  function setExpanded(expanded) {
    if (isMobile()) {
      document.body.classList.remove("sidebar-collapsed");
      sidebar.classList.toggle("open", expanded);
      backdrop.classList.toggle("show", expanded);
    } else {
      sidebar.classList.remove("open");
      backdrop.classList.remove("show");
      document.body.classList.toggle("sidebar-collapsed", !expanded);
      try {
        localStorage.setItem(STORAGE_KEY, expanded ? "0" : "1");
      } catch (e) {}
    }

    if (toggle) {
      toggle.setAttribute("aria-expanded", expanded ? "true" : "false");
      toggle.setAttribute("aria-label", expanded ? "Hide contents" : "Show contents");
    }
  }

  function initSidebar() {
    if (isMobile()) {
      setExpanded(false);
      return;
    }
    let collapsed = false;
    try {
      collapsed = localStorage.getItem(STORAGE_KEY) === "1";
    } catch (e) {}
    setExpanded(!collapsed);
  }

  if (toggle && sidebar) {
    toggle.addEventListener("click", function () {
      setExpanded(!isExpanded());
    });

    backdrop.addEventListener("click", function () {
      if (isMobile()) setExpanded(false);
    });

    links.forEach(function (link) {
      link.addEventListener("click", function () {
        if (isMobile()) setExpanded(false);
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && isMobile() && isExpanded()) {
        setExpanded(false);
      }
    });

    if (mq.addEventListener) {
      mq.addEventListener("change", initSidebar);
    } else if (mq.addListener) {
      mq.addListener(initSidebar);
    }

    initSidebar();
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
