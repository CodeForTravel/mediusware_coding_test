import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const apiClient = axios.create({
  baseURL: process.env.BACKEND_HOST,
});

const urlList = {
  settingsRootUrl: "/api/v1/settings/",

};

export default {

};
