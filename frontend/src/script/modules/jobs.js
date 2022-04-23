import { basUrl } from '../common/api.service.js'

export async function getAllJobs() {
  const request = fetch(`${basUrl}/jobs/recent/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await request.then((e) => e.json());
  return response.data
}

export async function findJob(keyword) {
  const request = fetch(`${basUrl}/jobs/search/${keyword}/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await request.then((e) => e.json());
  return response.data;
}

export async function getSelectedJob(id) {
  const request = fetch(`${basUrl}/jobs/detail/${id}/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await request.then((e) => e.json());
  return response.data;
}

export async function applyJob(id) {
  const token = localStorage.getItem('access_token')
  const request = fetch(`${basUrl}/jobs/apply/${id}/`, {
    method: "Post",
    headers: {
      'Authorization': token,
      "Content-Type": "application/json",
    }
  });

  const response = await request.then((e) => e.json());
  return response.data;
}

export async function addJob(payload) {
  const token = localStorage.getItem("access_token");
  const request = fetch(`${basUrl}/jobs/create/`, {
    method: "Post",
    headers: {
      "Authorization": token,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload)
  });

  const response = await request.then((e) => e.json())
  return response
}