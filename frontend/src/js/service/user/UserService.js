import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const apiClient = axios.create({
  baseURL: process.env.BACKEND_HOST,
});

const urlList = {
  urlRoot: "/api/v1/user/",
};

export default {
  getUserInfo() {
    let url = urlList.urlRoot + `profile/user-info/`;
    return apiClient.get(url);
  },
  getUserProfile(userId) {
    let url = urlList.urlRoot + `profile/${userId}/`;
    return apiClient.get(url);
  },
  updateUserProfile(userId, userProfile) {
    let url = urlList.urlRoot + `profile/${userId}/`;
    return apiClient.patch(url, userProfile);
  },
  changeUserPassword(data) {
    let url = urlList.urlRoot + `profile/change-password/`;
    return apiClient.post(url, data);
  },

  userLogin(userLoginData) {
    let url = urlList.urlRoot + `login/`;
    return apiClient.post(url, userLoginData);
  },
};
