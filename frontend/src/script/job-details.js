import { getSelectedJob, applyJob } from "./modules/jobs.js";
import { checkAuthNav } from "./baseUi.js";
import { getUser } from "./modules/auth.js";

// get id from window location
const id = window.location.search.slice(
  window.location.search.indexOf("=") + 1
);

// Draw ui of new info
async function drawUi() {
  const data = await getSelectedJob(id);
  const userInfo = await getUser()
  const isUserApplied = data.applied_users.indexOf(userInfo.data.id) !== -1 ? true : false
  // console.log(data.applied_users);
  // ui elements
  const cardsContainer = document.querySelector(".job-details article");

  const cardEl = `
    <div class="card note">
      <div class="card-inner px-5 py-3">
        <div class="tire d-flex justify-content-between align-items-center">
          <span class="job-type">${data.job_type}</span>
          <a href="company-details.html?id=${data.company.id}" class="c-img">
            <img src="https://images.wuzzuf-data.net/files/company_logo/Bcare-Egypt-33521-1555509900.png" alt="companies">
          </a>
        </div>
        <div class="job-titles">
          <h2 class="main-title">
            ${data.title}
          </h2>
          <div class="sub-title">
            <a href="company-details.html?id=${data.company.id}" >${
    data.company.company_name
  } -</a>
            <span>${data.city}, ${data.country}</span>
          </div>
        </div>
        <p class="jop-desc mb-0 text-muted">
          ${data.description}
        </p>
        <hr class="w-25">
        ${
          userInfo.data.user_type !== "Job-Seeker"
            ? ""
            : `<button class="btn btn-primary btn-lg m-0 mt-2 apply-btn ${isUserApplied ? 'disabled' : ''}" type="button">Apply</button>`
        }
      </div>
    </div>
  `;
  cardsContainer.innerHTML = cardEl;

}

window.onload = drawUi();

async function apply() {
  const request = await applyJob(id);
  console.log(request);
}


document.querySelector(".job-details").addEventListener('click', (e) => {
  if (!!e.target.closest(".apply-btn")) {
    e.preventDefault()
    apply()
  }
})