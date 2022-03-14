import { returnAllCountry } from './form.js'
import { addJob } from './modules/jobs.js'

// Draw Ui Country on Select input
returnAllCountry(".pp-country");

const btn = document.querySelector(".add-job-btn");

async function addNewJob() {
  const formEl = document.querySelector(".pp-form");

  const titleEl = formEl.querySelector("#title").value,
    experienceEl = formEl.querySelector("#experience").value,
    countryEl = formEl.querySelector("#country").value,
    cityEl = formEl.querySelector("#city").value,
    jobTypeEl = formEl.querySelector("#job_type").value,
    descEl = formEl.querySelector("#desc").value;
  
   // Validation
  if (
    !titleEl ||
    !titleEl.trim() ||
    !experienceEl ||
    !experienceEl.trim() ||
    !cityEl ||
    !cityEl.trim() ||
    !descEl ||
    !descEl.trim()
  ) {
    alert("Please Fill all Data");
    return;
  }

  const data = {
    title: titleEl,
    experience: experienceEl,
    country: countryEl,
    city: cityEl,
    job_type: jobTypeEl,
    description: descEl,
  };

  try {
    addJob(data);
    btn.setAttribute("data-dismiss", "modal");
  }
  catch (err) {
    console.log(err);
  }
}

btn.addEventListener("click", addNewJob);