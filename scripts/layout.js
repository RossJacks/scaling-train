document.addEventListener("DOMContentLoaded", () => {
    const pageTitle = document.body.dataset.pageTitle || "Ross' Rotisserie";
    const pageHeading = document.body.dataset.pageHeading || "Ross' Rotisserie";
    const contentTemplate = document.getElementById("page-content");
    const footerTemplate = document.getElementById("page-footer");

    if (!contentTemplate) {
        return;
    }

    fetch("template.html")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to load template");
            }
            return response.text();
        })
        .then((html) => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");

            doc.title = pageTitle;
            const headingEl = doc.getElementById("page-heading");
            if (headingEl) {
                headingEl.textContent = pageHeading;
            }

            const mainEl = doc.getElementById("main-content");
            if (mainEl) {
                mainEl.replaceChildren(contentTemplate.content.cloneNode(true));
            }

            const footerSlot = doc.getElementById("page-footer-slot");
            if (footerSlot && footerTemplate) {
                footerSlot.replaceChildren(footerTemplate.content.cloneNode(true));
            }

            document.open();
            document.write("<!DOCTYPE html>" + doc.documentElement.outerHTML);
            document.close();
        })
        .catch((error) => {
            console.error(error);
        });
});
