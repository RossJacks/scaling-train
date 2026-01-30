import { fetchHTML } from './fetch-utils.js';

document.addEventListener("DOMContentLoaded", () => {
    const includeTargets = Array.from(document.querySelectorAll("[data-include]"));

    Promise.all(
        includeTargets.map((el) => {
            const url = el.getAttribute("data-include");
            if (!url) {
                return Promise.resolve();
            }

            return fetchHTML(url)
                .then((html) => {
                    el.innerHTML = html;
                })
                .catch((error) => {
                    console.error(error);
                });
        })
    ).then(() => {
        const currentPage = (window.location.pathname.split("/").pop() || "index.html").toLowerCase();
        document.querySelectorAll("nav a").forEach((link) => {
            const href = (link.getAttribute("href") || "").toLowerCase();
            if (href === currentPage) {
                link.setAttribute("aria-current", "page");
            }
        });
    });
});
