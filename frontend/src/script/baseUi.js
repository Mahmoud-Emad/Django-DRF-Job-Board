import { getUser, getUserType, destroyerAuth } from "./modules/auth.js";

async function baseUi() {
  // Header
  // add bg color to header
  const header = document.querySelector('header nav')
  window.addEventListener("scroll", function () {
    if (this.pageYOffset > 80) {
      header.classList.add("sticky");
    } else {
      header.classList.remove("sticky");
    }
  });
  checkAuthNav();
}

export async function checkAuthNav() {
  // If User Signed In
  if (localStorage.getItem("access_token")) {
    const request = await getUser(),
      userType = await getUserType(),
      first_name = request.data.first_name,
      lastName = request.data.last_name,
      nav = document.querySelector(".navbar-nav.user");
    
    const el = `
      <li class="nav-item">
        <a href="#"
          class="nav-link waves-effect mr-3">
          <i class="fa-solid fa-user"></i> ${first_name} ${lastName}
        </a>
      </li>
      ${
        userType === "Employer"
          ? `<li class="nav-item">
            <button class=" primary nav-link waves-effect mr-3" data-toggle="modal" data-target="#modalContactForm">
            <i class="fa-solid fa-plus"></i> Add New Job
            </button>
          </li>
          `
          : ""
      }
      <li class="nav-item">
        <button class=" primary nav-link waves-effect mr-3 logout-btn">
        <i class="fa-solid fa-power-off"></i> Logout
        </button>
      </li>
    `;
    nav.innerHTML = el;
  }
}
baseUi();

// Logout Btn
document.querySelector(".navbar-nav.user").addEventListener("click", (e) => {
  if (e.target.closest('.logout-btn')) {
    destroyerAuth()
  }
});