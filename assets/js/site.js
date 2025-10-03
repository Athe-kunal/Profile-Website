(function () {
  function setCurrentYear() {
    const yearSpan = document.getElementById("year");
    if (yearSpan) {
      yearSpan.textContent = new Date().getFullYear();
    }
  }

  function highlightActiveNav() {
    const navLinks = document.querySelectorAll("nav .nav-links a");
    if (!navLinks.length) return;

    const currentPath = window.location.pathname;
    const currentFile = currentPath.split("/").pop() || "index.html";

    navLinks.forEach((link) => {
      const linkPath = new URL(link.href).pathname;
      const linkFile = linkPath.split("/").pop() || "index.html";
      if (linkFile === currentFile) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    setCurrentYear();
    highlightActiveNav();
  });
})();
