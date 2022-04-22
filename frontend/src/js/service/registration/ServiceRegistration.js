import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const apiClient = axios.create({
  baseURL: process.env.BACKEND_HOST,
});

const urlList = {
  urlRoot: "/api/v1/password_reset/",
};

export default {
  resetPassword(data) {
    return apiClient.post(urlList.urlRoot, data);
  },

  resetPasswordConfirm(data) {
    let url = urlList.urlRoot + "confirm/";
    return apiClient.post(url, data);
  },

  resetPasswordValidateToken(data) {
    let url = urlList.urlRoot + "validate_token/";
    return apiClient.post(url, data);
  },
};