window.onload = function() {
    // Change the report title
    document.title = "Payment Gateway Report";

    // Modify the Allure header
    let header = document.querySelector(".app-header");

    if (header) {
        // Add a custom logo
        let logo = document.createElement("img");
        logo.src = "https://icon.sabpaisa.in/sabpaisa/offline/challan-sabpaisalogo.png";  // Replace with your logo file
        logo.style.height = "50px";    // Adjust height as needed
        logo.style.marginRight = "10px";

        // Insert logo before the title
        header.insertBefore(logo, header.firstChild);

        // Modify the title text
        let titleElement = header.querySelector(".app-title");
        if (titleElement) {
            titleElement.innerText = "My Custom Report Name";
        }
    }
};
