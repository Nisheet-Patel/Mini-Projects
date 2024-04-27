// Fetching all data

var tab_list = [];
var project_list = {};
var fetch_counter = 0;
var all_project = 0;
var total_project = 0;

function fetchAllProjects(project) {
  return fetch(
    "https://raw.githubusercontent.com/Nisheet-Patel/Mini-Projects/master/" +
      project +
      "/README.md"
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((markdownText) => {
      // Remove leading and trailing whitespace
      const trimmedText = markdownText.trim();

      // Split the text into lines
      const lines = trimmedText.split("\n");

      // Initialize an array to store the table data
      const tableData = [];

      // Regular expression to match each row of the table
      const tableRowRegex = /\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|/;

      // Loop through each line of the text
      lines.forEach((line) => {
        // Check if the line matches the table row format
        const match = line.match(tableRowRegex);
        if (match && match.length === 5) {
          // Ensure match is not null and has all necessary groups
          // Extract data from the matched groups
          const [, number, title, description, developer] = match;
          const developerInfo = developer.match(/\[(.+?)\]\((.+?)\)/);
          if (developerInfo && developerInfo.length === 3) {
            // Ensure developerInfo is not null and has all necessary groups
            const developerName = developerInfo[1];
            const developerGitHub = developerInfo[2];

            // Extract URL from title and remove starting and ending brackets
            const titleInfo = title.match(/\[(.*?)\]\((.*?)\)/);
            const titleText = titleInfo ? titleInfo[1] : "";
            const url = titleInfo ? titleInfo[2].replace("../", "") : "";

            // Create an object for the row and push it to the tableData array
            tableData.push({
              Title: titleText.trim(),
              URL: url.trim(),
              Description: description.trim(),
              Developer: {
                Name: developerName.trim(),
                GitHub: developerGitHub.trim(),
              },
            });
          }
        }
      });

      return tableData;
    })
    .catch((error) => console.error("Error:", error));
}

// fetch tab_list
fetch(
  "https://raw.githubusercontent.com/Nisheet-Patel/Mini-Projects/master/README.md"
)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.text();
  })
  .then((text) => {
    // Split the text into lines
    const lines = text.split("\n");

    // Flag to indicate whether the "Languages & Frameworks" section has started
    let isLanguagesFrameworksSection = false;
    let activateBreakePoint = false;
    // Loop through each line of the text
    lines.forEach((line) => {
      // Check if the line contains the "Languages & Frameworks" section
      if (line.trim() == "## Languages & Frameworks") {
        isLanguagesFrameworksSection = true;
      }

      // Check if the line is empty or contains only spaces
      if (!line.trim() && activateBreakePoint) {
        // If an empty line is encountered, stop processing
        isLanguagesFrameworksSection = false;
        return;
      }

      // If we're in the "Languages & Frameworks" section and the line starts with '<a href='
      if (isLanguagesFrameworksSection && line.trim().startsWith("<a href=")) {
        // Extract the href value from the line
        const hrefMatch = line.match(/href="([^"]+)"/);
        if (hrefMatch) {
          const decodedHref = decodeURIComponent(hrefMatch[1]).substring(1);
          tab_list.push(decodedHref);
          activateBreakePoint = true;
        }
      }
    });

    // Log the array of href values to the console
    console.log(tab_list);
  })
  .catch((error) => console.error("Error:", error))
  .finally(() => {
    tab_list.forEach(function (element) {
      if (element != "All") {
        fetchAllProjects(element)
          .then((data) => {
            project_list[element] = data;
            console.log("Data:", data);
          })
          .catch((error) => {
            console.error("An error occurred:", error);
          })
          .finally(() => {
            console.log(tab_list.length);
            fetch_counter++;

            //  check if we get all data or not
            if (tab_list.length == fetch_counter) {
              render_all_project_list();
            }
          });
      }
    });

    render_tab_list();
  });

function render_tab_list() {
  tab_list.forEach(function (element) {
    document.querySelector(
      ".tab-container"
    ).innerHTML += `<div class="tab">${element}</div>`;
  });
}

function render_project_list(language) {
  total_project = 0;
  // Loop through each project in the current language
  project_list[language].forEach((project) => {
    total_project++;
    document.querySelector(".project-container").innerHTML += `
                
        <div class="project">
        <div class="title">${project.Title}</div>
        <div class="description">${project.Description}</div>
        <div class="footer">
            <div class="links">
                <a href="https://github.com/Nisheet-Patel/Mini-Projects/tree/master/${project.URL}" target="__blank__">
                    <button class="Btn">
                        <svg class="svgIcon" viewBox="0 0 496 512" height="1.4em"
                            xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z">
                            </path>
                        </svg>
                        <span class="text">Github</span>
                    </button>
                </a>
                <a href="#">
                    <button class="Btn">
                        <svg class="svgIcon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 30" width="16"
                            height="16">
                            <path
                                d="M 15 4 C 10.814 4 5.3808594 5.0488281 5.3808594 5.0488281 L 5.3671875 5.0644531 C 3.4606632 5.3693645 2 7.0076245 2 9 L 2 15 L 2 15.001953 L 2 21 L 2 21.001953 A 4 4 0 0 0 5.3769531 24.945312 L 5.3808594 24.951172 C 5.3808594 24.951172 10.814 26.001953 15 26.001953 C 19.186 26.001953 24.619141 24.951172 24.619141 24.951172 L 24.621094 24.949219 A 4 4 0 0 0 28 21.001953 L 28 21 L 28 15.001953 L 28 15 L 28 9 A 4 4 0 0 0 24.623047 5.0546875 L 24.619141 5.0488281 C 24.619141 5.0488281 19.186 4 15 4 z M 12 10.398438 L 20 15 L 12 19.601562 L 12 10.398438 z" />
                        </svg>
                        <span class="text">Youtube</span>
                    </button>
                </a>
                <a href="#">
                    <button class="Btn">
                        <svg class="svgIcon" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                            fill="#ffffff" class="bi bi-globe" viewBox="0 0 16 16">
                            <path
                                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m7.5-6.923c-.67.204-1.335.82-1.887 1.855A8 8 0 0 0 5.145 4H7.5zM4.09 4a9.3 9.3 0 0 1 .64-1.539 7 7 0 0 1 .597-.933A7.03 7.03 0 0 0 2.255 4zm-.582 3.5c.03-.877.138-1.718.312-2.5H1.674a7 7 0 0 0-.656 2.5zM4.847 5a12.5 12.5 0 0 0-.338 2.5H7.5V5zM8.5 5v2.5h2.99a12.5 12.5 0 0 0-.337-2.5zM4.51 8.5a12.5 12.5 0 0 0 .337 2.5H7.5V8.5zm3.99 0V11h2.653c.187-.765.306-1.608.338-2.5zM5.145 12q.208.58.468 1.068c.552 1.035 1.218 1.65 1.887 1.855V12zm.182 2.472a7 7 0 0 1-.597-.933A9.3 9.3 0 0 1 4.09 12H2.255a7 7 0 0 0 3.072 2.472M3.82 11a13.7 13.7 0 0 1-.312-2.5h-2.49c.062.89.291 1.733.656 2.5zm6.853 3.472A7 7 0 0 0 13.745 12H11.91a9.3 9.3 0 0 1-.64 1.539 7 7 0 0 1-.597.933M8.5 12v2.923c.67-.204 1.335-.82 1.887-1.855q.26-.487.468-1.068zm3.68-1h2.146c.365-.767.594-1.61.656-2.5h-2.49a13.7 13.7 0 0 1-.312 2.5m2.802-3.5a7 7 0 0 0-.656-2.5H12.18c.174.782.282 1.623.312 2.5zM11.27 2.461c.247.464.462.98.64 1.539h1.835a7 7 0 0 0-3.072-2.472c.218.284.418.598.597.933M10.855 4a8 8 0 0 0-.468-1.068C9.835 1.897 9.17 1.282 8.5 1.077V4z" />
                        </svg>
                        <span class="text">Link</span>
                    </button>
                </a>
            </div>
            <div class="developer"><a href="${project.Developer.GitHub}">${project.Developer.Name}</a></div>
        </div>
    </div>
                `;
  });

  update_total_project(total_project);
}

function render_all_project_list() {
  all_project = 0;
  for (const language in project_list) {
    total_project = 0;

    render_project_list(language);

    all_project += total_project;
  }

  update_total_project(all_project);
}

// Add event listener to the tab-container for click events
document
  .querySelector(".tab-container")
  .addEventListener("click", function (event) {
    // Check if the clicked element is a tab
    if (event.target.classList.contains("tab")) {
      // Get all tab elements
      var tabs = document.querySelectorAll(".tab-container .tab");

      // Remove 'active' class from all tabs
      tabs.forEach(function (tab) {
        tab.classList.remove("active");
      });

      // Add 'active' class to the clicked tab
      event.target.classList.add("active");

      if (event.target.textContent != "All") {
        clearProjectContainer();
        render_project_list(event.target.textContent);
      } else {
        clearProjectContainer();
        render_all_project_list();
      }
      // Print the clicked tab's text content in the console
      console.log(event.target.textContent);
    }
  });

function update_total_project(value) {
  document.querySelector("#total_project").innerHTML = value;
}

function clearProjectContainer() {
  document.querySelector(".project-container").innerHTML = "";
}
