const button = document.getElementById("searchBtn");
const input = document.getElementById("cityInput");
const weatherDiv = document.getElementById("weather");
const error = document.getElementById("error");
const loading = document.getElementById("loading");

const API_KEY = "abd84d942c0b108a524358e42a6c07dc";

button.addEventListener("click", getWeather);

async function getWeather() {
  const city = input.value;

  // Empty input check
  if (city === "") {
    error.textContent = "Please enter a city name";
    return;
  }

  error.textContent = "";
  weatherDiv.innerHTML = "";
  loading.textContent = "Loading...";

  try {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${city},in&appid=${API_KEY}&units=metric`
    );

    if (!response.ok) {
      throw new Error("City not found");
    }

    const data = await response.json();

    loading.textContent = "";

    weatherDiv.innerHTML = `
      <h2>${data.name}</h2>
      <p>Temperature: ${data.main.temp} °C</p>
      <p>Weather: ${data.weather[0].description}</p>
    `;

  } catch (err) {
    loading.textContent = "";
    error.textContent = err.message;
  }
}
