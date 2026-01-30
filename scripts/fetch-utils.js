/**
 * Fetches HTML content from a URL with error handling
 * @param {string} url - The URL to fetch
 * @returns {Promise<string>} - The HTML content as text
 * @throws {Error} - If the fetch fails
 */
export function fetchHTML(url) {
    return fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Failed to load ${url}`);
            }
            return response.text();
        });
}
