// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    // Marquee hover effect
    const marqueeText = document.querySelector(".marquee-text");
    const marqueeContainer = document.querySelector(".marquee-container");

    // Adding mouse hover event to start the marquee animation
    marqueeContainer.addEventListener("mouseenter", () => {
        marqueeText.style.animation = "marquee 10s linear infinite"; // Starts the animation on hover
    });

    // Adding mouse leave event to stop the marquee animation
    marqueeContainer.addEventListener("mouseleave", () => {
        marqueeText.style.animation = ""; // Resets the animation on mouse leave
    });

    // Adding an active class to the navbar items based on scroll position
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    window.addEventListener("scroll", () => {
        let currentSection = "";

        sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 50) {
                currentSection = section.getAttribute("id");
            }
        });

        navLinks.forEach((link) => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(currentSection)) {
                link.classList.add("active");
            }
        });
    });

    // Handling form submission via Formspree (you can replace it with your actual form ID)
    const form = document.querySelector("#contact-form");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(form.action, {
            method: form.method,
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            alert("Message sent successfully!");
            form.reset();
        })
        .catch(error => {
            alert("There was an error sending your message.");
        });
    });

    // Dynamically populating the Projects section using JavaScript
    const projects = [
        {
            name: "Calculator",
            description: "A Python-based calculator project.",
            link: "https://github.com/kleyneii/ePortfolio/blob/main/calculator.py",
            imgSrc: "bca3d7cf72fbce57be60ffd86878c5a9.jpg"
        },
        {
            name: "Time",
            description: "A Python-based time project that displays the current time.",
            link: "https://github.com/kleyneii/ePortfolio/blob/main/time.py",
            imgSrc: "07b146eec5b1c469ba6f847fbd8a5ec1.jpg"
        },
        {
            name: "Timer",
            description: "A Python-based timer project for countdowns.",
            link: "https://github.com/kleyneii/ePortfolio/blob/main/timer.py",
            imgSrc: "9e658c41b651b583b116411889e155fc.jpg"
        }
    ];

    const projectsList = document.getElementById("projects-list");
    projects.forEach(project => {
        const projectCard = document.createElement("div");
        projectCard.classList.add("col-md-4");
        projectCard.innerHTML = `
            <div class="project-card">
                <img src="${project.imgSrc}" class="img-fluid" alt="${project.name} Screenshot">
                <h4>${project.name}</h4>
                <p>${project.description}</p>
                <a href="${project.link}" class="btn btn-primary" target="_blank">View on GitHub</a>
            </div>
        `;
        projectsList.appendChild(projectCard);
    });
});
