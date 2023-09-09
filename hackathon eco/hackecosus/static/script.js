document.addEventListener("DOMContentLoaded", function () {
    const treeForm = document.getElementById("treeForm");
    const userName = document.getElementById("userName");
    const userTreesPlanted = document.getElementById("userTreesPlanted");
    const userBadges = document.getElementById("userBadges");
    const badgeCriteria = document.getElementById("badgeCriteria");
    const userRanking = document.getElementById("userRanking");
    const electricCarBtn = document.getElementById("electricCarBtn");
    const electricCarSection = document.getElementById("electricCarSection");
    const carNameInput = document.getElementById("carName");
    const fossilFuelSaved = document.getElementById("fossilFuelSaved");
    const contributionToEarth = document.getElementById("contributionToEarth");
    
    function toggleSolarPanelInfo() {
    if (solarPanelInfo.style.display === "none") {
        solarPanelInfo.style.display = "block";
    } else {
        solarPanelInfo.style.display = "none";
    }
}
solarPanelBtn.addEventListener("click", toggleSolarPanelInfo);
    // Sliding panel variables
    const slidingPanel = document.querySelector(".sliding-panel");
    const closePanelButton = document.getElementById("closePanel");
    
    // Function to open the sliding panel
    function openPanel() {
        slidingPanel.style.right = "0";
    }
    
    // Function to close the sliding panel
    function closePanel() {
        slidingPanel.style.right = "-400px";
    }
    
    // Event listener to close the sliding panel
    closePanelButton.addEventListener("click", closePanel);
    
    // Initialize user data from local storage or use default data
    let usersData = JSON.parse(localStorage.getItem("usersData")) || [
        { fullName: "John Doe", treesPlanted: 25, badges: 2, electricCar: false },
        { fullName: "Jane Smith", treesPlanted: 40, badges: 4, electricCar: true },
        { fullName: "Alice Johnson", treesPlanted: 75, badges: 7, electricCar: false },
    ];
    
    // Display users ranking
    displayRanking();
    
    treeForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const fullName = document.getElementById("fullName").value;
        const treesPlanted = parseInt(document.getElementById("treesPlanted").value);
    
        // Update or add user data
        let existingUser = false;
        usersData.forEach(user => {
            if (user.fullName === fullName) {
                user.treesPlanted += treesPlanted;
                user.badges = calculateBadges(user.treesPlanted);
                existingUser = true;
            }
        });
    
        if (!existingUser) {
            const newUser = {
                fullName: fullName,
                treesPlanted: treesPlanted,
                badges: calculateBadges(treesPlanted),
                electricCar: false, // Default to no electric car
            };
            usersData.push(newUser);
        }
    
        // Save user data to local storage
        localStorage.setItem("usersData", JSON.stringify(usersData));
    
        // Sort users by trees planted for ranking
        usersData.sort((a, b) => b.treesPlanted - a.treesPlanted);
    
       
        displayRanking();
        document.getElementById("treesPlanted").value = "";
    });
    
    electricCarBtn.addEventListener("click", function () {
        electricCarSection.style.display = "block";
    });
    
    electricCarSection.addEventListener("submit", function (e) {
        e.preventDefault();
        const carOwnerName = carNameInput.value;
    
        // Simulate fetching environmental impact data (replace with actual API calls)
        setTimeout(() => {
            const savedFuel = Math.random() * 1000; // Random value for demonstration
            const contribution = savedFuel * 2.3; // Random formula for demonstration
            fossilFuelSaved.textContent = `${savedFuel.toFixed(2)} gallons`;
            contributionToEarth.textContent = `${contribution.toFixed(2)} kg of CO2 saved`;
        }, 2000); // Simulated delay
    
        // Update user data with electric car information
        const electricCarUser = usersData.find(user => user.fullName === carOwnerName);
        if (electricCarUser) {
            electricCarUser.electricCar = true;
            electricCarUser.badges = calculateBadges(electricCarUser.treesPlanted);
        }
    
        // Change user name appearance in the ranking list to have a green background highlight
        displayRanking();
    
        // Save user data to local storage
        localStorage.setItem("usersData", JSON.stringify(usersData));
    });
    
    function calculateBadges(treesPlanted) {
        if (treesPlanted >= 100) {
            return 3; // Tree Hero Badge
        } else if (treesPlanted >= 50) {
            return 2; // Environmental Champion Badge
        } else if (treesPlanted >= 10) {
            return 1; // Green Thumb Badge
        } else {
            return 0; // No badge
        }
    }
    
    function displayRanking() {
        userRanking.innerHTML = "";
        usersData.forEach((user, index) => {
            const listItem = document.createElement("li");
            const userBadgeText = user.electricCar ? `${user.fullName} (Electric Car)` : `${user.fullName}`;
            listItem.textContent = `${userBadgeText} - ${user.treesPlanted} trees, ${user.badges} badges`;
            if (user.electricCar) {
                listItem.style.backgroundColor = "green"; // Add green background for users with electric cars
                listItem.style.color = "white"; // Set text color to white for better contrast
            }
            userRanking.appendChild(listItem);
        });
    }
});
