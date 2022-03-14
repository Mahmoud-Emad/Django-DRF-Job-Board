import { getAllJobs, findJob } from "./modules/jobs.js";

// Display Jobs
async function drawUi(el = null) {
  // data
  let data;
  // ui elements
  const cardsContainer = document.querySelector(".jobs .jobs-inner");

  // Check if have selected job
  if (el) {
    data = await el;
    cardsContainer.innerHTML = "";
  } else {
    data = await getAllJobs();
  }

  // loop throght data
  data.forEach((item) => {
    const cardEl = `
    <div class="job-item card py-3 px-4">
      <div class="job-item-inner">
        <div class="tire d-flex justify-content-between align-items-center">
          <div>
            <span class="job-type">${item.job_type}</span>
            ${
              item.most_recent
                ? `<span class="job-type bg-success">${item.most_recent}</span>`
                : ""
            }
          </div>
          <a href="company-details.html?id=${item.company.id}" class="c-img">
            <img src="https://images.wuzzuf-data.net/files/company_logo/Bcare-Egypt-33521-1555509900.png" alt="companies">
          </a>
        </div>
        <div class="job-titles">
          <h2 class="main-title">
            <a href="job-details.html?id=${item.id}" >${item.title}</a>
          </h2>
          <div class="sub-title">
            <a href="company-details.html?id=${item.company.id}">${
      item.company.company_name
    } - </a>
            <span>${item.city}, ${item.country}</span>
          </div>
        </div>
        <hr class="w-25">
        <p class="jop-desc mb-0 text-muted">
          ${item.description}
        </p>
      </div>
    </div>
  `;
    cardsContainer.innerHTML += cardEl;
  });
}

window.onload = () => {
  drawUi();
};

async function searchJob() {
  const jobInpEl = document.querySelector("form .search-bar-input"),
    data = await findJob(jobInpEl.value);
  drawUi(data);
}

document.getElementById("search-job").addEventListener("click", async (e) => {
  e.preventDefault();
  searchJob();
});
