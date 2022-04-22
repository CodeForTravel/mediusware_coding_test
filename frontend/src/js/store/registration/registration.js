import ServiceRegistration from "../../service/registration/ServiceRegistration.js";

export const namespaced = true;

export const state = {};

export const mutations = {};

export const actions = {
  resetPassword({}, data) {
    return ServiceRegistration.resetPassword(data)
      .then((resp) => {
        return resp;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  resetPasswordConfirm({}, data) {
    return ServiceRegistration.resetPasswordConfirm(data)
      .then((resp) => {
        return resp;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  resetPasswordValidateToken({}, data) {
    return ServiceRegistration.resetPasswordValidateToken(data)
      .then((resp) => {
        return resp;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },
};