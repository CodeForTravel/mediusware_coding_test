import UserService from "../../service/user/UserService.js";

export const namespaced = true;

export const state = {
  userInfo: null,
};

export const mutations = {
  SET_USER_INFO(state, userInfo) {
    state.userInfo = userInfo;
  },

};

export const actions = {
  getUserInfo({ commit }) {
    return UserService.getUserInfo()
      .then((resp) => {
        commit("SET_USER_INFO", resp.data);
        return resp;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  getUserProfile({}, { userId }) {
    return UserService.getUserProfile(userId)
      .then((resp) => {
        return resp;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  updateUserProfile({}, { userId, userProfile }) {
    UserService.updateUserProfile(userId, userProfile)
      .then((resp) => {
        Vue.toasted.show("Profile successfully updated", {
          className: "bg-success",
        });

        setTimeout(function() {
          location.reload();
        }, 3000);
      })
      .catch((err) => {
        if (err.response.status == 400) {
          var message = "";

          if (err.response.data.name) {
            message = "Name: " + err.response.data.name;
          } else if (err.response.data.timezone) {
            message = "Timezone: " + err.response.data.timezone;
          } else if (err.response.data.timestamp_format) {
            message = "Timestamp Format: " + err.response.data.timestamp_format;
          }

          if (message) {
            Vue.toasted.show(message, {
              className: "bg-danger",
            });
          }
        } else {
          Vue.toasted.show("Oops! something went wrong", {
            className: "bg-danger",
          });
        }
      });
  },


  changeUserPassword({}, data) {
    return UserService.changeUserPassword(data)
      .then((resp) => {
        Vue.toasted.show("Password successfully changed", {
          className: "bg-success",
        });
        return resp;
      })
      .catch((err) => {
        if (err.response.status == 400) {
          var message = "";

          if (err.response.data.old_password) {
            message = "Old Password: " + err.response.data.old_password;
          } else if (err.response.data.message) {
            message = err.response.data.message;
          } else if (err.response.data.non_field_errors) {
            message = err.response.data.non_field_errors[0];
          }

          if (message) {
            Vue.toasted.show(message, {
              className: "bg-danger",
            });
          }
        } else {
          Vue.toasted.show("Oops! something went wrong", {
            className: "bg-danger",
          });
        }

        return err.response;
      });
  },

  userLogin({ commit }, userLoginData) {
    return UserService.userLogin(userLoginData)
      .then((resp) => {
        return resp;
      })
      .catch((err) => {
        if (err.response.status == 400) {
          var message = "";

          if (err.response.data.detail) {
            message = err.response.data.detail;
          }
          if (message) {
            Vue.toasted.show(message, {
              className: "bg-danger",
            });
          }
        } else if (err.response.status == 404) {
          Vue.toasted.show("Please enter a correct username and password!", {
            className: "bg-danger",
          });
        } else {
          Vue.toasted.show("Oops! something went wrong", {
            className: "bg-danger",
          });
        }

        return err.response;
      });
  },
};
