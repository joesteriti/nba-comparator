const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menu.addEventListener('click', function() {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
});

const search_bar1 = document.getElementById('search_bar1');
const search_bar2 = document.getElementById('search_bar2');
const compare_button = document.getElementById('compare_button');
const resultsDiv = document.getElementById('results');

// API details
const BASE_URL = 'https://api-nba-v1.p.rapidapi.com/';
const API_KEY = '41c4debfe3mshb19c98476ad3e39p1b9b6bjsnf1057326c1b0'; // Replace with your actual RapidAPI key

const headers = {
  'x-rapidapi-host': 'api-nba-v1.p.rapidapi.com',
  'x-rapidapi-key': API_KEY,
};

// Function to search for players by their names
async function searchPlayers(player1, player2) {
  // If both player names are provided
  if (player1 && player2) {
    const url = `${BASE_URL}players?search=${player1},${player2}`;
    
    try {
      const response = await fetch(url, { method: 'GET', headers: headers });
      const data = await response.json();
      
      if (data && data.response) {
        displayResults(data.response);
      } else {
        resultsDiv.innerHTML = '<p>No players found.</p>';
      }
    } catch (error) {
      console.error('Error fetching player data:', error);
      resultsDiv.innerHTML = '<p>Error fetching data. Please try again later.</p>';
    }
  } else {
    resultsDiv.innerHTML = '<p>Please enter both player names.</p>';
  }
}

// Function to display the results in the page
function displayResults(players) {
  // Clear previous results
  resultsDiv.innerHTML = '';

  players.forEach(player => {
    const playerDiv = document.createElement('div');
    playerDiv.innerHTML = `
      <h3>${player.firstname} ${player.lastname}</h3>
      <p>Height: ${player.height}</p>
      <p>Weight: ${player.weight}</p>
      <p>Position: ${player.leagues.standard.pos}</p>
    `;
    resultsDiv.appendChild(playerDiv);
  });
}

// Event listener for the button click
compare_button.addEventListener('click', () => {
  const player1 = search_bar1.value.trim();
  const player2 = search_bar2.value.trim();
  
  searchPlayers(player1, player2); // Search players when the button is clicked
});
