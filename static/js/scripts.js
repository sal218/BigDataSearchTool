const cityInput = document.getElementById("city");
const stateInput = document.getElementById("state");
const suggestionsBox = document.getElementById("city-suggestions");

cityInput.addEventListener("input", async () => {
    const query = cityInput.value;
    const state = stateInput.value;

    if (query.length < 1) {
        suggestionsBox.innerHTML = "";
        return;
    }

    // Send the query along with the selected state (if any)
    const response = await fetch(`/autocomplete/cities?q=${encodeURIComponent(query)}&state=${encodeURIComponent(state)}`);
    const cities = await response.json();
    suggestionsBox.innerHTML = "";

    cities.forEach(city => {
        const suggestionItem = document.createElement("div");
        suggestionItem.classList.add("suggestion-item");
        suggestionItem.textContent = city;
        suggestionItem.addEventListener("click", () => {
            cityInput.value = city;
            suggestionsBox.innerHTML = "";
        });
        suggestionsBox.appendChild(suggestionItem);
    });
});

document.addEventListener("click", (event) => {
    if (!suggestionsBox.contains(event.target) && event.target !== cityInput) {
        suggestionsBox.innerHTML = "";
    }
});