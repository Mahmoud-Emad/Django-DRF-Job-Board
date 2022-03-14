import { basUrl } from "../common/api.service.js";

export async function topCompanies() {
  const request = fetch(`${basUrl}/jobs/top-companies/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await request.then((e) => e.json());
  return response.data;
}

export async function selectedCompanyDetailes(id) {
  const request = fetch(`${basUrl}/employers/${id}/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await request.then((e) => e.json());
  return response.data;
}
