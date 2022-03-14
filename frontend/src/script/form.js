import { register, login } from './modules/auth.js'
import countryList from "../countrys.json" assert { type: "json" }

// To Fill Options Of Select Element of All Countries
export function returnAllCountry(elContainer) {
  const parent = document.querySelector(`${elContainer}`)

  if (parent) {
    countryList.forEach((item) => {
      const optionEl = `
      <option value="${item.value}">${item.text}</option>
    `;
      parent.innerHTML += optionEl;
    });
  }
}

returnAllCountry("#country");

// Register

// Job Seeker
function regAsSeeker() {
  const formEl = document.querySelector(".sForm");
  const firstNameEl = formEl.querySelector("#firstname").value,
    lastnameEl = formEl.querySelector("#lastname").value,
    emailEl = formEl.querySelector("#email").value,
    passwordEl = formEl.querySelector("#password").value,
    phoneEl = formEl.querySelector("#phone").value,
    bioEl = formEl.querySelector("#bio").value,
    country = document.querySelector("#country").value,
    city = formEl.querySelector("#city").value;
  
  // Validation
  if (
    !firstNameEl ||
    !firstNameEl.trim() ||
    !lastnameEl ||
    !lastnameEl.trim() ||
    !emailEl ||
    !emailEl.trim() ||
    !passwordEl ||
    !passwordEl.trim() ||
    !country ||
    !city ||
    !city.trim()
  ) {
    alert('Please Fill all Data')
    return
  }
  else {
    const url = "/job-seekers/register/";
    const data = {
      first_name: firstNameEl,
      last_name: lastnameEl,
      email: emailEl,
      password: passwordEl,
      phone: phoneEl,
      description: bioEl,
      country: country,
      city: city,
    };

    // send req
    try {
      register(url, data)
      window.location.pathname = "/login.html";
    }
    catch (err) {
      console.log(err);
    }
  }
}

if (document.querySelector(".reg-btn")) {
  document.querySelector(".reg-btn").addEventListener("click", (e) => {
    e.preventDefault();
    regAsSeeker();
  });
}

// Employeer
function regAsEmployeer() {
  const formEl = document.querySelector(".emForm");

  const firstNameEl = formEl.querySelector("#emFirstname").value,
    lastnameEl = formEl.querySelector("#emLastname").value,
    emailEl = formEl.querySelector("#emEmail").value,
    passwordEl = formEl.querySelector("#emPassword").value,
    phoneEl = formEl.querySelector("#emPhone").value,
    bioEl = formEl.querySelector("#emBio").value,
    companyNameEl = formEl.querySelector("#emCompany").value,
    companySizeEl = formEl.querySelector("#emSize").value;

  // Validation
  if (
    !firstNameEl ||
    !firstNameEl.trim() ||
    !lastnameEl ||
    !lastnameEl.trim() ||
    !emailEl ||
    !emailEl.trim() ||
    !passwordEl ||
    !passwordEl.trim() ||
    !companyNameEl ||
    !companyNameEl.trim() ||
    !companySizeEl
  ) {
    alert("Please Fill all Data");
    return;
  } else {
    const url = "/employers/register/";
    const data = {
      first_name: firstNameEl,
      last_name: lastnameEl,
      email: emailEl,
      password: passwordEl,
      phone: phoneEl,
      description: bioEl,
      company_name: companyNameEl,
      company_size: companySizeEl,
    };

    // send req
    try {
      register(url, data);
      window.location.pathname = "/login.html";
    } catch (err) {
      console.log(err);
    }
  }
}

if (document.querySelector(".regEm-btn")) {
  document.querySelector(".regEm-btn").addEventListener('click', (e) => {
    e.preventDefault()
    regAsEmployeer()
  })
}


// Login
async function loginUser() {
  const formEl = document.querySelector(".login-form"),
    emailEl = formEl.querySelector("#email").value,
    passwordEl = formEl.querySelector("#password").value;
  
  if (!emailEl || !emailEl.trim() || !passwordEl || !passwordEl.trim()) {
    alert("Please Fill all Data");
    return;
  }
  const data = {
    email: emailEl,
    password: passwordEl
  };

  // send req
  try {
    const req = await login(data);
    localStorage.setItem("access_token", `Bearer ${req.data.access_token}`);
    window.location.pathname = "/index.html";
  } catch (error) {
    console.log(error);
  }
}

if (document.querySelector('.login-btn')) {
  document.querySelector(".login-btn").addEventListener('click', (e) => {
    e.preventDefault()
    loginUser();
  })
}