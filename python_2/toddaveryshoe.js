// Constants for reliability
const BASE_PRICE = 150;
const TAX_RATE = 0.08;
const SUPPORT_ADDONS = {
  "Standard": 0,
  "All-Terrain": 10,
  "Speed": 15,
  "Grip+": 20
};
const SEASONAL_COLORS = {
  "Spring": ["Spring Green", "Fresh Blue", "Sunrise Yellow"],
  "Summer": ["Ocean Blue", "Sandy Beige", "Coral Pink"],
  "Fall": ["Autumn Red", "Golden Brown", "Forest Green"],
  "Winter": ["Winter White", "Ice Blue", "Charcoal Gray"]
};
const CUSTOMER_DISCOUNTS = {
  "The Mentor": 15,
  "The First-Timer": 5,
  "The One Who Came Back": 10,
  "The Quiet Storm": 0
};

// Variables of different data types
let userName = ""; // string
let shoeSize = 0; // number
let isValid = false; // boolean

// DOM elements
const nameInput = document.getElementById("name");
const customerTypeSelect = document.getElementById("customerType");
const memoryTagInput = document.getElementById("memoryTag");
const seasonSelect = document.getElementById("season");
const colorSelect = document.getElementById("color");
const sizeInput = document.getElementById("size");
const tractionSelect = document.getElementById("traction");
const shoeImage = document.getElementById("shoeImage");
const calculatePriceBtn = document.getElementById("calculatePrice");
const showDetailsBtn = document.getElementById("showDetails");
const startTimerBtn = document.getElementById("startTimer");
const stopTimerBtn = document.getElementById("stopTimer");
const output = document.getElementById("output");

// Find element by class name
const card = document.querySelector(".card");

// Find element by tag name
const buttons = document.querySelectorAll("button");

// Custom function with multiple arguments and return value
function calculateFinalPrice(basePrice, supportAddon, discountPercent, taxRate) {
  const subtotal = basePrice + supportAddon;
  const discountAmount = subtotal * (discountPercent / 100);
  const afterDiscount = subtotal - discountAmount;
  const tax = afterDiscount * taxRate;
  const finalPrice = afterDiscount + tax;
  return Math.round(finalPrice * 100) / 100; // round to 2 decimals
}

// Loop over array
function updateColorOptions() {
  const selectedSeason = seasonSelect.value;
  colorSelect.innerHTML = '<option value="">Select...</option>';
  if (selectedSeason && SEASONAL_COLORS[selectedSeason]) {
    for (let color of SEASONAL_COLORS[selectedSeason]) {
      const option = document.createElement("option");
      option.value = color;
      option.textContent = color;
      colorSelect.appendChild(option);
    }
  }
}

// Event listeners
window.addEventListener("load", () => {
  console.log("Page loaded successfully!");
  output.textContent += "\nWelcome to ToddAvery!";
});

seasonSelect.addEventListener("change", updateColorOptions);

colorSelect.addEventListener("change", () => {
  const selectedColor = colorSelect.value;
  // Add new attribute
  shoeImage.setAttribute("data-color", selectedColor);
  console.log("Color selected:", selectedColor);
});

sizeInput.addEventListener("input", () => {
  shoeSize = parseFloat(sizeInput.value) || 0;
  isValid = shoeSize >= 5 && shoeSize <= 15;
  if (!isValid) {
    sizeInput.style.borderColor = "red";
  } else {
    sizeInput.style.borderColor = "#ccc";
  }
});

calculatePriceBtn.addEventListener("click", () => {
  userName = nameInput.value.trim();
  const customerType = customerTypeSelect.value;
  const traction = tractionSelect.value;

  // Mathematical operation
  const supportAddon = SUPPORT_ADDONS[traction] || 0;
  const discount = CUSTOMER_DISCOUNTS[customerType] || 0;

  // Logical operators
  if (userName && customerType && traction && isValid && !(!seasonSelect.value || !colorSelect.value)) {
    const finalPrice = calculateFinalPrice(BASE_PRICE, supportAddon, discount, TAX_RATE);
    output.textContent = `Hello ${userName}! Your custom shoe price is $${finalPrice}`;
    console.log(`Price calculated: $${finalPrice}`);
  } else {
    output.textContent = "Please fill all required fields correctly.";
    console.log("Validation failed");
  }
});

showDetailsBtn.addEventListener("click", () => {
  const color = colorSelect.value;
  let message = "Pick a color to begin your story.";
  if (color === "Autumn Red") {
    message = "🔥 Autumn Red — Strength in Roots.";
  } else if (color === "Golden Brown") {
    message = "🌰 Golden Brown — Warmth of Home.";
  } else if (color === "Forest Green") {
    message = "🌲 Forest Green — Growth and Renewal.";
  } else if (color) {
    message = `✨ ${color} — Your unique journey.`;
  }
  output.textContent = message;
  console.log(message);
});

// Timer functionality
let timerId = null;
startTimerBtn.addEventListener("click", () => {
  if (timerId) clearInterval(timerId);
  let count = 0;
  timerId = setInterval(() => {
    count++;
    shoeImage.style.transform = `rotate(${count * 10}deg)`;
    if (count > 36) {
      clearInterval(timerId);
      timerId = null;
      shoeImage.style.transform = "rotate(0deg)";
    }
  }, 100);
});

stopTimerBtn.addEventListener("click", () => {
  if (timerId) {
    clearInterval(timerId);
    timerId = null;
    shoeImage.style.transform = "rotate(0deg)";
  }
});

// Inline functions for mouseover (called from HTML)
function highlightImage() {
  shoeImage.style.border = "3px solid yellow";
}

function unhighlightImage() {
  shoeImage.style.border = "none";
}