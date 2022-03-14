import { basUrl } from '../common/api.service.js'

export async function register(url, payload) {
  const request = fetch(`${basUrl}${url}`, {
    method: "Post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  const response = await request.then((e) => e.json());
  return response;
}

export async function login(payload) {
  const request = fetch(`${basUrl}/auth/sign-in/`, {
    method: "Post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  const response = await request.then((e) => e.json());
  return response;
}

export function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};

export async function getUserType() {
  const token = localStorage.getItem("access_token");
  const request = fetch(`${basUrl}/user/${parseJwt(token).user_id}/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await request.then((e) => e.json());
  return response.data.user_type;
}

export async function getUser(url) {
  const token = localStorage.getItem("access_token");
  const user_type = await getUserType()
  
  if (user_type === 'Job-Seeker') {
    url = `/job-seekers/${parseJwt(token).user_id}/`;
  }
  else if (user_type === 'Employer') {
    url = `/employers/${parseJwt(token).user_id}/`;
  }
  const request = fetch(`${basUrl}${url}`, {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const response = await request.then((e) => e.json());
  return response;
}

export function checkAuth() {
  if (localStorage.getItem('access_token')) {
    return true
  }
  else {
    return false
  }
}

export function destroyerAuth() {
  if (localStorage.getItem('access_token')) {
    localStorage.removeItem("access_token");
    window.location.pathname = '/login.html'
  }
}