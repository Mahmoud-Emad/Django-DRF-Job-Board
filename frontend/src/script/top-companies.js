import { topCompanies, selectedCompanyDetailes } from "./modules/companies.js";
import { checkAuthNav } from "./baseUi.js";

// Display Companies
async function drawTopCompaniesUi() {
  const cardsContainer = document.querySelector(
    ".companies .company-inner .row"
  );

  const data = await topCompanies();

  data.forEach((item) => {
    const el = `
      <div class="col-md-6 mb-5">
        <div class="card card-image"
          style="background-image: url('https://mdbootstrap.com/img/Photos/Horizontal/City/6-col/img%20(47).webp');">
          <!-- Content -->
          <div class="text-white text-center d-flex justify-content-center align-items-center rgba-black-strong py-5 px-4">
            <div>
              <h3 class="card-title pt-2"><strong>${item.company_name}</strong></h3>
              <p>${item.description}</p>
              <a class="btn btn-primary" href="company-details.html?id=${item.id}"><i class="fas fa-clone left"></i> View Company</a>
            </div>
          </div>
        </div>
      </div>
    `;
    cardsContainer.innerHTML += el;
  });
}

if (document.querySelector(".companies .company-inner .row")) {
  drawTopCompaniesUi();
} else if (window.location.search) {
  drawCompanyDetails();
}

// Company details

async function drawCompanyDetails() {
  // get id from window location
  let id;
  if (window.location.search) {
    id = window.location.search.slice(window.location.search.indexOf("=") + 1);
  }

  const data = await selectedCompanyDetailes(id);
  companyJobs(data.jobs);

  const cardInfoContainer = document.querySelector(".company-details .above");

  const cardEl = `
    <div class="card card-cascade wider reverse">
      <!-- Card image -->
      <div class="view view-cascade overlay">
        <img class="card-img-top" src="https://mdbootstrap.com/img/Photos/Slides/img%20(70).webp"
          alt="Card image cap">
          <div class="mask rgba-white-slight"></div>
      </div>

      <!-- Card content -->
      <div class="card-body card-body-cascade text-center">

        <!-- Title -->
        <div class="company-titles">
          <h2 class="main-title">
            ${data.company_name}
          </h2>
          <div class="sub-title">
            <span >${data.company_size} employees - </span>
            <span>Jobs: ${data.jobs.length}</span>
          </div>
        </div>
        <!-- Text -->
        <p class="card-text mt-3">
          ${data.description}
        </p>
      </div>

    </div>
  `;
  cardInfoContainer.innerHTML = cardEl;
}

function companyJobs(jobsList) {
  const cardJobsContainer = document.querySelector(
    ".company-details .company-jobs"
  );

  jobsList.forEach((job) => {
    const jobEl = `
      <div class="job-item card py-3 px-4">
        <div class="job-item-inner">
          <div class="tire d-flex justify-content-between align-items-center">
            <span class="job-type">${job.job_type}</span>
            <img src="https://images.wuzzuf-data.net/files/company_logo/Bcare-Egypt-33521-1555509900.png" alt="companies">
          </div>
          <div class="job-titles">
            <h2 class="main-title">
              <a href="job-details.html?id=${job.id}" >${job.title}</a>
            </h2>
            <div class="sub-title">
              <span>${job.company.company_name} -</span>
              <span>${job.city}, ${job.country}</span>
            </div>
          </div>
          <hr class="w-25">
          <p class="jop-desc mb-0 text-muted">
            ${job.description}
          </p>
        </div>
      </div>
    `;
    cardJobsContainer.innerHTML += jobEl;
  });
}
